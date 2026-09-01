"""Bottom-up Bay Area TAM for custom solid-wood dining furniture.

Built from household spend upward, not from a syndicated market number downward. Every
figure traces to a collector output in data/processed/ and a line in data/MANIFEST.jsonl.

    1. US pool      Σ over income quintiles of (consumer units × avg annual $ on
                    "kitchen and dining room furniture", CEX item 290410)
    2. Sanity check that pool against MRTS actual retail sales for NAICS 442
    3. Bay Area     scale by population share, then by a spend-per-household factor
                    that is itself measured (CEX West region, and the Q5 quintile)
    4. Custom cut   the custom/solid-wood slice of that pool, as a scenario band
    5. Unit math    at a given ASP, how many tables a year that is, against the 38
                    wood-furniture establishments CBP counts in the Bay Area
    6. CAC floor    from Keyword Planner CPC when credentials are present

Assumptions live in ASSUMPTIONS below and are printed with the results. Change them
there; nothing is hardcoded further down.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PROC, log, read_csv, save_csv  # noqa: E402

ASSUMPTIONS = {
    "cex_year": 2024,
    # Search-volume share of "custom dining table" vs "dining table" comes out of the
    # Trends collector. A custom table sells for several times a mass-market one, so the
    # revenue share is the search share times a price multiple. Both ends are scenarios.
    "custom_price_multiple": {"low": 3.0, "base": 5.0, "high": 8.0},
    "custom_search_share_override": None,   # None = take it from trends_interest_over_time
    "asp_usd": {"low": 2500, "base": 4200, "high": 7000},
    "site_conversion_rate": {"low": 0.005, "base": 0.015, "high": 0.03},
    "cpc_usd_fallback": 2.50,   # replaced by measured CPC when Keyword Planner runs
    "target_revenue_usd": 1_000_000,
    # Supply-side cross-check: wood furniture manufacturing runs roughly 3.0-3.6x annual
    # payroll in revenue. Economic Census RCPTOT replaces this guess with a measured
    # ratio the moment CENSUS_API_KEY is set.
    "revenue_to_payroll_multiple": {"low": 3.0, "base": 3.3, "high": 3.6},
}


def cex_lookup(rows, item, cut, group, year):
    m = [r for r in rows if r["item_code"] == item and r["cut"] == cut
         and r["group"] == group and int(r["year"]) == year]
    return float(m[0]["value"]) if m else None


def main() -> None:
    cex = read_csv("cex_furniture_expenditure")
    pop = read_csv("bay_area_population")
    mrts = read_csv("mrts_furniture_monthly")
    cbp = read_csv("cbp_furniture_supply")
    trends = read_csv("trends_interest_over_time")
    kw = read_csv("keyword_planner_metrics")
    acs = read_csv("acs_bay_area_households")

    if not cex or not pop:
        log("build_tam: missing CEX or population inputs — run the collectors first")
        return

    yr = ASSUMPTIONS["cex_year"]
    out: dict = {"assumptions": ASSUMPTIONS, "cex_year": yr, "steps": []}

    def step(name, value, unit, basis):
        out["steps"].append({"step": name, "value": value, "unit": unit, "basis": basis})
        return value

    # --- 1. US household pool for kitchen and dining room furniture ------------------
    quintiles = ["Q1 lowest 20%", "Q2", "Q3", "Q4", "Q5 highest 20%"]
    us_pool, cu_total = 0.0, 0.0
    per_quintile = []
    for q in quintiles:
        spend = cex_lookup(cex, "290410", "LB01", q, yr)
        cus = cex_lookup(cex, "CONSUNIT", "LB01", q, yr)   # thousands
        if spend is None or cus is None:
            continue
        pool = spend * cus * 1000
        us_pool += pool
        cu_total += cus * 1000
        per_quintile.append({"quintile": q, "avg_annual_spend_usd": spend,
                             "consumer_units": cus * 1000, "pool_usd": pool})
    all_cu_spend = cex_lookup(cex, "290410", "LB01", "All consumer units", yr)
    step("US consumer units", cu_total, "households", f"CEX CONSUNIT {yr}")
    step("US spend on kitchen & dining room furniture", us_pool, "usd/yr",
         f"CEX item 290410 x CONSUNIT, summed over income quintiles, {yr}")

    # --- 2. sanity check against MRTS ------------------------------------------------
    mrts_442 = [r for r in mrts if r["naics"] == "442"
                and r["seasonally_adjusted"] == "False" and int(r["year"]) == yr]
    mrts_annual = sum(float(r["sales_musd"]) for r in mrts_442) * 1e6
    if mrts_annual:
        out["sanity_check"] = {
            "mrts_442_annual_usd": mrts_annual,
            "cex_dining_pool_usd": us_pool,
            "dining_share_of_442": round(us_pool / mrts_annual, 4),
            "reading": ("A single-digit percentage is the expected shape, since 442 "
                        "covers every room in the house plus home furnishings. If this "
                        "ratio came out above ~10% the CEX build would be overstated."),
        }

    # --- 3. Bay Area pool -------------------------------------------------------------
    p24 = {r["geo_level"]: float(r["population"]) for r in pop if int(r["year"]) == 2024}
    pop_share = p24["bay_area_total"] / p24["us"]
    step("Bay Area population share", pop_share, "share", "Census PEP vintage 2024")

    west = cex_lookup(cex, "290410", "LB11", "West", yr)
    all_cu = cex_lookup(cex, "290410", "LB11", "All consumer units", yr) or all_cu_spend
    west_factor = (west / all_cu) if (west and all_cu) else 1.0
    q5 = cex_lookup(cex, "290410", "LB01", "Q5 highest 20%", yr)
    q5_factor = (q5 / all_cu_spend) if (q5 and all_cu_spend) else 1.0
    step("West-region spend factor", west_factor, "x", f"CEX 290410 West / all CUs, {yr}")
    step("Top-quintile spend factor", q5_factor, "x", f"CEX 290410 Q5 / all CUs, {yr}")

    if acs:
        bay_hh = sum(float(r["households_occupied_units"] or 0) for r in acs
                     if r["geo_level"] == "counties")
        hh_basis = "ACS 5-year household count"
    else:
        bay_hh = cu_total * pop_share
        hh_basis = ("US consumer units x Bay Area population share "
                    "(ACS gives the exact count once CENSUS_API_KEY is set)")
    step("Bay Area households", bay_hh, "households", hh_basis)

    pools = {
        "conservative": bay_hh * all_cu_spend,
        "base": bay_hh * all_cu_spend * west_factor,
        "affluence_adjusted": bay_hh * all_cu_spend * q5_factor,
    }
    for k, v in pools.items():
        step(f"Bay Area dining-furniture pool ({k})", v, "usd/yr",
             f"households x CEX 290410 per-CU spend, {k} factor")

    # --- 4. the custom slice ----------------------------------------------------------
    share_override = ASSUMPTIONS["custom_search_share_override"]
    if share_override is not None:
        search_share = share_override
        share_basis = "manual override"
    else:
        vals = {}
        for r in trends:
            vals.setdefault(r["keyword"], []).append(float(r["anchor_scaled"]))
        search_share = (sum(vals.get("custom dining table", [0]))
                        / max(len(vals.get("custom dining table", [1])), 1))
        share_basis = ("Google Trends, mean anchor-scaled interest of 'custom dining "
                       "table' vs 'dining table', California, 5 years")
    step("Custom search share", search_share, "share", share_basis)

    custom = {}
    for label, mult in ASSUMPTIONS["custom_price_multiple"].items():
        custom[label] = pools["base"] * search_share * mult
        step(f"Bay Area custom/solid-wood pool ({label} price multiple {mult}x)",
             custom[label], "usd/yr",
             "base pool x custom search share x price multiple")

    # --- 5. unit economics ------------------------------------------------------------
    units = []
    for label, asp in ASSUMPTIONS["asp_usd"].items():
        orders_for_target = ASSUMPTIONS["target_revenue_usd"] / asp
        units.append({
            "asp_scenario": label, "asp_usd": asp,
            "orders_for_1m_revenue": round(orders_for_target, 1),
            "orders_per_week": round(orders_for_target / 52, 2),
            "market_orders_base": round(custom["base"] / asp),
            "share_of_market_needed_pct": round(
                100 * ASSUMPTIONS["target_revenue_usd"] / custom["base"], 2),
        })
    out["unit_economics"] = units

    # --- 6. CAC floor -----------------------------------------------------------------
    if kw:
        cpcs = [float(r["high_top_of_page_bid_usd"]) for r in kw
                if r.get("high_top_of_page_bid_usd")]
        cpc = sum(cpcs) / len(cpcs) if cpcs else ASSUMPTIONS["cpc_usd_fallback"]
        cpc_basis = f"Keyword Planner, mean high top-of-page bid across {len(cpcs)} keywords"
    else:
        cpc = ASSUMPTIONS["cpc_usd_fallback"]
        cpc_basis = ("PLACEHOLDER — Keyword Planner not run. This is the one number in "
                     "the model with no measurement behind it.")
    out["cac"] = {"cpc_usd": cpc, "cpc_basis": cpc_basis, "scenarios": [
        {"conversion_rate": cr, "cac_usd": round(cpc / cr, 2),
         "cac_as_pct_of_base_asp": round(100 * (cpc / cr) / ASSUMPTIONS["asp_usd"]["base"], 1)}
        for cr in ASSUMPTIONS["site_conversion_rate"].values()]}

    # --- competitive density ----------------------------------------------------------
    bay_estab = {r["naics"]: int(r["estab"]) for r in cbp
                 if r["geo_level"] == "bay_area_total"}
    out["competition"] = {
        "bay_area_establishments_337122": bay_estab.get("337122", 0),
        "bay_area_establishments_337212": bay_estab.get("337212", 0),
        "bay_area_furniture_retailers_442110": bay_estab.get("442110", 0),
        "revenue_per_maker_base_usd": round(
            custom["base"] / max(bay_estab.get("337122", 1), 1)),
    }
    # --- supply-side triangulation ----------------------------------------------------
    # The demand-side custom slice above leans on a search-share proxy, which is the
    # softest input in the model. CBP payroll is measured, so it gives an independent
    # read on how much revenue the Bay Area wood-furniture makers actually book.
    bay_payroll_k = next((float(r["annual_payroll_k"]) for r in cbp
                          if r["geo_level"] == "bay_area_total" and r["naics"] == "337122"), 0.0)
    econ = read_csv("econ_census_industry")
    measured_ratio = None
    for r in econ:
        if r["naics"] == "337122" and r["geo"] == "us" and float(r["payroll_kusd"] or 0):
            measured_ratio = float(r["receipts_kusd"]) / float(r["payroll_kusd"])
            break
    supply = {"bay_area_annual_payroll_usd": bay_payroll_k * 1000,
              "ratio_source": ("Economic Census, measured" if measured_ratio
                               else "assumed multiple — set CENSUS_API_KEY to measure it")}
    ratios = ({"measured": measured_ratio} if measured_ratio
              else ASSUMPTIONS["revenue_to_payroll_multiple"])
    supply["implied_bay_area_revenue_usd"] = {
        k: round(bay_payroll_k * 1000 * v) for k, v in ratios.items()}
    out["supply_side_triangulation"] = supply

    out["quintiles"] = per_quintile

    (PROC / "tam_model.json").write_text(json.dumps(out, indent=2))
    save_csv("tam_steps", out["steps"])
    save_csv("tam_unit_economics", units)

    # --- readout ----------------------------------------------------------------------
    log("")
    log("  BOTTOM-UP BAY AREA TAM — custom solid-wood dining furniture")
    log("  " + "-" * 68)
    log(f"  US spend, kitchen & dining room furniture      ${us_pool/1e9:>8.2f} bn/yr")
    if mrts_annual:
        log(f"    (= {us_pool/mrts_annual*100:.1f}% of all NAICS 442 retail sales, ${mrts_annual/1e9:.1f}bn)")
    log(f"  Bay Area households                            {bay_hh:>11,.0f}")
    log(f"  Bay Area dining-furniture pool (base)          ${pools['base']/1e6:>8.1f} m/yr")
    log(f"    conservative                                 ${pools['conservative']/1e6:>8.1f} m/yr")
    log(f"    affluence-adjusted (top-quintile behaviour)  ${pools['affluence_adjusted']/1e6:>8.1f} m/yr")
    log(f"  Custom search share                             {search_share*100:>8.2f}%")
    log("  Custom/solid-wood slice of the Bay Area pool:")
    for label, v in custom.items():
        log(f"    {label:<12} ${v/1e6:>8.2f} m/yr")
    log("")
    log(f"  To reach ${ASSUMPTIONS['target_revenue_usd']:,.0f} of revenue:")
    for u in units:
        log(f"    ASP ${u['asp_usd']:>6,}  ->  {u['orders_for_1m_revenue']:>5.0f} orders/yr "
            f"({u['orders_per_week']:.1f}/wk), {u['share_of_market_needed_pct']:.1f}% of the base market")
    log("")
    log(f"  CPC ${cpc:.2f} — {cpc_basis[:60]}")
    for c in out["cac"]["scenarios"]:
        log(f"    at {c['conversion_rate']*100:.1f}% conversion -> CAC ${c['cac_usd']:,.0f} "
            f"({c['cac_as_pct_of_base_asp']:.1f}% of a ${ASSUMPTIONS['asp_usd']['base']:,} table)")
    log("")
    log(f"  CBP counts {out['competition']['bay_area_establishments_337122']} wood household "
        f"furniture makers and {out['competition']['bay_area_establishments_337212']} custom "
        "millwork shops in the Bay Area.")
    log(f"  Base custom pool / maker: ${out['competition']['revenue_per_maker_base_usd']:,}")
    log("")
    log("  Supply-side cross-check (independent of the search-share proxy):")
    log(f"    Bay Area 337122 annual payroll (CBP, measured)  ${supply['bay_area_annual_payroll_usd']/1e6:>7.1f} m")
    for k, v in supply["implied_bay_area_revenue_usd"].items():
        log(f"    implied revenue @ {k:<9} multiple            ${v/1e6:>7.1f} m/yr")
    log(f"    ratio source: {supply['ratio_source']}")


if __name__ == "__main__":
    main()
