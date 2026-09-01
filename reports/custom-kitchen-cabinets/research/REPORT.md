---
purpose: The measured US market size for this idea — TAM, the beachhead article, SAM and SOM, each step with its basis.
generated: 2026-08-31 by scripts/research/build_report_us.py
---

# Configurable furniture from an autonomous factory — US market size

Generated 2026-08-31 from `scripts/research/run_all.py`. Every figure traces to a file in `data/processed/` and a line in `data/MANIFEST.jsonl`. Numbers that are assumptions rather than measurements are marked **(assumption)** where they are used.

## The three numbers

| | Value | What it is |
|---|---:|---|
| **TAM** | $88.0bn / yr | Everything US households spend on furniture, built bottom-up from CEX spend × consumer units |
| **SAM** | $52.7m / yr | The beachhead article, cut to the share of buyers who want it configured and can be sold to online — $52.7m product plus $0 assembly |
| **SOM** | $2.8m / yr | Year 3, capacity-led: what one autonomous cell can physically produce, at the blended tier price |

SOM is the smaller of what one cell can make (2,812 units/yr, derived from measured station cycle times) and what the market supports (1,249 units/yr). **Demand binds** — the cell is 2.3× larger than year-3 demand. The scarce thing is buyers, not throughput.

## What the data says

1. **The beachhead article is kitchen and dining room furniture** — the storage family: shelving, media units, wall systems. It wins not because demand for it is largest ($5.3bn a year, 6.0% of the furniture TAM) but because it is the only high-demand family that is fully machinable from nested sheet stock *and* ships flat. Sofas score higher overall on raw demand and custom interest, and are the largest furniture line in the country at $26.5bn a year — but roughly 85% of a sofa is foam, springs and sewing, so an autonomous panel factory cannot make one.

2. **Measured demand for *custom* is thin in every article family.** Across the generic/custom keyword pairs, the custom framing runs at well under 1% of the generic term. For the beachhead article the median pair is 0.55%. If the plan is to buy existing custom-furniture demand with ads, that is the ceiling being bought against, and it is small.

   The pairs behind that median are `custom dining table/dining table=0.55%`. The median is used rather than the mean because `closet organizer` is a weak denominator — it is not how people search for a closet — which inflates its pair to a figure that would drag the mean to 0.6% on its own. The spread is left visible rather than averaged away.

3. **The one place custom demand is genuinely large is next door, not here.** `custom cabinets` runs at 7.6% of `kitchen cabinets` — an order of magnitude above any furniture article. But that is home-improvement spend sold through installers, outside the CEX furniture TAM and outside a ship-it-flat business. It is the adjacency to grow into once there is a factory, not the article to launch with.

4. **The thesis rests on an assumption no available data can test.** The measured 0.55% is who searches for custom *today*, when custom means a large premium and a long wait from a joinery shop. An autonomous factory sells configurable at close to stock price, which is a different product to a different buyer. The SAM below assumes that removing the premium multiplies the willing share by 6× **(assumption)**. Everything about whether this is a $8.8m market or a $131.8m one turns on that one number, and the cheapest way to measure it is a configurator landing page with real pricing.

5. **The tier ladder carries the economics; the assembly service enables them.** Three tiers off one cell blend to a $2,532 order at a 56% margin. In-home assembly contributes $0 of that — 0.0% of revenue — because the attach can only be sold in metros where crews exist, and the top 25 metros are 42% of the country. Read the service as what makes a 2.36× premium tier credible, not as a second revenue line.

6. **Domestic manufacturing has been losing to imports for the whole period.** US wood-furniture imports run around $23.7bn a year. An autonomous factory is a bet on reversing that with labour cost, which is the actual thing being sold to an investor — the market-size numbers above are the smaller half of the argument.

## Which article to build

Every article line under CEX *Furniture* is sized from household spend and scored on four dimensions: pool size (what there is to sell), custom-search share (whether anyone wants it configured), machinability and flat-packability **(the last two are judgements about an autonomous panel cell, not measurements)**. Weights: pool 30%, custom_share 30%, machinable 25%, flatpack 15%.

