---
name: learn-craft
description: Generate a deep, book-grounded skill for any subject the user wants to master. Researches the canonical books on the topic, downloads them as PDFs (using the bundled `scripts/libgen.py` downloader), reads them in parallel via subagents, then synthesizes the books across each other into a concept-organized knowledge base — not a shelf of book summaries. Output is a tight `SKILL.md` plus per-concept `frameworks/` files (the working knowledge base, organized by idea) plus per-book `references/` deep-dives (the citation layer). Trigger whenever the user says they want to "learn X", "master X", "build a skill for X", "study X", "get smarter at X", "make me a skill on X", "I want to be good at X", "teach me X", "create a coach for X", or asks for help internalizing the canonical thinking on a craft, discipline, methodology, or domain. Don't trigger for "make a skill that does Y" (workflow automation — use /skill-creator). Trigger for "make a skill that helps me think like Y" (knowledge synthesis — that's this skill).
---

# learn-craft

Build a working, book-grounded skill on any craft the user wants to master.

The shape of the output mirrors the `ultimate-sales` skill: a tight `SKILL.md` (always loaded), a `frameworks/` folder organized by **concept** (the synthesized knowledge base — this is where the real value lives), and a `references/` folder organized by **book** (citation layer). The user gets a coach that thinks in concepts, not a shelf of book summaries.

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

## The mental model — concepts, not books

The single most important thing to understand about this skill: **the output is organized by concept, not by book.**

The wrong shape:

```
my-skill/
└── references/
    ├── book-1-summary.md     ← "what does Author 1 say?"
    ├── book-2-summary.md     ← "what does Author 2 say?"
    └── book-3-summary.md     ← "what does Author 3 say?"
```

This is a bookshelf, not a skill. To answer any real question the model has to read all three files and re-synthesize on the fly — every single time.

The right shape:

```
my-skill/
├── SKILL.md                       ← worldview + diagnose-first loop
├── frameworks/                    ← THE KNOWLEDGE BASE — organized by concept
│   ├── diagnose-first.md          ← cross-book; cites multiple authors
│   ├── tactical-empathy.md        ← named concept; main author + supporting
│   ├── question-arsenal.md        ← cross-book question taxonomy
│   └── ...
└── references/                    ← citation layer — read-on-demand
    ├── book-1.md                  ← deep-dive into Book 1's distinctive contribution
    ├── book-2.md
    └── ...
```

Now `frameworks/diagnose-first.md` *is* the synthesized concept — already cross-referenced, already prioritized, already de-duplicated. The `references/` layer is for when someone wants to drill into one author's original framing or hear their voice. Most queries never need to crack the references — the frameworks are sufficient on their own.

**This distinction is what separates a real skill from a glorified summary.** The synthesis stage (Stage 4) is where this happens. Don't skip it, don't shortcut it.

## The five-stage process

1. **Scope the craft** — confirm the topic and pick 4 canonical books.
2. **Download** — fetch each book as a PDF via the bundled `scripts/libgen.py`.
3. **Read in parallel** — spawn 4 subagents, one per book, each producing a structured per-book learnings document (working notes — not the final product).
4. **Synthesize** — extract concepts that span multiple books, name them, organize them. **This is the stage that's easy to skip and that ruins the skill if skipped.** Most of the orchestrator's thinking happens here.
5. **Author** — write the SKILL.md, frameworks/, and references/ from the synthesis.

Track these as five todos via TaskCreate so progress is visible to the user. Each stage is described below.

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
- **Avoid duplication** — three books on the same author's framework is wasteful. But *do* allow some overlap: synthesis only works if the books talk to each other on shared concepts.

Present the 4 books to the user as `Title — Author (year)` with a one-line "why this one" for each. Ask: *"Look right? Swap any?"* Wait for confirmation before downloading. This is the cheapest moment to course-correct.

If the user declines a book, propose a replacement and reconfirm. If they want fewer than 4 (e.g., "just 2 is fine"), proceed with what they want — the rest of the pipeline scales linearly.

---

## Stage 2 — Download

Create the working layout: `~/.claude/skills/<slug>/notes/`. Use a kebab-case slug derived from the topic (e.g., "investing", "stoic-philosophy", "negotiation"). The `notes/` directory will hold both the raw PDFs and the per-book learning files — these are working materials, not the final product, and the name reflects that.

For each book, call the bundled script directly:

