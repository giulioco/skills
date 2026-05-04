# Retention (Level 2)

Holiday: *"Retention trumps acquisition."* And: *"What's the point of driving a bunch of new customers through marketing channels if they immediately leak out through a hole in the bottom?"*

Bain: a 5% increase in customer retention can mean a 30% increase in profitability. Market Metrics: probability of selling to an existing customer is 60–70%; to a new prospect, 5–20%. Retention is a force multiplier on every channel — fix it once and every dollar spent on acquisition compounds.

## Three retention phases (Brian Balfour's framework)

| Phase | Window | Goal | Where most "low-hanging fruit" lives |
|---|---|---|---|
| **Initial** | First day (mobile), week (social), month/quarter (SaaS), 90 days (e-commerce) | Get user to convinced-or-churn point. **This is essentially activation 2.0.** | Onboarding, first-aha lifecycle emails, tooltip nudges. |
| **Medium** | Months 2–6 | Build a habit. The product becomes part of routine. Snapchat-checked-during-breakfast level. | Habit-forming triggers, daily/weekly use cases, lifecycle education. |
| **Long-term** | Month 6+ | Refresh the must-have feeling. Ship enhancements and new features that re-justify the subscription. | Roadmap visibility, big feature launches, loyalty programs. |

Dharmesh Shah (HubSpot): *the initial-retention phase is where most growth teams' "low-hanging fruit" lives*. Get a new user from signup to embedded in a week, and the rest of the retention work gets easier.

## The Smile Graph (Evernote)

Evernote noticed something counterintuitive: the longer people used the product, the **more likely** they were to keep using it. Plotted as a curve, retention dipped early, stabilized around 22%, then climbed back above the initial level after years 2–3. The shape of a smile.

The mechanism: **stored value**. The more notes you save, the more reason to come back. Same dynamic for:
- **Instagram** (more posts/follows = more reason to scroll)
- **Pinterest** (more boards = more saved memory)
- **QuickBooks** (more financial data = harder to switch)
- **Salesforce** (more contacts/customizations = embedded)
- **GitHub** (more repos and history = home base)

If your product has weak stored value, retention will struggle no matter how good acquisition is. The cure is to engineer stored value — features that *accumulate* per user.

For products with **episodic use** (apartment-alerts, job search, wedding planning, tax prep, moving services), stored value is weak by default — once the user solves the immediate problem, they stop using. To engineer stored value into an episodic product, build features that accumulate per user across the lifecycle: search history, saved-result graveyards, recommendations based on past behavior, profile data that becomes more useful over time, social/community angles that outlive the original use case. The smile graph requires a reason to come back even when the user doesn't *need* to.

## Cohort analysis is mandatory

Group users by **acquisition month** → track absolute retained users → translate to a retention curve (% retained over months).

Why it's mandatory: aggregate retention numbers hide cohort-level disasters. April–June cohort retention plummeting while January cohort stabilized is invisible at the aggregate level. Only cohort view shows it.

What to look for:
- **Curves that flatten** = PMF signal (must-have to those who stayed).
- **Curves that keep falling** = no PMF, or audience mismatch.
- **Cohorts where retention dropped vs. older cohorts** = something broke. Maybe a campaign brought wrong audience. Maybe a UX regression. Maybe a competitor launch.
- **Cohorts where retention rose** = something improved. Reverse-engineer it; double down.

Always compare cohorts side-by-side. The relative shape matters more than the absolute number.

## Retention benchmarks (verbatim)