| Score | Score if assembled | Article | US pool | % of TAM | Q5 skew | Custom share | Machinable | Flat-pack | Buildable here |
|---:|---:|---|---:|---:|---:|---:|---:|---:|:--:|
| 0.683 | 0.627 | Kitchen and dining room furniture ⭐ | $5.3bn | 6.0% | 2.36× | 0.55% | 97% | 96% | yes |
| 0.670 | 0.615 | Living room tables | $2.4bn | 2.8% | 1.83× | 0.61% | 95% | 95% | yes |
| 0.670 | 0.754 | Sofas | $26.5bn | 30.1% | 2.13× | 0.70% | 10% | 30% | no |
| 0.592 | 0.539 | Wall units, cabinets and other occasional furniture | $6.2bn | 7.1% | 1.87× | 0.48% | 72% | 90% | yes |
| 0.571 | 0.515 | Other bedroom furniture | $16.2bn | 18.4% | 2.26× | 0.20% | 65% | 92% | yes |
| 0.385 | 0.289 | Outdoor furniture | $6.4bn | 7.3% | 2.36× | — | 70% | 92% | yes |
| 0.370 | 0.274 | Living room chairs | $8.0bn | 9.0% | 1.85× | — | 55% | 95% | yes |
| 0.352 | 0.248 | Infants' furniture | $1.5bn | 1.7% | 1.82× | — | 80% | 90% | yes |
| 0.325 | 0.240 | Mattresses and springs | $15.5bn | 17.6% | 1.75× | — | 0% | 100% | no |

*Q5 skew is how much more the top income quintile spends on that article than the average household — a measure of how far the category can be priced up.*

The top-scoring article and the chosen article differ, and that is the point of the `Buildable here` column: the score ranks demand, the column applies the constraint. **Kitchen and dining room furniture** is the highest-scoring article this factory can actually make.

`Score if assembled` re-runs the same scoring with the flat-pack weight cut from 15% to 3% — the question of whether selling in-home assembly should change which article you build, since a crew in the customer's home removes the reason to fear a bulky box. It does not: **Kitchen and dining room furniture** wins under both weightings. The service tier changes the margin on the article, not the choice of it.

## The model, step by step

| Step | Value | Basis |
|---|---:|---|
| US consumer units | 135,761,000 | CEX CONSUNIT 2024 |
| US household furniture spend (TAM) | $88.0bn | CEX FURNITUR x consumer units, summed over income quintiles, 2024 |
| Beachhead article | Kitchen and dining room furniture | highest beachhead score (0.6831) among articles this factory can physically build |
| Serviceable population share | 0.41912 | Census CBSA vintage 2024: the top 25 metros hold 41.9% of the US population |
| Blended revenue per order | 2532.25 | tier mix x tier price, plus the assembly attach earned inside serviced metros |
| SAM (base, product + service) | $52.7m | product: article pool x (measured custom search share x willing multiple) x online-addressable share; service: the order count that implies x blended attach x assembly price |
| SOM (year 3, capacity-led) | $2.8m | the smaller of factory capacity and market demand — demand binds; ramped over three years, valued at the blended tier price plus the assembly attach |

**Sanity check.** The CEX build puts US household furniture spend at 66% of Census retail sales for NAICS 442 ($132.7bn). NAICS 442 covers furniture plus home furnishings — rugs, lamps, window treatments, housewares — so CEX furniture landing at roughly two-thirds of it is the expected shape. Above 1.0 or below 0.4 would mean the CEX build is wrong.

## Tiers and the assembly attach

Three tiers off the same cell, plus in-home assembly at $0 **(assumption)**. The premium price multiple is the one number here that is not a guess: it is the article's measured Q5 spend skew — the top income quintile already spends 2.36× the average household on this article, which is the observable evidence for how far it can be priced up. Tier mix, margins and attach rates are **assumptions**.

**There is no assembly attach.** kigumi joinery assembles by hand without tools or fasteners, so white-glove assembly has nothing to do. That also removes a constraint: with nothing to install, nothing caps sales to the 42% of the US population inside serviced metros. The columns below are kept at zero so the service can be switched back on by changing numbers rather than restructuring the model.

| Tier | Price | Mix | Margin | Attach in-metro | Effective attach | Revenue / order | Gross profit / order |
|---|---:|---:|---:|---:|---:|---:|---:|
| essential (0.75×) | $1,740 | 45% | 50% | 0% | 0.0% | $1,740 | $870 |
| signature (1.0×) | $2,320 | 40% | 55% | 0% | 0.0% | $2,320 | $1,276 |
| premium (2.36×) | $5,475 | 15% | 62% | 0% | 0.0% | $5,475 | $3,395 |
| **blended** | **$2,532** | 100% | **56%** | — | **0.0%** | **$2,532** | **$1,411** |

**The tier ladder does more than the service does.** The premium tier lifts the blended product price to $2,532 and the blended margin to 56%. The assembly attach adds $0 per order — 0.0% of revenue. At this scale in-home assembly is a conversion and differentiation lever, not a revenue line: it is what lets you sell a premium tier at 2.36× and hold a 62% margin, and the direct revenue is rounding error against that.

