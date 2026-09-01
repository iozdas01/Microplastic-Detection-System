"""Cabinet cell: the panel factory, the process, and where labour actually goes.

The chair was solid timber and 5-axis joinery. A frameless kitchen cabinet is the
opposite: flat sheet goods, a nested router, an edgebander. The machining is nearly
commodity. The cost is somewhere else, and this model exists to show where.

Frameless / 32mm system. Doors and drawer fronts are BOUGHT IN for stage one --
that removes the entire finishing department, which is the largest capex and the
largest labour block in a conventional cabinet shop.
"""
from __future__ import annotations
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import PROC, log  # noqa: E402

A = {
    # ---- the product: one kitchen ----
    "linear_feet_per_kitchen": 27,      # US average kitchen, base + wall run
    "boxes_per_kitchen": 14,
    "price_per_linear_foot": 650,       # semi-custom / custom band
    "sheets_34_per_kitchen": 22,        # 3/4" ply or MFC, box parts
    "sheets_14_per_kitchen": 4,         # 1/4" backs
    "sheet_34_cost": 82.0,
    "sheet_14_cost": 38.0,
    "edgeband_cost_per_kitchen": 85.0,
    "hardware_cost_per_kitchen": 470.0,  # hinges, slides, connectors, pins
    "doors_bought_in_per_kitchen": 2800.0,
    "consumables_per_kitchen": 120.0,
    "packaging_per_kitchen": 140.0,
    "delivery_per_kitchen": 260.0,

    # ---- cycle times, minutes per kitchen ----
    # split machine vs human, because that is the whole argument
    "cycle": {
        "CNC nest, cut and bore":      {"machine": 264, "human": 55},
        "Edgeband":                    {"machine": 80,  "human": 60},
        "Box assembly":                {"machine": 0,   "human": 350},
        "Hardware — hinges and slides":{"machine": 0,   "human": 210},
        "QC and pack":                 {"machine": 0,   "human": 60},
    },
    # the kigumi idea, carried over: CNC-cut locking joints that snap together
    "locking_joint_assembly_min": 95,   # replaces 350 min of screwed assembly

    # ---- plant ----
    "capex": [
        ("Nested-base CNC router, ATC, vacuum table, drill block", 150000,
         "cuts and bores every box part from the sheet in one operation"),
        ("Automatic edgebander — premill, glue, trim, scrape, buff", 95000,
         "mandatory for frameless. The one machine with no cheap substitute."),
        ("Dust collection and compressor", 33000, ""),
        ("Case clamp and assembly benches", 22000, ""),
        ("Install, power, commissioning", 25000, ""),
        ("Sheet vacuum lifter and material racking", 16000, ""),
        ("Tooling, spoilboard, spares", 14000, ""),
        ("Pack and shipping station", 8000, ""),
        ("Software build — see the AI architecture", 120000,
         "intake, layout engine, quoting, CAD/CAM generation, shop scheduling"),
        ("Lease deposit and fit-out, 5,000 sqft", 45000, ""),
    ],
    "sqft": 5000,
    "lease_usd_per_sqft_yr": 11.0,
    "hourly_wage_loaded": 32.85,
    "software_per_year": 18000,
    "utilities_per_year": 14000,
    "maintenance_pct_of_equipment": 0.055,
    "insurance_pct_of_capex": 0.012,
    "equipment_life_years": 8,
    "operating_days_per_year": 250,
    "machine_hours_per_day_attended": 7.0,
    "human_hours_per_day": 7.5,
    "oee": 0.75,

    # ---- the front office, which is where cabinets actually burn money ----
    "designer_hours_per_kitchen_manual": 9.0,   # measure, layout, revisions, quote
    "engineering_hours_per_kitchen_manual": 4.5, # cut list, CNC programs, hardware sched
    "designer_wage_loaded": 52.0,
}


