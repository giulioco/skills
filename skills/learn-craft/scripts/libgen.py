#!/usr/bin/env python3
"""
libgen-download: search libgen.li and download PDFs locally.

Reverse-engineered from libgen.li traffic. Three-step flow:
  1. GET /index.php?req=...        -> HTML results table (id=tablelibgen)
  2. GET /ads.php?md5=<MD5>        -> HTML with one-time get.php?md5=...&key=... link
  3. GET /<get.php link>           -> 307 redirect to a CDN that serves the file bytes

Stdlib only. Pages column on libgen is "0", "0 / 368", "703 / 703", or "815".
"All pages" means: not "0" and not starting with "0 /" — i.e. either X/X where
X > 0, or a single positive integer (born-digital PDF).
"""

from __future__ import annotations

import argparse
import gzip
import html as html_lib
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
BASE = "https://libgen.li"
TIMEOUT = 30


def _fetch(url: str, referer: Optional[str] = None) -> tuple[str, urllib.request.addinfourl]:
    headers = {
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US,en;q=0.9",
    }
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=TIMEOUT)
    raw = resp.read()
    if resp.headers.get("Content-Encoding") == "gzip":
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", errors="replace"), resp


def _strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(re.sub(r"<[^>]+>", "", s))).strip()


@dataclass
class Candidate:
    md5: str
    title: str
    author: str
    publisher: str
    year: str          # may be ""
    language: str
    pages_raw: str     # e.g. "703 / 703" or "815" or "0 / 198"
    pages_total: int   # parsed total (0 if unknown)
    has_all_pages: bool
    size_raw: str      # e.g. "2 MB"
    size_bytes: int    # parsed approx bytes (for tiebreak)
    fmt: str           # lowercased


def _parse_size(raw: str) -> int:
    """Approximate size in bytes for tiebreaking. Accepts '584 kB', '2 MB', '1.2 GB'."""
    m = re.match(r"\s*([\d.]+)\s*(kb|mb|gb|b)\s*", raw, re.I)
    if not m:
        return 0
    n, unit = float(m.group(1)), m.group(2).lower()
    return int(n * {"b": 1, "kb": 1024, "mb": 1024**2, "gb": 1024**3}[unit])


def _parse_pages(raw: str) -> tuple[int, bool]:
    """Return (total_pages, has_all_pages). 'has_all_pages' means the listing
    isn't a partial scan: bare positive int, OR 'X / X' with X > 0.
    """
    raw = raw.strip()
    if not raw or raw == "0":
        return 0, False
    if "/" in raw:
        parts = [p.strip() for p in raw.split("/")]
        try:
            scanned, total = int(parts[0]), int(parts[1])
        except (ValueError, IndexError):
            return 0, False
        return total, scanned > 0 and scanned == total
    try:
        total = int(raw)
        return total, total > 0
    except ValueError:
        return 0, False


def search(query: str) -> list[Candidate]:
    """Run a libgen search and return parsed candidates (any format)."""
    params = [
        ("req", query),
        ("columns[]", "t"),
        ("objects[]", "f"),
        ("topics[]", "l"),
        ("topics[]", "c"),
        ("topics[]", "f"),
        ("topics[]", "a"),
        ("topics[]", "m"),
        ("topics[]", "r"),
        ("topics[]", "s"),
        ("res", "25"),
        ("filesuns", "all"),
    ]
    url = f"{BASE}/index.php?" + urllib.parse.urlencode(params)
    html, _ = _fetch(url)

    m = re.search(r'<table[^>]*id="tablelibgen"[^>]*>(.*?)</table>', html, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), re.DOTALL | re.IGNORECASE)

    out: list[Candidate] = []
    for r in rows:
        tds = re.findall(r"<td[^>]*>(.*?)</td>", r, re.DOTALL | re.IGNORECASE)
        if len(tds) < 9:
            continue
        md5_m = re.search(r"ads\.php\?md5=([a-f0-9]+)", r, re.IGNORECASE)
        if not md5_m:
            continue
        title_a = re.search(r'<a[^>]*href="(?:edition|ads)\.php[^"]*"[^>]*>(.*?)</a>', tds[0], re.DOTALL | re.IGNORECASE)
        title = _strip_tags(title_a.group(1)) if title_a else _strip_tags(tds[0])
        pages_raw = _strip_tags(tds[5])
        total, all_pages = _parse_pages(pages_raw)
        size_raw = _strip_tags(tds[6])
        out.append(Candidate(
            md5=md5_m.group(1),
            title=title,
            author=_strip_tags(tds[1]),
            publisher=_strip_tags(tds[2]),
            year=_strip_tags(tds[3]),
            language=_strip_tags(tds[4]),
            pages_raw=pages_raw,
            pages_total=total,
            has_all_pages=all_pages,
            size_raw=size_raw,
            size_bytes=_parse_size(size_raw),
            fmt=_strip_tags(tds[7]).lower(),
        ))
    return out