Raising the attach price or the serviced-metro count moves 0.0% of revenue. Raising the premium tier's mix share by ten points moves considerably more. If the service is meant to be a business rather than an enabler, it needs a materially higher price or an attach that reaches beyond the top 25 metros.

## SAM — the configurable, online-addressable slice

Article pool $5.3bn × willing share × online-addressable share. The willing share starts from the measured 0.55% search share and is multiplied to reflect that an autonomous factory removes the custom premium; the multiple is an **assumption**, capped at 50%. The online-addressable share is also an **assumption** — Census e-commerce share by merchandise line would measure it.

| Willing share | online 20% | online 30% | online 40% |
|---|---:|---:|---:|
| floor — 0.6% of buyers (measured, no uplift) | $5.9m | $8.8m | $11.7m |
| base — 3.3% of buyers (assumed) | $35.1m | $52.7m | $70.3m |
| ceiling — 8.3% of buyers (assumed) | $87.8m | $131.8m | $175.7m |

That grid sizes the **product** SAM. Assembly is a service and sits outside the CEX furniture pool entirely, so it is additional rather than a slice of the same dollars: the base product SAM implies 20,814 orders a year, which at an 0.0% blended attach adds $0 — a total SAM of **$52.7m**.

Base product case **$52.7m a year**. The spread across the grid is $5.9m to $175.7m — a 30× range driven almost entirely by two assumptions. Treat the floor row as the only defensible number until the willing share is measured.

## SOM — the smaller of what we can make and what we can sell

One cell, 250 operating days, 7.0h of machine time per shift, 95% yield, 0.224h per unit **(assumption — replace with the cycle time off your own cell)**, valued at the blended order of $2,532 from the tier table above. Cycle time is no longer assumed: build_factory.py: 13.4 min takt at the 5-axis joinery — legs and stiles station, 72% OEE, 4 units to an order.

| Shifts | Units / yr | Revenue at blended order | % of total SAM |
|---:|---:|---:|---:|
| 1 (low) | 1,406 | $3.6m | 6.76% |
| 2 (base) | 2,812 | $7.1m | 13.51% |
| 3 (high) | 4,218 | $10.7m | 20.27% |

### Three-year ramp at 2 shifts

| Year | Utilisation | Units | Units / wk | Product rev | Installs | Service rev | Crews | Total revenue | Gross profit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Year 1 | 25% | 312 | 6.0 | $790,593 | 0 | $0 | 0.0 | $790,593 | $440,574 |
| Year 2 | 60% | 749 | 14.4 | $1.9m | 0 | $0 | 0.0 | $1.9m | $1.1m |
| Year 3 | 90% | 1,124 | 21.6 | $2.8m | 0 | $0 | 0.0 | $2.8m | $1.6m |

Gross profit is the blended figure from the tier table. Year 3 is 21.6 orders a week out of a single cell — a manufacturing number, and the plant is not short of room to make it.

**The factory does not deliver the assumed margin at this volume.** The tier ladder assumes 56%; at 1,124 units the modelled cost is $1,727 a unit against a $2,532 order — 32%. They converge near 5,000 units a year. The cost build-up is in `reports/autonomous-factory-plan.html`.

### Can you buy the demand to fill the line?

CPC basis: PLACEHOLDER — Keyword Planner not run. The only unmeasured number in the acquisition maths. ($2.50). Gross profit per order $1,411, blended across the tier mix and the assembly attach.

| Site conversion | Implied CAC | % of order value | % of gross profit | Year-3 ad spend |
|---:|---:|---:|---:|---:|
| 0.5% | $500 | 19.7% | 35.4% | $562,000 |
| 1.5% | $167 | 6.6% | 11.8% | $187,333 |
| 3.0% | $83 | 3.3% | 5.9% | $93,667 |

At a 0.5% conversion rate paid acquisition eats most of the gross profit, and the capacity plan stops being fundable from its own margin. Getting the real CPC out of Keyword Planner is the highest-value missing measurement in this model.

## Who already makes this (Census CBP 2022, US)

| NAICS | Industry | Establishments | Employees | Annual payroll | Under 5 staff |
|---|---|---:|---:|---:|---:|
| 337/// | Furniture and related product manufacturing | 14,606 | 371,164 | $18.5bn | 6,846 |
| 3371// | Household and institutional furniture | 10,187 | 230,036 | $10.6bn | 5,278 |
| 337122 | Nonupholstered wood household furniture | 2,126 | 23,526 | $1.0bn | 1,280 |
| 337212 | Custom architectural woodwork and millwork | 2,352 | 43,464 | $2.6bn | 870 |
| 442110 | Furniture stores (retail) | 22,286 | 197,264 | $9.9bn | 11,783 |

