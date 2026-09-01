"""Stage-1 model: the cheapest plant that can make and ship the chair.

build_factory.py models the full autonomous cell. This models the version you start
with: one CNC, bought-in S4S timber, no robots, two people. Same chair, same BOM,
same joint count — only the plant around it changes.

Every capex line is marked `quoted` or `est`. Nothing here is quoted yet.
"""
from __future__ import annotations
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import PROC, ROOT, log  # noqa: E402

A = {
    # --- volume ---
    "chairs_per_week": 20,
    "operating_weeks": 52,
    "units_per_order": 4,

    # --- material: buy S4S, do not mill it ---
    # build_factory buys rough at $7.50/bf and mills it, losing 45% to yield.
    # Buying dimensioned stock moves that loss into the supplier's price.
    "finished_board_feet": 5.67,
    "s4s_usd_per_board_foot": 14.0,
    "s4s_waste_factor": 1.18,      # offcuts and defect skip still happen, just less
    "finish_per_unit": 5.20,
    "consumables_per_unit": 4.40,
    "packaging_per_unit": 18.00,
    "freight_per_unit": 28.00,

    # --- capex: one CNC, no robots, no lumber line ---
    "capex": [
        ("CNC router, 5x10, 4th-axis rotary", 90000, "est",
         "3-axis + indexer. Assumes joints redesigned off 5-axis - see the fork."),
        ("Cobot tending cell - arm, gripper, part fixturing, safety", 85000, "est",
         "this is the autonomy: the CNC runs unattended overnight. 3.2x the output "
         "of the same machine attended, for less than half the cost of a second one."),
        ("Dust collection and compressor", 18000, "est", ""),
        ("Wide-belt sander, used", 20000, "est", ""),
        ("Oil bench, cure racks, extraction", 12000, "est", ""),
        ("Pack bench, cartons, strapping", 6000, "est", ""),
        ("Tooling, fixtures, gauges", 15000, "est",
         "go/no-go gauges replace the $68k optical metrology at this volume"),
        ("Install, power, commissioning, robot integration", 18000, "est", ""),
        ("Configurator and parametric model", 40000, "est",
         "built, not bought; the demand test the market model asks for"),
        ("Lease deposit and fit-out, 2,500 sqft", 25000, "est", ""),
    ],

    # --- opex ---
    "sqft": 2500,
    "lease_usd_per_sqft_yr": 12.0,
    "hourly_wage_loaded": 32.85,   # BLS furniture production 2026-07, x1.31 burden
    "production_fte": 1.0,
    "founder_salary": 0,           # unpaid in stage 1; flagged in the doc
    "software_per_year": 4660,   # itemised in the plan: Shopify, Fusion+MFG, Xero, Workspace, hosting
    "utilities_per_year": 6000,
    "maintenance_pct_of_equipment": 0.055,
    "insurance_pct_of_capex": 0.012,
    "equipment_life_years": 8,

    # --- price: from the tier ladder in tam_us_model.json ---
    "blended_order_usd": 2532.25,
}

# handling minutes per chair, from the full model's station table
HANDLING_MIN = 12.9
MACHINE_MIN = 30.2