| Industry | Retention |
|---|---|
| **SaaS (annual)** | >90% (Pacific Crest 2013) |
| **Best mobile apps (1 month)** | >60% |
| **Average mobile app (1 month)** | 10% |
| **Fast-food (McDonald's, monthly)** | 78% |
| **US credit cards (annual churn)** | ~20% |
| **EU mobile carriers (churn)** | 20–40% |
| **Costco** | 91% retention = 9% churn |

If you're below these, retention is your bottleneck — not acquisition.

## Tactics by phase

### Initial retention (the activation 2.0 problem)

- **Lifecycle emails triggered by inaction.** Dropbox emails users who signed up but haven't uploaded a file. Twitter emails users who haven't followed enough accounts. Build a trigger for each step in the funnel where users get stuck.
- **Onboarding that drives the aha behavior.** Twitter's growth hacker Josh Elman noticed in the data that users who manually picked 5–10 accounts to follow on day one were dramatically more likely to be retained. They redesigned onboarding around exactly that.
- **Manual concierge follow-up at small scale.** DogVacay called Holiday personally three days after he signed up and went silent — walked him through, helped complete his profile, set him up with his first host. Not scalable, not supposed to be — it's how you convert "looky-loos" into active users at the first hundred or thousand.
- **Reward small actions that deepen lock-in.** Dropbox: 250MB extra for taking the product tour, 125MB for sending 90 characters of feedback. Each action ratchets the user deeper into the product.

### Medium retention (the habit problem)

- **Habit loop instrumentation** — trigger → action → reward → investment. Identify what triggers a daily/weekly user to come back, and engineer it into the product (push, email, SMS, browser tab).
- **Continuous improvement.** Facebook never stopped shipping — Live, Slideshow, sports notifications, anniversaries, memories. Every shipped feature is a re-engagement event.
- **Stored value compounding.** See above — anything that makes the product more useful the more you use it.
- **Community.** Users connected to other users churn at far lower rates. (See `channels/community.md`.)

### Long-term retention (the must-have refresh problem)

- **Big feature launches** that change the user's mental model of the product. They don't just keep paying — they upgrade, refer, write LinkedIn posts.
- **Loyalty / status tiers.** Years-of-service badges, Top Contributor recognition, premium-tier perks.
- **Annual plan transitions.** Inman improved retention by replacing month-to-month with 3-month plans. Annual plans dramatically improve retention — every retention point compounds.
- **Resurrection campaigns** with referrer-segmented messaging. (See below.)

## Resurrection: the cheapest growth channel

Holiday's Uber example: he signed up for Uber in LA in 2011/2012, never used it, bounced. A year later a $50 Uber gift card (from someone else's referral) plus a needed cab ride pulled him back in. After his ride, Uber asked him to rate the driver, then emailed a coupon. Loop closed. *"That is retention and optimization. It is marketing to someone who is a lot more likely to convert than some busy stranger you might otherwise try flashing an online banner ad to."*

### Josh Elman's resurrection script (4 questions, verbatim)
For dormant users you successfully bring back, call/email and ask:

1. Why did you sign up in the first place?
2. What didn't work for you? Why'd you bail?
3. What caused you to come back and try again?
4. What worked this time?

Their answers are gold for retention design — they tell you exactly what triggered re-engagement.

## Common mistakes

- **Treating retention as ops, not marketing.** Onboarding, lifecycle emails, re-engagement — these *are* marketing. Holiday: *"This doesn't seem like marketing at all. How could a feature inside the service — the Twitter suggested user list — be considered marketing? But if it drives better user adoption it is."*
- **Throwing more money at acquisition when growth lags.** If the bucket leaks, more inflow makes the leak worse.
- **Ignoring conversion rate and bounce data from your existing funnel.** It's right there.
- **Chasing vanity metrics instead of retention metrics.** Holiday: *"We weren't chasing vanity metrics. If the BitTorrent promotion hadn't driven sales, I wouldn't have told you about it."*
- **Looking at aggregate retention instead of cohort retention.** Aggregate hides everything.
- **Forgetting "everything can be improved."** Sean Beausoleil (Mailbox): *"Whatever your current state is, it can be better."*

## "Treat users as scarce" — the mindset

You already have email lists, customer databases, dormant signups. Working those is higher-ROI than chasing strangers. Almost everyone neglects it because new acquisition feels more exciting.

> *"You're better off rolling out new features that get more out of your customer base, that turn potential users into active users, than going out and pounding the pavement for more potentials."*

## Diagnostic questions for the founder

1. "Plot retention by cohort for the last 12 months. Which cohort is your worst, which is your best, and why?"
2. "Where does your retention curve flatten? Or does it keep falling?"
3. "What stored value does your product accumulate per user over time?"
4. "What % of last month's churned users came from the same channel?"
5. "When did you last run a resurrection campaign — and what was the open rate?"

If the user can't show cohort retention, that's the work — before any acquisition experiment.