The under-5-staff column is the competitive read: this industry is mostly very small shops. That is what makes an automation thesis plausible, and also what makes the incumbents impossible to acquire share from quickly — they are local, referral-fed and numerous.

## Purchase intent (Google Trends, US, five years)

Every term is scaled against the same anchor (`dining table` = 1.00), so all batches are comparable. Custom-share per family is the pair ratio.

| Generic term | Interest | Custom term | Interest | Custom share |
|---|---:|---|---:|---:|
| desk | 4.182 | custom desk | 0.026 | 0.61% |
| sofa | 2.287 | custom sofa | 0.016 | 0.70% |
| dresser | 1.124 | custom dresser | 0.002 | 0.20% |
| bed frame | 1.119 | custom bed frame | 0.004 | 0.37% |
| dining table | 1.000 | custom dining table | 0.006 | 0.55% |
| coffee table | 0.877 | custom coffee table | 0.005 | 0.61% |
| tv stand | 0.628 | custom tv stand | 0.002 | 0.39% |
| kitchen cabinets | 0.603 | custom cabinets | 0.046 | 7.61% |
| bookshelf | 0.504 | custom bookshelf | 0.002 | 0.48% |
| wardrobe | 0.466 | custom wardrobe | 0.001 | 0.20% |
| nightstand | 0.324 | custom nightstand | 0.002 | 0.54% |
| closet organizer | 0.114 | custom closet | 0.034 | 29.71% |

### Which customisable furniture is most in demand

Every term is a `custom X` anchored on `custom furniture`, so the categories are comparable to each other. `0/1 weeks` is the share of weeks the index sat at or below 1 — above 80% the series is at the Trends resolution floor and is reported as unresolved rather than ranked, because a number that is 95% zeros is not a small number, it is an absent one.

| Article | Level | Custom share of generic | Genuinely furniture | 0/1 weeks | Score |
|---|---:|---:|---:|---:|---:|
| custom cabinets ~ | 1.054 | 7.61% | 100% | 0% | 0.914 |
| custom bar ~ | 1.202 | — | 47% | 0% | 0.840 |
| custom closet ~ | 0.589 | 29.71% | — | 0% | 0.643 |
| custom desk | 0.665 | 0.61% | 48% | 0% | 0.532 |
| custom chair | 0.694 | — | 42% | 3% | 0.529 |
| custom vanity ~ | 0.342 | — | 75% | 0% | 0.424 |
| custom shelving ~ | 0.103 | — | 100% | 75% | 0.360 |
| custom sofa | 0.480 | 0.70% | 18% | 54% | 0.334 |
| custom bench | 0.312 | 0.25% | 36% | 14% | 0.289 |
| custom dining table | 0.209 | 0.55% | 100% | 91% | _unresolved_ |
| custom coffee table | 0.180 | 0.61% | 100% | 86% | _unresolved_ |
| custom bed frame | 0.139 | 0.37% | 100% | 90% | _unresolved_ |
| custom stool | 0.081 | — | 100% | 93% | _unresolved_ |
| custom bookshelf | 0.076 | 0.48% | — | 94% | _unresolved_ |
| custom kitchen island ~ | 0.073 | — | 100% | 93% | _unresolved_ |
| custom outdoor furniture ~ | 0.070 | — | 0% | 94% | _unresolved_ |
| custom wardrobe | 0.055 | 0.20% | 100% | 92% | _unresolved_ |
| custom headboard | 0.050 | — | — | 94% | _unresolved_ |
| custom dining chair | 0.048 | 1.01% | 100% | 94% | _unresolved_ |
| custom console table | 0.041 | 0.84% | — | 95% | _unresolved_ |
| custom nightstand | 0.040 | 0.54% | — | 95% | _unresolved_ |
| custom built ins ~ | 0.007 | — | — | 100% | _unresolved_ |
| custom mantel ~ | 0.007 | — | 100% | 99% | _unresolved_ |
| custom conference table | 0.006 | — | 100% | 100% | _unresolved_ |

*~ = not free-standing furniture: a built-in or an adjacent trade.*

**15 of 24 categories cannot be ranked at all** — they sit at the index floor. Of the 9 that resolve, 5 are built-ins rather than furniture.

The best-resolved free-standing furniture is `custom desk`, and even that is only 48% genuinely furniture in its related searches — the rest is accessories.

**Momentum is not reported.** 13 of 25 series peak in the same week (2026-04-12) across independent query batches, which is an index artifact rather than demand; any year-on-year figure spanning it measures the artifact. The ranking uses level only.

