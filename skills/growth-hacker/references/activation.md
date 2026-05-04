# Activation (Level 2)

Activation is the rate at which new users reach their aha moment. It's the most common bottleneck in growth — and the highest-leverage one to fix because *it compounds with every channel*. A 2× activation rate effectively doubles every channel's CAC efficiency.

> *"98% of website traffic does not lead to activation."*
> *"Most mobile apps lose up to 80% of their users within three days."*

## Sean Ellis's three-step framework

### 1. Map every step in the customer journey to the aha moment.

For a grocery-delivery app: download → search → add-to-cart → create account (name/card/delivery) → purchase → receive order at home.

For a SaaS like Slack: signup → invite team → first message sent → 100 messages → 1,000 messages → 2,000 messages (the aha threshold).

For a real-estate alerts SaaS: visit → signup → create alert with filters → first match received → first match clicked → first listing visited → conversion to paid.

Write down every step. Number them. The funnel will surprise you.

### 2. Create a funnel report showing conversion + drop-off at each step, segmented by channel.

Use Mixpanel, Kissmetrics, GA, Amplitude, or Adobe SiteCatalyst. **Segmenting by channel is the unlock** — you'll find that paid-Facebook converts at 5.5%, paid-AdWords at 6.5%, social-Twitter at 0.9%. The channels with low activation are not necessarily worth less traffic; they may be miscast (wrong audience, wrong landing page, wrong intent).

A naive channel decision shuts off the low-converting channel. The right move: investigate *why* it converts low, fix it if you can, *then* reallocate.

### 3. Survey users at drop-off points.

Survey both:
- Users who **dropped off** — what stopped them?
- Users who **just completed** the desired action — they can tell you what *almost* stopped them.

