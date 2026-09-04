---
name: Predecessor Base Rate
category: historical
excluded_because: "needs a named category with predecessors whose outcomes have already resolved — there is nothing to enumerate before a vertical is chosen"
applicable_at: [validation, mutation]
assumption_categories_it_helps: [market, competition, business_model]
source:
  title: "Constructed for this repo, 2026-09-03"
  author: in-house
  note: >
    Written after a graveyard table of eleven hand-picked famous companies was being read
    as if it were a base rate. It is not one, and the difference is the whole card.
---

## Core Insight

A list of famous predecessors cannot produce a probability. Companies become famous by having
extreme outcomes — the $3bn incineration, the IPO — so a hand-picked list is drawn from both
tails and contains none of the middle. Any percentage computed from it is fiction in both
directions, and it is *confidently* wrong, which is worse than having no number.

A base rate requires a **cohort**: a population defined by a rule someone else could re-run,
enumerated exhaustively, with every member classified on the same outcome ladder — including
the members nobody has heard of.

The second insight is the one that pays. **The rate is almost never the finding.** A rate tells
you the category is hard, which you already suspected. Sorting the same cohort by one variable
at a time — capital raised, channel, whether they held inventory, who the buyer was — is what
tells you *which* thing kills companies here. A cohort where every member above a funding
threshold is dead says something a percentage cannot.

Run it to find the sorting variable. The percentage is a by-product.

## Process

1. **Write the population rule first, before looking at any company.** Geography, business
   model, product shape, founding-year range, funding floor. Writing it after you have the list
   is how a base rate gets rigged without anyone intending to.
2. **Cap the founding year.** Members need enough elapsed time to have an outcome. Including
   companies too young to have failed inflates survival and is the most common error.
3. **Enumerate exhaustively from category listings, trade press and funding databases** — not
   from memory. Memory returns the famous, which is the bias the card exists to defeat.
4. **Record every exclusion with its reason, in the output.** Exclusions are where the result
   is decided. A reader must be able to disagree with one specifically.
5. **Classify on a fixed ladder**, set before classifying: exited above invested capital /
   independent and growing / independent and flat / acquired below raise (rolled up) /
   distressed acquisition / dead.
6. **Pick the bar explicitly and quote it with the number.** "Exit above invested capital",
   "still trading", and "founder still owns a profitable business" are three different
   questions with wildly different answers. A rate quoted without its bar is unusable.
7. **Sort by one variable at a time and look for a clean split.** This is the step that produces
   the finding. Capital raised, inventory held, channel, buyer type, whether the product is a
   repeat purchase.
8. **Find the mechanism behind the split, in someone else's numbers.** A clean split with no
   mechanism is a coincidence in a small sample. A split plus arithmetic — purchase frequency,
   freight per order, recovery of acquisition cost — is a finding.
9. **State the error band and the direction of the residual bias.** Companies that failed
   quietly are the ones missing from any enumeration, so a cohort assembled from press coverage
   always overstates survival. Say so.

## Examples

**The shape that works.** A cohort of ten D2C made-to-order furniture companies produced a 30%
survival rate — mildly interesting. Sorting the same ten by capital raised produced the finding:
every company that raised over $20M was dead or rolled up, every company still independent had
raised single-digit millions. The mechanism was already published — a sofa is bought once a
decade, so acquisition cost has to be recovered on a single order and bought growth can never
be paid back. Capital was the accelerant, not the fuel. No percentage carries that.

**The shape that fails.** "Nine of these eleven famous companies died, therefore this category
has an 18% success rate." The eleven were selected for being notable. The rate is meaningless
and the confidence it creates is actively harmful.

## Limitations

- Cohorts in a narrow category are typically 10–50 members. That resolves 10% from 40% and
  nothing finer. Do not report a decimal place you cannot defend.
- Undisclosed acquisition prices are common and force qualitative classification — a
  consolidator buying the brand, staff not transferring, a founder departing. Say when a class
  rests on signals rather than price.
- Aggregator funding figures disagree, sometimes by multiples. Where two sources conflict,
  report both rather than choosing; a single figure that loses an argument in a meeting is worse
  than a stated range.
- Quiet failures are structurally invisible. Every cohort assembled from public sources is
  biased toward survival.
- The base rate describes the population, not the entrant. Its use is to name the mechanism the
  entrant must be exempt from — never to argue that the entrant is likely to succeed because
  the number looked acceptable.
