---
name: learn-craft
description: Generate a deep, book-grounded skill for any subject the user wants to master. Researches the canonical books on the topic, downloads them as PDFs (using the bundled `scripts/libgen.py` downloader), reads them in parallel via subagents, and synthesizes everything into a new installed skill with progressive disclosure (a tight SKILL.md plus per-book deep-dive references). Trigger whenever the user says they want to "learn X", "master X", "build a skill for X", "study X", "get smarter at X", "make me a skill on X", "I want to be good at X", "teach me X", "create a coach for X", or asks for help internalizing the canonical thinking on a craft, discipline, methodology, or domain. Don't trigger for "make a skill that does Y" (workflow automation — use /skill-creator). Trigger for "make a skill that helps me think like Y" (knowledge synthesis — that's this skill).
---

# learn-craft

Build a working, book-grounded skill on any craft the user wants to master.

The shape of the output mirrors the `ultimate-sales` skill in this repo: one tight `SKILL.md` with operating principles and a diagnose-first loop, plus a `references/` folder containing per-book deep-dives that load only when needed. The user gets a coach they can converse with, not a pile of bullet points.

## What's bundled

The book-fetching script (`scripts/libgen.py`) is bundled here — no separate install required. It's a stdlib-only Python script that searches libgen.li, picks the best complete English PDF, and saves it locally.

## When to use

Trigger when the user wants the canonical thinking on a topic distilled into something they can act on. Examples:
- "I want to learn investing" → topic = investing
- "make me a skill on negotiation"
- "I want to get really good at writing"
- "create a coach for product strategy"

Don't trigger for:
- Pure workflow automation ("make a skill that scrapes X") → that's `/skill-creator`.
- Single-book summaries ("summarize Atomic Habits") → just read the file.
- Already-existing skills (check `~/.claude/skills/` first; if a skill on this topic exists, ask whether to extend it or replace it).

## The four-stage process

1. **Scope the craft** — confirm the topic and pick 4 canonical books.
2. **Download** — fetch each book as a PDF via the bundled `scripts/libgen.py`.
3. **Read in parallel** — spawn 4 subagents, one per book, each producing a structured learnings document.
4. **Synthesize** — merge the learnings into a single new skill with progressive disclosure.

Track these as four todos via TaskCreate so progress is visible to the user. Each stage is described below.

---

## Stage 1 — Scope the craft

If the user didn't name the topic, ask: *"What craft do you want to learn?"* Keep it open — they might say "investing", "Stoic philosophy", "negotiation", "Olympic weightlifting".

Once you have the topic, pick 4 canonical books. Use **WebSearch** with queries like:
- `"best books on <topic>" canonical`
- `"<topic>" foundational reading list`
- `"<topic>" recommended books site:reddit.com OR site:hacker news` (community wisdom often beats SEO listicles)

**How to choose 4 books:**
- Prefer **canonical/foundational** texts over recent bestsellers, unless the field is fast-moving (then mix one recent).
- Prefer **practitioner-written** over academic surveys — the user wants to *do* the thing, not write a paper about it.
- Cover **different angles**: theory, practice, contrarian, biography/case-study. A Stoic skill might be Aurelius (primary source), Holiday (modern bridge), Pigliucci (philosophical defense), Robertson (psychological application).
- **Avoid duplication** — three books on the same author's framework is wasteful.

Present the 4 books to the user as `Title — Author (year)` with a one-line "why this one" for each. Ask: *"Look right? Swap any?"* Wait for confirmation before downloading. This is the cheapest moment to course-correct — once we've downloaded and read, swapping a book costs minutes.

If the user declines a book, propose a replacement and reconfirm. If they want fewer than 4 (e.g., "just 2 is fine"), proceed with what they want — the rest of the pipeline scales linearly.

---

## Stage 2 — Download

Create a working directory: `~/.claude/skills/<slug>/source-books/`. Use a kebab-case slug derived from the topic (e.g., "investing", "stoic-philosophy", "negotiation").

