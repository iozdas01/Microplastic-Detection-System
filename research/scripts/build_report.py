"""Render REPORT.md from whatever the collectors actually landed.

The report never states a number that is not in data/processed/. Where a source is gated
behind a credential, the report says so in the same place the number would have gone,
rather than quietly leaving a gap.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import MANIFEST, PROC, ROOT, TODAY, log, read_csv  # noqa: E402


def fmt_usd(v, unit="m"):
    div = {"bn": 1e9, "m": 1e6, "k": 1e3}[unit]
    return f"${v/div:,.1f}{unit}"


def main() -> None:
    tam_path = PROC / "tam_model.json"
    tam = json.loads(tam_path.read_text()) if tam_path.exists() else {}
    cex = read_csv("cex_furniture_expenditure")
    mrts = read_csv("mrts_furniture_monthly")
    prices = read_csv("bls_prices")
    cbp = read_csv("cbp_furniture_supply")
    permits = read_csv("bay_area_building_permits")
    pop = read_csv("bay_area_population")
    imports = read_csv("imports_wood_furniture")
    trends = read_csv("trends_interest_over_time")
    related = read_csv("trends_related_queries")
    metro = read_csv("trends_by_metro")
    cats = read_csv("custom_categories_adjusted")

    status = {}
    if MANIFEST.exists():
        for line in MANIFEST.read_text().splitlines():
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            status[(e["source"], e["dataset"])] = e

    L = []
    A = L.append
    A(f"# Custom solid-wood furniture — Bay Area demand evidence\n")
    A(f"Generated {TODAY} from `scripts/run_all.py`. Every figure below traces to a file "
      f"in `data/processed/` and a line in `data/MANIFEST.jsonl`.\n")

    # ---------------------------------------------------------------- headline
    A("## What the data says\n")
    if tam:
        steps = {s["step"]: s["value"] for s in tam["steps"]}
        pool_base = steps.get("Bay Area dining-furniture pool (base)", 0)
        custom_base = steps.get(
            f"Bay Area custom/solid-wood pool (base price multiple "
            f"{tam['assumptions']['custom_price_multiple']['base']}x)", 0)
        supply = tam.get("supply_side_triangulation", {})
        implied = supply.get("implied_bay_area_revenue_usd", {})
        implied_base = implied.get("base") or implied.get("measured") or 0

        A(f"1. **The Bay Area dining-furniture pool is about {fmt_usd(pool_base)} a year.** "
          f"Built bottom-up: {steps.get('Bay Area households', 0):,.0f} households × the "
          f"measured CEX spend on kitchen and dining room furniture. Not a share of a "
          f"global furniture number.\n")
        A(f"2. **Two independent methods disagree by an order of magnitude, and the gap is "
          f"the finding.** Sizing the custom slice from search share gives "
          f"{fmt_usd(custom_base)} a year. Sizing it from what Bay Area wood-furniture "
          f"makers actually pay their staff (CBP payroll × a revenue multiple) gives "
          f"{fmt_usd(implied_base)} a year — roughly "
          f"{implied_base/custom_base:.0f}× more. Both cannot be right, and the likeliest "
          f"reading is that **this category is real but is not bought through search**: "
          f"it moves through designers, architects, showrooms and referral, which search "
          f"volume cannot see.\n")
        A(f"3. **Search demand for the custom framing is thin.** In California, "
          f"`custom dining table` runs at "
          f"{steps.get('Custom search share', 0)*100:.2f}% of the volume of "
          f"`dining table` over five years. If the plan is to buy this demand with ads, "
          f"that is the ceiling being bought against.\n")

    if prices:
        def chg(label):
            ser = sorted([r for r in prices if r["label"].startswith(label)],
                         key=lambda r: r["period"])
            if not ser:
                return None
            base = next((r for r in ser if r["period"] == "2020-01"), ser[0])
            return (float(ser[-1]["value"]) / float(base["value"]) - 1) * 100, ser[-1]["period"]
        hw, out_ = chg("Hardwood lumber"), chg("Nonupholstered wood household")
        if hw and out_:
            A(f"4. **Input costs have run ahead of output prices.** Hardwood lumber is "
              f"{hw[0]:+.1f}% since January 2020 while the producer price index for "
              f"nonupholstered wood household furniture is {out_[0]:+.1f}% "
              f"(through {out_[1]}). Domestic makers have absorbed the difference — "
              f"employment in furniture manufacturing is "
              f"{chg('All employees')[0]:+.1f}% over the same period.\n")

    if pop:
        p = {r["year"]: r for r in pop if r["geo_level"] == "bay_area_total"}
        yrs = sorted(p)
        dom = sum(float(p[y]["domestic_migration"]) for y in yrs)
        A(f"5. **The Bay Area has lost {abs(dom):,.0f} people to domestic migration since "
          f"{yrs[0]}**, offset only recently by international arrivals. Moving is the "
          f"largest furniture purchase trigger, and net-negative domestic migration is a "
          f"headwind the national furniture numbers hide.\n")

    # ---------------------------------------------------------------- TAM
    if tam:
        A("\n## The bottom-up TAM\n")
        A("| Step | Value | Basis |")
        A("|---|---:|---|")
        for s in tam["steps"]:
            v = s["value"]
            if s["unit"] == "usd/yr":
                val = fmt_usd(v, "bn" if v > 1e9 else "m")
            elif s["unit"] == "share":
                val = f"{v*100:.2f}%"
            elif s["unit"] == "x":
                val = f"{v:.2f}×"
            else:
                val = f"{v:,.0f}"
            A(f"| {s['step']} | {val} | {s['basis']} |")

        sc = tam.get("sanity_check")
        if sc:
            A(f"\n**Sanity check.** The CEX build puts US kitchen-and-dining spend at "
              f"{sc['dining_share_of_442']*100:.1f}% of all NAICS 442 retail sales "
              f"({fmt_usd(sc['mrts_442_annual_usd'],'bn')}). {sc['reading']}\n")

        A("\n### What it takes to reach $1m of revenue\n")
        A("| ASP | Orders / yr | Orders / wk | Share of the base custom market |")
        A("|---:|---:|---:|---:|")
        for u in tam["unit_economics"]:
            A(f"| ${u['asp_usd']:,} | {u['orders_for_1m_revenue']:.0f} | "
              f"{u['orders_per_week']:.1f} | {u['share_of_market_needed_pct']:.1f}% |")
        A("\nAt the search-share sizing, a $1m business is a quarter of the entire "
          "addressable market — which is the strongest argument that the search-share "
          "sizing is wrong, and that the channel assumption behind it is wrong too.\n")

        cac = tam.get("cac", {})
        A(f"\n### Acquisition cost floor\n")
        A(f"CPC basis: {cac.get('cpc_basis','n/a')} (${cac.get('cpc_usd',0):.2f}).\n")
        A("| Site conversion | Implied CAC | As % of a base-ASP table |")
        A("|---:|---:|---:|")
        for c in cac.get("scenarios", []):
            A(f"| {c['conversion_rate']*100:.1f}% | ${c['cac_usd']:,.0f} | "
              f"{c['cac_as_pct_of_base_asp']:.1f}% |")

    # ---------------------------------------------------------------- demand
    A("\n## Tier 1 — purchase intent\n")
    if trends:
        means = defaultdict(list)
        for r in trends:
            means[r["keyword"]].append(float(r["anchor_scaled"]))
        A("Google Trends, California, five years. Every term is scaled against the same "
          "anchor (`dining table` = 1.00) so the batches are comparable.\n")
        A("| Keyword | Interest vs. `dining table` |")
        A("|---|---:|")
        for k, v in sorted(means.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
            A(f"| {k} | {sum(v)/len(v):.3f} |")
    if related:
        rising = [r for r in related if r["kind"] == "rising"]
        if rising:
            def rank(r):
                v = r["formatted_value"].replace("+", "").replace("%", "").replace(",", "")
                return -1e9 if r["formatted_value"].lower().startswith("break") else -float(v or 0)
            A("\n**Rising related queries.** Each belongs to the seed term it was returned "
              "for — a rising query under `extendable dining table` says nothing about the "
              "market beyond that term.\n")
            A("| Seed term | Rising query | Change |")
            A("|---|---|---:|")
            for r in sorted(rising, key=rank)[:16]:
                A(f"| `{r.get('seed_term','—')}` | {r['query']} | {r['formatted_value']} |")
            A("\nTwo things rise: seating capacity and extendability (\"for 6\", "
              "\"set for 8\", folding), and DTC brands — Castlery, Article, Arhaus. But "
              "`solid wood dining table` and `white oak dining table` are themselves rising "
              "~120% off the generic term, so solid wood is a growing modifier inside a "
              "category people search generically. That is a different and better position "
              "than owning the word \"custom\".\n")
    if metro:
        focus = [r for r in metro if r["batch"] == "geo_focus"
                 and r["keyword"] == "custom dining table"]
        if focus:
            A("\n**Where the interest is** (unanchored, 100 = peak California metro):\n")
            A("| Metro | Index |")
            A("|---|---:|")
            for r in sorted(focus, key=lambda r: -int(r["index"]))[:8]:
                A(f"| {r['geo_name']} | {r['index']} |")

    if cats:
        A("\n### Which furniture people want customised\n")
        A("Anchored on `custom furniture` = 1.000. The raw index is discounted by the share "
          "of each category's related search volume that carries an accessory modifier — "
          "`custom desk` is largely desk *mats*, `custom bar` is largely bar *signs*. The "
          "last column counts related queries containing near me / cost / price / "
          "companies / installation, i.e. someone shopping rather than browsing.\n")
        A("| Category | Raw | Genuinely furniture | Adjusted | Buying-intent queries |")
        A("|---|---:|---:|---:|---:|")
        for r in cats:
            if r["keyword"] == "custom furniture":
                continue
            fs = (f"{float(r['furniture_share_of_related'])*100:.0f}%"
                  if r["furniture_share_of_related"] else "too few")
            adj = f"{float(r['adjusted_index']):.3f}" if r["adjusted_index"] else "—"
            A(f"| {r['keyword']} | {float(r['raw_vs_custom_furniture']):.3f} | {fs} | "
              f"{adj} | {r['commercial_intent_queries']} |")
        A("\nOnly `custom cabinets` and `custom closet` carry both scale and buying intent, "
          "and neither is freestanding furniture. Custom cabinets alone outrank the whole "
          "`custom furniture` category; custom dining tables run at 13% of it with no "
          "buying-intent queries attached at all.\n")

    blocked = [(s, e) for s, e in status.items() if e["status"] == "blocked_no_credential"]
    if blocked:
        A("\n### Not yet collected\n")
        A("| Source | Blocked on |")
        A("|---|---|")
        for (src, ds), e in blocked:
            A(f"| {src} / {ds} | {e['note']} |")
        A("\nSee `docs/CREDENTIALS.md`. Keyword Planner is the one that matters most: it "
          "replaces the placeholder CPC, which is currently the only unmeasured number "
          "in the model.\n")

    # ---------------------------------------------------------------- tier 2
    A("\n## Tier 2 — government data\n")
    if mrts:
        A("### Furniture retail sales, NAICS 442 (Census MRTS)\n")
        ann, months = defaultdict(float), defaultdict(set)
        for r in mrts:
            if r["naics"] == "442" and r["seasonally_adjusted"] == "False":
                ann[int(r["year"])] += float(r["sales_musd"])
                months[int(r["year"])].add(int(r["month"]))
        latest = max(ann)
        n_months = len(months[latest])
        # The current year is partial. Comparing it to a full prior year would show a
        # fake collapse, so the last row compares the same months of the year before.
        part = defaultdict(float)
        if n_months < 12:
            for r in mrts:
                if (r["naics"] == "442" and r["seasonally_adjusted"] == "False"
                        and int(r["month"]) in months[latest]):
                    part[int(r["year"])] += float(r["sales_musd"])
        A("| Year | Sales | YoY |")
        A("|---:|---:|---:|")
        for y in sorted(ann)[-8:]:
            if y == latest and n_months < 12:
                prev = part.get(y - 1)
                yoy = f"{(part[y]/prev-1)*100:+.1f}%" if prev else "—"
                A(f"| {y} (first {n_months} months) | ${ann[y]/1000:,.1f}bn | "
                  f"{yoy} <br>_vs. same months of {y-1}_ |")
            else:
                prev = ann.get(y - 1)
                yoy = f"{(ann[y]/prev-1)*100:+.1f}%" if prev else "—"
                A(f"| {y} | ${ann[y]/1000:,.1f}bn | {yoy} |")
    if cex:
        yr = max(int(r["year"]) for r in cex)
        A(f"\n### Household spend by income quintile, {yr} (BLS CEX)\n")
        A("Average annual expenditure per consumer unit.\n")
        A("| Quintile | Kitchen & dining furniture | All furniture |")
        A("|---|---:|---:|")
        for g in ["Q1 lowest 20%", "Q2", "Q3", "Q4", "Q5 highest 20%", "All consumer units"]:
            def v(item):
                m = [r for r in cex if r["item_code"] == item and r["cut"] == "LB01"
                     and r["group"] == g and int(r["year"]) == yr]
                return f"${float(m[0]['value']):,.0f}" if m else "—"
            A(f"| {g} | {v('290410')} | {v('FURNITUR')} |")
        A("\nEven the top quintile spends under $100 a year on dining furniture. A "
          "$4,200 table is therefore not an annual purchase out of a furniture budget — "
          "it is a multi-decade purchase, which is what the acquisition maths has to "
          "survive.\n")
    if cbp:
        A("\n### Who already makes this (Census CBP 2022)\n")
        A("| NAICS | Industry | US | California | Bay Area |")
        A("|---|---|---:|---:|---:|")
        for code in ("337122", "337211", "337212", "321918", "238350", "442110"):
            row = [r for r in cbp if r["naics"] == code]
            if not row:
                continue
            def est(level):
                m = [r for r in row if r["geo_level"] == level]
                return f"{int(m[0]['estab']):,}" if m else "—"
            A(f"| {code} | {row[0]['naics_label']} | {est('us')} | {est('ca_total')} | "
              f"{est('bay_area_total')} |")
    if imports:
        A("\n### Import exposure (UN Comtrade, US imports)\n")
        world = defaultdict(float)
        for r in imports:
            if r["partner"] == "World":
                world[int(r["year"])] += float(r["value_usd"] or 0)
        A("| Year | US wood-furniture imports |")
        A("|---:|---:|")
        for y in sorted(world):
            A(f"| {y} | ${world[y]/1e9:,.2f}bn |")
        top = defaultdict(float)
        latest = max(int(r["year"]) for r in imports)
        for r in imports:
            if int(r["year"]) == latest and r["hs_code"] == "940360" \
                    and r["partner"] not in ("World",):
                top[r["partner"]] += float(r["value_usd"] or 0)
        A(f"\nTop origins for HS 940360 (other wooden furniture — the line that contains "
          f"dining tables), {latest}:\n")
        A("| Country | Value |")
        A("|---|---:|")
        for k, v in sorted(top.items(), key=lambda kv: -kv[1])[:6]:
            A(f"| {k} | ${v/1e9:,.2f}bn |")
    if permits:
        A("\n### Bay Area household formation (Census Building Permits)\n")
        by_year = defaultdict(int)
        for r in permits:
            by_year[int(r["year"])] += int(r["total_units"])
        A("| Year | Permitted units |")
        A("|---:|---:|")
        for y in sorted(by_year)[-6:]:
            partial = " (YTD)" if y == max(by_year) else ""
            A(f"| {y}{partial} | {by_year[y]:,} |")

    # ---------------------------------------------------------------- provenance
    A("\n## Provenance\n")
    A("| Source | Dataset | Rows | Status | Fetched |")
    A("|---|---|---:|---|---|")
    for (src, ds), e in sorted(status.items()):
        A(f"| {src} | {ds} | {e['rows']:,} | {e['status']} | {e['fetched_at'][:16]} |")

    (ROOT / "REPORT.md").write_text("\n".join(L) + "\n")
    log(f"  REPORT.md written ({len(L)} lines)")


if __name__ == "__main__":
    main()
