---
name: Pricing Tier Test
category: customer-validation
excluded_because: "needs the world: a live page with three instrumented tiers + cold traffic"
applicable_at: [validation]
assumption_categories_it_helps: [buyer, market]
source:
  title: "Startup Validation Framework 2026: The Ultimate Guide to Testing Ideas"
  author: Presta / WeArePresta
  url: ""
  date: "2026-01-26"
---

## Core Insight

Founders set prices by guess. The Pricing Tier Test replaces the guess with observed selection: display three tiers on the same page and measure which tier gets clicked. The distribution of clicks across the tiers is a behavioral answer to a question that surveys cannot answer honestly. Buyers asked "how much would you pay?" produce noise; buyers presented with three prices produce signal, because the act of clicking picks one of them.

The mechanism: humans anchor on relative price, not absolute price. Three tiers create three anchors, and the click distribution reveals where the buyer's mental model of value places your offering. If everyone clicks the highest tier ("Enterprise, Contact Us"), the offering is under-priced — the buyer's willingness-to-pay is above your top tier. If everyone clicks the lowest tier or the free trial, the middle tier isn't compelling — either the differentiation isn't clear or the middle price is above the perceived value. If clicks distribute across all three, you have discovered your price segmentation.

This is not a WTP test — nobody has paid. It is a price *sensitivity* test. It surfaces where the market thinks your value lives, on the specific relative scale you offered.

## Process

1. **Prerequisite:** Smoke Test Landing Page has already validated solution resonance. Running a pricing test on a broken offer produces meaningless data.
2. **Design three tiers with distinct value framing.** Not just "cheap / medium / expensive" — three genuinely different offers:
   - **Self-Serve tier:** monthly subscription, self-onboarding, feature-limited. E.g., $29/mo for consumer or SMB, $299/mo for prosumer.
   - **Pro tier:** higher-tier features, onboarding assistance, priority support. Typically 2.5–3x the Self-Serve price.
   - **Enterprise tier:** "Contact Us" — no price shown, implies custom deal, integration, procurement. Includes a form field or calendar link.
3. **Display all three tiers on a single page** with visible feature-difference bullets. Do not hide any tier behind a click — the comparison itself is the experiment.
4. **Instrument each CTA separately.** Track: clicks on Self-Serve, clicks on Pro, clicks on Enterprise. Also track total page visits — the click *rate* per tier matters, not just the absolute click count.
5. **Drive cold traffic** as with the Smoke Test — network traffic invalidates the signal.
6. **Read the distribution against these patterns:**
   - **Enterprise dominates (>50% of clicks):** You are severely under-priced. The market perceives higher value than your Pro tier suggests. Raise all prices — probably 2–5×.
   - **Self-Serve dominates but few complete signup:** Price is right for interest but not for commitment. The visible offering is not compelling enough at any price.
   - **Pro dominates:** Your middle price captures the median buyer. Good — this is often the target.
   - **Distribution is even across all three:** You've found segmentation. Different buyer types self-select into different tiers. Confirm by follow-up interviews with each cohort.
   - **Free Trial (if offered) dominates and nobody converts:** Your value isn't clear to the buyer. They want to test-drive because they don't yet believe.
7. **Iterate one variable at a time.** If the distribution is wrong, change one tier price (typically Pro up or down 30–50%) and re-run. Changing all three simultaneously destroys the ability to attribute the shift.

## Example

From the article: if 100% of clicks go to "Enterprise, Contact Us," the interpretation is unambiguous — the buyer's mental price ceiling is above your visible tiers. Realistic case: a founder shows $49/$149/Contact Us on a B2B tool. 80% click "Contact Us." Those inbound calls turn into $30k/year contracts. The founder discovers, in one week of ad spend, that their perceived-value ceiling was 20× their initial guess. Without the test, they would have shipped at $149 and left 95% of revenue on the table.

Buffer's original two-tier test worked similarly — Joel Gascoigne showed a pricing page before the product existed. The click distribution across plans told him which pricing model resonated. That informed the actual pricing at launch.

## Limitations

- **Does not measure absolute WTP — only relative.** A buyer clicking your Pro tier doesn't mean they'll pay $79/mo. It means the Pro tier is more attractive than the other two at those prices, on that page, in that visit. Pair with Pre-Sale WTP Test for absolute WTP.
- **Anchoring is manipulable.** Adding a fake $999 "Ultimate" tier will drag more clicks to the "Pro" tier below it. This is a real psychological effect (decoy pricing), but if you use it as a manipulation you're validating the manipulation, not the pricing.
- **Enterprise "Contact Us" clicks are ambiguous.** They can mean "I'll definitely buy at any price" or "I want more info because your visible tiers are unclear." Interview the first 3 who click to disambiguate.
- **B2C consumer psychology differs from B2B.** Consumer buyers cluster around the anchor. Enterprise buyers with procurement processes may click Enterprise regardless of the value proposition, because that's how they buy anything. Calibrate by segment.
- **Cannot use for pre-product-existence enterprise deals.** For $50k+ enterprise contracts, no landing page will produce meaningful pricing signal. Use LOI with named prices instead.

## Connection to the Loop

Run after the Smoke Test Landing Page has confirmed solution resonance and before you commit to a launch price. This is a diagnostic experiment, not a validator — it tells you which of three price hypotheses is closest to right. If the offering is B2B enterprise, skip this method and use LOI B2B Validation to test price with a specific buyer. Set kill criteria before running: e.g., "If total CTR across all three tiers combined is under 5% from cold traffic, the offer is broken, and pricing data is meaningless — return to smoke test H1 iteration."

See also: `practices/smoke-test-landing-page.md`, `practices/pre-sale-wtp-test.md`, `practices/letter-of-intent-b2b.md`, `validation/kill-criteria-contract.md`