#### Survey rules
- 1–2 questions max.
- Open-ended preferred over multiple choice (don't shoehorn answers).
- Two trigger conditions:
  1. Activity indicates confusion — lingering, hovering, leaving the page.
  2. Right after a step many *don't* take (account creation, purchase).
- Pop-up on intent-to-leave for browsers without contact info.

#### Verbatim drop-off questions (use as templates)
- "Is there anything preventing you from signing up at this point?"
- "What concerns are keeping you from completing your order?"
- "If you did not make a purchase today, can you tell us why not?"
- "What information would you need to feel comfortable signing up today?"

#### The "one thing" question (high response rate)
On the post-purchase confirmation screen: **"What's the one thing that nearly stopped you from completing your order?"** This question is gold because it captures the *barely-converted* user's psychology before they forget.

## Sean's friction formula

> **DESIRE − FRICTION = CONVERSION RATE**

The more the user wants the product, the more friction they tolerate. Early adopters power through pain. Later users abandon at the slightest irritation.

Two fixes:

**Increase desire** — better positioning, sharper value prop, customer-language messaging, social proof. (See `aha-moment.md` for language sources.)

**Reduce friction** — remove steps, default values, eliminate decisions, reduce typing, eliminate page loads, defer non-essential fields, replace forms with single-click sign-in.

The two are interchangeable as a math identity but **friction reduction usually has higher leverage** because desire is harder to manufacture and friction is something you can see.

> *"Designers who built the product can't see its friction."* Watch real users stumble. Record sessions. Run usability tests. Friction is invisible to the team that built it.

## Triggers

The activation chapter closes with **triggers** — prompts that pull users back to the aha behavior:

- **Used right** (HubSpot Sidekick: *"the application has installed successfully and you're ready to start sending email"*) → unlocks activation.
- **Used wrong** → alienates, feels spammy, gets unsubscribed.

Trigger rules:
- Tie triggers to the aha event the user already wants.
- Time them based on user behavior, not calendar.
- Personalize with at least the user's name + the action they're missing.
- One channel for the trigger first (email or push), not both.

## Language / market fit (James Currier)

Average human attention span on new info: **8 seconds** (down from 12 in 2000). Your messaging has to land in that window.

Famous language fixes:

- **Tickle** (James Currier's startup): *"Store your photos online"* → *"Share your photos online"*. Added 53M users in 6 months from one word change.
- **Steve Jobs / iPod:** *"1,000 Songs in Your Pocket"* — reframed the entire category.
- **LogMeIn:** signups jumped 3× when the language was changed to make it clear the product was actually free.

### The Upworthy method
1. Writers draft **25 headlines per story**.
2. Curator picks favorites.
3. Editor green-lights 2–3 for testing.
4. A/B with two Bitly URLs across two demographically-similar Facebook cities.
5. Set a timer (e.g. 60 minutes), count clicks, declare winner.

> *"A good headline can be the difference between 1,000 people and 1,000,000 people reading."*

### Where to mine language
- Customer reviews (your own + competitors')
- Social posts mentioning your category
- Must-have survey responses (especially Q3 — how they describe the product to friends)
- Support call transcripts
- Forums (Reddit, Quora)

**Use customers' words back at them.** Don't invent your own taxonomy.

## Case studies

### HubSpot Sidekick (the persistence story)

Sales-email tracker, sluggish activation despite organic word-of-mouth.

- **Step 1:** segmented by traffic source, job role, email type, email service. Found work-email signups activated more than personal-email signups → forced work-email at signup.
- **Step 2:** data showed non-activated users never sent more than one email; surveyed them → *"we don't understand how to use it."*
- Tried 11 different educational onboarding experiments → **every one failed.**
- Stepped back, dove into data again. Realized education wasn't the issue — they needed to **remove a step, not add one**.
- Replaced post-install landing page with: *"the application has installed successfully and you're ready to start sending email"* → activation jumped.
- Went on to run **68 separate experiments** before activation was solved.

**Lesson:** persistence is the moat. The 12th experiment was the one that worked. Don't quit after 3.

### Qualaroo (Sean's own)

Aha was **50 survey responses**. Ran experiments to push trial users to that threshold:
- Better email copy
- Tutorial videos
- Recommended easier-to-deploy survey types (NPS instead of long surveys)
- Proactive customer-success outreach

Combined: dramatic increase in activation **even as they tripled the price.** The activation work created enough value that pricing was no longer the bottleneck.

### Etsy (off-the-internet activation)

Sent a team to craft fairs. Took crafters to lunch. Learned they coalesced around the feminist magazine *Bust* and Stitch 'n Bitch groups. Built community forums + Seller Handbook + sharing hooks. Result: **87–91% organic traffic at IPO**, $1.93B in sales.

The "activation" wasn't a button — it was understanding what crafters needed to feel at home on the platform.

### Tinder (the on-the-ground network play)

Whitney Wolfe went on the ground to college sororities/fraternities. Activated one tightly-networked sorority, walked across the street to its rival fraternity to show *"look who just signed up"* → instant signup. Localized network effect → organic explosion to 24M MAU in 30 months.

## Common mistakes

- **Optimizing the funnel before identifying the aha.** You're optimizing for the wrong destination. (See `aha-moment.md`.)
- **Skipping segmentation by channel.** Aggregate metrics hide channel-specific failures.
- **Asking "why didn't you sign up?" after they've already left.** Survey at the moment of friction.
- **Adding educational content when the issue is friction, not understanding.** Sidekick's 11 failures.
- **Ignoring the post-conversion survey.** The "one thing" question only works post-purchase.
- **Running A/B tests on minor changes when traffic doesn't support them.** Need ~72k users per variant for a 5% lift on 3% baseline conversion. At low traffic, only run dramatic tests.
- **Hiding friction behind "it's a feature."** Required forced field signups, captchas, multi-step onboarding — usually friction dressed up.

## Diagnostic questions for the founder

1. "Map every step from first-touch to your aha. How many steps?"
2. "What % of users complete each step? Show me the funnel by channel."
3. "Have you surveyed users who dropped off — and the ones who *just barely* completed?"
4. "What's the time from signup to first aha event for your average user?"
5. "What's the smallest version of your onboarding that still gets users to aha?"

If the user can't show you the funnel report by channel, that's the work — before any activation experiment.
