---
name: Kill Criteria Contract
category: inversion
excluded_because: "written before an experiment, about that experiment"
applicable_at: [validation]
assumption_categories_it_helps: [pain, buyer, market, timing]
source:
  title: "Startup Validation Framework 2026: The Ultimate Guide to Testing Ideas"
  author: Presta / WeArePresta
  url: ""
  date: "2026-01-26"
---

## Core Insight

Founders fail to kill bad ideas not because they lack evidence — they fail because they never defined what "enough evidence to stop" looks like before they started. Confirmation bias is strongest when you have sunk cost. The moment you have invested time, money, or identity into an idea, your brain selectively upgrades every weak positive signal and discounts every strong negative one. The only defense is to write the kill criteria *before you have skin in the game*.

The mechanism: pre-commitment removes motivated reasoning from the interpretation step. If you write "we will kill this idea if we don't get 10 pre-orders by January 31st" before any work begins, a result of 3 pre-orders on February 1st is unambiguous. If you write nothing, 3 pre-orders can always become "strong early signal" in hindsight. The contract is not about pessimism — it is about making the success bar concrete enough that the result is readable by a stranger.

A secondary insight from the article's framing: in 2026, the cost of building has collapsed (AI, no-code). The new scarce resource is attention — yours, your co-founder's, your early team's. Kill criteria protect that resource the way a circuit breaker protects a power grid.

## Process

1. Before starting any validation experiment, write one sentence in this form: "We will kill [idea/assumption] if [specific measurable outcome] is not achieved by [specific date]."
2. Make the metric behavioral — not "positive feedback" but "pre-orders," "signed LOIs," "customers who ask when they can buy without being prompted," "interview subjects who escalate to peers."
3. Set the date first, then the number. Reverse-engineering from "what number feels safe" produces sandbagging; setting the time window first forces realism.
4. Have a second person (co-founder, advisor, Red Team member) co-sign it. Their job is to hold you to it when you argue for an exception.
5. When the date arrives, read the criteria with a stranger — if a stranger would say "you hit it," you hit it. If a stranger would say "you're rationalizing," you are.
6. If the criteria are not met: celebrate the kill. You have just recovered the time and capital you would have spent on the next phase.

## Example

The article cites the failure mode explicitly: "We've already spent 3 months building this, we can't stop now." This is the sunk cost fallacy — the most common founder death by slow bleeding. Kill criteria are the antidote. A concrete implementation: before running a $500 landing page experiment, write "If we don't achieve >15% CTR on the CTA and at least 3 pre-orders from cold traffic by [date], we pivot the positioning or kill the test." If you end up with 8% CTR and 1 pre-order and you're still talking yourself into continuing — you didn't set kill criteria, you set aspirations.

## Limitations

- Kill criteria are only as useful as the specificity of the metric. "Not enough traction" is not a kill criterion; "fewer than 10 paying customers" is.
- Setting criteria too easy defeats the purpose — if you set a bar you'd hit by accident, you're producing false confidence, not a real test.
- Some assumptions take longer to test than any reasonable calendar date. For high-magnitude, low-frequency enterprise pain, a 4-week kill date is meaningless. Match the time window to the sales cycle of the assumption being tested, not to your impatience.
- Does not tell you *what* to build or test — only when to stop. Pairs with Hair-on-Fire Classification (determines what kind of evidence is the right bar) and Pre-Sale WTP Test (generates the behavioral metric worth measuring).

## Connection to the Loop

Set kill criteria at the start of every validation experiment, before any work begins. This is the guard rail on the entire loop — without it, every test becomes unfalsifiable in hindsight. Applies to every assumption category but is most critical for **pain** (the most emotionally laden assumption, and the one founders most resist invalidating). The kill criteria output feeds the Evidence Ledger: a missed criterion is hard negative evidence, not ambiguity.

See also: `validation/hair-on-fire-classification.md`, `practices/pre-sale-wtp-test.md`, `validation/failure-inversion.md`
