---
method: segment-wedge-map
run_id: "2026-08-31"
mode: explore
card: methods/ideation/segment-wedge-map.md
depends_on: [corpus-pool, jtbd-substitute-map]
counter_query_run: yes - "which segments have already solved it"
---

# Segment and wedge map

Segments defined per the card as **customer type + affected role + workflow circumstance** —
not as industries.

## Segment universe

| Segment | Role | Pain evidence | Workaround / spend | Reach | Substitute quality | Incumbent posture | Path out | Conf |
|---|---|---|---|---|---|---|---|---|
| **Custom / commercial millwork, 80%+ one-off** | owner / CNC programmer | **verbatim, unprompted**: *"garbage"*, *"horrendous to custom build with"*, coordinates typed by hand, materials allocated on paper across 25 rooms | owns Mozaik anyway, 30 yrs of working around it | WOODWEB, trade shows — reachable | **fails at exactly this** | **served poorly — business model conflicts**: Mozaik's economics are volume-priced at $125/mo for box shops; deep custom is a different product | into standard cabinetry, then panels | **medium** |
| Small cabinet shop, standard boxes | owner-estimator | quoting spread 5 min – 7 hrs; *"overwhelmed"*, *"exhausting"*; 30 of 72 bids wasted | Excel + PDF + email; price-per-inch scales | same | **good — users are happy** | **actively served** (Mozaik) | — | high |
| Structural / misc steel fabricator | estimator | 4-8 hrs manual takeoff per mid-size package, named the main bottleneck | manual takeoff, or hire estimators | trade bodies | thin, tools emerging | actively being entered now | — | medium |
| CNC / sheet-metal job shop | owner-estimator | quotes due in 24 hrs–1 wk; shops pushing 5 days → 1-2 | Paperless Parts exists | Practical Machinist | improving | **actively served** — Protolabs, Xometry, Fictiv, Paperless Parts | — | high |
| US panel processing at carcass scale | shop / contractor / consumer | **none found** | unknown | unknown | absent in US; solved in UK (Cutwrights 2009) | unknown | — | **low** |
| Stone / quartz countertops | fabricator | none — digital templating standard, 20-45 min layouts | SlabSmith | — | **good** | actively served | — | high |
| Freestanding furniture | consumer | prior E1/E2: custom demand <1% of generic | catalogue | — | good | actively served + a graveyard | — | high |

## Distinguishing dismissal from rational avoidance (card step 5)

The custom-millwork pocket is **not** ignored because incumbents are lazy. Mozaik serves 1-20
person box shops at $125/month; building deep parametric custom capability is a different and
much more expensive product for a smaller, more heterogeneous market. Cabinet Vision aimed at
it and is described by 1-25 employee shops in one-star terms, *"tired of being gouged"*, and
*"I can't remember the last time it was even opened."*

So: incumbents tried the top end and are losing it on usability and price, while the cheap
tool deliberately stops short. **That is a genuine structural gap rather than an oversight** —
which is what the card is asking. The avoidance is rational for *them*, not necessarily for a
new entrant.

**But the counter-test the card demands** — does the segment have enough pain, spend,
aggregation and path outward to support a company? — is **unanswered**. Custom millwork shops
are few, fragmented, and their spend is unknown. Nobody said this costs them money.

## Recommended wedge

**Custom / commercial millwork one-off work** — the only segment in the universe where a
practitioner described the belief's exact mechanism failing, in their own words, unprompted.

**Why this segment first:** it is the single point where the design-to-machine coupling is
still manual after everything else in the corpus has been automated. Standard boxes: solved
for $125/month. Metal parts: solved since 1999. Countertops: solved. Freestanding furniture:
no demand. This pocket is what is left, and it is left for a reason that looks structural.

**Why incumbents underserve it:** volume-priced box software cannot fund deep custom
parametric work; the vendor that tried it is being abandoned on usability and price.

**Why incumbent avoidance may be rational:** small, fragmented, heterogeneous segment; every
shop builds differently (*"it will adapt to the way YOU build cabinets"*), so the thing being
automated may not generalise across shops. **This is the strongest argument against the wedge
and it is not resolved.**

**Adjacent expansion:** custom millwork → standard cabinetry → panel goods generally → any
per-order panel product. Credible, but unverified.

## Counter-query — which segments have already solved it

Run. It eliminated three candidates outright: **stone/quartz countertops** (digital templating
standard, SlabSmith exports to CNC, 20-45 min layouts), **standard cabinet boxes** (Mozaik,
with actively satisfied users), and **CNC/sheet-metal job-shop parts** (Protolabs, Xometry,
Fictiv, Paperless Parts). Running this query first would have saved the first pass from
ranking cabinetry at all.

## Unknowns

- Does the custom-millwork pain cost money, or only time and irritation? Nobody said.
- Is cncpgmr representative, or one unusual shop? **n=1.**
- Segment size, aggregate spend, and reachability: all unknown.
- Whether per-shop build methods are too heterogeneous to automate — the rational-avoidance
  case, untested.