**Google Trends is a relative index, not a volume.** Keyword Planner turns these into monthly search counts and a cost per click, and is the only way to resolve the 15 categories that are invisible here.

**Where `custom furniture` interest sits** (unanchored, 100 = peak state):

| State | Index |
|---|---:|
| Wyoming | 52 |
| North Carolina | 46 |
| Vermont | 44 |
| Mississippi | 40 |
| New York | 39 |
| Connecticut | 39 |
| Montana | 39 |
| West Virginia | 39 |

## Household furniture spend by income quintile, 2024 (BLS CEX)

Average annual expenditure per consumer unit.

| Quintile | Kitchen and dining room furniture | All furniture |
|---|---:|---:|
| Q1 lowest 20% | $15 | $275 |
| Q2 | $9 | $371 |
| Q3 | $22 | $462 |
| Q4 | $57 | $795 |
| Q5 highest 20% | $92 | $1,334 |
| All consumer units | $39 | $648 |

The top income quintile spends $92 a year on the beachhead article. A $2,320 unit is therefore not an annual purchase out of a furniture budget — at that rate it is a 25-year purchase, which is what the acquisition maths above has to survive.

### US furniture retail sales, NAICS 442 (Census MRTS)

| Year | Sales | YoY |
|---:|---:|---:|
| 2019 | $118.0bn | +1.3% |
| 2020 | $111.1bn | -5.9% |
| 2021 | $138.1bn | +24.2% |
| 2022 | $140.5bn | +1.8% |
| 2023 | $135.6bn | -3.5% |
| 2024 | $132.7bn | -2.1% |
| 2025 | $135.6bn | +2.2% |
| 2026 (first 6 months) | $65.1bn | -2.0% vs. the same months of 2025 |

### Import exposure (UN Comtrade, US imports)

| Year | US wood-furniture imports |
|---:|---:|
| 2019 | $20.7bn |
| 2020 | $21.2bn |
| 2021 | $27.8bn |
| 2022 | $31.8bn |
| 2023 | $23.6bn |
| 2024 | $25.4bn |
| 2025 | $23.7bn |

## Not yet collected

| Source | Blocked on |
|---|---|
| census-acs / bay-area-households | CENSUS_API_KEY not set |
| census-econ / industry-shipments | CENSUS_API_KEY not set |
| etsy / listings-and-shop-sales | ETSY_API_KEY not set |
| google-ads / keyword-metrics | missing: GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET, GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_AD |
| semrush / competitor-organic-keywords | SEMRUSH_API_KEY not set |

See `scripts/research/CREDENTIALS.md`. Keyword Planner is the one that matters most: it replaces the placeholder CPC, which drives the whole acquisition section.

## Provenance

| Source | Dataset | Rows | Status | Fetched |
|---|---|---:|---|---|
| analysis | cabinet-tam | 13 | ok | 2026-08-28 14:54 |
| analysis | custom-category-adjustment | 25 | ok | 2026-08-28 12:23 |
| analysis | custom-demand-ranking | 24 | ok | 2026-08-28 12:25 |
| analysis | factory-model | 23 | ok | 2026-08-28 12:38 |
| bls-cex | furniture-expenditure | 1,430 | ok | 2026-08-27 20:41 |
| bls-prices | prices-and-employment | 1,378 | ok | 2026-08-28 10:45 |
| census-acs | bay-area-households | 0 | blocked_no_credential | 2026-08-27 20:17 |
| census-bps | bay-area-permits | 92 | ok | 2026-08-27 20:13 |
| census-cbp | establishments-by-naics | 457 | ok | 2026-08-28 12:35 |
| census-econ | industry-shipments | 0 | blocked_no_credential | 2026-08-27 20:17 |
| census-mrts | monthly-retail-442 | 2,070 | ok | 2026-08-27 20:13 |
| census-popest | county-population-migration | 60 | ok | 2026-08-27 20:13 |
| census-popest | metro-coverage | 387 | ok | 2026-08-27 21:06 |
| etsy | listings-and-shop-sales | 0 | blocked_no_credential | 2026-08-27 20:43 |
| google-ads | keyword-metrics | 0 | blocked_no_credential | 2026-08-27 20:43 |
| google-trends | custom-furniture-categories | 118 | ok | 2026-08-28 12:23 |
| google-trends | purchase-intent-terms | 14,968 | ok | 2026-08-28 12:19 |
| semrush | competitor-organic-keywords | 0 | blocked_no_credential | 2026-08-27 20:43 |
| un-comtrade | us-wood-furniture-imports | 4,663 | ok | 2026-08-27 20:17 |
