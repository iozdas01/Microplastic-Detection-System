"""TAM / SAM / SOM for custom kitchen cabinets, with every step labelled and sourced.

Two things make this model different from the furniture one it replaces.

First, the market size is *measured*, not inferred from search. Census County Business
Patterns records how many cabinet makers exist, how many people they employ and what they
pay them. Payroll times a revenue multiple gives industry revenue — that is revealed
demand: those businesses exist because people buy from them.

Second, the custom share is measured on an instrument that can resolve it. "custom
cabinets" against "kitchen cabinets" sits at 7.6% with zero weeks at the Trends index
floor, unlike every free-standing furniture term, which sits at the floor 90%+ of the
time and cannot be read at all.

Every step below carries a `kind`:

    measured   a number from a public dataset, with the source named
    derived    arithmetic on measured numbers
    assumed    a judgement — stated, not hidden, and the ones that move the answer

Nothing here is a syndicated market number.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PROC, log, read_csv, record, save_csv  # noqa: E402

ASSUMPTIONS = {
    # CBP publishes payroll, not revenue. Wood kitchen cabinet manufacturing runs roughly
    # 3.0-3.6x annual payroll in revenue; the Economic Census RCPTOT would replace this
    # with a measured ratio the moment CENSUS_API_KEY is set.
    "revenue_to_payroll_multiple": {"low": 3.0, "base": 3.3, "high": 3.6},
    # Share of the cabinet market that is custom or semi-custom rather than stock.
    # The measured search share is used as the base; the band around it reflects that
    # industry convention splits the market roughly 60/30/10 stock/semi/custom.
    "custom_share_override": None,      # None = take the measured search share
    # The band around the measured search share. The high end is deliberately far above
    # it: third-party remodelling surveys put custom *and semi-custom* cabinets at a much
    # larger share of purchases than the number of people typing "custom cabinets" into
    # Google. Semi-custom — a factory box with configurable sizes, doors and finishes — is
    # arguably exactly what a configurator sells, so the measured share is a conservative
    # floor rather than a centre. Those survey figures are not used in the arithmetic;
    # they only justify the width of the band.
    "custom_share_band": {"low": 0.05, "measured": None, "high": 0.37},
    # Of custom cabinet spend, how much can be won without a showroom or a local
    # installer relationship. This is the assumption that most needs testing.
    "online_addressable_share": {"low": 0.08, "base": 0.15, "high": 0.25},
    # No market-share assumption. The SOM is what the plant can physically build.
    # Capacity is not re-derived here: the factory model in the build plan
    # (reports/kitchens-without-drafting.html) works it out from 22 sheets a kitchen at
    # 11 minutes a sheet on the router plus 80 minutes on the edgebander, and lands on
    # 228 kitchens a year. Re-deriving it from a second, looser set of cycle times would
    # only give the two documents different answers to the same question.
    "machine_capacity_kitchens_per_year": 228,
    "capacity_source": ("factory model in the build plan — router and edgebander at "
                        "22 sheets a kitchen"),
    "asp_per_kitchen_usd": 17_550,      # 27 linear feet at $650/lf, as the build plan prices it
    "boxes_per_kitchen": 14,
    # What SOM revenue turns into. Gross margin is what survives materials, direct
    # labour and freight; annual fixed cost is the plant, the salaried team and
    # depreciation. Both are ASSUMPTIONS until the cabinet factory model replaces the
    # kigumi one — see build_factory.py, which is currently specced for solid timber.
    "gross_margin": {"low": 0.38, "base": 0.46, "high": 0.54},
    "annual_fixed_cost_usd": 1_150_000,

    # Two ways to reach the same market. The plan so far has assumed the first, but the
    # second is what makes a year-one breakeven arithmetically possible — and it tests
    # the assumption the first one bets $3.2m on.
    "routes": {
        "build the factory first": {
            "capex_usd": 3_220_000, "annual_fixed_usd": 1_150_000,
            "gross_margin": 0.46,
            "note": "our own panel plant: nesting router, edgebander, drilling",
        },
        "sell first, subcontract production": {
            "capex_usd": 180_000, "annual_fixed_usd": 310_000,
            "gross_margin": 0.26,
            "note": "configurator, samples and a small team; boxes bought finished from "
                    "one of the 6,118 existing cabinet shops",
        },
    },
}


def main() -> None:
    cbp = read_csv("cbp_furniture_supply")
    rank = read_csv("custom_demand_ranking")
    prices = read_csv("bls_prices")
    if not cbp:
        log("build_cabinet_tam: no CBP data — run scripts/t2_cbp_supply.py first")
        return

    A = ASSUMPTIONS
    steps: list[dict] = []

    def step(name, value, unit, kind, source, plain):
        steps.append({"step": name, "value": value, "unit": unit, "kind": kind,
                      "source": source, "plain_english": plain})
        return value

    us = {r["naics"]: r for r in cbp if r["geo_level"] == "us"}
    cab = us.get("337110")
    if not cab:
        log("build_cabinet_tam: NAICS 337110 missing — re-run t2_cbp_supply.py")
        return

    estab = int(cab["estab"])
    emp = int(cab["employees"])
    payroll = int(cab["annual_payroll_k"]) * 1000

    step("Cabinet makers in the US", estab, "establishments", "measured",
         "Census County Business Patterns 2022, NAICS 337110",
         "How many businesses in America manufacture wood kitchen cabinets.")
    step("People they employ", emp, "employees", "measured",
         "Census CBP 2022, NAICS 337110",
         "Total employment across those businesses.")
    step("What they pay those people", payroll, "usd/yr", "measured",
         "Census CBP 2022, NAICS 337110",
         "Total annual payroll. This is the anchor for the whole model: a business "
         "cannot pay wages out of demand that does not exist.")

    mult = A["revenue_to_payroll_multiple"]
    tam = payroll * mult["base"]
    step("TAM — US cabinet manufacturing revenue", tam, "usd/yr", "derived",
         f"payroll x {mult['base']}x revenue-to-payroll multiple",
         "The whole industry, at manufacturer prices: every wood cabinet and countertop "
         "made in America, across all 6,118 makers. The size of the pond.")

    # --- the custom slice, measured ---------------------------------------------------
    row = next((r for r in rank if r["custom_term"] == "custom cabinets"), None)
    if A["custom_share_override"] is not None:
        share, share_kind, share_src = A["custom_share_override"], "assumed", "override"
    elif row and row.get("custom_share_of_generic") not in (None, "", "None"):
        share = float(row["custom_share_of_generic"])
        share_kind = "measured"
        share_src = ("Google Trends US 5y: 'custom cabinets' vs 'kitchen cabinets', "
                     f"0% of weeks at the index floor")
    else:
        share, share_kind, share_src = 0.076, "assumed", "fallback"
    step("Share of cabinet demand that wants custom", share, "share", share_kind,
         share_src,
         "Of everyone looking for kitchen cabinets, the fraction looking for custom "
         "ones. Unlike every furniture term tested, this one is measurable: it never "
         "sits at the Trends resolution floor.")

    custom_pool = tam * share
    step("The custom slice of it", custom_pool, "usd/yr", "derived",
         "TAM x custom share",
         "The part of the industry that is custom rather than stock. This is the part "
         "we would compete in.")

    online = A["online_addressable_share"]
    sam = custom_pool * online["base"]
    step("SAM — the part our model can serve", sam, "usd/yr", "assumed",
         f"TAM x {online['base']:.0%} sellable direct",
         "Cabinets are normally sold through kitchen designers, showrooms and remodelers. "
         "This is the slice a direct, configurator-led business could compete for. Still "
         "not our revenue — it is what is available to us to win.")

    # --- SOM: the plant's ceiling, not a share of the market --------------------------
    kitchens_cap = A["machine_capacity_kitchens_per_year"]
    boxes = kitchens_cap * A["boxes_per_kitchen"]
    som = kitchens_cap * A["asp_per_kitchen_usd"]
    step("SOM — everything the factory can build", som, "usd/yr", "derived",
         A["capacity_source"],
         "Not a share of the market — the market is far bigger than the plant. This is "
         "the ceiling the machines impose, so it is what binds.")
    gm = A["gross_margin"]
    gross_profit = som * gm["base"]
    step("Gross profit on that", gross_profit, "usd/yr", "assumed",
         f"SOM x {gm['base']:.0%} gross margin",
         "What is left after the sheet goods, the bought-in doors, the hardware and the "
         "freight. Not profit yet — the plant still has to be paid for.")
    operating = gross_profit - A["annual_fixed_cost_usd"]
    step("Operating profit after the factory", operating, "usd/yr", "assumed",
         f"gross profit - ${A['annual_fixed_cost_usd']:,} annual fixed cost",
         "The money actually kept. This is the number the whole model exists to produce.")

    step("Cabinet boxes that means cutting", boxes, "boxes/yr", "derived",
         f"{kitchens_cap} kitchens x {A['boxes_per_kitchen']} boxes",
         "What the router and edgebander actually have to get through.")
    kitchens = som / A["asp_per_kitchen_usd"]
    step("Kitchens a year at year 3", kitchens, "kitchens/yr", "derived",
         f"SOM / ${A['asp_per_kitchen_usd']:,} per kitchen",
         "What that revenue means in orders. A custom kitchen is one order of many "
         "boxes, not one cabinet.")
    step("Cabinet boxes a year at year 3", kitchens * A["boxes_per_kitchen"],
         "boxes/yr", "derived",
         f"kitchens x {A['boxes_per_kitchen']} boxes",
         "What the factory actually has to cut.")

    # --- scenario grid ----------------------------------------------------------------
    grid = {}
    for ml, mv in mult.items():
        for ol, ov in online.items():
            grid[f"{ml}/{ol}"] = payroll * mv * share * ov

    band = dict(A["custom_share_band"])
    band["measured"] = share
    share_band = {k: {"share": v, "custom_pool_usd": round(tam * v),
                      "sam_usd": round(tam * v * online["base"])}
                  for k, v in band.items() if v}

    # --- why cabinets and not furniture -----------------------------------------------
    comparison = []
    for naics, label in [("337110", "Wood kitchen cabinets"),
                         ("337122", "Nonupholstered wood household furniture"),
                         ("337212", "Custom architectural woodwork"),
                         ("236118", "Residential remodelers")]:
        r = us.get(naics)
        if not r:
            continue
        pay = int(r["annual_payroll_k"]) * 1000
        comparison.append({
            "naics": naics, "label": label,
            "establishments": int(r["estab"]), "employees": int(r["employees"]),
            "annual_payroll_usd": pay,
            "implied_revenue_usd": pay * mult["base"],
        })

    resolved = [r for r in rank if r["resolved"] == "True"]
    routes = []
    for name, r in A["routes"].items():
        be_rev = r["annual_fixed_usd"] / r["gross_margin"]
        routes.append({
            "route": name, "note": r["note"],
            "capex_usd": r["capex_usd"],
            "annual_fixed_usd": r["annual_fixed_usd"],
            "gross_margin": r["gross_margin"],
            "breakeven_revenue_usd": round(be_rev),
            "breakeven_kitchens": round(be_rev / A["asp_per_kitchen_usd"]),
            "breakeven_kitchens_per_week": round(
                be_rev / A["asp_per_kitchen_usd"] / 52, 1),
            "cash_at_risk_usd": r["capex_usd"] + r["annual_fixed_usd"],
        })

    money = []
    for gl, gv in gm.items():
        for sl, sv in {"quarter": 0.25, "half": 0.5, "full": 1.0}.items():
            rev = som * sv
            gp = rev * gv
            money.append({"margin": gl, "margin_pct": gv, "volume": sl,
                          "revenue_usd": round(rev), "gross_profit_usd": round(gp),
                          "operating_usd": round(gp - A["annual_fixed_cost_usd"]),
                          "breakeven": gp >= A["annual_fixed_cost_usd"]})

    out = {
        "capacity": {
            "source": A["capacity_source"],
            "boxes_per_year": round(boxes), "kitchens_per_year": round(kitchens_cap),
            "revenue_at_capacity_usd": round(som),
            "share_of_sam": round(som / sam, 4),
            "note": ("Capacity is a fraction of the reachable market, so the factory is "
                     "the constraint and no market-share assumption is needed."),
        },
        "custom_share_band": share_band,
        "share_band_note": (
            "The measured 7.6% counts people searching the words 'custom cabinets'. It is "
            "a share of searches, not a share of revenue, and it excludes semi-custom "
            "entirely — a factory box with configurable sizes and finishes, which is what "
            "a configurator actually sells. Third-party remodelling surveys put custom and "
            "semi-custom together far higher. Those figures disagree with each other and "
            "are not used in the arithmetic; they are why the top of the band is 37%."),
        "routes": routes,
        "money": money,
        "breakeven_revenue_usd": round(A["annual_fixed_cost_usd"] / gm["base"]),
        "breakeven_kitchens": round(A["annual_fixed_cost_usd"] / gm["base"]
                                    / A["asp_per_kitchen_usd"]),
        "layers": {
            "tam_usd": tam,
            "custom_slice_usd": custom_pool,
            "sam_usd": sam,
            "som_usd": som,
            "note": ("TAM, SAM and SOM are three nested slices, and only the last is "
                     "revenue. TAM is the whole cabinet industry; the custom slice is "
                     "the part we would compete in; SAM is what our model could serve; "
                     "SOM is what we would actually book — and margin turns that into "
                     "what we would keep."),
        },
        "assumptions": A,
        "steps": steps,
        "tam_usd": tam, "custom_pool_usd": custom_pool, "sam_usd": sam, "som_usd": som,
        "sam_grid": {k: round(v) for k, v in grid.items()},
        "industry_comparison": comparison,
        "why_cabinets": {
            "search_rank": next((i + 1 for i, r in enumerate(rank)
                                 if r["custom_term"] == "custom cabinets"), None),
            "weeks_at_index_floor": float(row["weeks_at_or_below_1"]) if row else None,
            "genuinely_furniture": float(row["furniture_share_of_related"])
            if row and row["furniture_share_of_related"] not in ("", "None") else None,
            "resolved_categories": len(resolved),
            "total_categories": len(rank),
            "reading": ("Cabinets are the only category where the demand evidence and the "
                        "supply evidence agree. Search ranks it first and can actually "
                        "resolve it; CBP shows an industry five times the size of "
                        "non-upholstered wood furniture. Every free-standing furniture "
                        "article fails on one side or the other."),
        },
    }
    (PROC / "cabinet_tam_model.json").write_text(json.dumps(out, indent=2, default=str))
    save_csv("cabinet_tam_steps", steps)
    record("analysis", "cabinet-tam", "scripts/build_cabinet_tam.py", len(steps),
           note=f"TAM ${tam/1e9:.1f}bn, SAM ${sam/1e6:.0f}m, SOM ${som/1e6:.1f}m")

    log("  Custom kitchen cabinets — every step, with what kind of number it is:")
    for s in steps:
        v = s["value"]
        if s["unit"] == "usd/yr":
            vs = f"${v/1e9:,.2f}bn" if v >= 1e9 else f"${v/1e6:,.1f}m"
        elif s["unit"] == "share":
            vs = f"{v:.2%}"
        else:
            vs = f"{v:,.0f}"
        log(f"    [{s['kind']:<8}] {s['step']:<42} {vs:>12}")
    log("")
    log(f"  Capacity: {kitchens_cap:,} kitchens = {boxes:,.0f} boxes = ${som/1e6:,.2f}m, "
        f"which is {som/sam:.1%} of the SAM")
    log(f"  Breakeven: ${A['annual_fixed_cost_usd'] / gm['base']:,.0f} of revenue "
        f"= {A['annual_fixed_cost_usd'] / gm['base'] / A['asp_per_kitchen_usd']:,.0f} "
        f"kitchens a year, at a {gm['base']:.0%} gross margin")
    log("  Money kept, by margin and volume:")
    log(f"    {'':<12}" + "".join(f"{v:>16}" for v in ("25% util", "50% util", "full")))
    for gl, gv in gm.items():
        cells = "".join(
            f"{(som*sv*gv - A['annual_fixed_cost_usd'])/1e6:>+15,.2f}m"
            for sv in (0.25, 0.5, 1.0))
        log(f"    {gl+' '+format(gv,'.0%'):<12}{cells}")
    log("")
    log("  Two routes to the same market:")
    for r in routes:
        log(f"    {r['route']:<36} capex ${r['capex_usd']:>9,}  "
            f"breakeven {r['breakeven_kitchens']:>4,} kitchens/yr "
            f"({r['breakeven_kitchens_per_week']}/wk)  "
            f"cash at risk ${r['cash_at_risk_usd']:,}")
    log("")
    log("  Why cabinets and not a furniture article:")
    for c in comparison:
        log(f"    {c['naics']} {c['label'][:42]:<42} {c['establishments']:>7,} estabs "
            f"${c['implied_revenue_usd']/1e9:>6.1f}bn")


if __name__ == "__main__":
    main()
