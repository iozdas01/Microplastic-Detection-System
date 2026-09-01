# Custom solid-wood furniture — Bay Area demand evidence

Generated 2026-08-27 from `scripts/run_all.py`. Every figure below traces to a file in `data/processed/` and a line in `data/MANIFEST.jsonl`.

## What the data says

1. **The Bay Area dining-furniture pool is about $138.9m a year.** Built bottom-up: 3,157,577 households × the measured CEX spend on kitchen and dining room furniture. Not a share of a global furniture number.

2. **Two independent methods disagree by an order of magnitude, and the gap is the finding.** Sizing the custom slice from search share gives $3.9m a year. Sizing it from what Bay Area wood-furniture makers actually pay their staff (CBP payroll × a revenue multiple) gives $47.2m a year — roughly 12× more. Both cannot be right, and the likeliest reading is that **this category is real but is not bought through search**: it moves through designers, architects, showrooms and referral, which search volume cannot see.

3. **Search demand for the custom framing is thin.** In California, `custom dining table` runs at 0.57% of the volume of `dining table` over five years. If the plan is to buy this demand with ads, that is the ceiling being bought against.

4. **Input costs have run ahead of output prices.** Hardwood lumber is +42.7% since January 2020 while the producer price index for nonupholstered wood household furniture is +28.7% (through 2026-07). Domestic makers have absorbed the difference — employment in furniture manufacturing is -13.7% over the same period.

5. **The Bay Area has lost 519,506 people to domestic migration since 2020**, offset only recently by international arrivals. Moving is the largest furniture purchase trigger, and net-negative domestic migration is a headwind the national furniture numbers hide.


## The bottom-up TAM

| Step | Value | Basis |
|---|---:|---|
| US consumer units | 135,761,000 | CEX CONSUNIT 2024 |
| US spend on kitchen & dining room furniture | $5.3bn | CEX item 290410 x CONSUNIT, summed over income quintiles, 2024 |
| Bay Area population share | 2.33% | Census PEP vintage 2024 |
| West-region spend factor | 1.13× | CEX 290410 West / all CUs, 2024 |
| Top-quintile spend factor | 2.36× | CEX 290410 Q5 / all CUs, 2024 |
| Bay Area households | 3,157,577 | US consumer units x Bay Area population share (ACS gives the exact count once CENSUS_API_KEY is set) |
| Bay Area dining-furniture pool (conservative) | $123.1m | households x CEX 290410 per-CU spend, conservative factor |
| Bay Area dining-furniture pool (base) | $138.9m | households x CEX 290410 per-CU spend, base factor |
| Bay Area dining-furniture pool (affluence_adjusted) | $290.5m | households x CEX 290410 per-CU spend, affluence_adjusted factor |
| Custom search share | 0.57% | Google Trends, mean anchor-scaled interest of 'custom dining table' vs 'dining table', California, 5 years |
| Bay Area custom/solid-wood pool (low price multiple 3.0x) | $2.4m | base pool x custom search share x price multiple |
| Bay Area custom/solid-wood pool (base price multiple 5.0x) | $3.9m | base pool x custom search share x price multiple |
| Bay Area custom/solid-wood pool (high price multiple 8.0x) | $6.3m | base pool x custom search share x price multiple |

**Sanity check.** The CEX build puts US kitchen-and-dining spend at 4.0% of all NAICS 442 retail sales ($132.7bn). A single-digit percentage is the expected shape, since 442 covers every room in the house plus home furnishings. If this ratio came out above ~10% the CEX build would be overstated.


### What it takes to reach $1m of revenue

| ASP | Orders / yr | Orders / wk | Share of the base custom market |
|---:|---:|---:|---:|
| $2,500 | 400 | 7.7 | 25.4% |
| $4,200 | 238 | 4.6 | 25.4% |
| $7,000 | 143 | 2.8 | 25.4% |

At the search-share sizing, a $1m business is a quarter of the entire addressable market — which is the strongest argument that the search-share sizing is wrong, and that the channel assumption behind it is wrong too.


### Acquisition cost floor

CPC basis: PLACEHOLDER — Keyword Planner not run. This is the one number in the model with no measurement behind it. ($2.50).

| Site conversion | Implied CAC | As % of a base-ASP table |
|---:|---:|---:|
| 0.5% | $500 | 11.9% |
| 1.5% | $167 | 4.0% |
| 3.0% | $83 | 2.0% |

## Tier 1 — purchase intent

Google Trends, California, five years. Every term is scaled against the same anchor (`dining table` = 1.00) so the batches are comparable.

