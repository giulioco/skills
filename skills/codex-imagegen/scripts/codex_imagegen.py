#!/usr/bin/env python3
"""Generate or edit images by driving Codex's built-in image_gen tool via `codex exec`.

Codex ships a "$imagegen" skill whose default mode is a built-in `image_gen` tool
that runs against Codex's own backend using the user's ChatGPT login — no
OPENAI_API_KEY required. That tool is internal to the Codex agent runtime and has
no standalone subcommand, but a one-shot `codex exec` run can invoke it.

This wrapper builds the right prompt, runs `codex exec`, finds the PNG(s) Codex
just wrote under $CODEX_HOME/generated_images/, and copies the newest one(s) into
the chosen output directory with a clean, descriptive filename.

Usage:
    codex_imagegen.py generate --prompt "a red fox in snow" [--out ./fox.png] [-n 1]
    codex_imagegen.py edit --image ./in.png --prompt "make it night time" [--out ./out.png]

The path Codex reports is parsed from its output; as a fallback we diff the
generated_images tree before/after the run and take whatever is new. The before/after
diff is the source of truth, so it is robust even if Codex's phrasing changes.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))


def generated_images_dir() -> Path:
    return codex_home() / "generated_images"


def snapshot_pngs() -> dict[Path, float]:
    root = generated_images_dir()
    if not root.exists():
        return {}
    out: dict[Path, float] = {}
    for p in root.rglob("*.png"):
        try:
            out[p] = p.stat().st_mtime
        except OSError:
            pass
    return out


def slugify(text: str, limit: int = 50) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return (text[:limit].strip("-") or "image")


def build_generate_prompt(user_prompt: str, n: int) -> str:
    count = (
        "a single image"
        if n == 1
        else f"{n} separate images (one built-in image_gen call per image)"
    )
    return (
        "Use the imagegen skill's built-in image_gen tool (NOT the CLI fallback, "
        "NOT scripts/image_gen.py, NOT OPENAI_API_KEY) to generate "
        f"{count} for this request:\n\n"
        f"{user_prompt}\n\n"
        "Render the image(s) with the built-in tool only. Do not write any code, "
        "do not call the OpenAI API, do not create files other than the generated "
        "image(s). When done, print the absolute file path of each saved PNG on its "
        "own line prefixed with 'SAVED: '."
    )


def build_edit_prompt(user_prompt: str, image_path: Path) -> str:
    return (
        "Use the imagegen skill's built-in image_gen tool (NOT the CLI fallback, "
        "NOT scripts/image_gen.py, NOT OPENAI_API_KEY) to EDIT an existing local "
        f"image.\n\nFirst load the local image at this absolute path with the "
        f"built-in view_image tool so it is in context:\n{image_path}\n\n"
        f"Then apply this edit using the built-in image_gen tool:\n{user_prompt}\n\n"
        "Preserve everything not mentioned in the edit. Do not write code, do not "
        "call the OpenAI API. When done, print the absolute file path of the saved "
        "PNG on its own line prefixed with 'SAVED: '."
    )


def run_codex(prompt: str, timeout: int) -> str:
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        prompt,
    ]
    print(f"[codex-imagegen] running codex exec (timeout {timeout}s)...", file=sys.stderr)
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd="/tmp",  # neutral cwd; Codex resets cwd anyway
    )
    out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if proc.returncode != 0:
        print(out, file=sys.stderr)
        raise SystemExit(
            f"[codex-imagegen] codex exec exited {proc.returncode}. "
            "Is `codex` logged in? Try `codex login`."
        )
    return out


def parse_saved_paths(output: str) -> list[Path]:
    paths: list[Path] = []
    for line in output.splitlines():
        m = re.search(r"SAVED:\s*(\S.+\.png)", line)
        if m:
            p = Path(m.group(1).strip().strip("`").strip())
            if p.exists():
                paths.append(p)
    # de-dup, preserve order
    seen = set()
    uniq = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


def newly_created(before: dict[Path, float], after: dict[Path, float]) -> list[Path]:
    """Files that are new, or whose mtime advanced, since the snapshot."""
    fresh = []
    for p, mt in after.items():
        if p not in before or mt > before[p]:
            fresh.append((mt, p))
    fresh.sort(reverse=True)  # newest first
    return [p for _, p in fresh]


def resolve_outputs(out_arg: str | None, count: int, prompt: str) -> list[Path]:
    """Return desired destination paths in cwd (or wherever --out points)."""
    if out_arg:
        base = Path(out_arg)
        if base.is_dir() or out_arg.endswith(os.sep):
            base.mkdir(parents=True, exist_ok=True)
            stem = slugify(prompt)
            return [
                base / (f"{stem}.png" if count == 1 else f"{stem}-{i+1}.png")
                for i in range(count)
            ]
        if base.suffix.lower() != ".png":
            base = base.with_suffix(".png")
        base.parent.mkdir(parents=True, exist_ok=True)
        if count == 1:
            return [base]
        return [base.with_name(f"{base.stem}-{i+1}{base.suffix}") for i in range(count)]

    stem = slugify(prompt)
    cwd = Path.cwd()
    return [
        cwd / (f"{stem}.png" if count == 1 else f"{stem}-{i+1}.png")
        for i in range(count)
    ]


def unique_dest(dest: Path, force: bool) -> Path:
    if force or not dest.exists():
        return dest
    i = 2
    while True:
        cand = dest.with_name(f"{dest.stem}-v{i}{dest.suffix}")
        if not cand.exists():
            return cand
        i += 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)

    g = sub.add_parser("generate", help="Generate new image(s)")
    g.add_argument("--prompt", required=True)
    g.add_argument("-n", type=int, default=1, help="number of distinct images (1-10)")
    g.add_argument("--out", help="output file or directory (default: cwd)")
    g.add_argument("--force", action="store_true", help="overwrite existing files")
    g.add_argument("--timeout", type=int, default=300)

    e = sub.add_parser("edit", help="Edit an existing local image")
    e.add_argument("--image", required=True, help="path to the image to edit")
    e.add_argument("--prompt", required=True)
    e.add_argument("--out", help="output file (default: cwd, '<name>-edited.png')")
    e.add_argument("--force", action="store_true")
    e.add_argument("--timeout", type=int, default=300)

    args = ap.parse_args()

    if shutil.which("codex") is None:
        raise SystemExit("[codex-imagegen] `codex` CLI not found on PATH.")

    if args.command == "generate":
        n = max(1, min(10, args.n))
        prompt = build_generate_prompt(args.prompt, n)
        label = args.prompt
        expected = n
    else:
        img = Path(args.image).expanduser().resolve()
        if not img.exists():
            raise SystemExit(f"[codex-imagegen] image not found: {img}")
        prompt = build_edit_prompt(args.prompt, img)
        label = f"{img.stem}-edited"
        expected = 1

    before = snapshot_pngs()
    started = time.time()
    output = run_codex(prompt, args.timeout)

    saved = parse_saved_paths(output)
    if not saved:
        after = snapshot_pngs()
        saved = newly_created(before, after)
        # keep only files created during this run
        saved = [p for p in saved if p.stat().st_mtime >= started - 1]

    if not saved:
        print(output, file=sys.stderr)
        raise SystemExit(
            "[codex-imagegen] Could not find any generated image. "
            "Codex may have declined or used a different tool. See output above."
        )

    saved = saved[:expected] if expected else saved

    if args.command == "edit":
        dests = resolve_outputs(args.out, 1, label)
    else:
        dests = resolve_outputs(args.out, len(saved), args.prompt)

    final: list[Path] = []
    for src, dest in zip(saved, dests):
        dest = unique_dest(dest, args.force)
        shutil.copy2(src, dest)
        final.append(dest)
        print(f"[codex-imagegen] wrote {dest}")

    print()
    for p in final:
        print(p.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
