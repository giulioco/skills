# Product-Market Fit (Level 1)

The founder asking "how do I grow?" before achieving PMF is asking the wrong question. Holiday: *"The race has changed. The prize and spoils no longer go to the person who makes it to market first. They go to the person who makes it to Product Market Fit first. Because once you get there, your marketing efforts become like a spark applied to a bed of kindling soaked in kerosene. The old way? It's striking a match . . . and hoping it starts a fire somewhere."*

Marc Andreessen (quoted in Holiday): companies need to *"do whatever is required to get to product/market fit. Including changing out people, rewriting your product, moving into a different market, telling customers no when you don't want to, telling customers yes when you don't want to, raising that fourth round of highly dilutive venture capital — whatever is required."* Everything is on the table.

## How to know you have PMF — two complementary signals

### 1. The Sean Ellis 40% test

A 1-question survey to active users.

> "How disappointed would you be if this product no longer existed tomorrow?
> a) Very disappointed
> b) Somewhat disappointed
> c) Not disappointed (it really isn't that useful)
> d) N/A — I no longer use it"

**Interpretation:**
- **≥ 40% "very disappointed"** → must-have status. Push for growth.
- **25–40%** → "what's needed are tweaks either to the product or to the language used to describe the product and how to use it."
- **< 25%** → "either the audience you've attracted is the wrong fit for your product, or the product itself needs more substantial development."

**Methodology:**
- Target **active users**, not dormant ones (dormant responses are uninformative — they tell you why they left, not whether the product is must-have for those who stay).
- Need **a few hundred responses** for reliability. Below that, supplement with customer interviews.
- Stop running the test once growth has clearly taken off — you don't want to suggest your product might disappear to a happy base.

**Companion questions on the same survey** (each unlocks something specific):

| # | Question | What it unlocks |
|---|---|---|
| 1 | "What would you likely use as an alternative to [product] if it were no longer available?" (a/I probably wouldn't use an alternative; b/I would use: ___) | Real competitive set + features users prefer about competitors |
| 2 | "What is the primary benefit that you have received from [product]?" | Actual core value (often differs from your pitch) |
| 3 | "Have you recommended [product] to anyone?" (No / Yes — please explain how you described it) | Word-of-mouth language (use this in your marketing) |
| 4 | "What type of person do you think would benefit most from [product]?" | Better-defined customer niche (Inman: training product was actually a fit for new agents → re-targeted) |
| 5 | "How can we improve [product] to better meet your needs?" | Features and barriers |
| 6 | "Would it be okay if we followed up by email...?" | Builds your interview pipeline |

### 2. Stable retention curve

A retention curve that **flattens at a meaningfully high rate** is the second half of the PMF signal. A high curve that's still falling = users still churning. A lower curve that's stabilized at, say, 40% can be PMF if that 40% is your true core. Without flattening, the 40% test alone can mislead.

**Benchmarks:**
- **SaaS:** > 90% annual retention (Pacific Crest 2013).
- **Best mobile apps:** > 60% at 1 month. Average: 10%.
- **Fast-food (McDonald's 2012):** 78% monthly.
- **US credit cards:** ~20% annual churn.
- **Costco:** 91% retention.

Track retention weekly or monthly. Plot cohorts. A flat curve at month 3 that holds through month 6 is more meaningful than a flat month 1 that erodes.

## What to do if you fail the test

**Do not whiteboard new features.** That's the engineer's instinct and almost always wrong. Yelp grew by *removing* features (pared down to reviews) — beware feature creep.

Instead, run three tracks in parallel:

1. **Customer interviews + surveys** — use the 5 companion questions above. Mine the actual language. Look for the niche where the product is already a must-have.
2. **Efficient experimental testing** of product changes and messaging. Holiday calls out LogMeIn (turned out users didn't believe it was free — language fix tripled conversions).
3. **A deep plunge into user data** to find behaviors that predict the few users who *do* love the product. That's the kernel — find more like them.

Holiday's specific advice (from his PMF chapter):
- **Start with an MVP** and iterate based on feedback — opposite of launching a "finished" product.
- **Open up to feedback.** SurveyMonkey, Wufoo, or Google Forms. Not friends — strangers, scientifically.
- **Use the Socratic method** on every assumption. Repeatedly question who the product is for and why anyone would use it.
- **Use behavioral analytics** (Optimizely, Mixpanel, GA) to see what users actually do, not what they say.
- **Be willing to pivot dramatically.** Burbn → Instagram. Airbedandbreakfast.com → Airbnb. Tote → Pinterest.

## Common mistakes

- **"Going to market with the product you have, not the one you want."** Holiday calls this attitude self-destructive.
- **Thinking marketing's job starts after product is finished.** Marketing helps cause PMF, not just exploit it.
- **Confusing the product for what was originally launched.** Most known services are fundamentally different from their launch versions.
- **Asking friends what they think instead of running structured surveys.**
- **Pouring more marketing muscle into a product that isn't resonating.** This makes things worse — you burn through your addressable market and earn negative word-of-mouth.
- **Skipping the retention curve check.** A high 40%-test score with a still-falling retention curve means you're early, not done.

## Case studies

- **Instagram (was Burbn).** Location-based social with optional photos and $500K in funding. Founders saw users only engaged with the photo+filter feature, asked *"what is the one thing that makes this product unique and interesting?"*, killed everything else, relaunched as Instagram. 100K users in a week. $1B sale 18 months later.
- **Airbnb (was Airbedandbreakfast.com).** Iterated from "air mattresses on conference attendees' floors with breakfast" → "alternative for travelers who hate hotels" → finally "Airbnb-as-we-know-it." Each pivot driven by usage data + feedback. Now $80B+.
- **Yelp.** Founders thought they were a friends-asking-for-recs app. Data showed **reviews** were the buried hit. Pivoted, seeded with 20M Bay Area business profiles. CitySearch (the 800-lb competitor) became a footnote.
- **LogMeIn.** Failed 40% test signal. Survey revealed users didn't believe it was free. Language fix → 3× conversion.
- **Evernote.** Refused to spend on marketing for years; everything went into product. Phil Libin: *"people [who are] thinking about things other than making the best product, never make the best product."* Product strong → it markets itself.

## Diagnostic questions for the founder

Use these in conversation:

1. "How would your most engaged 100 users answer: *'How disappointed would you be if this disappeared tomorrow?'*"
2. "Plot a retention curve by signup cohort. Does it flatten? At what month? At what %?"
3. "What is the one thing that makes your product unique and interesting? (asked Burbn-style — answer in one sentence)"
4. "Who is this product for, and why would they use it? Why do *you* use it?"
5. "If your product disappeared tomorrow, what would your top 10% users use instead — and what would they miss?"

If the founder cannot answer these crisply, you do not have PMF and a marketing investment is premature.
