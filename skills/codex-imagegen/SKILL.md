---
name: codex-imagegen
description: Generate or edit raster images (photos, illustrations, mockups, logos, product shots, game/UI assets, textures, infographics) using Codex's built-in image_gen tool — driven headlessly through `codex exec`. Billed via the user's ChatGPT/Codex login, so it needs NO OpenAI API key. Use whenever the user wants to create a brand-new image from a text prompt, edit an existing local image (background swap, lighting/weather change, object add/remove, restyle), or produce several image variants. Trigger on "generate an image", "make a picture/illustration/logo/mockup of X", "create a hero image", "edit this image", "change the background of X", "turn this photo into Y", "imagegen", "use codex to make an image". Do NOT use for vector/SVG icon systems, diagrams better built in code/HTML/CSS, or when the user explicitly wants the OpenAI Image API directly (that's the gpt-image CLI path).
---

# codex-imagegen

Generate and edit bitmap images from Claude Code by driving **Codex's built-in `image_gen` tool** through a one-shot `codex exec` run.

## Why this works (the mechanism)

Codex ships a `$imagegen` skill with two modes:

1. **Built-in `image_gen` tool (this skill uses it)** — runs against Codex's own backend using the user's **ChatGPT/Codex login** (`~/.codex/auth.json`). **No `OPENAI_API_KEY` required**, no per-image API billing. It's the default Codex mode.
2. CLI fallback (`scripts/image_gen.py`) — hits the OpenAI Image API directly, needs `OPENAI_API_KEY`. This skill does **not** use it.

The built-in tool is internal to Codex's agent runtime — there is no `codex image` subcommand. But a headless `codex exec "<prompt>"` run **can** invoke it. The wrapper script builds a tightly-scoped prompt that forces Codex to use only the built-in tool, runs `codex exec`, then locates the PNG Codex just wrote under `$CODEX_HOME/generated_images/` and copies it into the working directory with a clean filename.

Source it wraps: `~/.codex/skills/.system/imagegen/` (Codex's installed skill).

## Prerequisites

- `codex` CLI on PATH and **logged in** (`codex login`). Verify: `codex login status` or just run a generation — the wrapper reports a clear error if Codex isn't authed.
- No API key needed. The wrapper explicitly tells Codex *not* to use the API/CLI fallback.

## Usage

The wrapper lives at `scripts/codex_imagegen.py` (resolve its absolute path relative to this SKILL.md).

### Generate

```bash
python3 scripts/codex_imagegen.py generate \
  --prompt "a minimal hero image of a ceramic coffee mug, soft studio lighting, lots of negative space" \
  --out ./hero.png
```

- `--out` accepts a file (`./hero.png`), a directory (`./images/` → auto-named from the prompt), or is omitted (lands in cwd, named from a slug of the prompt).
- `-n 3` generates 3 **distinct** images (one built-in call each). With `-n>1` and a file `--out`, outputs are suffixed `-1`, `-2`, `-3`.
- Existing files are never overwritten unless `--force`; otherwise a `-v2` sibling is written.

### Edit an existing local image

```bash
python3 scripts/codex_imagegen.py edit \
  --image ./photo.png \
  --prompt "change the background to a warm sunset gradient; keep the subject unchanged" \
  --out ./photo-sunset.png
```

The wrapper makes Codex load the local file with its built-in `view_image` tool first, then edit it. Default output (no `--out`) is `<name>-edited.png` in cwd.

### Output

On success the script prints `[codex-imagegen] wrote <path>` lines and then the absolute path(s) on their own line(s). Each run takes ~30–90s (it spins up a Codex agent). Report the final path(s) to the user and, when useful, Read the PNG to show it inline.

## Prompting guidance

The built-in tool renders well from a structured spec. Shape the user's request into: **scene/backdrop → subject → details → constraints**, plus intended use for the right polish level.

- Already-detailed prompt → normalize it, don't pad it.
- Generic prompt → add only tasteful, materially-helpful detail (composition, lighting, intended use). Don't invent extra subjects, brands, slogans, or palettes the user didn't imply.
- Quote exact in-image text verbatim and specify placement/typography.
- For **edits**, state invariants every time: "change only X; keep Y unchanged."
- For many *distinct* assets, issue separate generations — don't ask for one image "containing" all of them.

Use cases the built-in tool handles well: photorealistic scenes, product mockups, UI mockups, infographics, ads/marketing creatives, logos, illustrations, stylized concept art, and edits (object swap, lighting/weather, background replace, restyle, composite).

## Transparent backgrounds

The built-in tool has no native transparency control. For a transparent cutout of a *simple* opaque subject: generate it on a flat `#00ff00` chroma-key background (`#ff00ff` if the subject is green), then key it out locally with Codex's helper:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
  --input <source.png> --out <final.png> \
  --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill
```

Truly hard cases (hair, fur, glass, smoke, soft shadows) need real transparency, which only the OpenAI-API CLI fallback (`gpt-image-1.5 --background transparent`) provides — that requires `OPENAI_API_KEY` and is out of scope for this skill. Tell the user if a request needs it.

## When NOT to use

- Vector/SVG icon or logo *systems* already in the repo — edit those natively.
- Diagrams/wireframes better built deterministically in HTML/CSS/canvas/SVG.
- The user explicitly wants the OpenAI Image API directly with size/quality/fidelity flags — that's Codex's CLI fallback path, not this one.

## Troubleshooting

- **"codex exec exited non-zero" / auth error** → run `codex login`.
- **"Could not find any generated image"** → Codex may have declined the prompt or chosen another tool. The wrapper falls back to diffing `$CODEX_HOME/generated_images/` before/after the run, so this usually only happens on refusal or a true failure; check the printed Codex output.
- **Slow** → normal; each run boots a Codex agent. Use `--timeout` to extend (default 300s).
```
