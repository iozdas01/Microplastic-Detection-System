---
name: Smoke Test Landing Page
category: customer-validation
excluded_because: "needs the world: a built page + $200–500 cold ad spend"
applicable_at: [validation]
assumption_categories_it_helps: [pain, buyer, market]
source:
  title: "Startup Validation Framework 2026: The Ultimate Guide to Testing Ideas"
  author: Presta / WeArePresta
  url: ""
  date: "2026-01-26"
---

## Core Insight

A landing page is not a marketing asset — it is a scientific instrument. The smoke test isolates one variable: does the way you have framed the solution create enough interest in a stranger, seeing it for the first time, to click "Get Access." Click-through rate on the CTA from cold traffic is the behavioral signal. High CTR means the framing resonates; low CTR means the buyer either doesn't recognize the pain in your language, doesn't believe you can solve it, or doesn't care enough to click. You learn this in days, before you have written a line of product code.

The mechanism: a click is a small commitment, but it is a commitment. Unlike an email signup on a "coming soon" page (which costs nothing), a "Get Access" or "Pre-Order" click implies the visitor expects to receive something. That expectation is what filters interest from indifference. The cold-traffic requirement is critical: any positive CTR from your own network is confounded by social bias — friends click to support you. Strangers click only when the framing lands.

The smoke test measures *solution resonance* — whether your framing of the outcome maps to a pain the buyer recognizes. It does not measure whether they will pay (that's Pre-Sale WTP Test) and does not measure whether they will retain (that's a product test). It measures whether the door is worth opening.

## Process

1. **Build a one-page site with exactly four elements:**
   - **H1 headline:** benefit-driven, specific, in the buyer's language (mined from Reddit/LinkedIn). Not "AI-powered inspection platform" — name the outcome, the number and the deadline the buyer already lives by.
   - **Visual proof:** a screenshot, mockup, or 30-second video of the outcome the product delivers. Can be simulated (Framer, Figma) — does not need to be a real product.
   - **The "magic" CTA button:** wording that implies immediate access. "Get Early Access," "Pre-Order," "Reserve My Spot." Not "Learn More" (too passive) and not "Contact Sales" (too high friction).
   - **Tracking pixel:** PostHog, Microsoft Clarity, or Meta Pixel. You need to measure scroll depth and click behavior at minimum.
2. **Drive cold traffic.** Paid ads on Google or Meta targeted at your buyer archetype. $200–500 is enough for a readable signal. Do not drive traffic from your own network — the signal will be confounded.
3. **Measure three things:**
   - **CTR on the CTA** from cold traffic — the primary signal.
   - **Scroll depth** — if 80%+ don't scroll past the fold, the H1 is broken.
   - **Time on page** — if <5 seconds, the visual/H1 mismatch is turning them away instantly.
4. **Compare against benchmarks:** >15% CTR from cold traffic = strong resonance. 5–15% = partial resonance, iterate the H1. <5% = broken framing, either wrong buyer or wrong pain articulation.
5. **After the click, redirect to a "we're rolling out in batches" page** — Buffer-style. Capture email. The email list is not the validation signal; the click was. But the email is useful for follow-up interviews.
6. **Interview 3–5 people who clicked but didn't enter email.** The drop-off between click and email capture is where the second layer of signal lives.

## Example

The article's referenced benchmark: >15% CTR is strong resonance. A concrete case: Dropbox's early landing page was a two-minute demo video with a "sign up for beta" button. The video was the visual proof; the demo demonstrated the outcome (files sync across machines) without any working code. The beta signup CTR was strong enough that the beta list went from 5,000 to 75,000 overnight. That behavioral signal, from a stranger audience, was enough to justify building the actual product. Dropbox validated the *concept* before the code.

## Limitations

- **Does not validate WTP.** A click means "I'm interested." A payment attempt means "I'll pay." These are different behaviors. Pair with Pre-Sale WTP Test to convert click-interest into paid interest.
- **CTR benchmarks are audience-dependent.** 15% CTR from a highly targeted enterprise audience is different from 15% CTR from a broad consumer audience. Calibrate against the CTR norm for your industry's typical paid campaign.
- **Requires cold traffic.** Traffic from your network — Twitter followers, email list, LinkedIn — is contaminated by social bias. If you can't afford paid ads, at minimum use paid Reddit/LinkedIn promoted posts to reach strangers.
- **Framing is confounded with pain.** A low CTR could mean the pain is real but your framing is off, OR the pain isn't real. You need to iterate the H1 (holding everything else constant) before concluding pain is absent.
- **Consumer smoke tests convert differently from B2B smoke tests.** Enterprise buyers rarely convert on a landing page — they need a conversation. Use LOI for B2B validation instead.

## Connection to the Loop

Run **after** you have a pain vocabulary (from community mining and Mom Test interviews) and **before** you commit to building. The Smoke Test Landing Page is the cheapest solution-verification experiment — it costs $200–500 in ads and 4–8 hours of design work. It is the natural bridge between "we understand the pain" and "the market recognizes our proposed solution." Chain into Pre-Sale WTP Test (add a payment mechanism) and Pricing Tier Test (add three prices). Set a Kill Criteria Contract before launching: "If CTR is under 8% after $500 spend, we pivot the H1 or kill the offer."

See also: `practices/pre-sale-wtp-test.md`, `practices/pricing-tier-test.md`, `validation/kill-criteria-contract.md`, `practices/mom-test-interview-script.md`