| Keyword | Interest vs. `dining table` |
|---|---:|
| dining table | 1.000 |
| custom furniture | 0.048 |
| extendable dining table | 0.046 |
| farmhouse dining table | 0.018 |
| solid wood dining table | 0.017 |
| walnut dining table | 0.008 |
| custom dining table | 0.006 |
| custom wood desk | 0.002 |
| handmade dining table | 0.001 |
| live edge dining table | 0.001 |
| white oak dining table | 0.001 |
| reclaimed wood dining table | 0.000 |
| made to order furniture | 0.000 |

**Rising related queries.** Each belongs to the seed term it was returned for — a rising query under `extendable dining table` says nothing about the market beyond that term.

| Seed term | Rising query | Change |
|---|---|---:|
| `solid wood dining table` | scandinavian solid wood folding dining table | Breakout |
| `farmhouse dining table` | rustic farmhouse dining table set for 8 | Breakout |
| `extendable dining table` | 4 to 6 extendable dining table set | Breakout |
| `dining table` | castlery dining table | +1,350% |
| `dining table` | transformer table | +850% |
| `farmhouse dining table` | rustic farmhouse dining table set for 6 | +750% |
| `solid wood dining table` | solid wood dining table for 6 | +450% |
| `extendable dining table` | transformer table | +350% |
| `extendable dining table` | seb extendable dining table | +350% |
| `dining table` | small dining table set for 4 | +300% |
| `dining table` | dining table set for 4 | +300% |
| `dining table` | oval dining table for 6 | +300% |
| `farmhouse dining table` | solid wood dining table | +300% |
| `dining table` | dining table set for 6 | +250% |
| `dining table` | arhaus | +250% |
| `custom furniture` | custom furniture dubai | +250% |

Two things rise: seating capacity and extendability ("for 6", "set for 8", folding), and DTC brands — Castlery, Article, Arhaus. But `solid wood dining table` and `white oak dining table` are themselves rising ~120% off the generic term, so solid wood is a growing modifier inside a category people search generically. That is a different and better position than owning the word "custom".


**Where the interest is** (unanchored, 100 = peak California metro):

| Metro | Index |
|---|---:|
| Yuma AZ-El Centro CA | 21 |
| San Diego CA | 14 |
| San Francisco-Oakland-San Jose CA | 13 |
| Sacramento-Stockton-Modesto CA | 13 |
| Monterey-Salinas CA | 13 |
| Bakersfield CA | 13 |
| Medford-Klamath Falls OR | 12 |
| Los Angeles CA | 11 |

### Which furniture people want customised

Anchored on `custom furniture` = 1.000. The raw index is discounted by the share of each category's related search volume that carries an accessory modifier — `custom desk` is largely desk *mats*, `custom bar` is largely bar *signs*. The last column counts related queries containing near me / cost / price / companies / installation, i.e. someone shopping rather than browsing.

| Category | Raw | Genuinely furniture | Adjusted | Buying-intent queries |
|---|---:|---:|---:|---:|
| custom cabinets | 1.064 | 100% | 1.064 | 4 |
| custom closet | 0.548 | 100% | 0.548 | 4 |
| custom bar | 1.262 | 37% | 0.462 | 0 |
| custom desk | 0.670 | 43% | 0.287 | 0 |
| custom sofa | 0.511 | 35% | 0.180 | 0 |
| custom vanity | 0.248 | 69% | 0.172 | 0 |
| custom coffee table | 0.141 | 100% | 0.141 | 0 |
| custom dining table | 0.141 | 100% | 0.141 | 0 |
| custom bed frame | 0.109 | 100% | 0.109 | 0 |
| custom bench | 0.216 | 30% | 0.064 | 0 |
| custom headboard | 0.045 | 100% | 0.045 | 0 |
| custom wardrobe | 0.042 | 100% | 0.042 | 0 |
| custom shelving | 0.037 | 100% | 0.037 | 0 |
| custom kitchen island | 0.019 | 100% | 0.019 | 0 |
| custom outdoor furniture | 0.042 | 0% | 0.000 | 0 |
| custom bookshelf | 0.061 | too few | — | 0 |
| custom nightstand | 0.041 | too few | — | 0 |
| custom built ins | 0.004 | too few | — | 0 |
| custom mantel | 0.003 | too few | — | 0 |
| custom conference table | 0.001 | too few | — | 0 |

Only `custom cabinets` and `custom closet` carry both scale and buying intent, and neither is freestanding furniture. Custom cabinets alone outrank the whole `custom furniture` category; custom dining tables run at 13% of it with no buying-intent queries attached at all.


### Not yet collected

| Source | Blocked on |
|---|---|
| google-ads / keyword-metrics | missing: GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET, GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID |
| semrush / competitor-organic-keywords | SEMRUSH_API_KEY not set |
| etsy / listings-and-shop-sales | ETSY_API_KEY not set |
| census-acs / bay-area-households | CENSUS_API_KEY not set |
| census-econ / industry-shipments | CENSUS_API_KEY not set |

