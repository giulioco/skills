# The Weekly Growth Cycle (Level 4)

Once you have PMF (L1), a clear growth equation and aha (L2), and a working channel (L3), the work becomes optimization: running a high-tempo experimentation cycle that compounds learning.

## The team (and the solo founder version)

### Six roles in a growth team

| Role | Responsibility |
|---|---|
| **Growth Lead** | "Battalion commander" — sets focus, runs the weekly meeting, "part manager, part product owner, part scientist." Required: data fluency, product fluency, experiment design, industry familiarity. **For startups, the founder usually plays this role.** |
| **Product Manager** | "CEO of the product" (Horowitz). Strong on customer surveying and dev process. |
| **Software Engineer(s)** | *"The very essence of growth hacking is the hacker spirit."* Don't relegate to order-takers. They invent the loops (see Airbnb-Craigslist hack). |
| **Marketing Specialist** | Choose by channel: content marketer for content-led, email director for email-led, SEO for SEO-led. Cross-pollinates with engineering. |
| **Data Analyst** | *"Data analysis must not be farmed out to the intern."* Designs statistically valid experiments, queries multiple sources, builds the data lake. |
| **Product Designer** | UX/visual; user-psych and interface insights. |

**Solo founder version:** you wear all hats with weekly discipline. The cadence matters more than the headcount. The compounding asset is **codified learning**, which a solo founder can build alone.

### Reporting structure
Two models per the McInnes/Miyoshi survey:
- **Functional / product-led** (team reports to head of product, like Pinterest)
- **Independent** (reports to CEO, like Uber, Facebook)

### Executive sponsorship is required
*"Growth cannot be a side project."*

- **Zuckerberg (2005):** Noah Kagan brought him a revenue idea. Zuck stopped him mid-pitch, walked to whiteboard, wrote one word — **"Growth"** — and refused to entertain anything else. Two years before the team was officially formed.
- **Zillow:** an annual 9–12 month growth focus the whole company aligns to (e.g. SEO in 2008 to catch Trulia, ultimately bought them for $3B in 2015).

## ICE Score (verbatim from the book)

> When submitting ideas, the submitter should rate each idea on a **ten-point scale**, across each of the following three criteria: the idea's potential **impact**, the submitter's level of **confidence** in how effective it will be, and how **easy** it will be to implement. Then those ratings are **averaged** to provide an aggregate score for each idea.

| Dimension | Definition |
|---|---|
| **IMPACT** | Expected degree to which the idea will improve the focused metric. |
| **CONFIDENCE** | How strongly you believe the idea will produce the expected impact. Higher when iterating on a previously successful test ("doubling down") or when a similar test elsewhere worked. |
| **EASE** | Time and resources to run. Provides reality check + identifies low-hanging fruit. |

### Example scoring (verbatim from the book's grocery-app worked example)

| Idea | Impact | Confidence | Ease | Avg |
|---|---|---|---|---|
| Add Shopping List feature | 4 | 8 | 2 | 4.67 |
| $10 first-time-shopper promo | 7 | 4 | 8 | 6.33 |
| Improve visibility of free delivery for $50 orders | 6 | 7 | 6 | 6.33 |
| Improve recommendation engine | 4 | 6 | 3 | 4.33 |

### Rules
- Scores are subjective — use as **relative-prioritization guide**, not absolute truth.
- The growth lead reviews and overrides scores when needed.
- **Don't squabble over scoring.** It's a way to surface the highest-leverage ideas, not a courtroom.
- **Lowest-rated experiments sometimes win huge.** GrowthHackers moved a signup form from page bottom to top — Morgan scored it 4 on impact, it produced a **700% lift**.
- Other systems exist (TIR, PIE) — pick one and stick with it.

## The four-stage weekly loop

Cadence: **one-week or two-week cycle**. GrowthHackers uses one week. Tempo: leading teams run **20–30 experiments/week**. Start with **1–2/week** as a solo founder and ramp.

### 1. Analyze
Data analyst dives into user data; marketer runs surveys/interviews. Produce reports for the team a week before the next meeting. Sample analyst questions:

- **Best-customer behaviors:** features used, screens visited, time of day, average order, purchase items.
- **Best-customer characteristics:** acquisition source, devices, demographics.
- **Abandonment events:** highest exit screens, bugs, missing actions.

### 2. Ideate
Over the four days between meetings, every team member submits ideas in a **templated format**:

| Field | Content |
|---|---|
| **IDEA NAME** | Under 50 chars |
| **IDEA DESCRIPTION** | Who, what, where, when, why, how (executive-summary style) |
| **HYPOTHESIS** | "By making it easier for shoppers to view and reorder previously purchased items, the number of people who make repeat purchases will increase by 20%." Specific cause-effect, with predicted lift. |
| **METRICS TO BE MEASURED** | Track downstream metrics, not just the surface metric. **Always >1 metric**, since improvements in one can come at the expense of others. |

