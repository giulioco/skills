# Publishing Guide for giulioco/skills

This guide walks you through publishing this skills collection to GitHub and making it available via `npx add-skill giulioco/skills`.

## Current Status

✅ Repository initialized at `~/git/skills`
✅ All files committed to git
✅ Ready to push to GitHub

## Repository Contents

```
skills/
├── README.md                       # Main documentation
├── LICENSE                         # Apache 2.0 license
├── CONTRIBUTING.md                 # Contribution guidelines
├── .gitignore                      # Git ignore rules
└── skills/
    └── social-growth-engineer/     # First skill
        ├── SKILL.md                # 5.6 KB
        └── references/
            ├── complete-playbook.md        # 35 KB
            ├── hooks-and-formats.md        # 29 KB
            └── case-studies.md             # 22 KB
```

**Total Size**: ~91 KB of knowledge

## Step 1: Create GitHub Repository

### Option A: Using GitHub CLI (Recommended)

```bash
cd ~/git/skills

# Create repository on GitHub
gh repo create giulioco/skills --public --source=. --description="Claude Code skills collection for developers, marketers, and founders" --push

# This will:
# - Create giulioco/skills on GitHub
# - Add remote origin
# - Push master branch
```

### Option B: Using GitHub Web Interface

1. Go to https://github.com/new

2. Fill in details:
   - **Owner**: giulioco
   - **Repository name**: skills
   - **Description**: Claude Code skills collection for developers, marketers, and founders
   - **Visibility**: Public
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)

3. Click "Create repository"

4. Connect local repository to GitHub:
   ```bash
   cd ~/git/skills
   git remote add origin https://github.com/giulioco/skills.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Verify Installation Works

Test that users can install your skill:

```bash
# Test installation (will install to ~/.claude/skills/)
npx add-skill giulioco/skills

# Or test specific skill
npx add-skill giulioco/skills --skill social-growth-engineer

# List available skills
npx add-skill giulioco/skills --list
```

## Step 3: Test in Claude Code

1. Open Claude Code
2. Type `/` to see if `social-growth-engineer` appears
3. Test automatic invocation:
   ```
   How do I grow my app virally?
   ```
4. Test manual invocation:
   ```
   /social-growth-engineer

   Help me launch my dating app in 30 days
   ```

## Step 4: Configure Repository Settings (Optional)

### Add Topics

On GitHub, go to repository settings and add topics:
- `claude-code`
- `claude-skills`
- `ai-assistant`
- `developer-tools`
- `growth-hacking`
- `viral-marketing`
- `tiktok`
- `social-media`

### Enable Discussions

1. Go to Settings → Features
2. Check "Discussions"
3. Set up discussion categories:
   - 💡 Ideas (for new skill suggestions)
   - 🙏 Q&A (for usage questions)
   - 📣 Show and tell (for user success stories)

### Add Description & Website

- **Description**: Claude Code skills for developers, marketers, and founders
- **Website**: https://socialgrowth.engineer (or your preference)

## Step 5: Share with the Community

### Announce on Social Media

**Twitter/X**:
```
🚀 Just open-sourced my Claude Code skills collection!

The social-growth-engineer skill teaches Claude everything about growing apps virally through TikTok/Reels:
• 100+ real case studies ($10K to $5.5M ARR)
• 50+ proven hooks & 30+ video formats
• Platform tactics, monetization, UGC strategies

Install: npx add-skill giulioco/skills

https://github.com/giulioco/skills
```

**LinkedIn**:
```
I've open-sourced a comprehensive Claude Code skill for viral app growth!

It's built from analyzing 100+ successful app launches and contains:
- Complete growth frameworks and scaling strategies
- 50+ viral hook formulas with real metrics
- 30+ video format templates
- 100+ case studies from $10K to $5.5M ARR apps
- Niche-specific playbooks for study apps, dating, fitness, and more

Anyone building consumer apps can now install this knowledge into Claude with one command:

npx add-skill giulioco/skills

Check it out: https://github.com/giulioco/skills
```

### Submit to Claude Code Community

If Anthropic has a skills registry or community showcase:
1. Submit your repository
2. Include description and use cases
3. Link to documentation

### Post on Relevant Communities

- r/ClaudeAI
- Hacker News (Show HN)
- Indie Hackers
- Product Hunt (if appropriate)

## Step 6: Maintain and Update

### Versioning Strategy

Use git tags for releases:

```bash
cd ~/git/skills

# Tag initial release
git tag -a v1.0.0 -m "Release v1.0.0: social-growth-engineer skill

- 100+ case studies with verified metrics
- Complete growth frameworks
- 50+ hooks, 30+ formats
- 91 KB knowledge base"

git push origin v1.0.0
```

Future updates:
- **v1.x.x**: Minor updates (new case studies, hooks, fixes)
- **v2.x.x**: Major updates (new skills, restructuring)

### Keep Content Fresh

Regular updates (monthly or quarterly):
- Add new case studies as apps launch
- Update metrics for existing case studies
- Add new hooks and formats that emerge
- Remove outdated information

### Respond to Issues and PRs

- Review contributions within 1 week
- Thank contributors
- Provide constructive feedback
- Merge quality contributions quickly

## Ongoing Workflow

### Adding New Skills

```bash
cd ~/git/skills

# Create new skill directory
mkdir -p skills/new-skill-name/references

# Create SKILL.md
# ... edit files ...

# Test locally
npx add-skill .

# Commit and push
git add .
git commit -m "Add new-skill-name skill"
git push
```

### Updating Existing Skills

```bash
cd ~/git/skills

# Edit skill files
# skills/social-growth-engineer/references/case-studies.md

git add .
git commit -m "Update: Add 5 new case studies to social-growth-engineer"
git push

# Tag if it's a significant update
git tag -a v1.1.0 -m "v1.1.0: Added 5 new case studies"
git push origin v1.1.0
```

## Success Metrics

Track these to measure impact:

- **GitHub Stars**: Community interest
- **Forks**: People extending your work
- **Issues/Discussions**: Engagement level
- **Pull Requests**: Community contributions
- **npm install stats** (if tracked by add-skill)
- User testimonials and success stories

## Troubleshooting

### Users can't install

**Check**:
- Repository is public
- Files are in correct structure (`skills/*/SKILL.md`)
- No syntax errors in YAML frontmatter

**Test yourself**:
```bash
npx add-skill giulioco/skills --list
```

### Skill doesn't appear in Claude Code

**Check**:
- SKILL.md has proper frontmatter
- Skill was installed to `~/.claude/skills/`
- Restart Claude Code if needed

### Skill not auto-triggering

**Check**:
- Description has relevant keywords
- Try manual invocation first: `/social-growth-engineer`
- Description might be too specific or too vague

## Next Steps

1. ✅ Push to GitHub (see Step 1 above)
2. ✅ Test installation works
3. ✅ Add topics and configure repository
4. ✅ Share with community
5. ✅ Set up regular update schedule
6. 🎯 Plan next skill to add to collection

## Future Skills Ideas

Consider adding these skills to expand the collection:

- **data-analyst**: Advanced data analysis workflows
- **api-designer**: RESTful API best practices
- **devops-expert**: Infrastructure and deployment
- **seo-specialist**: Search optimization strategies
- **design-system**: Component library management
- **technical-writer**: Documentation excellence

---

**Ready to publish?** Run the commands in Step 1 and you're live! 🚀

Any questions? Open an issue on GitHub or check the [Claude Code documentation](https://code.claude.com/docs/en/skills.md).