def main() -> None:
    price = A["linear_feet_per_kitchen"] * A["price_per_linear_foot"]
    mats = (A["sheets_34_per_kitchen"] * A["sheet_34_cost"]
            + A["sheets_14_per_kitchen"] * A["sheet_14_cost"]
            + A["edgeband_cost_per_kitchen"] + A["hardware_cost_per_kitchen"]
            + A["doors_bought_in_per_kitchen"] + A["consumables_per_kitchen"])
    variable = mats + A["packaging_per_kitchen"] + A["delivery_per_kitchen"]

    mach = sum(v["machine"] for v in A["cycle"].values())
    human = sum(v["human"] for v in A["cycle"].values())
    human_lock = human - A["cycle"]["Box assembly"]["human"] + A["locking_joint_assembly_min"]

    front_manual = A["designer_hours_per_kitchen_manual"] + A["engineering_hours_per_kitchen_manual"]

    capex_rows = [{"item": i, "usd": v, "note": n} for i, v, n in A["capex"]]
    capex_total = sum(r["usd"] for r in capex_rows)
    equipment = capex_total - 120000 - 45000

    # capacity: whichever binds
    mach_cap = int(A["operating_days_per_year"] * A["machine_hours_per_day_attended"]
                   * 60 * A["oee"] / mach)
    def people_cap(h, n): return int(A["operating_days_per_year"] * A["human_hours_per_day"] * 60 * n / h)

    fixed = {
        "lease": A["sqft"] * A["lease_usd_per_sqft_yr"],
        "software and cloud": A["software_per_year"],
        "utilities": A["utilities_per_year"],
        "maintenance and tooling": equipment * A["maintenance_pct_of_equipment"],
        "insurance": capex_total * A["insurance_pct_of_capex"],
        "equipment depreciation": equipment / A["equipment_life_years"],
    }

    out = {
        "assumptions": A,
        "product": {"price_per_kitchen": price, "linear_feet": A["linear_feet_per_kitchen"],
                    "boxes": A["boxes_per_kitchen"]},
        "materials": {"total_per_kitchen": round(mats, 2),
                      "doors_share_pct": round(100 * A["doors_bought_in_per_kitchen"] / mats, 1),
                      "variable_per_kitchen": round(variable, 2),
                      "material_pct_of_price": round(100 * variable / price, 1)},
        "time": {"machine_min": mach, "human_min_screwed": human,
                 "human_min_locking_joint": human_lock,
                 "human_hours_screwed": round(human / 60, 1),
                 "human_hours_locking": round(human_lock / 60, 1),
                 "front_office_hours_manual": front_manual,
                 "total_hours_manual": round(human / 60 + front_manual, 1)},
        "capacity": {"machine_bound_kitchens_yr": mach_cap,
                     "shopfloor_2p_screwed": people_cap(human, 2),
                     "shopfloor_2p_locking": people_cap(human_lock, 2),
                     "front_office_1p_manual": people_cap(front_manual * 60, 1)},
        "capex": {"rows": capex_rows, "total_usd": capex_total, "equipment_usd": equipment},
        "fixed": {k: round(v) for k, v in fixed.items()},
        "fixed_total": round(sum(fixed.values())),
    }
    (PROC / "cabinet_factory.json").write_text(json.dumps(out, indent=2))
    log("build_cabinet_factory: wrote cabinet_factory.json")

    print(f"\nONE KITCHEN — {A['linear_feet_per_kitchen']} linear ft, {A['boxes_per_kitchen']} boxes")
    print(f"   price            ${price:>9,.0f}")
    print(f"   variable cost    ${variable:>9,.0f}   ({out['materials']['material_pct_of_price']}% of price)")
    print(f"      of which bought-in doors ${A['doors_bought_in_per_kitchen']:,.0f} "
          f"= {out['materials']['doors_share_pct']}% of materials")
    print(f"   contribution     ${price-variable:>9,.0f}")

    print(f"\nWHERE THE TIME GOES, per kitchen")
    print(f"{'step':<34}{'machine':>9}{'human':>8}")
    for k, v in A["cycle"].items():
        print(f"   {k:<31}{v['machine']:>9}{v['human']:>8}")
    print(f"   {'SHOP FLOOR TOTAL (min)':<31}{mach:>9}{human:>8}")
    print(f"   {'design + engineering (min)':<31}{'—':>9}{front_manual*60:>8.0f}")
    print(f"   {'ALL-IN PER KITCHEN (hours)':<31}{mach/60:>9.1f}{human/60+front_manual:>8.1f}")

    print(f"\n   Front office is {100*front_manual/(human/60+front_manual):.0f}% of all human time.")
    print(f"   THIS is what AI removes — not the machine tending.")

    print(f"\nCAPACITY, kitchens/yr")
    print(f"   machines (CNC + bander)          {mach_cap:>5,}")
    print(f"   2 shop floor, screwed assembly   {people_cap(human,2):>5,}")
    print(f"   2 shop floor, locking joints     {people_cap(human_lock,2):>5,}")
    print(f"   1 designer, manual front office  {people_cap(front_manual*60,1):>5,}   <-- binds")

    print(f"\nCAPEX  ${capex_total:,}  (equipment ${equipment:,})")
    for r in capex_rows: print(f"   ${r['usd']:>7,}  {r['item']}")
    print(f"\nFIXED ${sum(fixed.values()):,.0f}/yr (before wages)")


if __name__ == "__main__":
    main()