DERIVATIVE_TERMS = (
    "workbook", "summary", "summaries", "study guide", "analysis",
    "companion", "review of", "summary of", "summary &",
    "key takeaways", "cheat sheet",
)


def _title_relevance(title: str, query: str) -> int:
    """Count how many query words appear in the title. Used to push genuine
    matches above derivatives (workbooks, summaries) when libgen returns both.
    """
    title_l = title.lower()
    words = [w for w in re.findall(r"\w+", query.lower()) if len(w) > 2]
    return sum(1 for w in words if w in title_l)


def _is_derivative(title: str) -> bool:
    t = title.lower()
    return any(term in t for term in DERIVATIVE_TERMS)


EXCERPT_PAGE_THRESHOLD = 30  # below this, almost certainly an excerpt/sample


def _lang_match(c_lang: str, preferred: str) -> bool:
    """Match libgen's language strings ('English', 'en', 'Italian', 'it', '')
    against a preferred code/name. Empty/unknown is *not* a match — be strict
    so a non-English book doesn't sneak through when English is requested.
    """
    if not preferred:
        return True
    if not c_lang:
        return False
    cl = c_lang.strip().lower()
    p = preferred.strip().lower()
    aliases = {
        "english": {"english", "en", "eng"},
        "italian": {"italian", "it", "ita", "italiano"},
        "spanish": {"spanish", "es", "esp", "español", "espanol"},
        "french":  {"french", "fr", "fra", "français", "francais"},
        "german":  {"german", "de", "deu", "ger", "deutsch"},
        "russian": {"russian", "ru", "rus"},
        "chinese": {"chinese", "zh", "chi", "中文"},
        "portuguese": {"portuguese", "pt", "por"},
    }
    # Find canonical name for the preferred code
    pref_set = None
    for name, codes in aliases.items():
        if p in codes:
            pref_set = codes
            break
    if pref_set is None:
        pref_set = {p}
    return cl in pref_set


def rank_pdfs(cands: list[Candidate], query: str = "",
              lang: str = "english") -> list[Candidate]:
    """Filter to complete PDFs and rank.

    Sort priority (lower tuple = better):
      1. Language matches `lang` (default English) — most users want English
         and libgen's search is language-agnostic, so a generic "Sapiens"
         query happily returns the Italian translation. Push non-matches down.
      2. Not-a-likely-excerpt (>= 30 pages) beats likely-excerpt (< 30).
         A 4-page "Atomic Habits" PDF is a marketing sample, not the book.
      3. Not-a-derivative beats derivative (workbook/summary/study guide).
      4. Title-keyword overlap with the query — distinguishes the real book
         from same-author derivatives at the same length.
      5. Most total pages (most complete edition).
      6. Most recent year.
      7. Smallest file size (cleaner born-digital over re-OCRed).
    """
    pdfs = [c for c in cands if c.fmt == "pdf" and c.has_all_pages]

    def year_key(c: Candidate) -> int:
        try:
            return int(c.year)
        except (ValueError, TypeError):
            return 0

    pdfs.sort(key=lambda c: (
        0 if _lang_match(c.language, lang) else 1,
        1 if c.pages_total < EXCERPT_PAGE_THRESHOLD else 0,
        1 if _is_derivative(c.title) else 0,
        -_title_relevance(c.title, query),
        -c.pages_total,
        -year_key(c),
        c.size_bytes,
    ))
    return pdfs


