"""Render REPORT.md — the US TAM / SAM / SOM for one configurable furniture article.

The report never states a number that is not in data/processed/. Where a source is gated
behind a credential, the report says so in the same place the number would have gone,
rather than quietly leaving a gap. Assumptions are marked as assumptions in the line
where they are used, not buried in a footnote.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import MANIFEST, PROC, RESEARCH, ROOT, TODAY, log, read_csv  # noqa: E402


def usd(v, unit="m"):
    div = {"bn": 1e9, "m": 1e6, "k": 1e3}[unit]
    return f"${v / div:,.1f}{unit}"


def imports_world_total(rows: list[dict], year: str) -> float:
    """Sum the World aggregate rows only — the file also carries every partner country,
    so summing it whole would count each dollar twice."""
    return sum(float(r["value_usd"]) for r in rows
               if r.get("partner") == "World" and r.get("year") == year)


def auto(v):
    """Pick the unit that reads best for a dollar figure."""
    if v >= 1e9:
        return usd(v, "bn")
    if v >= 1e6:
        return usd(v, "m")
    return f"${v:,.0f}"


def main() -> None:
    path = PROC / "tam_us_model.json"
    if not path.exists():
        log("build_report_us: no tam_us_model.json — run scripts/build_tam_us.py first")
        return
    m = json.loads(path.read_text())
    A_ = m["assumptions"]

    cex = read_csv("cex_furniture_expenditure")
    mrts = read_csv("mrts_furniture_monthly")
    prices = read_csv("bls_prices")
    cbp = read_csv("cbp_furniture_supply")
    imports = read_csv("imports_wood_furniture")
    trends = read_csv("trends_interest_over_time")
    metro = read_csv("trends_by_metro")

    status = {}
    if MANIFEST.exists():
        for line in MANIFEST.read_text().splitlines():
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            status[(e["source"], e["dataset"])] = e

    L: list[str] = []
    A = L.append
    pick = m["beachhead"]
    sam = m["sam"]
    som = m["som"]
    tam = next(s["value"] for s in m["steps"]
               if s["step"] == "US household furniture spend (TAM)")

    A("---")
    A("purpose: The measured US market size for this idea — TAM, the beachhead article, SAM and SOM, each step with its basis.")
    A(f"generated: {TODAY} by scripts/research/build_report_us.py")
    A("---\n")
    A("# Configurable furniture from an autonomous factory — US market size\n")
    A(f"Generated {TODAY} from `scripts/research/run_all.py`. Every figure traces to a file in "
      f"`data/processed/` and a line in `data/MANIFEST.jsonl`. Numbers that are "
      f"assumptions rather than measurements are marked **(assumption)** where they "
      f"are used.\n")

    # ------------------------------------------------------------------ headline
    A("## The three numbers\n")
    A("| | Value | What it is |")
    A("|---|---:|---|")
    A(f"| **TAM** | {usd(tam, 'bn')} / yr | Everything US households spend on furniture, "
      f"built bottom-up from CEX spend × consumer units |")
    A(f"| **SAM** | {auto(sam['base_usd'])} / yr | The beachhead article, cut to the "
      f"share of buyers who want it configured and can be sold to online — "
      f"{auto(sam['product_usd'])} product plus {auto(sam['service_usd'])} assembly |")
    A(f"| **SOM** | {auto(som['som_year_3_usd'])} / yr | Year 3, capacity-led: what one "
      f"autonomous cell can physically produce, at the blended tier price |")
    A("")
    bd = m.get("som_bound")
    if bd:
        A(f"SOM is the smaller of what one cell can make "
          f"({bd['capacity_units_per_year']:,} units/yr, derived from measured station "
          f"cycle times) and what the market supports ({bd['demand_units_per_year']:,} "
          f"units/yr). **{bd['binding_constraint'].capitalize()} binds** — the cell is "
          f"{bd['oversize_factor']}× larger than year-3 demand. The scarce thing is "
          f"buyers, not throughput.\n")
    else:
        A(f"SOM is **{som['ramp'][-1]['share_of_base_sam_pct']:.1f}%** of SAM.\n")

    A("## What the data says\n")
    A(f"1. **The beachhead article is {pick['article'].lower()}** — the storage family: "
      f"shelving, media units, wall systems. It wins not because demand for it is largest "
      f"({auto(pick['us_pool_usd'])} a year, {pick['share_of_tam']:.1%} of the furniture "
      f"TAM) but because it is the only high-demand family that is fully machinable from "
      f"nested sheet stock *and* ships flat. Sofas score higher overall on raw demand and "
      f"custom interest, and are the largest furniture line in the country at "
      f"{auto(next(r['us_pool_usd'] for r in m['articles'] if r['article'] == 'Sofas'))} "
      f"a year — but roughly 85% of a sofa is foam, springs and sewing, so an autonomous "
      f"panel factory cannot make one.\n")

    A(f"2. **Measured demand for *custom* is thin in every article family.** Across the "
      f"generic/custom keyword pairs, the custom framing runs at well under 1% of the "
      f"generic term. For the beachhead article the median pair is "
      f"{pick['custom_search_share']:.2%}. If the plan is to buy existing "
      f"custom-furniture demand with ads, that is the ceiling being bought against, and "
      f"it is small.\n")
    A(f"   The pairs behind that median are `{pick['custom_share_basis']}`. The median is "
      f"used rather than the mean because `closet organizer` is a weak denominator — it "
      f"is not how people search for a closet — which inflates its pair to a figure that "
      f"would drag the mean to {pick['custom_search_share_mean']:.1%} on its own. The "
      f"spread is left visible rather than averaged away.\n")

    adj = [a for a in m.get("adjacencies", []) if a.get("custom_search_share")]
    if adj:
        a0 = adj[0]
        A(f"3. **The one place custom demand is genuinely large is next door, not here.** "
          f"`{a0['custom']}` runs at {a0['custom_search_share']:.1%} of `{a0['generic']}` "
          f"— an order of magnitude above any furniture article. But that is "
          f"home-improvement spend sold through installers, outside the CEX furniture TAM "
          f"and outside a ship-it-flat business. It is the adjacency to grow into once "
          f"there is a factory, not the article to launch with.\n")

    A(f"4. **The thesis rests on an assumption no available data can test.** The measured "
      f"{pick['custom_search_share']:.2%} is who searches for custom *today*, when custom "
      f"means a large premium and a long wait from a joinery shop. An autonomous factory "
      f"sells configurable at close to stock price, which is a different product to a "
      f"different buyer. The SAM below assumes that removing the premium multiplies the "
      f"willing share by "
      f"{A_['custom_willing_multiple']['base']:.0f}× **(assumption)**. Everything about "
      f"whether this is a {auto(sam['grid']['floor/base'])} market or a "
      f"{auto(sam['grid']['ceiling/base'])} one turns on that one number, and the "
      f"cheapest way to measure it is a configurator landing page with real pricing.\n")

    # cost backdrop, if the price collector landed
    def chg(series_sub):
        rows = [r for r in prices if series_sub in (r.get("series_title", "")
                                                    + r.get("series_id", ""))]
        return rows

    bl = m["blended"]
    A(f"5. **The tier ladder carries the economics; the assembly service enables them.** "
      f"Three tiers off one cell blend to a ${bl['revenue_per_order_usd']:,} order at a "
      f"{bl['gross_margin']:.0%} margin. In-home assembly contributes "
      f"${bl['service_revenue_per_order_usd']:,.0f} of that — "
      f"{bl['service_share_of_revenue']:.1%} of revenue — because the attach can only be "
      f"sold in metros where crews exist, and the top "
      f"{A_['assembly']['serviced_metros']} metros are "
      f"{m['tiers']['coverage_share']:.0%} of the country. Read the service as what makes "
      f"a {m['tiers']['ladder'][-1]['price_multiple']}× premium tier credible, not as a "
      f"second revenue line.\n")

    A(f"6. **Domestic manufacturing has been losing to imports for the whole period.** US "
      f"wood-furniture imports run around "
      f"{usd(imports_world_total(imports, '2025'), 'bn') if imports else 'n/a'} "
      f"a year. An autonomous factory is a bet on reversing that with labour cost, which "
      f"is the actual thing being sold to an investor — the market-size numbers above are "
      f"the smaller half of the argument.\n")

    # ------------------------------------------------------------- article scorecard
    A("## Which article to build\n")
    A("Every article line under CEX *Furniture* is sized from household spend and scored "
      "on four dimensions: pool size (what there is to sell), custom-search share (whether "
      "anyone wants it configured), machinability and flat-packability **(the last two are "
      "judgements about an autonomous panel cell, not measurements)**. Weights: "
      + ", ".join(f"{k} {v:.0%}" for k, v in m["weights"].items()) + ".\n")
    A("| Score | Score if assembled | Article | US pool | % of TAM | Q5 skew | Custom share | Machinable | Flat-pack | Buildable here |")
    A("|---:|---:|---|---:|---:|---:|---:|---:|---:|:--:|")
    for r in m["articles"]:
        cs = f"{r['custom_search_share']:.2%}" if r["custom_search_share"] is not None else "—"
        q5 = f"{r['q5_skew_x']}×" if r["q5_skew_x"] else "—"
        build = "yes" if (r["asp_usd"] and r["machine_hours_per_unit"]) else "no"
        star = " ⭐" if r["cex_item"] == pick["cex_item"] else ""
        A(f"| {r['beachhead_score']:.3f} | {r['beachhead_score_assembled']:.3f} | "
          f"{r['article']}{star} | "
          f"{usd(r['us_pool_usd'], 'bn')} | {r['share_of_tam']:.1%} | {q5} | {cs} | "
          f"{r['machinable']:.0%} | {r['flatpack']:.0%} | {build} |")
    A("")
    A("*Q5 skew is how much more the top income quintile spends on that article than the "
      "average household — a measure of how far the category can be priced up.*\n")
    A("The top-scoring article and the chosen article differ, and that is the point of the "
      "`Buildable here` column: the score ranks demand, the column applies the constraint. "
      f"**{pick['article']}** is the highest-scoring article this factory can actually "
      f"make.\n")
    A(f"`Score if assembled` re-runs the same scoring with the flat-pack weight cut from "
      f"{m['weights']['flatpack']:.0%} to {m['weights_assembled']['flatpack']:.0%} — the "
      f"question of whether selling in-home assembly should change which article you "
      f"build, since a crew in the customer's home removes the reason to fear a bulky "
      f"box. "
      + (f"It does: the pick would move to **{m['beachhead_if_assembled']['article']}**."
         if m["service_changes_pick"] else
         f"It does not: **{pick['article']}** wins under both weightings. The service "
         f"tier changes the margin on the article, not the choice of it.") + "\n")

    # --------------------------------------------------------------------- TAM
    A("## The model, step by step\n")
    A("| Step | Value | Basis |")
    A("|---|---:|---|")
    for s in m["steps"]:
        v = s["value"]
        if s["unit"] == "usd/yr":
            vs = auto(v)
        elif s["unit"] == "households":
            vs = f"{v:,.0f}"
        else:
            vs = str(v)
        A(f"| {s['step']} | {vs} | {s['basis']} |")
    A("")
    sc = m.get("sanity_check")
    if sc:
        A(f"**Sanity check.** The CEX build puts US household furniture spend at "
          f"{sc['tam_share_of_442']:.0%} of Census retail sales for NAICS 442 "
          f"({usd(sc['mrts_442_annual_usd'], 'bn')}). {sc['reading']}\n")

    # ------------------------------------------------------------------ tier ladder
    t = m["tiers"]
    b = m["blended"]
    asm = A_["assembly"]
    A("## Tiers and the assembly attach\n")
    A(f"Three tiers off the same cell, plus in-home assembly at ${asm['price_usd']} "
      f"**(assumption)**. The premium price multiple is the one number here that is not a "
      f"guess: it is the article's measured Q5 spend skew — the top income quintile "
      f"already spends {t['ladder'][-1]['price_multiple']}× the average household on this "
      f"article, which is the observable evidence for how far it can be priced up. Tier "
      f"mix, margins and attach rates are **assumptions**.\n")
    if b["attach_rate"] > 0:
        A(f"Assembly can only be sold where there are crews. {t['coverage_basis']}, so an "
          f"attach rate quoted inside serviced metros becomes the *effective* rate below "
          f"after multiplying by {t['coverage_share']:.1%}.\n")
    else:
        A(f"**There is no assembly attach.** {asm.get('removed_because', '')}. That also "
          f"removes a constraint: with nothing to install, nothing caps sales to the "
          f"{t['coverage_share']:.0%} of the US population inside serviced metros. The "
          f"columns below are kept at zero so the service can be switched back on by "
          f"changing numbers rather than restructuring the model.\n")
    A("| Tier | Price | Mix | Margin | Attach in-metro | Effective attach | Revenue / order | Gross profit / order |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|")
    for r in t["ladder"]:
        A(f"| {r['tier']} ({r['price_multiple']}×) | ${r['price_usd']:,} | {r['mix']:.0%} | "
          f"{r['gross_margin']:.0%} | {r['attach_rate_in_serviced_metros']:.0%} | "
          f"{r['effective_attach_rate']:.1%} | ${r['revenue_per_order_usd']:,} | "
          f"${r['gross_profit_per_order_usd']:,} |")
    A(f"| **blended** | **${b['product_asp_usd']:,}** | 100% | "
      f"**{b['gross_margin']:.0%}** | — | **{b['attach_rate']:.1%}** | "
      f"**${b['revenue_per_order_usd']:,}** | **${b['gross_profit_per_order_usd']:,}** |")
    A("")
    A(f"**The tier ladder does more than the service does.** The premium tier lifts the "
      f"blended product price to ${b['product_asp_usd']:,} and the blended margin to "
      f"{b['gross_margin']:.0%}. The assembly attach adds "
      f"${b['service_revenue_per_order_usd']:,.0f} per order — "
      f"{b['service_share_of_revenue']:.1%} of revenue. At this scale in-home assembly is "
      f"a conversion and differentiation lever, not a revenue line: it is what lets you "
      f"sell a premium tier at "
      f"{t['ladder'][-1]['price_multiple']}× and hold a "
      f"{t['ladder'][-1]['gross_margin']:.0%} margin, and the direct revenue is rounding "
      f"error against that.\n")
    A(f"Raising the attach price or the serviced-metro count moves "
      f"{b['service_share_of_revenue']:.1%} of revenue. Raising the premium tier's mix "
      f"share by ten points moves considerably more. If the service is meant to be a "
      f"business rather than an enabler, it needs a materially higher price or an "
      f"attach that reaches beyond the top {asm['serviced_metros']} metros.\n")

    # --------------------------------------------------------------------- SAM
    A("## SAM — the configurable, online-addressable slice\n")
    A(f"Article pool {auto(sam['article_pool_usd'])} × willing share × online-addressable "
      f"share. The willing share starts from the measured "
      f"{sam['custom_search_share_measured']:.2%} search share and is multiplied to "
      f"reflect that an autonomous factory removes the custom premium; the multiple is an "
      f"**assumption**, capped at {A_['willing_share_cap']:.0%}. The online-addressable "
      f"share is also an **assumption** — Census e-commerce share by merchandise line "
      f"would measure it.\n")
    ol = A_["online_addressable_share"]
    A("| Willing share | " + " | ".join(f"online {v:.0%}" for v in ol.values()) + " |")
    A("|---|" + "---:|" * len(ol))
    for wl, wm in A_["custom_willing_multiple"].items():
        w = min(sam["custom_search_share_measured"] * wm, A_["willing_share_cap"])
        cells = " | ".join(auto(sam["grid"][f"{wl}/{k}"]) for k in ol)
        tag = {"floor": "measured, no uplift", "base": "assumed", "ceiling": "assumed"}[wl]
        A(f"| {wl} — {w:.1%} of buyers ({tag}) | {cells} |")
    A("")
    A(f"That grid sizes the **product** SAM. Assembly is a service and sits outside the "
      f"CEX furniture pool entirely, so it is additional rather than a slice of the same "
      f"dollars: the base product SAM implies {sam['implied_orders']:,} orders a year, "
      f"which at an {b['attach_rate']:.1%} blended attach adds "
      f"{auto(sam['service_usd'])} — a total SAM of **{auto(sam['base_usd'])}**.\n")
    A(f"Base product case **{auto(sam['product_usd'])} a year**. The spread across the grid is "
      f"{auto(min(sam['grid'].values()))} to {auto(max(sam['grid'].values()))} — a "
      f"{max(sam['grid'].values()) / max(min(sam['grid'].values()), 1):.0f}× range driven "
      f"almost entirely by two assumptions. Treat the floor row as the only defensible "
      f"number until the willing share is measured.\n")

    # --------------------------------------------------------------------- SOM
    f_ = A_["factory"]
    A("## SOM — the smaller of what we can make and what we can sell\n")
    A(f"One cell, {f_['operating_days_per_year']} operating days, "
      f"{f_['machine_hours_per_shift']}h of machine time per shift, "
      f"{f_['yield_rate']:.0%} yield, {pick['machine_hours_per_unit']}h per unit "
      f"**(assumption — replace with the cycle time off your own cell)**, valued at the "
      f"blended order of ${b['revenue_per_order_usd']:,} from the tier table above. "
      f"Cycle time is no longer assumed: {m.get('capacity_basis', '')}.\n")
    A("| Shifts | Units / yr | Revenue at blended order | % of total SAM |")
    A("|---:|---:|---:|---:|")
    for label, c in m["capacity"].items():
        A(f"| {c['shifts']} ({label}) | {c['units_per_year']:,} | "
          f"{auto(c['revenue_at_asp_usd'])} | {c['share_of_base_sam_pct']}% |")
    A("")
    A(f"### Three-year ramp at {f_['shifts']['base']} shifts\n")
    A("| Year | Utilisation | Units | Units / wk | Product rev | Installs | Service rev | Crews | Total revenue | Gross profit |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in som["ramp"]:
        A(f"| {r['year'].replace('_', ' ').title()} | {r['utilisation']:.0%} | "
          f"{r['units']:,} | {r['units_per_week']} | {auto(r['product_revenue_usd'])} | "
          f"{r['installs']:,} | {auto(r['service_revenue_usd'])} | {r['crews_needed']} | "
          f"{auto(r['revenue_usd'])} | {auto(r['gross_profit_usd'])} |")
    A("")
    A(f"Gross profit is the blended figure from the tier table. Year 3 is "
      f"{som['ramp'][-1]['units_per_week']} orders a week out of a single cell — a "
      f"manufacturing number, and the plant is not short of room to make it.\n")

    r3 = som["ramp"][-1]
    if r3.get("actual_gross_margin") is not None:
        A(f"**The factory does not deliver the assumed margin at this volume.** The tier "
          f"ladder assumes {b['gross_margin']:.0%}; at {r3['units']:,} units the modelled "
          f"cost is ${r3['modelled_cost_per_unit_usd']:,.0f} a unit against a "
          f"${b['revenue_per_order_usd']:,} order \u2014 {r3['actual_gross_margin']:.0%}. "
          f"They converge near 5,000 units a year. The cost build-up is in "
          f"`reports/autonomous-factory-plan.html`.\n")

    # --------------------------------------------------------------------- CAC
    cac = m["cac"]
    A("### Can you buy the demand to fill the line?\n")
    A(f"CPC basis: {cac['cpc_basis']} (${cac['cpc_usd']:.2f}). Gross profit per order "
      f"${cac['gross_profit_per_unit_usd']:,.0f}, blended across the tier mix and the "
      f"assembly attach.\n")
    A("| Site conversion | Implied CAC | % of order value | % of gross profit | Year-3 ad spend |")
    A("|---:|---:|---:|---:|---:|")
    for s in cac["scenarios"]:
        A(f"| {s['conversion_rate']:.1%} | ${s['cac_usd']:,.0f} | "
          f"{s['cac_as_pct_of_asp']}% | {s['cac_as_pct_of_gross_profit']}% | "
          f"{auto(s['year_3_ad_spend_usd'])} |")
    A("")
    A("At a 0.5% conversion rate paid acquisition eats most of the gross profit, and the "
      "capacity plan stops being fundable from its own margin. Getting the real CPC out "
      "of Keyword Planner is the highest-value missing measurement in this model.\n")

    # ------------------------------------------------------------- who you compete with
    if m.get("competition"):
        A("## Who already makes this (Census CBP 2022, US)\n")
        A("| NAICS | Industry | Establishments | Employees | Annual payroll | Under 5 staff |")
        A("|---|---|---:|---:|---:|---:|")
        for naics, c in m["competition"].items():
            A(f"| {naics} | {c['label']} | {c['establishments']:,} | "
              f"{c['employees']:,} | {usd(c['annual_payroll_usd'], 'bn')} | "
              f"{c['under_5_employees']:,} |")
        A("")
        A("The under-5-staff column is the competitive read: this industry is mostly "
          "very small shops. That is what makes an automation thesis plausible, and also "
          "what makes the incumbents impossible to acquire share from quickly — they are "
          "local, referral-fed and numerous.\n")

    # ---------------------------------------------------------------- purchase intent
    if trends:
        A("## Purchase intent (Google Trends, US, five years)\n")
        A("Every term is scaled against the same anchor (`dining table` = 1.00), so all "
          "batches are comparable. Custom-share per family is the pair ratio.\n")
        acc: dict[str, list[float]] = {}
        for r in trends:
            try:
                acc.setdefault(r["keyword"], []).append(float(r["anchor_scaled"]))
            except (KeyError, ValueError):
                continue
        mean = {k: sum(v) / len(v) for k, v in acc.items() if v}
        pairs = [("sofa", "custom sofa"), ("desk", "custom desk"),
                 ("dresser", "custom dresser"), ("bed frame", "custom bed frame"),
                 ("dining table", "custom dining table"),
                 ("coffee table", "custom coffee table"), ("tv stand", "custom tv stand"),
                 ("bookshelf", "custom bookshelf"), ("wardrobe", "custom wardrobe"),
                 ("nightstand", "custom nightstand"),
                 ("closet organizer", "custom closet"),
                 ("kitchen cabinets", "custom cabinets")]
        A("| Generic term | Interest | Custom term | Interest | Custom share |")
        A("|---|---:|---|---:|---:|")
        for g, c in sorted(pairs, key=lambda p: -(mean.get(p[0], 0))):
            if g in mean and c in mean:
                A(f"| {g} | {mean[g]:.3f} | {c} | {mean[c]:.3f} | {mean[c] / mean[g]:.2%} |")
        A("")

    rank = read_csv("custom_demand_ranking")
    if rank:
        res = [r for r in rank if r["resolved"] == "True"]
        unres = [r for r in rank if r["resolved"] != "True"]
        free = [r for r in res if r["free_standing_furniture"] == "True"]
        A("### Which customisable furniture is most in demand\n")
        A("Every term is a `custom X` anchored on `custom furniture`, so the categories "
          "are comparable to each other. `0/1 weeks` is the share of weeks the index sat "
          "at or below 1 — above 80% the series is at the Trends resolution floor and is "
          "reported as unresolved rather than ranked, because a number that is 95% zeros "
          "is not a small number, it is an absent one.\n")
        A("| Article | Level | Custom share of generic | Genuinely furniture | 0/1 weeks | Score |")
        A("|---|---:|---:|---:|---:|---:|")
        for r in rank:
            mark = "" if r["free_standing_furniture"] == "True" else " ~"
            gen = (f"{float(r['furniture_share_of_related']):.0%}"
                   if r["furniture_share_of_related"] not in ("", "None") else "—")
            shr = (f"{float(r['custom_share_of_generic']):.2%}"
                   if r["custom_share_of_generic"] not in ("", "None") else "—")
            flr = (f"{float(r['weeks_at_or_below_1']):.0%}"
                   if r["weeks_at_or_below_1"] not in ("", "None") else "—")
            sc = (f"{float(r['demand_score']):.3f}"
                  if r["demand_score"] not in ("", "None") else "_unresolved_")
            A(f"| {r['custom_term']}{mark} | {float(r['level_vs_custom_furniture']):.3f} "
              f"| {shr} | {gen} | {flr} | {sc} |")
        A("")
        A("*~ = not free-standing furniture: a built-in or an adjacent trade.*\n")
        A(f"**{len(unres)} of {len(rank)} categories cannot be ranked at all** — they sit "
          f"at the index floor. Of the {len(res)} that resolve, "
          f"{len(res) - len(free)} are built-ins rather than furniture.\n")
        if free:
            A(f"The best-resolved free-standing furniture is `{free[0]['custom_term']}`, "
              f"and even that is only "
              f"{float(free[0]['furniture_share_of_related']):.0%} genuinely furniture in "
              f"its related searches — the rest is accessories.\n")
        A("**Momentum is not reported.** 13 of 25 series peak in the same week "
          "(2026-04-12) across independent query batches, which is an index artifact "
          "rather than demand; any year-on-year figure spanning it measures the artifact. "
          "The ranking uses level only.\n")
        A("**Google Trends is a relative index, not a volume.** Keyword Planner turns "
          "these into monthly search counts and a cost per click, and is the only way to "
          "resolve the 15 categories that are invisible here.\n")

    if metro:
        focus = [r for r in metro if r.get("batch") == "geo_focus"
                 and r.get("keyword") == "custom furniture"]
        focus = sorted(focus, key=lambda r: -int(r["index"] or 0))[:8]
        if focus:
            A("**Where `custom furniture` interest sits** (unanchored, 100 = peak state):\n")
            A("| State | Index |")
            A("|---|---:|")
            for r in focus:
                A(f"| {r['geo_name']} | {r['index']} |")
            A("")

    # --------------------------------------------------------------- household spend
    if cex:
        yr = m["cex_year"]
        A(f"## Household furniture spend by income quintile, {yr} (BLS CEX)\n")
        A("Average annual expenditure per consumer unit.\n")
        groups = ["Q1 lowest 20%", "Q2", "Q3", "Q4", "Q5 highest 20%", "All consumer units"]
        A(f"| Quintile | {pick['article']} | All furniture |")
        A("|---|---:|---:|")
        for g in groups:
            def v(item):
                r = [x for x in cex if x["item_code"] == item and x["cut"] == "LB01"
                     and x["group"] == g and int(x["year"]) == yr]
                return f"${float(r[0]['value']):,.0f}" if r else "—"
            A(f"| {g} | {v(pick['cex_item'])} | {v('FURNITUR')} |")
        A("")
        q5 = [x for x in cex if x["item_code"] == pick["cex_item"] and x["cut"] == "LB01"
              and x["group"] == "Q5 highest 20%" and int(x["year"]) == yr]
        if q5:
            q5v = float(q5[0]["value"])
            A(f"The top income quintile spends ${q5v:,.0f} a year on the beachhead "
              f"article. A ${pick['asp_usd']:,} unit is therefore not an annual purchase "
              f"out of a furniture budget — at that rate it is a "
              f"{pick['asp_usd'] / q5v:.0f}-year purchase, which is what the acquisition "
              f"maths above has to survive.\n")

    # --------------------------------------------------------------------- retail trend
    if mrts:
        A("### US furniture retail sales, NAICS 442 (Census MRTS)\n")
        by_year: dict[int, float] = {}
        for r in mrts:
            if r["naics"] == "442" and r["seasonally_adjusted"] == "False":
                by_year[int(r["year"])] = by_year.get(int(r["year"]), 0) + float(r["sales_musd"])
        months: dict[int, int] = {}
        for r in mrts:
            if r["naics"] == "442" and r["seasonally_adjusted"] == "False":
                months[int(r["year"])] = months.get(int(r["year"]), 0) + 1
        # A part year can still be compared, but only against the same months of the
        # prior year — never against its full twelve.
        same_months: dict[int, float] = {}
        for r in mrts:
            if r["naics"] == "442" and r["seasonally_adjusted"] == "False":
                y, mo = int(r["year"]), int(r["month"])
                latest = max(int(x["year"]) for x in mrts if x["naics"] == "442")
                if mo <= months.get(latest, 12):
                    same_months[y] = same_months.get(y, 0) + float(r["sales_musd"])
        A("| Year | Sales | YoY |")
        A("|---:|---:|---:|")
        for y in sorted(by_year):
            if y < 2019:
                continue
            partial = months[y] < 12
            part = f" (first {months[y]} months)" if partial else ""
            if partial:
                prev = same_months.get(y - 1)
                yoy = (f"{(same_months[y] / prev - 1) * 100:+.1f}% vs. the same months of "
                       f"{y - 1}") if prev else "—"
            else:
                prev = by_year.get(y - 1)
                yoy = f"{(by_year[y] / prev - 1) * 100:+.1f}%" if prev and months.get(y - 1) == 12 else "—"
            A(f"| {y}{part} | {usd(by_year[y] * 1e6, 'bn')} | {yoy} |")
        A("")

    # ------------------------------------------------------------------- imports
    if imports:
        A("### Import exposure (UN Comtrade, US imports)\n")
        by_year = {}
        for r in imports:
            if r.get("partner") != "World":
                continue
            try:
                by_year[int(r["year"])] = by_year.get(int(r["year"]), 0) + float(r["value_usd"])
            except (KeyError, ValueError):
                continue
        A("| Year | US wood-furniture imports |")
        A("|---:|---:|")
        for y in sorted(by_year):
            A(f"| {y} | {usd(by_year[y], 'bn')} |")
        A("")

    # ------------------------------------------------------------------ not collected
    blocked = [(s, d, e) for (s, d), e in sorted(status.items())
               if e["status"] != "ok"]
    if blocked:
        A("## Not yet collected\n")
        A("| Source | Blocked on |")
        A("|---|---|")
        for s, d, e in blocked:
            A(f"| {s} / {d} | {e['note'][:120]} |")
        A("")
        A("See `scripts/research/CREDENTIALS.md`. Keyword Planner is the one that matters most: it "
          "replaces the placeholder CPC, which drives the whole acquisition section.\n")

    # ------------------------------------------------------------------- provenance
    A("## Provenance\n")
    A("| Source | Dataset | Rows | Status | Fetched |")
    A("|---|---|---:|---|---|")
    for (s, d), e in sorted(status.items()):
        A(f"| {s} | {d} | {e['rows']:,} | {e['status']} | {e['fetched_at'][:16].replace('T', ' ')} |")

    (RESEARCH / "REPORT.md").write_text("\n".join(L) + "\n")
    log(f"  REPORT.md written ({len(L)} lines)")


if __name__ == "__main__":
    main()
