---
name: Pre-Sale Willingness-to-Pay Test
category: customer-validation
excluded_because: "needs the world: a real payment mechanism + cold traffic"
applicable_at: [validation]
assumption_categories_it_helps: [buyer, pain]
source:
  title: "Startup Validation Framework 2026: The Ultimate Guide to Testing Ideas"
  author: Presta / WeArePresta
  url: ""
  date: "2026-01-26"
---

## Core Insight

Email signups, "great idea" comments, waitlist entries, and even landing-page clicks are all free to give. Money is not. The Pre-Sale WTP Test converts a landing page from a solution-resonance instrument into a payment-behavior experiment: you attach a real price to a real payment mechanism and observe who attempts to check out. The gap between "clicked Get Access" and "entered a credit card" is where most startup ideas die — and this test surfaces that gap before you have built anything.

The mechanism: attempted payment is the strongest behavioral signal a pre-product startup can generate. Unlike a click (which is cheap), entering a credit card is a costly, deliberate action. It requires the buyer to believe (a) the value is worth the money, (b) the offering is real enough to trust with card details, and (c) the price is in their range. Any drop-off in that sequence is diagnostic — click without checkout attempt means the price is wrong, checkout attempt without completion means the trust or urgency is missing.

The Buffer pattern (originator of the technique): after the buyer clicks "Buy" and enters payment info, redirect to a page saying "We're rolling out in batches — you're on the list. We haven't charged your card. We'll email when you can get in." The card is not actually charged; the *attempt* is the data.

## Process

1. **Prerequisite:** Smoke Test Landing Page has confirmed solution resonance (CTR passes threshold). Running a WTP test on an offer that doesn't resonate produces zero conversions for the wrong reason.
2. **Add a real price** to the landing page. Round number, currency-appropriate, credible to the buyer's tier. E.g., $50 lifetime access with "50% off for first 100 buyers" scarcity framing.
3. **Add a real payment mechanism** — Stripe Checkout, Gumroad, or Lemonsqueezy for consumer/prosumer; do not use "contact us" forms, which measure interest not commitment.
4. **After payment attempt, redirect to a "not yet" page.** Explicitly do not charge the card. Language pattern: "You're in. We're launching in batches — we haven't charged your card. Expect an email in [timeframe]." This is ethical (no charge without product) and legally required in most jurisdictions.
5. **Instrument three data points separately:**
   - Clicks on the payment CTA
   - Payment attempts started (buyer entered checkout flow)
   - Payment attempts completed (buyer clicked final confirm)
6. **Read the drop-off ladder against volumes:**
   - **0 completed attempts:** Offer is invalidated at this price. Pivot the value proposition, drop the price by 40–50%, or kill the test.
   - **1–10 completed attempts:** Signal exists but may be wrong audience. Interview each buyer — who are they, what did they think they were getting? Iterate audience targeting or price.
   - **50+ completed attempts:** Strong PMF signal. Build.
7. **Interview the near-misses.** Anyone who clicked the CTA but abandoned checkout is your most valuable interview subject. Their reason is the diagnostic signal — the article calls this "the pre-buy conversation."
8. **Compare completed-attempt volume against ad spend.** CAC (cost per completed attempt) is your first real economics data point. If you spent $500 and got 20 attempts, CAC is $25. That number goes directly into your Evidence Ledger.

## Example

Buffer, 2010: Joel Gascoigne built a two-page site. Page one described the product concept ("A better way to share on Twitter"). Page two showed pricing plans. Anyone who clicked a plan was told: "Sorry, Buffer isn't ready yet — leave your email and we'll notify you when we launch." Behind the scenes, he was not asking for opinions; he was measuring which plans people *tried to buy*. The behavioral signal — attempted click-throughs to payment — was enough to justify building the actual backend. The entire experiment cost the time to build two static pages. The validation cost him nothing but produced clean, unambiguous evidence of willingness to pay.

## Limitations

- **Ethical requirement:** you must not charge the card. Buffer's approach — capture attempt, redirect to "not yet" page — is the standard. Charging cards for a nonexistent product is fraud in most jurisdictions.
- **Consumer $ ≠ enterprise $.** A $50 pre-sale test works for prosumer/SMB. It will not work for enterprise deals where budget approval takes weeks and cannot happen through a checkout flow. For enterprise, use LOI B2B Validation instead.
- **Nice Friend contamination.** If your first 20 payment attempts are from personal network, discount them entirely. Segment by traffic source and read only the cold-traffic conversion rate.
- **Trust threshold varies with brand.** A stranger visiting an unknown domain with no reviews may not enter card details even at a low price. Add trust signals (a founder photo, a link to your LinkedIn, testimonials from any beta users) — but don't fake them.
- **Does not validate retention.** Attempted payment is one-time behavior. It says nothing about whether the buyer would remain a customer at month 3. Add a monthly recurring price to the test if retention is a critical assumption.
- **Cannot separate price sensitivity from value clarity.** Zero attempts could mean "price is too high" or "value isn't clear." Pair with Pricing Tier Test to isolate which.

## Connection to the Loop

The primary method for testing the **willingness-to-pay** dimension of the buyer assumption in B2C, prosumer, and SMB contexts. Chain from Smoke Test Landing Page (validates solution resonance) → Pricing Tier Test (finds the right anchor) → Pre-Sale WTP Test (converts click-interest to payment-attempt). Every stage feeds evidence into the Ledger. Set the Kill Criteria Contract before running: e.g., "If we get fewer than 5 completed payment attempts from $500 of cold traffic, we kill or pivot." For enterprise (B2B, $10k+ deal size), skip this method and use LOI B2B Validation directly.

See also: `practices/smoke-test-landing-page.md`, `practices/pricing-tier-test.md`, `practices/letter-of-intent-b2b.md`, `validation/kill-criteria-contract.md`, `practices/mom-test-interview-script.md`
