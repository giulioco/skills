# The Growth Equation & North Star Metric (Level 2)

Every company has its own growth equation — a multiplicative formula that decomposes growth into testable input variables. Andy Johns (ex-Facebook/Twitter/Quora growth) frames this as the "fundamental growth equation."

The point is **not** the equation itself. The point is reducing the noise of "the business" to ~5 levers you can run experiments on.

> *"The sheer volume of data...is daunting...Reducing the complexity of your business operations down to a basic formula is immensely helpful in allowing the growth team to focus on the right signals in this vast sea of data noise."*

## How to derive yours

Walk through the customer's full lifecycle and write down each multiplier. The equation will usually take the shape:

`(Inflow) × (Conversion at each step) × (Frequency / Volume per user) + (Retained users) + (Resurrected users) = Growth metric`

Some companies' equations (verbatim from the book):

### Inman News (subscription)
```
(WEBSITE TRAFFIC × EMAIL CONVERSION RATE × ACTIVE USER RATE × CONVERSION TO PAID SUBSCRIBER)
+ RETAINED SUBSCRIBERS
+ RESURRECTED SUBSCRIBERS
= SUBSCRIBER REVENUE GROWTH
```

### eBay
```
NUMBER OF SELLERS LISTING ITEMS
× NUMBER OF LISTED ITEMS
× NUMBER OF BUYERS
× NUMBER OF SUCCESSFUL TRANSACTIONS
= GROSS MERCHANDISE VOLUME GROWTH
```

### Amazon
```
VERTICAL EXPANSION
× PRODUCT INVENTORY PER VERTICAL
× TRAFFIC PER PRODUCT PAGE
× CONVERSION TO PURCHASE
× AVERAGE PURCHASE VALUE
× REPEAT PURCHASE BEHAVIOR
= REVENUE GROWTH
```

### Hypothetical grocery delivery app
```
NUMBER OF INSTALLS
× NUMBER OF MONTHLY ACTIVE USERS
× NUMBER OF PURCHASERS
× AVERAGE ORDER SIZE
× REPEAT PURCHASE RATE
= AMOUNT OF GROWTH
```

## Why decomposition matters

Each multiplier is a **separate experimentation focus area**. Improving any one of them lifts the whole equation. The growth team's weekly meeting picks one multiplier and runs experiments on it for the cycle.

Two-sided marketplaces have **two** equations — one for each side. eBay needs sellers AND buyers. Airbnb needs hosts AND guests. Uber needs drivers AND riders. Each side has its own growth flywheel that feeds the other.

## The North Star Metric

After deriving the equation, choose **one** metric that "most accurately captures the core value you create for your customers." If it goes up, more aha moments are happening.

| Company | North Star | Why |
|---|---|---|
| **eBay** | Gross Merchandise Volume | Captures both sides — sellers selling, buyers buying — at the value level |
| **WhatsApp** | Messages sent | A daily user sending 1 message isn't really using it as their messenger |
| **Airbnb** | Nights booked | Captures both sides; revenue follows |
| **Facebook** | Initially MAU → switched to DAU | DAU caught daily-habit health that MAU hid |
| **LinkedIn** | Total signups | Revenue from recruiter access scales with profile coverage |
| **YouTube** | Watch time | Captures depth, not just visits |
| **Slack** | Messages sent / paid teams | Active team usage, not seat count |

### Counter-warning
**DAU is "nonsensical"** for products where users don't have a daily reason to return — Airbnb, Yelp, TurboTax. Don't pick a metric just because Facebook picked it. The metric must match the user's actual visit cadence.

The North Star **changes over time** as the company evolves. Facebook's was MAU then DAU then time-spent. Match the metric to the current strategic question.

## Where the leak hides

Once your equation is written down, you can see where the leak is. Look at each multiplier and ask: *"What's the typical industry benchmark, and how do I compare?"*

| Multiplier | Healthy | Concerning |
|---|---|---|
| Visit → signup | 1–5% (consumer), 5–15% (B2B) | <1% |
| Signup → activation | 30–60% | <20% |
| Activation → paid (SaaS trial) | 5–15% | <2% |
| Monthly retention (SaaS) | 92–98% | <90% |
| Annual retention (SaaS) | >90% | <80% |

A 0% conversion at one step is louder than a small lift at any other step. Fix the largest leak first.

## How to use the equation in practice

1. **Write it down.** Pick your business's natural shape. Iterate until each multiplier is something you can measure weekly.
2. **Pick the multiplier that's most broken** vs. its industry benchmark. That's your **growth focus area** for the next 4–8 weeks.
3. **Run weekly experiments** targeting only that multiplier (see `growth-process.md`). Don't run experiments scattered across the funnel.
4. **Switch focus when the multiplier hits diminishing returns.** When your activation goes from 5% → 30%, the next gain is harder to extract; pivot to retention or revenue.
5. **Re-run the diagnosis quarterly.** Equations don't change often, but the *focus multiplier* does.

## Example: applying this to a real situation

Take a hypothetical freemium SaaS with low MRR: ~0.5% signup-to-paid conversion, 32% activation, 0% trial-to-paid. The equation:

```
(Organic + paid traffic)
× (signup rate)                       ← ~0.5% (low)
× (activation rate)                   ← 32% (low)
× (trial-to-paid conversion)          ← 0% (broken)
+ (retained subs)
+ (resurrected subs)
= MRR growth
```

The equation tells you the focus order:
1. **Trial-to-paid is 0% — that's the catastrophic leak.** Until that's fixed, more traffic just wastes money. This is L2/Activation work, not L3/Channel work.
2. **Activation 32% is the next leak** — fix it after the conversion crisis.
3. Only *after* both are healthy is "more traffic" the right answer — that's when L3/Bullseye becomes valuable.

Without the equation, the founder might spend a quarter trying to grow a new acquisition channel when the bottleneck is the checkout flow.

## Common mistakes

- **No equation written down.** You're managing by gut.
- **Picking a North Star that doesn't reflect value.** "Page views" or "signups" without retention reflects vanity, not health.
- **Forgetting the "+ retained + resurrected" terms.** Existing customers are the cheapest growth channel.
- **Working on the most fun multiplier instead of the most broken one.** The Everpix tragedy: they had a great product, but kept improving daily-active engagement when their actual problem was *converting to paid.* They ran out of cash. Focus on the right lever for the stage, not the most enjoyable one.
- **Treating two-sided marketplaces as single-sided.** Both equations must be tracked.

## Diagnostic questions for the founder

1. "What is the single number that, if it doubled tomorrow, would mean your business is healthy?"
2. "Write your business as a multiplication chain — traffic × signup × activation × revenue. What's each number?"
3. "Which multiplier in that chain is the most broken vs. its benchmark?"
4. "How would you know if the multiplier you're working on improved by 20%? What's the test design?"
5. "Is your North Star tied to user-visit cadence? (DAU is wrong for monthly products.)"

The first sentence of any growth conversation should be the equation. If the user can't write it down, that's the work.
