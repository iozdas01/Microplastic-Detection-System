---
purpose: What public reviews and trade sources say about misfits in made-to-measure window coverings.
idea: high-mix-manufacturing
collected: 2026-09-03
method: review sites and trade publications (Reddit/HN recon did not return — see note at end)
status: raw reconnaissance, no hunch attached
---

# Window covering misfits — what the public record says

Collected 2026-09-03. This is reconnaissance for a candidate lane, not evidence against any
live assumption. No hunch declares this segment yet.

## 1. The industry prices the misfit as a known, recurring cost

**SelectBlinds gives away "FIT Protection": a free remake at corrected dimensions if the
CUSTOMER measured wrong.** Not a defect warranty. A free do-over for the buyer's own error,
offered at checkout on any window covering.

That is the strongest single signal here, and it is a behaviour rather than an opinion. A
company does not absorb remakes on a made-to-order product unless the misfit rate is high
enough that fear of mismeasuring was blocking purchases, and eating the remake is cheaper
than losing the sale. They have measured this and decided to pay for it.

AmericanBlinds and Blinds.com run comparable fit guarantees. Terms are typically capped at
one remake per product within a window of about 90 days, though the full conditions sit
behind a separate terms page rather than the marketing one.

## 2. The remake economics, published by a manufacturer

Sun Glow (Canadian window covering manufacturer) states plainly in its dealer pricing guide
that on a remake from a mis-measure "you pay the product cost twice and the labour twice
while collecting once", and gives the profit arithmetic:

| Dealer margin | Similar jobs wiped out by ONE remake |
|---|---|
| 30% | 2.3 |
| 40% | 1.5 |
| 50% | 1.0 |
| 60% | 0.7 |

Their own note says this assumes the dealer absorbs only the product cost — adding the
return install makes it worse. They also advise dealers to get remake policy and remake
turnaround from suppliers **in writing before the first order**, which is not advice you
give about a rare event.

## 3. Custom means the buyer has no refund right

The recurring theme in negative reviews is that because the product is made to order there
is no refund path, only a goodwill remake. Where the fit guarantee is declined, the buyer
absorbs the full cost. Disputed fit-warranty claims appear repeatedly.

## 4. The remake turnaround is the pain, not the remake

From a page of 1-star SelectBlinds reviews on Trustpilot, the recurring themes were:

- **6 of them** on wrong size, poor fit, gaps or light leakage
- **5 of them** on how long a replacement took — ranging from 3-4 weeks to **six months**
- **3 of them** on a guarantee being refused or honoured only partially
- Amounts named: £995 for five blinds, $300 out of pocket, unspecified "expensive" motorised shades

Customer service responsiveness compounds it in nearly every one: the wait is not just
manufacturing time, it is time spent establishing whose fault the measurement was.

## 5. Why this is on-thesis

A misfit is a data-transfer failure. The window has a true dimension; a person measures it;
that number goes into an order system; the order drives a machine that cuts to size. Every
handoff can lose or corrupt the number, and nobody in the chain can verify it against the
actual window until the product arrives. That is the belief stated as a product category —
software and machines not talking, with a physical, expensive, per-unit consequence.

The open question this raises is who currently eats that cost, because that is who would pay
to remove it: the manufacturer absorbing remakes, the dealer whose margin it destroys, or the
consumer whose claim gets declined. The sources above show all three happening.

## What is NOT established

- **No misfit rate.** No source gives a percentage of orders remade. The Sun Glow model is
  per-remake economics, not frequency. Without the rate, none of this can be sized.
- **No causal split** between customer mismeasure, dealer error, manufacturing tolerance and
  out-of-square windows.
- **Review samples are self-selected.** A page of 1-star reviews describes the tail, not the
  distribution, and Trustpilot ratings for these retailers are not low overall.

## Method note

`scripts.data.community_recon` was run against a four-hypothesis plan (`query-plan.json`) and
did not return within the session. This is consistent with the standing note in
`api-registry.yaml`: Reddit OAuth is closed, the SearXNG path was re-measured DOWN on
2026-09-03, and the documented substitute is a Firecrawl scrape against a Reddit search URL.
**An empty Reddit result here is a tooling failure, not absence of complaints.** The plan is
kept so it can be rerun through the Firecrawl path.

Sources: selectblinds.com guarantees and returns pages; mysunglow.com dealer margin guide;
trustpilot.com/review/selectblinds.com (1-star filter); americanblinds.com guarantee page.

---

# Addendum, 2026-09-03 — the remake spend question

**Asked: does a number exist for what the industry spends on remakes? Answer: no.**
No trade body, market report or manufacturer publishes a remake rate or an aggregate remake
cost. Every figure below is either a measured denominator or an explicitly labelled bracket.

## The denominator IS measurable

| | Value | Source |
|---|---|---|
| US blind & shade manufacturing revenue | ~$2.4-2.5bn/yr | NAICS 337920, 2025 |
| Establishments | 484 | NAICS 337920, 2025 annual average |
| Employees | ~11,116 across 291 businesses | same |

This is manufacturing only. The installed retail market (dealer margin, measure and install
labour) sits on top and is materially larger.

## The bracket, and it is a bracket not a finding

Remade order value at the manufacturer level, if the rate were:

| Remake rate | Order value remade | 
|---|---|
| 3% | ~$73m/yr |
| 5% | ~$122m/yr |
| 10% | ~$245m/yr |

**These are arithmetic, not evidence.** The rate is invented. They are here only to show
that the answer spans 3x across a plausible range, so the rate is the whole question.

The true cost is worse than the table implies. Per Sun Glow's dealer guide the manufacturer
pays material and labour twice while collecting once, so what is destroyed is closer to the
full cost of the remade units, not their margin.

## Two independent hints that the rate is NOT trivial

1. **Blinds.com's SureFit caps free customer-error remakes at 4 windows per household.** A
   cap exists because the expected claim volume was worth capping.
2. **General manufacturing benchmark:** top-quartile B2B perfect-order fulfilment exceeds
   95%. Made-to-measure with a CUSTOMER-supplied measurement should be materially worse than
   a general manufacturing line, because the dominant error source sits outside the factory.

Neither is a rate. Both argue against the rate being negligible.

## Who actually knows the number

A manufacturer tracks remakes as a standing KPI — it hits cost of goods every month. This is
not a number that requires estimation from them, only willingness to say it.

- **Hunter Douglas** — largest custom window-fashions maker in North America, since 1919
- **Springs Window Fashions** (incl. Levolor) — all major residential and commercial channels
- **Norman Window Fashions** — founded 1976, among the world's largest
- Regional and private-label makers behind Blinds.com, SelectBlinds, JustBlinds

**Highest-leverage target, and it is not a manufacturer.** `BlindMatrix` sells ERP and
software into window covering manufacturers and dealers. A vendor with many customers on one
system sees remake rates ACROSS the industry rather than at one firm, and has no competitive
reason to hide the aggregate. It surfaced incidentally in the recon rather than by design.

## The question to ask

Not "what is your remake rate" as an opener. Ask about the last one:

- "Walk me through the last remake you did. What went wrong, and where was the error made?"
- "What share of orders come back for a remake, roughly?" — they know this.
- "When it is the customer's measurement, who ends up paying?"
- "How long does a remake take compared with a first order?"

The third question is the one that names the buyer, and the buyer is whoever eats the cost.