See `docs/CREDENTIALS.md`. Keyword Planner is the one that matters most: it replaces the placeholder CPC, which is currently the only unmeasured number in the model.


## Tier 2 — government data

### Furniture retail sales, NAICS 442 (Census MRTS)

| Year | Sales | YoY |
|---:|---:|---:|
| 2019 | $118.0bn | +1.3% |
| 2020 | $111.1bn | -5.9% |
| 2021 | $138.1bn | +24.2% |
| 2022 | $140.5bn | +1.8% |
| 2023 | $135.6bn | -3.5% |
| 2024 | $132.7bn | -2.1% |
| 2025 | $135.6bn | +2.2% |
| 2026 (first 6 months) | $65.1bn | -2.0% <br>_vs. same months of 2025_ |

### Household spend by income quintile, 2024 (BLS CEX)

Average annual expenditure per consumer unit.

| Quintile | Kitchen & dining furniture | All furniture |
|---|---:|---:|
| Q1 lowest 20% | $15 | $275 |
| Q2 | $9 | $371 |
| Q3 | $22 | $462 |
| Q4 | $57 | $795 |
| Q5 highest 20% | $92 | $1,334 |
| All consumer units | $39 | $648 |

Even the top quintile spends under $100 a year on dining furniture. A $4,200 table is therefore not an annual purchase out of a furniture budget — it is a multi-decade purchase, which is what the acquisition maths has to survive.


### Who already makes this (Census CBP 2022)

| NAICS | Industry | US | California | Bay Area |
|---|---|---:|---:|---:|
| 337122 | Nonupholstered wood household furniture | 2,126 | 193 | 38 |
| 337211 | Wood office furniture | 307 | 39 | 9 |
| 337212 | Custom architectural woodwork and millwork | 2,352 | 178 | 30 |
| 321918 | Other millwork (incl. flooring) | 1,516 | 81 | 3 |
| 238350 | Finish carpentry contractors | 32,169 | 2,782 | 581 |
| 442110 | Furniture stores (retail) | 22,286 | 2,201 | 494 |

### Import exposure (UN Comtrade, US imports)

| Year | US wood-furniture imports |
|---:|---:|
| 2019 | $20.67bn |
| 2020 | $21.24bn |
| 2021 | $27.85bn |
| 2022 | $31.77bn |
| 2023 | $23.63bn |
| 2024 | $25.40bn |
| 2025 | $23.67bn |

Top origins for HS 940360 (other wooden furniture — the line that contains dining tables), 2025:

| Country | Value |
|---|---:|
| Viet Nam | $2.64bn |
| China | $0.84bn |
| Mexico | $0.40bn |
| Indonesia | $0.35bn |
| Canada | $0.34bn |
| Malaysia | $0.31bn |

### Bay Area household formation (Census Building Permits)

| Year | Permitted units |
|---:|---:|
| 2021 | 17,896 |
| 2022 | 22,609 |
| 2023 | 18,026 |
| 2024 | 12,829 |
| 2025 | 17,057 |
| 2026 (YTD) | 10,435 |

## Provenance

| Source | Dataset | Rows | Status | Fetched |
|---|---|---:|---|---|
| analysis | custom-category-adjustment | 21 | ok | 2026-08-27T20:33 |
| bls-cex | furniture-expenditure | 550 | ok | 2026-08-27T20:13 |
| bls-prices | prices-and-employment | 803 | ok | 2026-08-27T20:13 |
| census-acs | bay-area-households | 0 | blocked_no_credential | 2026-08-27T20:17 |
| census-bps | bay-area-permits | 92 | ok | 2026-08-27T20:13 |
| census-cbp | establishments-by-naics | 359 | ok | 2026-08-27T20:13 |
| census-econ | industry-shipments | 0 | blocked_no_credential | 2026-08-27T20:17 |
| census-mrts | monthly-retail-442 | 2,070 | ok | 2026-08-27T20:13 |
| census-popest | county-population-migration | 60 | ok | 2026-08-27T20:13 |
| etsy | listings-and-shop-sales | 0 | blocked_no_credential | 2026-08-27T20:13 |
| google-ads | keyword-metrics | 0 | blocked_no_credential | 2026-08-27T20:13 |
| google-trends | custom-furniture-categories | 111 | ok | 2026-08-27T20:32 |
| google-trends | purchase-intent-terms | 4,470 | ok | 2026-08-27T20:34 |
| semrush | competitor-organic-keywords | 0 | blocked_no_credential | 2026-08-27T20:13 |
| un-comtrade | us-wood-furniture-imports | 4,663 | ok | 2026-08-27T20:17 |