def main() -> None:
    n = A["chairs_per_week"] * A["operating_weeks"]

    timber = A["finished_board_feet"] * A["s4s_waste_factor"] * A["s4s_usd_per_board_foot"]
    variable = (timber + A["finish_per_unit"] + A["consumables_per_unit"]
                + A["packaging_per_unit"] + A["freight_per_unit"])

    capex_rows = [{"item": i, "usd": v, "basis": b, "note": nt} for i, v, b, nt in A["capex"]]
    capex_total = sum(r["usd"] for r in capex_rows)
    # equipment = everything except the configurator and the lease deposit
    equipment = capex_total - 40000 - 25000

    fixed = {
        "lease": A["sqft"] * A["lease_usd_per_sqft_yr"],
        "production labour": A["production_fte"] * 2000 * A["hourly_wage_loaded"],
        "founder salary": A["founder_salary"],
        "software": A["software_per_year"],
        "utilities": A["utilities_per_year"],
        "maintenance and tooling": equipment * A["maintenance_pct_of_equipment"],
        "insurance": capex_total * A["insurance_pct_of_capex"],
        "equipment depreciation": equipment / A["equipment_life_years"],
    }
    fixed_total = sum(fixed.values())
    fixed_cash = fixed_total - fixed["equipment depreciation"]

    price_per_chair = A["blended_order_usd"] / A["units_per_order"]
    cost_per_chair = variable + fixed_total / n
    revenue = n * price_per_chair
    gross = n * (price_per_chair - variable)
    operating = revenue - (n * variable) - fixed_total

    # capacity of one CNC: both joinery ops on one machine
    takt = (11.0 + 8.5 + 1.0 + 1.0) * 1.12   # both part families + handling + changeover
    # attended day shift + unattended night, made possible by the tending cobot
    cnc_capacity = int(250 * 20 * 0.80 * 60 / takt)      # lights-out
    cnc_attended = int(250 * 7 * 0.72 * 60 / takt)       # what the same machine does without it

    breakeven = fixed_total / (price_per_chair - variable)

    out = {
        "assumptions": A,
        "volume": {"chairs_per_year": n, "chairs_per_week": A["chairs_per_week"],
                   "orders_per_year": n // A["units_per_order"]},
        "capex": {"rows": capex_rows, "total_usd": capex_total,
                  "equipment_usd": equipment,
                  "all_lines_are_estimates": all(r["basis"] == "est" for r in capex_rows)},
        "unit": {"timber_usd": round(timber, 2), "variable_usd": round(variable, 2),
                 "fixed_per_chair_usd": round(fixed_total / n, 2),
                 "total_cost_usd": round(cost_per_chair, 2),
                 "price_usd": round(price_per_chair, 2),
                 "margin_pct": round(100 * (price_per_chair - cost_per_chair) / price_per_chair, 1)},
        "opex": {"annual": {k: round(v) for k, v in fixed.items()},
                 "annual_total": round(fixed_total), "annual_cash": round(fixed_cash)},
        "pnl": {"revenue_usd": round(revenue), "gross_profit_usd": round(gross),
                "gross_margin_pct": round(100 * gross / revenue, 1),
                "operating_profit_usd": round(operating)},
        "labour": {"handling_hours_per_year": round(n * HANDLING_MIN / 60),
                   "handling_fte": round(n * HANDLING_MIN / 60 / 2000, 2),
                   "machine_hours_per_year": round(n * MACHINE_MIN / 60)},
        "capacity": {"one_cnc_takt_min": round(takt, 1),
                     "attended_chairs_per_year": cnc_attended,
                     "lights_out_chairs_per_year": cnc_capacity,
                     "robot_multiple": round(cnc_capacity / cnc_attended, 1),
                     "headroom_x": round(cnc_capacity / n, 1),
                     "unattended_hours_per_year": 250 * 13,
                     "note": "the machining cell is autonomous; sanding, oiling, "
                             "test-fit and pack are attended on the day shift"},
        "breakeven_chairs_per_year": round(breakeven),
        "breakeven_chairs_per_week": round(breakeven / 52, 1),
    }
    p = PROC / "lean_factory.json"
    p.write_text(json.dumps(out, indent=2))
    log(f"build_lean_factory: wrote {p}")

    print(f"\nCAPEX  ${capex_total:,}   (equipment ${equipment:,})")
    for r in capex_rows:
        print(f"   ${r['usd']:>7,}  {r['item']}")
    print(f"\nUNIT ECONOMICS at {n:,} chairs/yr ({A['chairs_per_week']}/wk)")
    print(f"   price/chair       ${price_per_chair:>8,.0f}")
    print(f"   variable/chair    ${variable:>8,.2f}   (timber ${timber:.2f})")
    print(f"   fixed/chair       ${fixed_total/n:>8,.2f}")
    print(f"   total cost/chair  ${cost_per_chair:>8,.2f}")
    print(f"   margin            {out['unit']['margin_pct']:>8}%")
    print(f"\nANNUAL")
    print(f"   revenue           ${revenue:>10,.0f}")
    print(f"   gross profit      ${gross:>10,.0f}  ({out['pnl']['gross_margin_pct']}%)")
    print(f"   fixed costs       ${fixed_total:>10,.0f}")
    print(f"   operating profit  ${operating:>10,.0f}")
    print(f"\n   breakeven         {out['breakeven_chairs_per_week']} chairs/wk "
          f"({out['breakeven_chairs_per_year']:,}/yr)")
    print(f"   one CNC attended  {cnc_attended:,}/yr")
    print(f"   with the cobot    {cnc_capacity:,}/yr  ({out['capacity']['robot_multiple']}x, "
          f"{out['capacity']['headroom_x']}x demand headroom)")
    print(f"   human handling    {out['labour']['handling_hours_per_year']} h/yr "
          f"= {out['labour']['handling_fte']} FTE")
    print("\nFIXED COST DETAIL")
    for k, v in sorted(fixed.items(), key=lambda x: -x[1]):
        if v: print(f"   ${v:>9,.0f}  {k}")


if __name__ == "__main__":
    main()
