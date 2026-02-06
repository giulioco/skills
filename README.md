# Giulio's Claude Code Skills Collection

A curated collection of Claude Code skills for developers, marketers, and founders. Install with a single command to extend Claude's capabilities with specialized knowledge and workflows.

## Quick Start

Install all skills:
```bash
npx add-skill giulioco/skills
```

Install specific skills only:
```bash
npx add-skill giulioco/skills --skill social-growth-engineer
```

## Available Skills

### 🎨 nano-banana-prompt

Master prompt engineering for Nano Banana Pro (Gemini) image generation.

**What it does**: Comprehensive guide for crafting highly effective prompts for Nano Banana Pro. Provides proven patterns, technical specifications, JSON structuring, and identity preservation techniques based on analyzing 60+ successful prompts.

**Use when**:
- Generating photorealistic portraits
- Creating product photography and e-commerce mockups
- Building creative experiments (3D renders, dioramas, surreal effects)
- Crafting era-specific aesthetics (Y2K, 2000s, 1990s)
- Editing and transforming images
- Preserving facial identity across transformations

**Knowledge includes**:
- Identity preservation techniques
- Technical specifications (cameras, lenses, lighting, film stocks)
- 5 comprehensive reference guides (photorealism, creative experiments, product/commercial, editing, JSON templates)
- Era-specific templates (2000s mirror selfie, Y2K scrapbook, 1990s flash photography)
- Quick reference templates for common use cases
- Advanced techniques (multi-element scenes, negative prompts, text integration)

**Size**: 38 KB (SKILL.md + 5 reference files)

[View Details →](skills/nano-banana-prompt/)

---

### 🚀 social-growth-engineer

Master viral app growth through organic social media marketing.

**What it does**: Teaches Claude everything about growing consumer apps virally through TikTok, Instagram Reels, and YouTube Shorts. Based on analyzing 100+ successful app launches generating billions of views and millions in monthly revenue.

**Use when**:
- Launching or growing a consumer app
- Creating viral content strategies
- Building UGC ambassador networks
- Optimizing monetization and conversion
- Analyzing competitor growth tactics

**Knowledge includes**:
- 100+ real case studies with verified metrics ($10K to $5.5M ARR)
- 50+ proven hook formulas
- 30+ video format templates
- Platform-specific tactics (TikTok, Instagram, YouTube)
- Niche playbooks (study apps, dating, fitness, Bible, AI companions, travel)
- Complete growth frameworks and scaling strategies

**Size**: 91 KB (SKILL.md + 3 reference files)

[View Details →](skills/social-growth-engineer/)

---

### 📈 postbridge-social-growth

Organic growth coach using the Post Bridge methodology.

**What it does**: Acts as a personalized organic growth coach for apps, products, and businesses seeking traffic from TikTok and Instagram short-form video. Based on the Post Bridge system that generated 500M+ views, 132K+ downloads, and $33K+ revenue with zero paid ads.

**Use when**:
- Starting organic social media growth from scratch
- Warming up new TikTok/Instagram accounts
- Finding winning content formats (content-market fit)
- Converting views into app downloads or customers
- Writing conversion-optimized social media bios
- Riding trends for momentum
- Scaling to multiple accounts and platforms

**Knowledge includes**:
- Complete 30-day growth roadmap
- 7-day account warmup protocol
- Content-market fit testing framework
- Conversion funnel optimization (views → downloads)
- Trend identification and adaptation playbook
- Three-phase scaling framework
- Bio writing formulas and CTA strategies

**Size**: 12 KB (SKILL.md + 1 reference file)

[View Details →](skills/postbridge-social-growth/)

---

## Installation

### Install All Skills

```bash
npx add-skill giulioco/skills
```

This installs all skills in the collection to your `~/.claude/skills/` directory.

### Install Specific Skills

List available skills first:
```bash
npx add-skill giulioco/skills --list
```

Then install only what you need:
```bash
npx add-skill giulioco/skills --skill social-growth-engineer
```

### Install Globally

```bash
npx add-skill -g giulioco/skills
```

### Non-Interactive Mode

```bash
npx add-skill giulioco/skills -y
```

## Usage

Once installed, skills are available in Claude Code:

### Automatic Invocation

Claude automatically activates skills when you ask relevant questions:

```
How do I grow my app virally?
What hooks work for dating apps?
Help me launch in 30 days
```

### Manual Invocation

Invoke a skill manually with slash commands:

```
/social-growth-engineer
```

Then ask your questions.

### List Your Skills

In Claude Code, type `/` to see all available skills.

## Repository Structure

```
skills/
├── README.md                       # This file
├── LICENSE                         # Apache 2.0
├── CONTRIBUTING.md                 # Contribution guidelines
├── .gitignore
└── skills/
    ├── nano-banana-prompt/         # Nano Banana Pro prompt engineering
    │   ├── SKILL.md                # Main skill file
    │   └── references/             # Supporting documentation
    │       ├── photorealism-portraits.md
    │       ├── creative-experiments.md
    │       ├── product-commercial.md
    │       ├── editing-transformation.md
    │       └── json-structure-guide.md
    ├── social-growth-engineer/     # Viral app growth
    │   ├── SKILL.md                # Main skill file
    │   └── references/             # Supporting documentation
    │       ├── complete-playbook.md
    │       ├── hooks-and-formats.md
    │       └── case-studies.md
    └── postbridge-social-growth/   # Post Bridge organic growth coach
        ├── SKILL.md                # Main skill file
        └── references/             # Supporting documentation
            └── methodology.md
```

## Skills Roadmap

**Coming Soon**:
- 📊 **data-analyst**: Advanced data analysis and visualization workflows
- 🎨 **design-system**: Building and maintaining design systems
- 🔧 **devops-expert**: Infrastructure, CI/CD, and deployment strategies
- 📝 **technical-writer**: Creating clear technical documentation

Want to see a specific skill? [Open an issue](https://github.com/giulioco/skills/issues) with your suggestion!

## Contributing

We welcome contributions! Whether you want to:
- Add new case studies to existing skills
- Create entirely new skills
- Fix errors or improve documentation
- Share your successful strategies

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Development

### Testing Skills Locally

Clone and test before installation:

```bash
git clone https://github.com/giulioco/skills.git
cd skills
npx add-skill .
```

Test the skill in Claude Code by asking relevant questions.

### Creating New Skills

1. Create a new directory in `skills/`:
   ```bash
   mkdir -p skills/my-new-skill
   ```

2. Create `SKILL.md` with proper frontmatter:
   ```yaml
   ---
   name: my-new-skill
   description: Clear description of what this skill does
   ---

   # Skill Content

   Instructions for Claude...
   ```

3. Test locally with `npx add-skill .`

4. Submit a PR!

See the [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills.md) for detailed skill authoring guidelines.

## License

This collection is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

Individual skills may have additional attributions in their reference materials.

## Acknowledgments

**social-growth-engineer** is built from analyzing the [Social Growth Engineer](https://socialgrowth.engineer) newsletter archive. All case studies and metrics are from real apps and verified sources.

## Support

- **Issues**: [GitHub Issues](https://github.com/giulioco/skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/giulioco/skills/discussions)
- **Documentation**: [Claude Code Skills Docs](https://code.claude.com/docs/en/skills.md)

## Links

- [Claude Code Documentation](https://code.claude.com/)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [add-skill Tool](https://add-skill.org/)

---

**Install now**: `npx add-skill giulioco/skills`

Built with ❤️ for the Claude Code community