def get_download_url(md5: str) -> str:
    """Resolve the one-time download URL by scraping ads.php."""
    detail_url = f"{BASE}/ads.php?md5={md5}"
    html, _ = _fetch(detail_url)
    m = re.search(r'href="(get\.php\?md5=[a-f0-9]+&key=[A-Z0-9]+)"', html, re.IGNORECASE)
    if not m:
        # ads.php sometimes nests the link inside an absolute URL too
        m = re.search(r'href="(https?://[^"]+/get\.php\?md5=[a-f0-9]+&key=[A-Z0-9]+)"', html, re.IGNORECASE)
        if not m:
            raise RuntimeError("Could not extract download key from ads.php — site layout may have changed")
        return m.group(1)
    return f"{BASE}/{m.group(1)}"


def _filename_from_disposition(disp: Optional[str]) -> Optional[str]:
    if not disp:
        return None
    m = re.search(r'filename\*?=(?:UTF-\d\'\')?"?([^";]+)"?', disp, re.IGNORECASE)
    if not m:
        return None
    name = m.group(1).strip()
    try:
        name = urllib.parse.unquote(name)
    except Exception:
        pass
    return name


def _safe_filename(name: str) -> str:
    name = re.sub(r"[/\x00]", "_", name).strip()
    return name[:200] or "book.pdf"


def download(md5: str, out_dir: Path, title_hint: Optional[str] = None,
             referer: Optional[str] = None) -> Path:
    """Download the file for a given MD5 to out_dir. Returns the saved path."""
    dl_url = get_download_url(md5)
    print(f"[libgen] download URL: {dl_url}", file=sys.stderr)

    headers = {
        "User-Agent": UA,
        "Accept": "*/*",
        "Accept-Encoding": "identity",  # don't gzip a binary
        "Referer": referer or f"{BASE}/ads.php?md5={md5}",
    }
    req = urllib.request.Request(dl_url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=TIMEOUT)  # follows 307

    fname = _filename_from_disposition(resp.headers.get("Content-Disposition"))
    if not fname:
        fname = f"{title_hint or md5}.pdf"
    fname = _safe_filename(fname)
    if not fname.lower().endswith(".pdf"):
        fname += ".pdf"

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / fname
    total = int(resp.headers.get("Content-Length") or 0)
    written = 0
    next_milestone = 10  # report every 10%
    with open(out_path, "wb") as f:
        while True:
            chunk = resp.read(64 * 1024)
            if not chunk:
                break
            f.write(chunk)
            written += len(chunk)
            if total:
                pct = 100 * written / total
                if pct >= next_milestone:
                    print(f"[libgen] {written/1_048_576:.1f} / {total/1_048_576:.1f} MB ({pct:.0f}%)",
                          file=sys.stderr)
                    next_milestone = int(pct) + 10
    if total and written != total:
        print(f"[libgen] warning: short read ({written} of {total} bytes)", file=sys.stderr)
    return out_path


