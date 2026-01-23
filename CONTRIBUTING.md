# Contributing to Giulio's Skills Collection

Thank you for your interest in contributing! This repository contains Claude Code skills that extend Claude's capabilities with specialized knowledge and workflows.

## Ways to Contribute

### 1. Improve Existing Skills

Found an error, outdated information, or want to add more knowledge to an existing skill?

**For social-growth-engineer**:
- Add new case studies with verified metrics
- Contribute new viral hooks or formats
- Update strategies with recent examples
- Fix errors in metrics or attributions

See each skill's individual contribution guidelines in `skills/[skill-name]/CONTRIBUTING.md` (if present).

### 2. Create New Skills

Have expertise in a domain that would make a valuable skill?

**Good skill candidates**:
- Deep domain expertise (e.g., SEO, data science, design systems)
- Proven workflows and frameworks
- Real-world examples and case studies
- Actionable, step-by-step guidance

**Not great for skills**:
- General knowledge Claude already has
- Opinion-based content without evidence
- Single-use scripts (better as standalone tools)

### 3. Report Issues

- Bug reports (broken links, incorrect information)
- Feature requests (new skills you'd like to see)
- Documentation improvements

## How to Contribute

### Quick Fix (Small Changes)

For typos, broken links, or minor corrections:

1. Click "Edit" on GitHub
2. Make your change
3. Submit a pull request

### Full Contribution (New Content or Skills)

1. **Fork and Clone**
   ```bash
   git clone https://github.com/giulioco/skills.git
   cd skills
   git checkout -b your-branch-name
   ```

2. **Make Your Changes**

   **To improve an existing skill**:
   - Edit files in `skills/[skill-name]/`
   - Follow existing format and style

   **To create a new skill**:
   ```bash
   mkdir -p skills/my-new-skill/references
   ```

   Create `skills/my-new-skill/SKILL.md`:
   ```yaml
   ---
   name: my-new-skill
   description: Clear, specific description of when Claude should use this skill
   ---

   # Skill Name

   Instructions for Claude on how to use this skill...
   ```

3. **Test Locally**
   ```bash
   npx add-skill .
   ```

   Then test in Claude Code:
   - Ask questions that should trigger the skill
   - Invoke manually with `/my-new-skill`
   - Verify Claude gives helpful, accurate responses

4. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add: [description of your contribution]"
   git push origin your-branch-name
   ```

5. **Create Pull Request**
   - Go to GitHub and create a PR
   - Describe what you changed and why
   - Link to any relevant issues

## Skill Creation Guidelines

### SKILL.md Structure

```yaml
---
name: skill-name                    # lowercase, hyphens only, max 64 chars
description: When Claude should use this skill. Be specific with keywords users would naturally say.
---

# Skill Title

Clear explanation of what this skill does.

## When to Use This Skill

List specific scenarios, keywords, or question types.

## How to Use This Skill

Step-by-step instructions for Claude to follow.

## Resources

Link to reference files in the skill directory.
```

### Best Practices

1. **Keep SKILL.md Focused** (under 500 lines)
   - Move detailed information to reference files
   - Use clear, actionable instructions
   - Include examples of expected behavior

2. **Write Clear Descriptions**
   - Use keywords users would naturally say
   - Examples: "When explaining code," "When creating a pull request," "When debugging"
   - More specific = fewer false triggers

3. **Include Real Examples**
   - Concrete examples > abstract explanations
   - Show expected output format
   - Reference real case studies when applicable

4. **Organize with Reference Files**
   ```
   skills/my-skill/
   ├── SKILL.md
   └── references/
       ├── playbook.md        # Detailed strategies
       ├── examples.md        # Usage examples
       └── case-studies.md    # Real-world examples
   ```

5. **Cite Sources**
   - Link to original sources
   - Verify metrics before including
   - Mark estimates as "estimated"

### Optional Frontmatter Fields

```yaml
---
name: skill-name
description: Description here
disable-model-invocation: true    # Only user can invoke (for side effects)
user-invocable: false             # Only Claude can invoke (background knowledge)
allowed-tools: Read, Grep, Glob   # Restrict which tools Claude can use
context: fork                     # Run in isolated subagent
agent: Explore                    # Which subagent type to use
model: sonnet                     # Override model for this skill
---
```

See [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills.md) for details.

## Content Standards

### Verified Information Only
- ✅ Metrics from public sources, verified screenshots, or trusted publications
- ✅ Strategies you've personally used with results
- ✅ Frameworks with proven track records
- ❌ Speculation or unverified claims
- ❌ Outdated information without context

### Actionable Guidance
- ✅ Step-by-step instructions
- ✅ Specific examples with context
- ✅ Clear "why" behind tactics
- ❌ Vague advice like "create engaging content"
- ❌ Generic tips without specifics

### Respectful & Neutral
- ✅ Present multiple approaches
- ✅ Acknowledge trade-offs
- ✅ Note when something is controversial
- ❌ Judgmental language
- ❌ Promoting unethical tactics without disclaimer

## Review Process

1. **Automated Checks**
   - Markdown linting
   - File structure validation
   - Size limits (SKILL.md < 500 lines recommended)

2. **Maintainer Review**
   - Verify sources and metrics
   - Check formatting consistency
   - Test skill functionality
   - Ensure value for users

3. **Merge & Release**
   - Approved PRs merged to main
   - Available immediately via `npx add-skill giulioco/skills`

## Code of Conduct

### Be Respectful
- Constructive feedback only
- No personal attacks or harassment
- Assume good intentions

### Be Helpful
- Help new contributors learn
- Share knowledge generously
- Suggest improvements, don't just criticize

### Be Accurate
- Cite sources properly
- Correct errors politely
- Don't embellish metrics

## Questions?

- **Issues**: Bug reports, feature requests
- **Discussions**: Questions, ideas, general conversation
- **Documentation**: [Claude Code Skills Docs](https://code.claude.com/docs/en/skills.md)

## Recognition

Contributors will be:
- Listed in acknowledgments (if desired)
- Credited in relevant skill sections
- Appreciated by the community!

Thank you for making these skills better! 🚀