```bash
python3 ~/.claude/skills/learn-craft/scripts/libgen.py "<title>" \
  --out ~/.claude/skills/<slug>/notes \
  --lang english
```

Run them in parallel by sending multiple Bash calls in a single message. Each download takes ~5–15 seconds.

**The script's behavior at a glance** (full docs in the comments at the top of `scripts/libgen.py`):
- Searches libgen.li with the given title (forwarded to libgen's fuzzy server-side match).
- Filters to complete PDFs (rejects `0` or `0/N` page counts that indicate unscanned/partial copies).
- Filters to English by default; non-English results get marked `⚠ off-language` and are not auto-downloaded. Override with `--lang any` or `--lang italian|spanish|french|german|...`.
- Ranks results: complete > derivative-free (workbook/summary penalty) > title-keyword overlap > most pages > most recent year > smallest size.
- Follows the libgen.li → CDN redirect, saves to `--out` with the filename from the server's `Content-Disposition`.
- Useful flags: `--list` (print top 5 candidates without downloading), `--pick N` (choose a non-default candidate by index), `--author NAME` (only add if the title alone is ambiguous — extra words tighten libgen's AND filter), `--year YYYY` (same caveat).
- Exit codes: `0` success / list-only, `1` no acceptable PDF, `2` network or HTTP error.
- On success, the saved file path is the only thing on stdout — everything else goes to stderr.

**Failure modes to handle:**
- **No English PDF found** (exit code 1): try once with the title alone (drop subtitle); if still nothing, ask the user whether to (a) accept an alternate edition with `--lang any`, (b) substitute a different book on the same topic, or (c) skip and proceed with three.
- **HTTP errors** (exit code 2): retry once after a few seconds — libgen.li is intermittently flaky.
- **Wrong book** (a workbook or summary slipped through): rerun with `--list` and `--pick N` after the user reviews.

After Stage 2, confirm with the user: list saved file paths and page counts. *"Got all four — ready to read them?"*

---

## Stage 3 — Read in parallel (working notes)

Spawn one **general-purpose** subagent per book in a single message (parallel execution). The output of this stage is **working notes** — raw structured extraction, not the final knowledge base. Be explicit with the subagent that the goal is to harvest material that the synthesis stage will then re-organize.

### Read the whole book — non-negotiable

The single most common failure of this stage: the subagent skims the table of contents, picks "the important chapters," and writes notes from those alone. This is **never acceptable.** The reason this skill exists at all is that the user can't summon four books worth of cross-pollinated thinking from chapter highlights — and neither can a subagent.

Enforce this in three ways:

1. **Use the Read tool's `pages` argument to walk the whole PDF.** A 300-page book read in 20-page chunks is 15 reads — perfectly fine for a subagent. Tell the subagent: "Read the entire PDF cover to cover, in chunks. Do not skip chapters. Do not 'read just the important parts.' Treat skipping as a failure mode you must avoid."
2. **Require evidence of full-book coverage in the output.** The notes file must include a "Coverage trace" section at the bottom listing every chapter or major section read, with a one-line note per section. If a section is missing, the orchestrator rejects the notes and respawns.
3. **Tell the subagent why.** Skimming feels efficient but produces shallow synthesis. The author's most important moves are often buried in mid-book chapters where they're applying the framework to messy real cases — exactly the material that lets you separate a sloganized concept from the operating concept. The point of having a subagent is that *it* pays the cost of full reading so the user doesn't have to.

The subagent has its own context window separate from the orchestrator's. Reading a full book consumes ~50–150K tokens of subagent context — well within budget.

### The read-and-extract task template

Each subagent gets this task template:

```
Read the PDF at <absolute-path> COVER TO COVER. This is "<title>" by <author>.

CRITICAL: read the entire book. Walk the PDF in chunks using the Read
tool's `pages` argument (e.g., pages: "1-20", then "21-40", etc.).
Do not skip chapters. Do not read only "the important parts." If you
catch yourself thinking "I've got the gist, I can stop now" — keep
reading. The whole point of this task is that you, not the orchestrator
or the user, pay the cost of full reading. Skimming is the failure mode.

Your output is WORKING NOTES that will be synthesized later — not a
standalone document. Bias toward extraction and faithfulness to the
author's framing. The synthesis stage will organize concepts across
books; your job is to give that synthesis the richest possible raw
material from THIS book.

Write to ~/.claude/skills/<slug>/notes/<book-slug>-notes.md with these
sections, in this order:

1. **Core thesis** (3-5 sentences) — what is this book's central claim?
   What does it think most practitioners get wrong?

2. **Named concepts and frameworks** — the author's named tools (e.g.,
   "SPIN", "OODA loop", "margin of safety", "tactical empathy"). For
   each: the exact name the author uses, what it is, when it applies,
   the steps, the most common misapplication. PRESERVE THE AUTHOR'S
   ORIGINAL TERMS — don't paraphrase "tactical empathy" into "active
   listening." The synthesis stage decides which terms survive.

3. **Operating principles** (5-12 numbered) — the rules the author
   would tattoo on a practitioner's forearm. Each: one-sentence rule,
   one-sentence why, one phrase for when it applies.

4. **Diagnostic questions** — the questions the author would ask a
   practitioner to figure out what stage of the work they're in.

5. **Tactical playbook** — concrete moves, scripts, checklists,
   templates. The "do this, say this, write this" stuff. Quote
   verbatim where the wording matters (Voss's "no-oriented questions"
   lose their power if paraphrased).

6. **Disagreements / contrarian takes** — anywhere the author
   explicitly contradicts conventional wisdom or other writers in
   this field. The synthesis stage uses these to surface productive
   tensions.

7. **Common failure modes** — what practitioners do wrong, why, and
   the fix. Anti-patterns.

8. **Memorable case studies** — 3-5 vivid stories or examples that
   illustrate the principles. These give the future skill teeth.

9. **Author's voice** — 2-3 short verbatim quotes (one or two
   sentences each) that capture how the author talks. The synthesis
   may pull these into the references/ deep-dive.

10. **What this book uniquely contributes** — what would be lost if
    this book dropped out of the canon? Be specific: name 2-3 things.

11. **Coverage trace** — at the END of the notes file, list every
    chapter (or major section) of the book in order, with a one-line
    note per chapter on what was in it and what (if anything) you
    pulled into the sections above. This is your proof-of-read. If
    you cannot produce this list, you didn't read the whole book —
    go back and finish.

Don't summarize chapter-by-chapter in sections 1-10 (that's what the
coverage trace is for). In sections 1-10, synthesize across the book.
Don't pad. Be specific, quote sparingly but exactly where the wording
carries the idea, skip filler.

Aim for 1500-3000 words across sections 1-10, plus the coverage trace.
Tight is better than complete in the synthesis sections; thorough beats
tight in the coverage trace.
```

### Verifying the read happened

When a subagent returns, check its notes file for the **Coverage trace** section before accepting it. If the trace covers fewer than ~80% of the book's chapters, or if multiple chapters are noted as "skipped" or "skimmed," respawn the subagent with explicit instructions to read the missing material. Do not let half-read notes flow into Stage 4 — the synthesis is only as good as its raw material.

While the subagents run, draft the synthesis spine (Stage 4 outline) so you're ready when they return. Don't wait idle.

---

## Stage 4 — Synthesize (the most important stage)

Once the per-book notes exist, **stop and think.** Don't jump to writing the skill yet. The output of this stage is a `frameworks/` directory of concept files — synthesized across books, organized by idea.

### Why this stage exists

If you skip this and go straight from notes → SKILL.md, you'll write a "shelf of book summaries" disguised as a skill. The reader has to do the synthesis on every query. Bad. The whole point is to do the hard work *once* in the skill so future invocations are cheap.

### Step 4a: Read all the per-book notes together

Read every `notes/<book-slug>-notes.md` file. Hold them all in context simultaneously. This is non-negotiable — you cannot synthesize what you haven't compared.

### Step 4b: Build the concept index

In your head (or as a scratch file), list every named concept that appears across the four books. For each, note:

- Which books mention it (even under different names — "tactical empathy" / "active listening with feeling-labels" / "rapport via labeling")
- Whether the books agree, disagree, or talk past each other
- Whether the concept has a *clean canonical name* (the term that travels best — usually the most evocative one, often coined by the most distinctive author)
- The concept's role in the craft: is it a *worldview* belief, an *operating principle*, a *named framework*, a *diagnostic*, a *tactic*, or an *anti-pattern*?

Spot the **spine** — the single through-line that all four books point at, even when they don't share vocabulary. For sales it's *diagnose before pitching*. For investing it might be *price ≠ value, time arbitrages temperament*. For weight training it might be *progressive overload + recovery is the entire game; everything else is a knob on those two dials*. The spine becomes the SKILL.md's opening.

### Step 4c: Choose the concept files

A concept earns its own `frameworks/<name>.md` file when:
- It appears in 2+ books (cross-book synthesis is meaningful), OR
- It's distinctive enough that the skill would be incomplete without it (a single-book concept can earn a file if it's foundational), OR
- It's the kind of thing the user will want to *load on demand* during a real task ("how do I run a discovery call?" → read `frameworks/discovery.md`).

Aim for **5–9 concept files** in `frameworks/`. Fewer means you under-synthesized; more means you fragmented.

For each concept file, the structure mirrors `ultimate-sales/frameworks/diagnose-first.md`:

```markdown
# <Concept Name>

[2-4 sentence framing — what's the unified concept across the books?
Why does it matter? Lead with the through-line, not with citations.]

This document is the deeper version of <where-it-lives-in-SKILL.md>.

---

## [Operating sub-section, e.g., "The five stages" or "The four
   diagnostic questions"]

[Synthesized content. Cite authors inline when one author's framing
is most precise: "Rackham's most underrated insight: small-sale
tactics actively damage large sales." Don't open every paragraph
with "According to X..." — the citations support the concept; the
concept doesn't support the citations.]

---

## When this fails

[Anti-patterns specific to this concept. Cross-cite books where
useful.]

---

## Quick reference

[Tables, checklists, scripts. The thing the user will quote-grep
during real work.]

---

## Going deeper

- For the original framing of <X>, see `references/<book>.md`
- For an opposing view on <Y>, see `references/<book>.md`
```

The hallmark of a good concept file: **someone reading it cold should not be able to tell which book "owns" the concept.** It's a synthesized idea now. Citations support; they don't dominate.

### Step 4d: Choose the per-book deep dives

For `references/<book>.md`, the question is: **what does this book contribute that the frameworks don't capture?** Usually:
- The book's *worldview* (the lens, not the tactics)
- The author's *voice* — verbatim phrasing that carries the idea
- *Distinctive* case studies and stories
- The author's *most original* framework, in their own framing
- Anything that the synthesis had to flatten or compromise on

A reference is *not* a summary of the book. It's the **delta** between what the book contributes and what the frameworks already captured. If a reference reads like a book report, you're doing it wrong.

Frontmatter for each:

```markdown
---
book: <Title>
author: <Author>
year: <Year>
loaded_when: <one-sentence trigger that's specific and action-oriented>
---
```

---

## Stage 5 — Author the skill

Now you write the user-facing files. The hard thinking is done; this is the carving stage.

### Final file layout

```
~/.claude/skills/<slug>/
├── SKILL.md                          # ≤500 lines, always loaded
├── frameworks/                       # THE KNOWLEDGE BASE
│   ├── <concept-1>.md                # 200–500 lines each
│   ├── <concept-2>.md
│   ├── ...
│   └── <concept-N>.md                # 5–9 total
├── references/                       # citation layer (per book)
│   ├── <book-1>.md
│   ├── <book-2>.md
│   ├── <book-3>.md
│   └── <book-4>.md
└── notes/                            # working materials, not loaded
    ├── <book-1>.pdf
    ├── <book-1>-notes.md
    └── ...
```

The `notes/` directory is preserved (useful for future re-synthesis when the canon shifts) but never loaded into context.

### SKILL.md template

```markdown
---
name: <slug>
description: [Pushy, specific, ~150-200 words. Lead with the worldview
              ("Master <craft> by..."). List 8-15 trigger phrases. Name
              the books synthesized so the user knows the provenance.
              End with what NOT to trigger on.]
---

# <Topic Title>

[2-3 sentences framing the worldview. What's the spine? What would
the merged author tell a beginner in one sentence?]

If a single instruction has to fit on a sticky note, it's this: **<one
imperative sentence>**.

---

## Core operating principles (read these every time)

[8-12 numbered principles, each 2-4 sentences. Each cites the book(s)
in parentheses at the end where the inheritance matters. Order: most
foundational first. These are the worldview — non-negotiable.]

---

## The diagnose-first loop

[3-7 questions to ask FIRST before applying any tactic. The "stop
before reaching for the tool" moment, adapted to this craft. For
each question: the question itself, then a stage→move table or a
short list of what each answer points to.]

---

## When to load each framework

The knowledge base lives in `frameworks/`. Each file is one concept,
already synthesized across the source books. Load them on demand:

- `frameworks/<concept-1>.md` — <one-sentence trigger>
- `frameworks/<concept-2>.md` — <one-sentence trigger>
- ...

---

## Quick playbook

[The 5-10 most common situations the user will face, with a one-line
prescription each and a pointer to the framework that goes deeper.
This is the index — the actual depth lives in `frameworks/`.]

---

## When the SKILL.md is too generic — go to the source

If you need an author's original framing, the references/ layer
preserves each book's distinctive contribution:

- `references/<book-1>.md` — <what's uniquely there>
- `references/<book-2>.md` — <what's uniquely there>
- ...

---

## Common failure modes

[5-10 cross-book anti-patterns. Each: the failure, why it happens,
the fix, and which framework to load if it's biting you.]
```

### Synthesis principles (apply throughout)

1. **Find the spine.** The opening of SKILL.md is the through-line across all 4 books. Most failed syntheses hedge here ("there are many perspectives on X") instead of committing.
2. **Promote consensus, footnote disagreement.** If 3 books agree and 1 dissents, lead with the consensus and note the dissent in a one-liner ("Some practitioners argue the opposite — see `references/<dissenter>.md`").
3. **Drop redundancy ruthlessly.** Two books with the same concept under different names → pick the cleaner name (often the one with the better metaphor) and cite both.
4. **Keep the author's voice — for the *coined* terms.** "Tactical empathy" stays "tactical empathy" — don't generic-ify it into "compassionate inquiry." But around the named terms, write in the synthesis's own voice.
5. **Lead with diagnosis, follow with tactics.** This shape forces thinking before doing — the most reliable upgrade you can give any practitioner.
6. **Length budget:** SKILL.md 300–500 lines. Each `frameworks/<concept>.md` 200–500 lines. Each `references/<book>.md` 200–500 lines. If you blow past, the skill is doing too much — split or trim.
7. **Pushy description field.** It's the only thing that decides whether the skill fires in future conversations. List 8-15 trigger phrases. List explicit DO-NOT-trigger contexts. Mention the books synthesized.
8. **The smell test for synthesis quality:** read a random `frameworks/<concept>.md` cold. If you can tell which book it came from in the first paragraph, it's not synthesized — it's a per-book summary in disguise. Rewrite.

---

## After authoring — verify and announce

1. **The "concept-organized" smell test:**
   - Open a random `frameworks/<concept>.md`. Does it read like a synthesized concept, or like "Author A says X, Author B says Y, Author C says Z"? If the latter, the synthesis didn't happen — go back to Stage 4.
   - Open the SKILL.md. Does the worldview at the top *commit* to a position, or does it hedge? Hedging is a sign of skipping the spine.

2. **File tree check** — confirm:
   - `frameworks/` exists and has 5–9 concept files
   - `references/` has one file per source book
   - `notes/` still has the raw PDFs and per-book notes (for future re-synthesis)
   - The slug in `name:` frontmatter matches the directory name

3. **Tell the user:**
   - The path: `~/.claude/skills/<slug>/`
   - The 4 books synthesized, with one sentence per book on what each uniquely contributes
   - The 5–9 frameworks that came out of the synthesis (these are the *real* output)
   - The trigger phrases that will fire the skill
   - The note that the skill is now live in this session (Claude Code reloads skills on each turn).

---

## Failure modes for the orchestrator itself

- **Topic is too broad** ("learn business"): ask the user to narrow ("Sales? Strategy? Operations? Founding?"). A 4-book canon needs a specific craft.
- **Topic is too narrow / niche** ("the GOAT chess engine"): there may be no 4 canonical books. Offer to (a) widen the scope, or (b) build the skill from web research + tutorials, skipping the libgen step.
- **Books don't exist on libgen** (rare for popular topics): proceed with what's available; if fewer than 2 are obtainable, escalate rather than synthesizing thin gruel.
- **Subagent fails to read PDF** (corrupt download, encoding issue): re-download once. If still failing, swap for an alternate.
- **Stage 4 collapsed into Stage 5.** The most common failure: the orchestrator skips the synthesis pass and writes the SKILL.md directly from per-book notes. Symptom: `frameworks/` files that read like book summaries rather than synthesized concepts. Fix: stop, re-read all four notes side-by-side, build the concept index, *then* write `frameworks/`.
- **Synthesis comes out flat / platitudinous** — sign you collapsed disagreements into bromides. Re-read the per-book notes, find the *contrarian takes* and *vivid examples*, and rebuild around productive tensions, not lowest-common-denominator advice.
