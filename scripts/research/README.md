# Market-evidence collectors

The pipeline that produced this repo's active idea. Built to the tiered source plan:
purchase intent first, then government data, then industry sources.

**The code lives here; everything it writes lands in
`reports/high-mix-manufacturing/research/`** — outputs are per-idea state and belong with
that idea's other artifacts. Paths are anchored once, in `common.py`.

It answers four questions with measurements rather than syndicated market numbers:

- **TAM** — how big is US household furniture spend, built bottom-up from CEX?
- **Which article** — of the nine CEX furniture lines, which one should this factory
  build first? Sized on demand, scored on whether a panel cell can actually make it.
- **SAM** — how much of that article is configurable-willing and reachable online?
- **SOM** — the smaller of what one cell can produce and what the market will buy,
  priced across a tier ladder with an in-home assembly attach.
- **The factory** — what it costs to build and run: bill of materials, station cycle
  times, a named equipment schedule, capital plan and unit-cost curve.

The Bay Area / dining-table version this started as is kept in
`reports/high-mix-manufacturing/research/archive/bay-area-dining-2026-08-27.md`; its model
and report generator (`build_tam.py`, `build_report.py`) still run if you want the local view.

## Run it

Run `scripts/setup.sh` once for the whole repo, then:

```bash
.venv/bin/python scripts/research/run_all.py
```

No credentials are required — the pipeline runs end to end on free, keyless sources and
tells you in the output which sources are gated. See `CREDENTIALS.md` beside this file for
what each key would add and how to get it. Keys are read from `.env` at the repo root.

```bash
.venv/bin/python scripts/research/run_all.py --tier2   # government sources only
.venv/bin/python scripts/research/build_factory.py     # capacity and cost from cycle times
.venv/bin/python scripts/research/build_tam_us.py      # re-run the market model
.venv/bin/python scripts/research/build_report_us.py   # re-render REPORT.md from the model
```

## Output

Everything below is relative to `reports/high-mix-manufacturing/research/`.

| Path | What |
|---|---|
| `REPORT.md` | The findings, regenerated from whatever the collectors landed |
| `../pages/window-covering-market.html` | The H3 market on one page — Census layers, calls, entry options |
| `../pages/window-covering-players.html` | Seven layers, seven numbers, seven calls |
| `../pages/market-ladder.html` | The market as a ladder of business sizes, with remake cost per rung |
| `../pages/startup-map.html` | The startup scene, arranged by risk taken on the outcome |
| `../pages/outreach-send-sheet.html` | The researcher email campaign as a working surface |
| `data/reference/equipment.csv` | The machine schedule — the one input that is typed, not fetched |
| `data/processed/us_article_scorecard.csv` | Every furniture article, sized and scored |
| `data/processed/*.csv` | Tidy tables, one per dataset |
| `data/processed/tam_us_model.json` | The full US model, every step with its basis |
| `data/raw/**` | Verbatim API payloads, never edited |
| `data/MANIFEST.jsonl` | One line per fetch: url, time, row count, status |

Nothing downstream quotes a number that has no manifest line.

## Collectors

**Tier 1 — purchase intent**

| Script | Source | Runs without a key |
|---|---|---|
| `t1_google_trends.py` | Google Trends | yes |
| `t1_google_ads_keywords.py` | Keyword Planner (volume + CPC) | no |
| `t1_etsy_supply.py` | Etsy Open API v3 | no |
| `t1_semrush.py` | Semrush domain organic | no |

**Tier 2 — government data**

| Script | Source | Runs without a key |
|---|---|---|
| `t2_census_mrts.py` | Monthly retail sales, NAICS 442 | yes |
| `t2_bls_cex.py` | Consumer Expenditure Survey | yes |
| `t2_bls_prices.py` | CPI / PPI / furniture employment | yes |
| `t2_cbp_supply.py` | County Business Patterns | yes |
| `t2_permits.py` | Building Permits Survey | yes |
| `t2_popest.py` | Population estimates + migration | yes |
| `t2_metro_coverage.py` | CBSA populations → in-home service reach | yes |
| `t2_trade_imports.py` | US wood-furniture imports by HS code | yes |
| `t2_census_acs.py` | ACS households, income, movers | no |
| `t2_census_econ.py` | Economic Census receipts | no |

## Design notes

**Google Trends is anchored.** Trends returns numbers relative to the peak of whatever
set you ask for, so five terms queried separately are five incomparable series. Every
batch carries the same anchor term (`dining table`) and is rescaled by it, which makes
every keyword comparable to every other. A second unanchored pass exists purely to
resolve the state geography, which the anchor otherwise flattens to 1.

**Which article to build is an output, not an input.** All nine CEX furniture lines are
collected and scored on pool size, custom-search share, machinability and
flat-packability. Articles this factory cannot physically make are scored anyway and then
excluded by a separate `buildable` filter, so the report can show what was given up.

**Custom share is a median, not a mean.** A CEX line covers several articles, and a weak
generic denominator (`closet organizer` is not how people search for a closet) inflates
its pair enough to move a mean on its own. The per-pair detail stays in the report.

**The premium tier is priced off measured data.** The premium multiple is not picked —
it is the article's CEX Q5 spend skew, i.e. how much more the top income quintile already
spends on that article than the average household. Tier mix, margins and attach rates
around it are assumptions.

**Service reach is measured, not assumed.** An in-home assembly crew covers a metro, so
`t2_metro_coverage.py` builds the cumulative CBSA population curve and the model
multiplies any in-metro attach rate by the real coverage share of the serviced metros.

**Supply is modelled before demand, on purpose.** `build_factory.py` derives capacity
from per-station cycle times and cost from a bill of materials; `build_tam_us.py` then
consumes both. The dependency runs one way, so the two halves cannot silently disagree —
and where they do disagree, the report says so instead of picking the flattering number.

**Capacity is derived, never assumed.** Nameplate output falls out of the slowest station,
not out of a guessed machine-hour. That is what turned the earlier "throughput binds"
conclusion into "demand binds".

**The search share is a floor, not an estimate.** Trends measures who wants custom at
today's premium. An autonomous factory sells configurable near stock price, which is a
different offer to a different buyer — so the measured share anchors the bottom of a
band, and the multiple above it is an assumption the report labels as one. That single
number moves the SAM 30×, which makes measuring it the first thing worth doing.

**Assumptions are in one place.** `ASSUMPTIONS` at the top of `build_tam_us.py`.
Nothing is hardcoded below it, and every assumption is printed alongside the results and
marked **(assumption)** in the report line that uses it.

**The USITC substitute.** DataWeb needs an account token. UN Comtrade's public preview
endpoint carries the same US import statistics with no credential, so `t2_trade_imports.py`
uses that instead — same HS lines, same numbers.