def find_and_download(query: str, out_dir: Path,
                      author: Optional[str] = None,
                      year: Optional[str] = None,
                      pick: Optional[int] = None,
                      list_only: bool = False,
                      lang: str = "english") -> Optional[Path]:
    full_query = query
    if author:
        full_query += f" {author}"
    if year:
        full_query += f" {year}"

    print(f"[libgen] searching: {full_query!r} (lang={lang or 'any'})", file=sys.stderr)
    cands = search(full_query)
    print(f"[libgen] {len(cands)} total results", file=sys.stderr)

    pdfs = rank_pdfs(cands, query=query, lang=lang)
    matching = [c for c in pdfs if _lang_match(c.language, lang)] if lang else pdfs
    print(f"[libgen] {len(pdfs)} complete PDFs ({len(matching)} in {lang or 'any language'})",
          file=sys.stderr)

    if not pdfs:
        # Show partial PDFs so the user can see what's there
        partial = [c for c in cands if c.fmt == "pdf"][:5]
        print("[libgen] no complete PDFs found.", file=sys.stderr)
        if partial:
            print("[libgen] partial-PDF candidates (not downloaded):", file=sys.stderr)
            for i, c in enumerate(partial):
                print(f"  [{i}] {c.title[:80]} | {c.author[:40]} | "
                      f"{c.year} | {c.language} | pages={c.pages_raw} | {c.size_raw}",
                      file=sys.stderr)
        return None

    print("[libgen] top PDF candidates:", file=sys.stderr)
    for i, c in enumerate(pdfs[:5]):
        marker = "*" if i == (pick or 0) else " "
        lang_flag = "" if _lang_match(c.language, lang) else "  ⚠ off-language"
        print(f" {marker}[{i}] {c.title[:80]} | {c.author[:40]} | "
              f"{c.year} | {c.language or '?'} | {c.pages_total}p | {c.size_raw} | "
              f"md5={c.md5[:8]}{lang_flag}", file=sys.stderr)

    if list_only:
        return None

    chosen = pdfs[pick or 0]
    if lang and not _lang_match(chosen.language, lang) and pick is None:
        print(f"[libgen] no {lang} PDF found — top result is in {chosen.language or 'unknown'}. "
              f"Re-run with --lang any or --pick N to override.", file=sys.stderr)
        return None
    print(f"[libgen] downloading: {chosen.title[:80]} "
          f"({chosen.language or '?'}, {chosen.pages_total}p, {chosen.size_raw})",
          file=sys.stderr)
    title_hint = re.sub(r"[^\w\s.-]", "", chosen.title)[:100].strip()
    path = download(chosen.md5, out_dir, title_hint=title_hint)
    print(f"[libgen] saved: {path}", file=sys.stderr)
    return path


def main() -> int:
    p = argparse.ArgumentParser(description="Search and download books from libgen.li")
    p.add_argument("query", help="Book title (and optional author keywords)")
    p.add_argument("--author", help="Filter/refine by author")
    p.add_argument("--year", help="Filter/refine by year")
    p.add_argument("--out", default=str(Path.home() / "Downloads"),
                   help="Output directory (default: ~/Downloads)")
    p.add_argument("--pick", type=int,
                   help="Index of candidate to download (default: 0, top-ranked)")
    p.add_argument("--list", action="store_true",
                   help="Just list candidates, don't download")
    p.add_argument("--lang", default="english",
                   help="Preferred language (default: english). "
                        "Use 'any' to disable filtering. Other examples: italian, spanish, french, german.")
    args = p.parse_args()
    lang = "" if args.lang.lower() in ("any", "all", "*") else args.lang

    try:
        path = find_and_download(
            query=args.query,
            out_dir=Path(args.out).expanduser(),
            author=args.author,
            year=args.year,
            pick=args.pick,
            list_only=args.list,
            lang=lang,
        )
    except urllib.error.HTTPError as e:
        print(f"[libgen] HTTP error: {e.code} {e.reason}", file=sys.stderr)
        return 2
    except urllib.error.URLError as e:
        print(f"[libgen] network error: {e.reason}", file=sys.stderr)
        return 2
    except RuntimeError as e:
        print(f"[libgen] {e}", file=sys.stderr)
        return 1

    if path is None:
        # list_only or abort-on-no-match — both leave a useful summary on stderr
        return 0 if args.list else 1
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