### 3. Prioritize
Score every idea with ICE. Day before the meeting, growth lead asks each member to **nominate up to 3** for discussion.

### 4. Test
Selected experiments move to "Up Next" queue. Owners assigned. Engineers code, marketers create assets, analyst sets up control/experiment groups.

## The Weekly Growth Meeting (verbatim 60-minute agenda)

| Time | Topic |
|---|---|
| **15 min** | **Metrics review & focus area:** North Star + key metrics; key positive factors; key negative factors; growth focus area (confirm or shift, e.g. acquisition → retention). |
| **10 min** | **Review last week's testing activity:** tempo (launched vs goal); what was Up Next but didn't launch and why. |
| **15 min** | **Key lessons from analyzed experiments:** preliminary + conclusive results, codify learnings. |
| **15 min** | **Select growth tests for current cycle:** discuss nominated experiments, reach consensus or growth lead decides; assign owners. |
| **5 min** | **Check growth idea pipeline:** if ideation is down, prompt for more; recognize top contributors. |

Ellis runs his on **Tuesdays** (Monday for prep). The meeting is **NOT for brainstorming** — that happens between meetings. If the meeting becomes a brainstorm, the cadence is broken.

## Testing rules of the road

### Use a 99% statistical confidence level
> *"A 95% confidence level means a 'winning' test can still be wrong 5% of the time. That means 1 out of 20 tests that come back as winners could actually be losers. At 99% confidence, however, that number of false-positive tests drops to 1 out of 100."*

### Control always wins
When a test is inconclusive (ties), stick with control. The new variant could still be a long-term loser; without conclusive data, you have no business switching.

### Sample size matters dramatically

Andy Johns's table for a **3% base conversion rate**:

| % change vs control | Required sample/variant | Test days (at, say, 1k visitors/day) |
|---|---|---|
| 5% | 72,300 | 72 |
| 10% | 18,500 | 18 |
| 30% | 2,250 | 2 |

> *"Don't just move a button on a page... Produce dramatic lifts if you're a young start-up."*

At low traffic, **only run tests that could plausibly produce a 30%+ change**. Anything subtler will be statistically invisible for months.

### Knowledge base
Every test gets a written summary stored where everyone can search to avoid repeat tests. Required fields:

- Name
- Type
- Screenshots (before/after)
- Metrics
- Dates
- Hypothesis + ICE score
- Sample sizes
- Statistical confidence achieved
- Confounding issues
- Conclusions

Share via "wins" email list, Slack channel, or printed-and-posted in the office. The compounding asset is the codified learnings — over a year of cycles, the team's knowledge base becomes a dramatic competitive moat.

## What to test (the focus question)

Each cycle, **focus on ONE growth area**: acquisition, activation, retention, or revenue. Don't run experiments scattered across the funnel. Pick the most-broken multiplier (see `growth-equation.md`), aim every experiment at it, switch focus when it hits diminishing returns.

The Everpix tragedy: they had a great product and active users but kept improving daily-active engagement when their actual problem was *converting to paid*. They ran out of cash. **Focus on the right lever for the stage**, not the most fun one.

## Solo founder adaptations

For a solo founder running this cadence alone:

- **Tuesday weekly meeting with yourself.** Block 60 minutes. Run the agenda. Take notes.
- **1–2 tests/week** is the realistic max. Don't try for 20 — you'll cut corners on rigor.
- **Templated ideation file.** A single doc where you drop ideas as they come. Score weekly.
- **Knowledge base = a single growing markdown file.** Each test = a section. Searchable, compounds.
- **The hardest discipline is the analyze step.** No analyst means you have to do it yourself; you'll be tempted to skip into ideation. Resist.

## Common mistakes

- **Running tests at insufficient sample size.** Calling winners that aren't.
- **Picking tests by "interesting" rather than ICE.** ICE forces honesty about ease and confidence.
- **Skipping the knowledge base.** A year later you'll re-run the same losing test.
- **Letting the meeting become a brainstorm.** It's a decision meeting, not idea generation.
- **No focus area.** Scattering tests across the funnel = no compounding learning.
- **No executive sponsor.** Solo founders are the sponsor by default — but if you're at a startup with a non-technical founder running it, growth must report to them, not to product.
- **No tempo.** *"Tempo of testing is itself the strategy."* — Sean Ellis. The act of running 1–2 tests/week, every week, for a year, is what compounds.

## Diagnostic questions for the founder

1. "What's your testing tempo? Tests per week, last 4 weeks?"
2. "Where's your knowledge base? Show me the last 5 test write-ups."
3. "What's your single growth focus area for this cycle?"
4. "What's your minimum-detectable-effect at your traffic level — and are your experiments designed above that floor?"
5. "Did your Tuesday meeting happen this week?"

If the answer to #1 is zero or "we don't really track that," start there. The cadence is the work.
