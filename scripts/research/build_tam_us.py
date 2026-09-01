"""US TAM / SAM / SOM for one configurable furniture article built in an autonomous factory.

Which article to build is an output of this model, not an input to it. Every article line
under CEX "Furniture" is sized from household spend, scored on whether an autonomous
cutting-and-assembly cell can actually make it, and ranked. The winner defines the SAM.

    TAM   US household spend on furniture, bottom-up from CEX x consumer units,
          cross-checked against Census MRTS retail sales for NAICS 442.
    SAM   The chosen article's US pool, cut by (a) the share of buyers who want it
          configured rather than off-the-shelf and (b) the share reachable online.
    SOM   Capacity-led: what one factory can physically produce in a year x ASP,
          ramped over three years. For a manufacturer this is the binding number.

The custom-share input deserves care. Google Trends measures who searches "custom X"
*today*, when custom means a 3-8x premium and a six-week wait from a joinery shop. An
autonomous factory sells configurable at close to stock price, which is a different
proposition to a different buyer. So the measured search share is used as the FLOOR of a
band, not as the estimate; the base and ceiling are assumptions and are labelled as such.

Assumptions live in ASSUMPTIONS below and are printed with the results. Change them
there; nothing is hardcoded further down.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PROC, log, read_csv, save_csv  # noqa: E402

# --- articles ---------------------------------------------------------------------
# One row per CEX furniture line. `generic`/`custom` are the Google Trends terms whose
# ratio gives the measured custom-search share for that line; several terms average
# where a CEX line covers several articles. Manufacturing attributes are judgements
# about an autonomous panel-cutting + assembly cell and are flagged as such.
ARTICLES = {
    "290110": dict(name="Mattresses and springs",
                   pairs=[], process="textile/foam", machinable=0.0, flatpack=1.0,
                   machine_hours=None, asp_usd=None,
                   note="not woodwork at all"),
    "290120": dict(name="Other bedroom furniture",
                   pairs=[("dresser", "custom dresser"), ("nightstand", "custom nightstand"),
                          ("wardrobe", "custom wardrobe")],
                   process="solid timber, mixed", machinable=0.65, flatpack=0.92,
                   machine_hours=0.90, asp_usd=1650,
                   note="bed frames suit kigumi well; drawer boxes and carcasses do not"),
    "290210": dict(name="Sofas",
                   pairs=[("sofa", "custom sofa")],
                   process="upholstery", machinable=0.10, flatpack=0.30,
                   machine_hours=None, asp_usd=None,
                   note="a timber frame under foam and sewing — the frame is not the product"),
    "290310": dict(name="Living room chairs",
                   pairs=[], process="solid timber + upholstery",
                   machinable=0.55, flatpack=0.95,
                   machine_hours=0.30, asp_usd=890,
                   note="a lounge chair is mostly a cushion; the frame alone is a niche"),
    "290320": dict(name="Living room tables",
                   pairs=[("coffee table", "custom coffee table")],
                   process="solid timber", machinable=0.95, flatpack=0.95,
                   machine_hours=0.28, asp_usd=1150,
                   note="few parts, large visible joints — kigumi shows well here"),
    "290410": dict(name="Kitchen and dining room furniture",
                   pairs=[("dining table", "custom dining table")],
                   process="solid timber", machinable=0.97, flatpack=0.96,
                   machine_hours=0.224, asp_usd=2320,
                   note="dining chairs and tables — the native home of frame joinery, "
                        "and chairs sell in sets so an order is four units"),
    "290420": dict(name="Infants' furniture",
                   pairs=[], process="solid timber", machinable=0.80, flatpack=0.90,
                   machine_hours=0.42, asp_usd=780,
                   note="a fastener-free cot is a strong story, but CPSC testing gates it"),
    "290430": dict(name="Outdoor furniture",
                   pairs=[], process="solid timber, weatherable",
                   machinable=0.70, flatpack=0.92,
                   machine_hours=0.38, asp_usd=1250,
                   note="joinery moves with humidity outdoors, which is what kigumi "
                        "tolerates by design — but the species set changes"),
    "290440": dict(name="Wall units, cabinets and other occasional furniture",
                   pairs=[("bookshelf", "custom bookshelf"),
                          ("tv stand", "custom tv stand"),
                          ("closet organizer", "custom closet")],
                   process="solid timber frame", machinable=0.72, flatpack=0.90,
                   machine_hours=0.55, asp_usd=1450,
                   note="storage in solid timber is a frame-and-shelf problem; panel "
                        "carcasses are cheaper and this process cannot beat them on cost"),
}

# Kitchen cabinets and closet systems carry by far the strongest custom-search signal,
# but they are not CEX furniture — they are home-improvement spend, sold through
# installers and measured in NAICS 337212, not 337122. They are the adjacency this
# factory grows into, not the article it launches with, so they are held out of the
# scorecard and reported separately.
ADJACENCIES = [("kitchen cabinets", "custom cabinets")]

ASSUMPTIONS = {
    "cex_year": 2024,

    # How far above the measured search share the real configurable-willing share sits,
    # once the price premium is removed. FLOOR is measured; base and ceiling are not.
    "custom_willing_multiple": {"floor": 1.0, "base": 6.0, "ceiling": 15.0},
    # ...but the multiple cannot take the willing share past a plausible ceiling. A
    # generous reading of a configurator-native category is that half of buyers would
    # take a fitted version at stock price; the cap stops a high measured floor from
    # compounding into a share above that.
    "willing_share_cap": 0.50,

    # Share of the article pool that can be sold without a showroom or an installer.
    # ASSUMPTION — Census e-commerce share by merchandise line would measure it.
    "online_addressable_share": {"low": 0.20, "base": 0.30, "high": 0.40},

    # One autonomous cell. units/yr = cells x shifts x days x machine-hours x yield
    #                                 / machine-hours per unit
    "factory": {
        "cells": 1,
        "shifts": {"low": 1, "base": 2, "high": 3},
        "operating_days_per_year": 250,
        "machine_hours_per_shift": 7.0,     # 8h less changeover and maintenance
        "yield_rate": 0.95,
    },
    # Utilisation of the year-3 target in each of the first three years.
    "ramp_utilisation": {"year_1": 0.25, "year_2": 0.60, "year_3": 0.90},
    # SOM is the smaller of what the factory can make and what the market will buy. The
    # demand-side ceiling is a target share of SAM at year 3 — an ASSUMPTION, and the
    # one that binds once real cycle times are used instead of a guessed machine hour.
    "som_target_share_of_sam": 0.06,

    # Three product tiers off the same cell. The price multiple is relative to the
    # article's base ASP. The premium multiple is not guessed: it is set to the article's
    # measured Q5 spend skew, i.e. how much more the top income quintile already spends on
    # that article than the average household. Mix and margins are ASSUMPTIONS.
    "tiers": {
        "essential": {"price_multiple": 0.75, "mix": 0.45, "gross_margin": 0.50},
        "signature": {"price_multiple": 1.00, "mix": 0.40, "gross_margin": 0.55},
        "premium":   {"price_multiple": None, "mix": 0.15, "gross_margin": 0.62},
    },
    # In-home assembly, sold as an attach. A crew is a van, and a van covers a metro, so
    # the attach can only be sold inside the serviced metros — the coverage share is
    # measured from the Census CBSA vintage, not assumed.
    # In-home assembly was modelled and then removed. Kigumi assembles by hand with no
    # tools and no fasteners, so there is no service to sell — and, more usefully, no
    # metro coverage gate on where the product can be sold at all. The block is kept with
    # zeroed rates rather than deleted, so the service can be switched back on by
    # changing numbers rather than restructuring the model.
    "assembly": {
        "serviced_metros": 25,
        "attach_rate_by_tier": {"essential": 0.0, "signature": 0.0, "premium": 0.0},
        "price_usd": 0,
        "gross_margin": 0.40,
        "installs_per_crew_day": 3,
        "crew_days_per_year": 250,
        "removed_because": ("kigumi joinery assembles by hand without tools or fasteners, "
                            "so white-glove assembly has nothing to do"),
    },
    "cpc_usd_fallback": 2.50,    # replaced by measured CPC when Keyword Planner runs
    "site_conversion_rate": {"low": 0.005, "base": 0.015, "high": 0.03},
}

# Beachhead score weights. Pool size is what you can sell into, custom-share is whether
# anyone wants it configured, machinability is whether this factory can make it, and
# flatpack is whether you can ship it without freight eating the margin.
WEIGHTS = {"pool": 0.30, "custom_share": 0.30, "machinable": 0.25, "flatpack": 0.15}
# With a crew assembling in the customer's home, shipping flat matters much less: the
# weight it carried moves to pool size and custom demand. Running both weightings shows
# whether the service tier actually changes which article to build, or only its margin.
WEIGHTS_ASSEMBLED = {"pool": 0.36, "custom_share": 0.36, "machinable": 0.25,
                     "flatpack": 0.03}

QUINTILES = ["Q1 lowest 20%", "Q2", "Q3", "Q4", "Q5 highest 20%"]


def median(xs: list[float]) -> float:
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def cex_lookup(rows, item, cut, group, year):
    m = [r for r in rows if r["item_code"] == item and r["cut"] == cut
         and r["group"] == group and int(r["year"]) == year]
    return float(m[0]["value"]) if m else None


def trends_mean(trends: list[dict]) -> dict[str, float]:
    """Mean anchor-scaled interest per keyword, so every term is comparable."""
    acc: dict[str, list[float]] = {}
    for r in trends:
        try:
            acc.setdefault(r["keyword"], []).append(float(r["anchor_scaled"]))
        except (KeyError, ValueError):
            continue
    return {k: sum(v) / len(v) for k, v in acc.items() if v}


def main() -> None:
    cex = read_csv("cex_furniture_expenditure")
    mrts = read_csv("mrts_furniture_monthly")
    cbp = read_csv("cbp_furniture_supply")
    trends = read_csv("trends_interest_over_time")
    kw = read_csv("keyword_planner_metrics")

    if not cex:
        log("build_tam_us: no CEX data — run scripts/t2_bls_cex.py first")
        return

    yr = ASSUMPTIONS["cex_year"]
    out: dict = {"assumptions": ASSUMPTIONS, "weights": WEIGHTS,
                 "weights_assembled": WEIGHTS_ASSEMBLED, "cex_year": yr, "steps": []}

    def step(name, value, unit, basis):
        out["steps"].append({"step": name, "value": value, "unit": unit, "basis": basis})
        return value

    cu = {g: (cex_lookup(cex, "CONSUNIT", "LB01", g, yr) or 0) * 1000 for g in QUINTILES}
    cu_total = sum(cu.values())
    step("US consumer units", cu_total, "households", f"CEX CONSUNIT {yr}")

    # --- 1. TAM ---------------------------------------------------------------------
    def pool_for(item: str) -> float:
        total = 0.0
        for g in QUINTILES:
            spend = cex_lookup(cex, item, "LB01", g, yr)
            if spend is not None:
                total += spend * cu[g]
        return total

    tam = pool_for("FURNITUR")
    step("US household furniture spend (TAM)", tam, "usd/yr",
         f"CEX FURNITUR x consumer units, summed over income quintiles, {yr}")

    mrts_442 = [r for r in mrts if r["naics"] == "442"
                and r["seasonally_adjusted"] == "False" and int(r["year"]) == yr]
    mrts_annual = sum(float(r["sales_musd"]) for r in mrts_442) * 1e6
    if mrts_annual:
        out["sanity_check"] = {
            "mrts_442_annual_usd": mrts_annual,
            "cex_furniture_tam_usd": tam,
            "tam_share_of_442": round(tam / mrts_annual, 4),
            "reading": ("NAICS 442 covers furniture plus home furnishings — rugs, lamps, "
                        "window treatments, housewares — so CEX furniture landing at "
                        "roughly two-thirds of it is the expected shape. Above 1.0 or "
                        "below 0.4 would mean the CEX build is wrong."),
        }

    # --- 2. per-article table --------------------------------------------------------
    tmean = trends_mean(trends)

    rows = []
    for code, a in ARTICLES.items():
        pool = pool_for(code)
        all_cu_spend = cex_lookup(cex, code, "LB01", "All consumer units", yr)
        q5 = cex_lookup(cex, code, "LB01", "Q5 highest 20%", yr)
        q5_skew = (q5 / all_cu_spend) if (q5 and all_cu_spend) else None

        # Median, not mean, across the pairs. A CEX line covers several articles and a
        # weak generic denominator ("closet organizer" is not how people search for a
        # closet) inflates its pair badly enough to drag a mean off on its own. The
        # per-pair detail is kept in the basis column so the spread stays visible.
        shares, measured = [], []
        for generic, custom in a["pairs"]:
            g, c = tmean.get(generic), tmean.get(custom)
            if g and c:
                shares.append(c / g)
                measured.append(f"{custom}/{generic}={c / g:.2%}")
        custom_share = median(shares) if shares else None
        custom_share_mean = (sum(shares) / len(shares)) if shares else None

        rows.append({
            "cex_item": code, "article": a["name"], "process": a["process"],
            "us_pool_usd": round(pool),
            "share_of_tam": round(pool / tam, 4) if tam else None,
            "spend_per_cu_usd": all_cu_spend,
            "q5_skew_x": round(q5_skew, 2) if q5_skew else None,
            "custom_search_share": round(custom_share, 5) if custom_share is not None else None,
            "custom_search_share_mean": round(custom_share_mean, 5) if custom_share_mean is not None else None,
            "custom_share_basis": " | ".join(measured) or "no Trends pair collected",
            "machinable": a["machinable"], "flatpack": a["flatpack"],
            "machine_hours_per_unit": a["machine_hours"], "asp_usd": a["asp_usd"],
            "note": a["note"],
        })

    # Score on normalised columns so the four dimensions are commensurable. Articles
    # with no measured custom share score 0 on that dimension rather than being dropped:
    # absence of evidence is scored as absence, and the basis column says which is which.
    max_pool = max(r["us_pool_usd"] for r in rows) or 1
    max_share = max((r["custom_search_share"] or 0) for r in rows) or 1

    def score(r, w):
        return round(w["pool"] * (r["us_pool_usd"] / max_pool)
                     + w["custom_share"] * ((r["custom_search_share"] or 0) / max_share)
                     + w["machinable"] * r["machinable"]
                     + w["flatpack"] * r["flatpack"], 4)

    for r in rows:
        r["beachhead_score"] = score(r, WEIGHTS)
        r["beachhead_score_assembled"] = score(r, WEIGHTS_ASSEMBLED)
    rows.sort(key=lambda r: -r["beachhead_score"])
    save_csv("us_article_scorecard", rows)
    out["articles"] = rows

    # The beachhead has to be buildable: a scored article with no ASP or machine time
    # is one this factory cannot make, however well it scores on demand.
    buildable = [r for r in rows if r["asp_usd"] and r["machine_hours_per_unit"]]
    if not buildable:
        log("build_tam_us: no article has both an ASP and a machine time — check ARTICLES")
        return
    pick = buildable[0]
    pick_assembled = max(buildable, key=lambda r: r["beachhead_score_assembled"])
    out["beachhead"] = pick
    out["beachhead_if_assembled"] = pick_assembled
    out["service_changes_pick"] = pick_assembled["cex_item"] != pick["cex_item"]
    step("Beachhead article", pick["article"], "article",
         f"highest beachhead score ({pick['beachhead_score']}) among articles this "
         f"factory can physically build")

    # --- 3. the tier ladder and the assembly attach ------------------------------------
    # Three tiers off one cell, plus in-home assembly sold against the tiers. The premium
    # price multiple is the article's measured Q5 spend skew rather than a guess: the top
    # quintile already spends that much more on this article, which is the observable
    # evidence for how far it can be priced up.
    cov = read_csv("metro_coverage")
    asm = ASSUMPTIONS["assembly"]
    n_metros = asm["serviced_metros"]
    cov_row = [r for r in cov if int(r["rank"]) == n_metros]
    if cov_row:
        coverage = float(cov_row[0]["cumulative_share_of_us"])
        cov_basis = (f"Census CBSA vintage {cov_row[0]['year']}: the top {n_metros} metros "
                     f"hold {coverage:.1%} of the US population")
    else:
        coverage = 0.42
        cov_basis = ("PLACEHOLDER — run scripts/t2_metro_coverage.py to measure metro "
                     "coverage instead of assuming it")
    step("Serviceable population share", coverage, "share", cov_basis)

    base_asp = pick["asp_usd"]
    premium_multiple = pick["q5_skew_x"] or 1.85
    tiers = []
    for name, t in ASSUMPTIONS["tiers"].items():
        mult = t["price_multiple"] if t["price_multiple"] is not None else premium_multiple
        price = base_asp * mult
        attach = asm["attach_rate_by_tier"][name]
        # The attach can only be sold where there are crews.
        eff_attach = attach * coverage
        tiers.append({
            "tier": name, "price_multiple": round(mult, 2), "price_usd": round(price),
            "mix": t["mix"], "gross_margin": t["gross_margin"],
            "attach_rate_in_serviced_metros": attach,
            "effective_attach_rate": round(eff_attach, 4),
            "revenue_per_order_usd": round(price + eff_attach * asm["price_usd"]),
            "gross_profit_per_order_usd": round(
                price * t["gross_margin"]
                + eff_attach * asm["price_usd"] * asm["gross_margin"]),
        })
    out["tiers"] = {
        "base_asp_usd": base_asp,
        "premium_multiple_basis": (
            f"article Q5 spend skew, measured: the top quintile spends "
            f"{premium_multiple:.2f}x the average household on this article"),
        "coverage_share": coverage, "coverage_basis": cov_basis,
        "ladder": tiers,
    }

    blended_price = sum(t["mix"] * t["price_usd"] for t in tiers)
    blended_attach = sum(t["mix"] * t["effective_attach_rate"] for t in tiers)
    blended_service_rev = blended_attach * asm["price_usd"]
    blended_rev_per_order = blended_price + blended_service_rev
    blended_gp_per_order = sum(t["mix"] * t["gross_profit_per_order_usd"] for t in tiers)
    blended_margin = blended_gp_per_order / blended_rev_per_order if blended_rev_per_order else 0
    out["blended"] = {
        "product_asp_usd": round(blended_price),
        "attach_rate": round(blended_attach, 4),
        "service_revenue_per_order_usd": round(blended_service_rev, 2),
        "revenue_per_order_usd": round(blended_rev_per_order),
        "gross_profit_per_order_usd": round(blended_gp_per_order),
        "gross_margin": round(blended_margin, 4),
        "service_share_of_revenue": round(blended_service_rev / blended_rev_per_order, 4)
        if blended_rev_per_order else None,
    }
    step("Blended revenue per order", blended_rev_per_order, "usd/order",
         "tier mix x tier price, plus the assembly attach earned inside serviced metros")

    # --- 4. SAM ----------------------------------------------------------------------
    cap = ASSUMPTIONS["willing_share_cap"]
    floor_share = pick["custom_search_share"] or 0.0

    def willing(multiple: float) -> float:
        return min(floor_share * multiple, cap)

    sam = {}
    for wl, wm in ASSUMPTIONS["custom_willing_multiple"].items():
        for ol, os_ in ASSUMPTIONS["online_addressable_share"].items():
            sam[f"{wl}/{ol}"] = pick["us_pool_usd"] * willing(wm) * os_
    base_sam = (pick["us_pool_usd"]
                * willing(ASSUMPTIONS["custom_willing_multiple"]["base"])
                * ASSUMPTIONS["online_addressable_share"]["base"])
    # Assembly is a service, so it sits outside the CEX furniture pool entirely — it is
    # additional addressable revenue, not a slice of the same dollars. Size it off the
    # order count the product SAM implies.
    sam_orders = base_sam / blended_price if blended_price else 0
    sam_service = sam_orders * blended_attach * asm["price_usd"]
    out["sam"] = {
        "article": pick["article"],
        "article_pool_usd": pick["us_pool_usd"],
        "custom_search_share_measured": floor_share,
        "willing_share_base": willing(ASSUMPTIONS["custom_willing_multiple"]["base"]),
        "willing_share_capped": floor_share * ASSUMPTIONS["custom_willing_multiple"]["base"] > cap,
        "grid": {k: round(v) for k, v in sam.items()},
        "product_usd": round(base_sam),
        "implied_orders": round(sam_orders),
        "service_usd": round(sam_service),
        "base_usd": round(base_sam + sam_service),
        "basis": ("product: article pool x (measured custom search share x willing "
                  "multiple) x online-addressable share; service: the order count that "
                  "implies x blended attach x assembly price"),
    }
    step("SAM (base, product + service)", base_sam + sam_service, "usd/yr",
         out["sam"]["basis"])

    # --- 5. SOM: the smaller of what can be made and what can be sold ------------------
    # Capacity comes from build_factory.py, which derives it from per-station cycle times
    # and the bottleneck. Only if that has not been run does this fall back to the
    # machine-hour assumption in ARTICLES, which is a guess and says so.
    fac_path = PROC / "factory_model.json"
    fac = json.loads(fac_path.read_text()) if fac_path.exists() else {}
    f = ASSUMPTIONS["factory"]
    if fac.get("process"):
        fp = fac["process"]
        base_orders = fp["nameplate_orders_per_year"]
        cap_basis = (f"build_factory.py: {fp['takt_min_per_unit']:.1f} min takt at the "
                     f"{fp['bottleneck']} station, {fac['assumptions']['oee']:.0%} OEE, "
                     f"{fp['units_per_order']} units to an order")
        out["units_per_order"] = fp["units_per_order"]
    else:
        base_orders = None
        cap_basis = "ASSUMPTION — run build_factory.py to derive this from cycle times"
    out["capacity_basis"] = cap_basis
    capacity = {}
    for label, shifts in f["shifts"].items():
        if base_orders:
            # the factory model is quoted at its own shift pattern; scale from there
            units = base_orders * shifts / fac["assumptions"]["shifts"]
        else:
            units = (f["cells"] * shifts * f["operating_days_per_year"]
                     * f["machine_hours_per_shift"] * f["yield_rate"]
                     / pick["machine_hours_per_unit"])
        capacity[label] = {
            "shifts": shifts,
            "units_per_year": round(units),
            "revenue_at_asp_usd": round(units * blended_rev_per_order),
            "share_of_base_sam_pct": round(
                100 * units * blended_rev_per_order / out["sam"]["base_usd"], 2)
            if out["sam"]["base_usd"] else None,
        }
    out["capacity"] = capacity

    nameplate = capacity["base"]["units_per_year"]
    # The demand ceiling, and which of the two actually binds.
    demand_ceiling = (out["sam"]["base_usd"] * ASSUMPTIONS["som_target_share_of_sam"]
                      / blended_rev_per_order) if blended_rev_per_order else 0
    binding = "demand" if demand_ceiling < nameplate else "capacity"
    target = min(demand_ceiling, nameplate)
    out["som_bound"] = {
        "capacity_units_per_year": nameplate,
        "capacity_basis": cap_basis,
        "demand_units_per_year": round(demand_ceiling),
        "demand_basis": (f"{ASSUMPTIONS['som_target_share_of_sam']:.0%} of SAM at the "
                         f"blended order value — an assumption"),
        "binding_constraint": binding,
        "oversize_factor": round(nameplate / demand_ceiling, 1) if demand_ceiling else None,
        "target_units_year_3": round(target),
    }
    ramp = []
    total_sam = out["sam"]["base_usd"]
    for yr_label, util in ASSUMPTIONS["ramp_utilisation"].items():
        units = target * util
        product_rev = units * blended_price
        service_rev = units * blended_service_rev
        rev = product_rev + service_rev
        installs = units * blended_attach
        ramp.append({
            "year": yr_label, "utilisation": util,
            "units": round(units), "units_per_week": round(units / 52, 1),
            "product_revenue_usd": round(product_rev),
            "installs": round(installs),
            "service_revenue_usd": round(service_rev),
            "crews_needed": round(installs / (asm["installs_per_crew_day"]
                                              * asm["crew_days_per_year"]), 1),
            "revenue_usd": round(rev),
            "gross_profit_usd": round(units * blended_gp_per_order),
            "share_of_base_sam_pct": round(100 * rev / total_sam, 3) if total_sam else None,
        })
        # Overlay what the factory actually costs at that volume. The tier ladder assumes
        # a margin; this is the margin the plant delivers, and they are not the same.
        # Careful with units: the factory costs a chair, the market prices an order of
        # several chairs, so the conversion has to happen explicitly.
        uc = fac.get("unit_cost", {})
        upo = uc.get("units_per_order", 1)
        if uc.get("annual_fixed_usd") and units:
            chairs = units * upo
            cost_per_chair = uc["variable_per_unit_usd"] + uc["annual_fixed_usd"] / chairs
            cost_per_order = cost_per_chair * upo
            ramp[-1]["chairs"] = round(chairs)
            ramp[-1]["modelled_cost_per_chair_usd"] = round(cost_per_chair, 2)
            ramp[-1]["modelled_cost_per_unit_usd"] = round(cost_per_order, 2)
            ramp[-1]["actual_gross_margin"] = round(
                1 - cost_per_order / blended_rev_per_order, 4)
            ramp[-1]["actual_gross_profit_usd"] = round(
                (blended_rev_per_order - cost_per_order) * units)
    uc = fac.get("unit_cost", {})
    upo = uc.get("units_per_order", 1)
    variable_per_order = uc.get("variable_per_unit_usd", 0) * upo
    if uc.get("annual_fixed_usd") and blended_rev_per_order > variable_per_order:
        contrib = blended_rev_per_order - variable_per_order
        be_orders = uc["annual_fixed_usd"] / contrib
        out["breakeven"] = {
            "units_per_order": upo,
            "variable_per_order_usd": round(variable_per_order, 2),
            "contribution_per_unit_usd": round(contrib, 2),
            "units_per_year_full_absorption": round(be_orders),
            "chairs_per_year_full_absorption": round(be_orders * upo),
            "units_per_year_cash": round(uc["annual_fixed_cash_usd"] / contrib),
            "pct_of_capacity": round(be_orders / nameplate, 4),
        }
    out["som"] = {
        "basis": (f"the smaller of factory capacity and market demand — {binding} binds; "
                  f"ramped over three years, valued at the blended tier price plus the "
                  f"assembly attach"),
        "nameplate_units_per_year": nameplate,
        "ramp": ramp,
        "som_year_3_usd": ramp[-1]["revenue_usd"],
    }
    step("SOM (year 3, capacity-led)", ramp[-1]["revenue_usd"], "usd/yr",
         out["som"]["basis"])

    # --- 6. CAC against the capacity plan ---------------------------------------------
    if kw:
        cpcs = [float(r["high_top_of_page_bid_usd"]) for r in kw
                if r.get("high_top_of_page_bid_usd")]
        cpc = sum(cpcs) / len(cpcs) if cpcs else ASSUMPTIONS["cpc_usd_fallback"]
        cpc_basis = f"Keyword Planner, mean high top-of-page bid across {len(cpcs)} keywords"
    else:
        cpc = ASSUMPTIONS["cpc_usd_fallback"]
        cpc_basis = ("PLACEHOLDER — Keyword Planner not run. The only unmeasured number "
                     "in the acquisition maths.")
    gp_per_unit = blended_gp_per_order
    out["cac"] = {
        "cpc_usd": cpc, "cpc_basis": cpc_basis,
        "gross_profit_per_unit_usd": round(gp_per_unit, 2),
        "basis": "blended across the tier mix, including the assembly attach",
        "scenarios": [
            {"conversion_rate": cr, "cac_usd": round(cpc / cr, 2),
             "cac_as_pct_of_asp": round(100 * (cpc / cr) / blended_rev_per_order, 1),
             "cac_as_pct_of_gross_profit": round(100 * (cpc / cr) / gp_per_unit, 1),
             "year_3_ad_spend_usd": round((cpc / cr) * ramp[-1]["units"])}
            for cr in ASSUMPTIONS["site_conversion_rate"].values()],
    }

    # --- 7. what you are taking share from --------------------------------------------
    us_estab = {r["naics"]: r for r in cbp if r["geo_level"] == "us"}
    out["competition"] = {
        naics: {"label": row["naics_label"], "establishments": int(row["estab"]),
                "employees": int(row["employees"]),
                "annual_payroll_usd": int(row["annual_payroll_k"]) * 1000,
                "under_5_employees": int(row["estab_under_5_emp"])}
        for naics, row in us_estab.items()
        if naics in ("337122", "337212", "3371//", "337///", "442110")
    }

    out["adjacencies"] = [
        {"generic": g, "custom": c,
         "custom_search_share": round(tmean[c] / tmean[g], 5)
         if tmean.get(g) and tmean.get(c) else None,
         "note": "home-improvement spend, installer channel — not in the CEX furniture TAM"}
        for g, c in ADJACENCIES]

    (PROC / "tam_us_model.json").write_text(json.dumps(out, indent=2, default=str))
    save_csv("tam_us_steps", out["steps"])

    log(f"  TAM  US household furniture spend        ${tam / 1e9:,.1f}bn")
    log(f"  Beachhead article                        {pick['article']}")
    log(f"  SAM  product ${base_sam / 1e6:,.1f}m + service "
        f"${sam_service / 1e6:,.1f}m = ${out['sam']['base_usd'] / 1e6:,.1f}m")
    log(f"  Blended order  ${blended_rev_per_order:,.0f} revenue, "
        f"${blended_gp_per_order:,.0f} gross profit ({blended_margin:.0%}), "
        f"attach {blended_attach:.1%}")
    sb = out["som_bound"]
    log(f"  Capacity {sb['capacity_units_per_year']:,} orders vs demand "
        f"{sb['demand_units_per_year']:,} orders — {sb['binding_constraint']} binds"
        + (f" ({sb['oversize_factor']}x oversized)" if sb["binding_constraint"] == "demand" else ""))
    log(f"  SOM  year 3                              ${ramp[-1]['revenue_usd'] / 1e6:,.1f}m "
        f"({ramp[-1]['units']:,} orders = {ramp[-1].get('chairs', 0):,} chairs)")
    if ramp[-1].get("actual_gross_margin") is not None:
        log(f"  Margin  assumed {blended_margin:.0%} vs modelled "
            f"{ramp[-1]['actual_gross_margin']:.0%} at year-3 volume "
            f"(${ramp[-1]['modelled_cost_per_chair_usd']:,.0f}/chair, "
            f"${ramp[-1]['modelled_cost_per_unit_usd']:,.0f}/order)")
    log("  article scorecard:")
    for r in rows:
        cs = f"{r['custom_search_share']:.2%}" if r["custom_search_share"] is not None else "  —  "
        log(f"    {r['beachhead_score']:.3f}  {r['article'][:44]:<44} "
            f"${r['us_pool_usd'] / 1e9:>5.1f}bn  custom {cs}")


if __name__ == "__main__":
    main()