For each book, call the bundled script directly. It lives at `scripts/libgen.py` next to this SKILL.md, so the path is the directory containing this file:

```bash
python3 ~/.claude/skills/learn-craft/scripts/libgen.py "<title>" \
  --out ~/.claude/skills/<slug>/source-books \
  --lang english
```

Run them in parallel by sending multiple Bash calls in a single message. Each download takes ~5–15 seconds.

**The script's behavior at a glance** (full docs in the comments at the top of `scripts/libgen.py`):
- Searches libgen.li with the given title (forwarded to libgen's fuzzy server-side match).
- Filters to complete PDFs (rejects `0` or `0/N` page counts that indicate unscanned/partial copies).
- Filters to English by default; non-English results get marked `⚠ off-language` and are not auto-downloaded. Override with `--lang any` or `--lang italian|spanish|french|german|...`.
- Ranks results: complete > derivative-free (workbook/summary penalty) > title-keyword overlap > most pages > most recent year > smallest size.
- Follows the libgen.li → CDN redirect, saves to `--out` with the filename from the server's `Content-Disposition`.
- Useful flags: `--list` (print top 5 candidates without downloading), `--pick N` (choose a non-default candidate by index), `--author NAME` (only add this if the title alone is ambiguous — extra words tighten libgen's AND filter and can drop legitimate matches), `--year YYYY` (same caveat).
- Exit codes: `0` success / list-only, `1` no acceptable PDF, `2` network or HTTP error.
- On success, the saved file path is the only thing on stdout — everything else goes to stderr, so you can capture it.

**Failure modes to handle:**
- **No English PDF found** (exit code 1, "no english PDF found"): try once with the title alone (drop subtitle); if still nothing, ask the user whether to (a) accept an alternate edition with `--lang any`, (b) substitute a different book on the same topic, or (c) skip and proceed with three.
- **HTTP errors** (exit code 2): retry once after a few seconds — libgen.li is intermittently flaky. If still failing, escalate.
- **Wrong book** (e.g., a workbook or summary slipped through): the script ranks against derivatives, but if the saved filename clearly isn't the real book, rerun with `--list` and `--pick N` after the user reviews.

After Stage 2, confirm with the user: list saved file paths and page counts. *"Got all four — ready to read them?"*

---

## Stage 3 — Read in parallel

Spawn one **general-purpose** subagent per book in a single message (parallel execution). Each subagent gets the same task template:

```
Read the PDF at <absolute-path>. This is "<title>" by <author>.

Your job: produce a structured learnings document at
~/.claude/skills/<slug>/source-books/<book-slug>-learnings.md
that a future skill author can use to build a coaching skill
on <topic>.

The document MUST contain these sections, in this order:

1. **Core thesis** (3-5 sentences) — what is this book's central claim?
   What does it think most practitioners get wrong?

2. **Operating principles** (5-10 numbered bullets) — the rules the
   author would tattoo on a practitioner's forearm. Each bullet:
   one-sentence rule, one-sentence why, one phrase for when it applies.

3. **Frameworks and models** (the named tools — e.g., "SPIN", "OODA loop",
   "margin of safety"). For each: what it is, when to use, the steps,
   and the most common misapplication.

4. **Diagnostic questions** — the questions the author would ask a
   practitioner to figure out what stage of the work they're in and
   what move the moment rewards. These become the heart of the future
   skill's diagnose-first loop.

5. **Tactical playbook** — concrete moves, scripts, checklists,
   templates. The "do this, say this, write this" stuff.

6. **Common failure modes** — what practitioners do wrong, why, and
   the fix. Phrased as anti-patterns.

7. **Memorable case studies / examples** — 3-5 vivid stories or
   examples from the book that illustrate the principles. These
   make the future skill stick.

8. **What this book uniquely contributes** — what would be lost if
   this book were dropped from the canon? (This guides synthesis —
   if two books say the same thing, the synthesizer can drop the
   redundant one.)

Don't summarize the book chapter-by-chapter. Synthesize. The audience
is a skill author, not a student writing a book report. Be specific,
quote sparingly, and skip filler.

Aim for 800-1500 words. Tight is better than complete.
```

Use the `Plan` agent type only if you also want architectural review; for pure read-and-extract, `general-purpose` is right. Each agent reads its PDF (subagents have Read tool which handles PDFs natively) and writes one markdown file.

While the subagents run, you can pre-draft the synthesis structure (Stage 4 outline) so you're ready when they return. Don't wait idle.

---

## Stage 4 — Synthesize

Once all four learning docs exist, write the new skill at `~/.claude/skills/<slug>/`:

### File layout

```
~/.claude/skills/<slug>/
├── SKILL.md                          # ≤500 lines, always loaded
├── source-books/                     # raw PDFs + raw learnings
│   ├── <book-1>.pdf
│   ├── <book-1>-learnings.md
│   └── ...
└── references/                       # progressive-disclosure deep dives
    ├── <book-1>-deep-dive.md         # one per book, loaded on demand
    ├── <book-2>-deep-dive.md
    ├── <book-3>-deep-dive.md
    ├── <book-4>-deep-dive.md
    └── playbooks.md                  # cross-book tactical scripts
```

Keep the `source-books/` directory — the raw PDFs and per-book learning notes are useful for future re-synthesis if the skill needs revising. They don't get loaded into context unless explicitly read.

### SKILL.md structure (mandatory template)

```markdown
---
name: <slug>
description: [one paragraph — what the skill does, when to trigger, with
              specific phrases. Pushy: list the synonyms and adjacent
              topics. Mention the books synthesized so the user knows
              the provenance. End with what NOT to trigger on.]
---

# <Topic Title>

[2-3 sentences framing the skill's worldview — what's the central
synthesis across these four books? What would the merged author tell
a beginner in one sentence?]

If a single instruction has to fit on a sticky note, it's this: **<one
imperative sentence>**.

---

## Core operating principles (read these every time)

[8-12 numbered principles, each 2-4 sentences. Each one cites the
book(s) it comes from in parentheses at the end. Order: most
foundational first. These are the worldview — non-negotiable.]

---

## The diagnose-first loop

[A short flowchart-style section: the questions to ask FIRST before
applying any tactic. This is the crucial "don't pitch before
diagnosing" moment, adapted to this craft.

Format:

1. **What stage of the work are you in?** [list 3-5 stages]
2. **What does this stage reward?** [matrix or table mapping stage →
   moves]
3. **What's the diagnostic question for this stage?** [the question
   that, if answered honestly, tells you what to do next]
]

---

## Frameworks (when each one shines)

[For each major framework from the books — 4-8 total — give:
- Name
- One-sentence what-it-is
- The trigger ("use this when…")
- The steps
- The trap (the most common misapplication)

Keep each to ~10 lines. The deep dive lives in references/.]

---

## Tactical playbook

[The concrete moves. Scripts, templates, checklists. This is what
the user will quote-grep when they're actually doing the thing.]

---

## When to go deeper

The four books each contribute something the others don't. If you
need to drill into one, read the corresponding reference:

- `references/<book-1>-deep-dive.md` — <what's uniquely there>
- `references/<book-2>-deep-dive.md` — <what's uniquely there>
- `references/<book-3>-deep-dive.md` — <what's uniquely there>
- `references/<book-4>-deep-dive.md` — <what's uniquely there>

Use these when the SKILL.md guidance feels too generic or you want
the original framing.

---

## Common failure modes

[5-10 anti-patterns from the books, each with the fix. This is where
the synthesized wisdom about how practitioners go wrong lives.]
```

### references/<book-N>-deep-dive.md

For each book, write a 200-400 line deep-dive that goes beyond what's in SKILL.md. This is where the unique contribution of each book lives. Frontmatter:

```markdown
---
book: <Title>
author: <Author>
year: <Year>
loaded_when: <one-sentence trigger — e.g., "drilling into how to handle objections" or "needing scripts for hard conversations">
---

# <Title> — Deep Dive

[Open with the book's distinctive contribution — what's lost if we
skip this book.]

## Sections (mirror the per-book learnings doc):
- Core thesis
- Operating principles (full version, not pruned)
- Frameworks (with examples and edge cases)
- Tactical playbook (full scripts, full checklists)
- Case studies
- The author's voice (a few short quotes that capture their tone — useful for skill consumers who want to channel the author's mindset)
```

The `loaded_when` field is what tells future-Claude when to read this file — make it specific and action-oriented.

### references/playbooks.md

A cross-book tactical layer: situations that span multiple books. E.g., for a sales skill, "handling a stalled deal" pulls from Voss + Blount + Keenan. For a writing skill, "fixing a flabby first draft" pulls from Strunk + Zinsser + King.

### Synthesis principles

When merging four books into one SKILL.md:

1. **Find the spine.** What's the through-line across all 4? That's the worldview at the top.
2. **Promote the consensus, footnote the disagreements.** If 3 books say discovery > closing and 1 says the opposite, lead with the consensus and note the dissent ("Some practitioners (e.g., X) argue the opposite — see deep dive").
3. **Drop redundancy ruthlessly.** If two books contribute the same framework under different names, pick the cleaner name and cite both.
4. **Keep the author's voice.** Don't generic-ify everything into corporate-speak. If Voss says "tactical empathy," don't rename it "compassionate inquiry."
5. **Lead with diagnosis, follow with tactics.** Mirror the `ultimate-sales` structure: principles → diagnostic loop → frameworks → playbook → failure modes. This shape works because it forces the user to think before acting.
6. **Length budget:** SKILL.md 300–500 lines. Each deep-dive 200–400 lines. Playbooks.md 100–250 lines. If you blow past, the skill is doing too much — split it.
7. **Description-field optimization (the YAML frontmatter):** be pushy and specific. List 8-15 trigger phrases. List explicit DO-NOT-trigger contexts. The description is the only thing that decides whether the skill fires in future conversations — don't shortchange it.

---

## After synthesis — verify and announce

1. **Smoke-test:** read the SKILL.md you just wrote with fresh eyes. Does it read like a coach speaking, or like a book report? If the latter, rewrite with imperatives ("Diagnose first" not "It is important to diagnose first").
2. **Check the file tree** — confirm the structure exists and the slug matches what's in the frontmatter `name:` field.
3. **Tell the user:**
   - The path: `~/.claude/skills/<slug>/`
   - The 4 books synthesized
   - One sentence per book on what each uniquely contributes
   - The trigger phrases that will fire the skill
   - The note that the skill is now live in this session (Claude Code reloads skills on each turn).

---

## Failure modes for the orchestrator itself

- **Topic is too broad** ("I want to learn business"): ask the user to narrow ("Sales? Strategy? Operations? Founding?"). A 4-book canon needs a specific craft.
- **Topic is too narrow / niche** ("I want to learn how to use the GOAT chess engine"): there may be no 4 canonical books. Offer to (a) widen the scope, or (b) build the skill from web research + tutorials instead, skipping the libgen step.
- **Books don't exist on libgen** (rare for popular topics, common for niche ones): proceed with what's available; if fewer than 2 are obtainable, escalate to the user rather than synthesizing thin gruel.
- **Subagent fails to read PDF** (corrupt download, encoding issue): re-download the book once. If still failing, swap for an alternate.
- **Synthesis comes out flat** — sign you collapsed the books into platitudes. Re-read the per-book learnings, find the *disagreements* and the *vivid examples*, and rebuild around those.
