"""The factory: a solid-timber kigumi cell — bill of materials, cycle times, capex, opex.

The article is a chair joined with Japanese kigumi joinery: interlocking tsugite and
shiguchi geometry, tapered wedges under compression, no screws, no cams, no glue. That
choice drives everything downstream:

  * Solid hardwood, not sheet goods. There is no nesting router and no edgebander here —
    the machines are a lumber line and 5-axis machining centres.
  * 0.1-0.2 mm joint tolerance, which is a moisture-control problem before it is a
    machining problem. The kiln and the conditioning room are load-bearing capex.
  * Nothing is assembled in the factory. Parts are machined, finished, test-fitted and
    flat-packed; the customer assembles by hand, which is the product story rather than
    a cost we carry.
  * Robots move parts between machining centres. That is what makes the cell autonomous —
    not robotic assembly, which nobody can do reliably across a varying part mix.

    1. Product    a bill of materials in board feet of rough hardwood
    2. Process    per-station cycle times, the bottleneck, and derived capacity
    3. Equipment  a named machine list, phased
    4. Facility   land and three-phase power are owned; the shell is not
    5. Opex       headcount at the BLS measured production wage, power, consumables
    6. Unit cost  a cost curve as a function of volume, priced downstream

Equipment prices are indicative and quote-driven. Each carries a `basis` string, and
data/reference/equipment.csv is written out so real quotes can replace the whole list
without touching this file.
"""
from __future__ import annotations

import csv as _csv
import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from common import PROC, ROOT, log, read_csv, record, save_csv  # noqa: E402

# --------------------------------------------------------------------------- product
# A dining chair in white oak. Dimensions are finished sizes in millimetres; rough stock
# is recovered from them by the yield factor below, which is where most of the timber
# cost actually sits.
PARTS = [
    # name,                qty, length, width, thickness, joinery ops
    ("rear leg / stile",     2,  950,  90, 28, 4),
    ("front leg",            2,  440,  42, 42, 3),
    ("side rail",            2,  400,  70, 25, 2),
    ("front rail",           1,  420,  70, 25, 2),
    ("back rail",            1,  380,  70, 25, 2),
    ("crest rail",           1,  400,  80, 30, 3),
    ("back slat",            2,  300,  60, 16, 2),
    ("seat slat",            5,  420,  70, 18, 2),
    ("locking wedge / key",  8,   60,  12,  8, 1),
]
BF_PER_M3 = 423.776

ASSUMPTIONS = {
    # --- materials (USD) -----------------------------------------------------------
    "species": "white oak, FAS, kiln dried",
    "timber_usd_per_board_foot": 7.50,
    "rough_to_finished_yield": 0.55,   # rough board foot -> finished part
    "finish_per_unit": 5.20,           # hardwax oil, applied and cured
    "consumables_per_unit": 4.40,      # tooling wear, abrasives, labels
    "hardware_cost_per_unit": 0.0,     # kigumi: there is no hardware, by design
    "packaging_per_unit": 18.0,
    "freight_per_unit": 28.0,          # flat-packed parts, per chair
    "scrap_rate": 0.05,                # tighter tolerance, so a higher reject rate

    # --- the order --------------------------------------------------------------------
    # Chairs sell in sets. Capacity is counted in chairs; the market model prices orders.
    "units_per_order": 4,

    # --- what happens after the parts are cut ------------------------------------------
    # Three ways to finish the job, costed side by side. "customer" is the plan of record.
    # The robotic options are here because a robot-assembly foundation model makes them a
    # live question, and the honest way to answer it is to price it, not to argue about it.
    "assembly_mode": "customer",

    # --- process, minutes per unit at each station ---------------------------------
    # Handling is low at the machining centres because a robot loads them; it is not zero
    # because fixturing and first-off checks still take a person some of the time.
    "cycle_minutes": {
        "timber prep — crosscut, rip, moulder":      {"machine": 3.2, "handling": 1.4},
        "5-axis joinery — legs and stiles":          {"machine": 11.0, "handling": 1.0},
        "5-axis joinery — rails, slats and keys":    {"machine": 8.5, "handling": 1.0},
        "sanding and surface prep":                  {"machine": 4.5, "handling": 1.8},
        "finishing — oil and cure":                  {"machine": 3.0, "handling": 2.2},
        "QC, joint test-fit and flat-pack":          {"machine": 0.0, "handling": 5.5},
    },
    "changeover_allowance": 0.12,
    "oee": 0.72,

    "shifts": 2,
    "machine_hours_per_shift": 7.0,
    "operating_days_per_year": 250,

    # --- facility --------------------------------------------------------------------
    "building_sqft": 16000,            # timber storage and conditioning need the space
    "building_cost_per_sqft": {"fit_out_existing": 34.0, "new_pemb_turnkey": 118.0},
    "building_scenario": "new_pemb_turnkey",
    "land_cost": 0.0,
    "power_connection_cost": 0.0,

    # --- opex -------------------------------------------------------------------------
    "headcount": {
        "lumber line operator": 1, "CNC cell operator": 1,
        "finishing": 1, "QC and pack": 1, "production engineer / CAM": 1,
    },
    "wage_burden": 1.31,
    "salaried_roles": {"production engineer / CAM": 98000},
    "connected_load_kw": 210,          # 5-axis spindles, extraction, kiln
    "load_duty_factor": 0.58,
    "electricity_usd_per_kwh": 0.089,
    "maintenance_pct_of_equipment": 0.055,   # 5-axis and tooling are harder on spares
    "software_subscription_per_year": 44000,
    "insurance_pct_of_capex": 0.012,
    "equipment_life_years": 8,
    "building_life_years": 25,
}

# Each mode adds a station, changes freight and packaging, and adds capital. Flat-packed
# parts ship in roughly a sixth of the volume of an assembled chair, which is where the
# freight numbers come from.
ASSEMBLY_MODES = {
    "customer": dict(
        label="Customer assembles by hand",
        station=None, capex=0, freight=28.0, packaging=18.0, scrap_delta=0.0,
        note="flat-packed parts; kigumi needs no tools, so the customer does the work"),
    "robotic_ship_assembled": dict(
        label="Robot assembles in the factory, ship assembled",
        station=("robotic assembly and wedge seating", 7.5, 2.0),
        capex=420_000, freight=124.0, packaging=46.0, scrap_delta=0.03,
        note="an assembled chair is roughly six times the shipping volume of its parts, "
             "and the robot has to seat tapered joints under load"),
    "robotic_test_fit": dict(
        label="Robot test-fits every chair, then flat-packs",
        station=("robotic test-fit and disassembly", 4.5, 1.0),
        capex=340_000, freight=28.0, packaging=18.0, scrap_delta=-0.015,
        note="the robot proves the joints fit and takes the chair apart again; ships flat, "
             "and catches the one defect this product actually has"),
}

# --------------------------------------------------------------------------- equipment
EQUIPMENT = [
    (1, "Timber", "Weinig OptiCut-class optimising crosscut with scanning", 1, 178_000,
     "indicative; defect-skip optimisation is what protects the timber yield"),
    (1, "Timber", "Straight-line / gang rip saw", 1, 118_000, "indicative"),
    (1, "Timber", "Four-side moulder, Weinig Powermat-class, to S4S blanks", 1, 224_000,
     "indicative"),
    (1, "Timber", "Dehumidification kiln and conditioning room, 6% MC control", 1, 142_000,
     "kigumi needs 0.1-0.2mm stability; this is a tolerance item, not a nicety"),
    (1, "Machining", "5-axis CNC machining centre — legs and stiles "
        "(SCM Accord / HOMAG CENTATEQ P-310 class)", 1, 395_000,
     "5-axis is required for tsugite and shiguchi geometry"),
    (1, "Machining", "5-axis CNC machining centre — rails, slats and keys", 1, 395_000,
     "second centre so fixtures need not change between part families"),
    (1, "Robotics", "6-axis robot transfer cell with vision part ID, between "
        "machining centres", 1, 188_000,
     "this is the autonomy: parts move machine to machine without a person"),
    (1, "Robotics", "Robot load/unload gantry for the lumber line to CNC handoff",
     1, 146_000, "indicative"),
    (1, "Finishing", "Wide-belt sander and profile sanding", 1, 96_000, "indicative"),
    (1, "Finishing", "Oil application booth, cure racks and extraction", 1, 158_000,
     "indicative"),
    (1, "Quality", "Optical joint metrology — first-off and SPC on joint fit", 1, 68_000,
     "the joint is the product; measuring it cannot be optional"),
    (1, "Services", "Dust and chip extraction, silo and briquetting", 1, 98_000,
     "solid timber makes far more waste volume than panel work"),
    (1, "Services", "Compressor, dryer and ring main", 1, 28_000, "indicative"),
    (1, "Packing", "Carton erector, part-kitting station, strapping and labelling",
     1, 72_000, "no assembly line — this is the last station in the plant"),
    (1, "Software", "5-axis CAM, joint parametrics, nesting and MES licences", 1, 145_000,
     "perpetual plus first year; subscription carried in opex"),
    (1, "Software", "Customer-facing configurator build and integration", 1, 150_000,
     "the demand-side experiment the market model asks for"),
    (1, "Install", "Rigging, power distribution, air, commissioning and training",
     1, 212_000, "typically 8-12% of equipment value"),
    (1, "Facility", "Timber racking, floor prep, tooling and spares package", 1, 82_000,
     "indicative"),

    (2, "Robotics", "Robotic sanding cell with force-compliant end effector", 1, 214_000,
     "phase 2 — removes the second-largest manual station"),
    (2, "Robotics", "AMR fleet for inter-station and finished-goods transport", 1, 124_000,
     "phase 2"),
    (2, "Finishing", "Automated oil line with inline cure", 1, 186_000, "phase 2"),

    (3, "Timber", "Automated rough-mill grading, scanning and infeed", 1, 340_000,
     "phase 3 — the last manual touch on the timber side"),
    (3, "Packing", "Automated kitting and carton pack cell", 1, 265_000, "phase 3"),
]


def latest(prices, label_prefix):
    ser = sorted([r for r in prices if r["label"].startswith(label_prefix)],
                 key=lambda r: r["period"])
    return (float(ser[-1]["value"]), ser[-1]["period"]) if ser else (None, None)


def main() -> None:
    prices = read_csv("bls_prices")
    A = ASSUMPTIONS
    out: dict = {"assumptions": A, "notes": [],
                 "method": "solid timber, kigumi joinery, no fasteners, no factory assembly"}

    # ---------------------------------------------------------------- 1. bill of materials
    finished_m3 = 0.0
    joinery_ops = 0
    part_rows = []
    for name, qty, ln, wd, th, ops in PARTS:
        vol = qty * (ln / 1000) * (wd / 1000) * (th / 1000)
        finished_m3 += vol
        joinery_ops += qty * ops
        part_rows.append({"part": name, "qty": qty, "length_mm": ln, "width_mm": wd,
                          "thickness_mm": th, "joinery_ops": qty * ops,
                          "finished_bf": round(vol * BF_PER_M3, 3)})
    save_csv("factory_bom", part_rows)

    finished_bf = finished_m3 * BF_PER_M3
    rough_bf = finished_bf / A["rough_to_finished_yield"]
    timber = rough_bf * A["timber_usd_per_board_foot"]
    _mode = ASSEMBLY_MODES[A["assembly_mode"]]
    material = (timber + A["finish_per_unit"] + A["consumables_per_unit"]
                + A["hardware_cost_per_unit"]) * (1 + A["scrap_rate"]
                                                  + _mode["scrap_delta"])
    out["materials"] = {
        "species": A["species"],
        "finished_board_feet": round(finished_bf, 2),
        "rough_board_feet": round(rough_bf, 2),
        "yield": A["rough_to_finished_yield"],
        "joinery_operations_per_unit": joinery_ops,
        "rows": [
            {"item": f"rough {A['species']}", "qty": round(rough_bf, 2),
             "cost_usd": round(timber, 2)},
            {"item": "finish (hardwax oil)", "qty": None, "cost_usd": A["finish_per_unit"]},
            {"item": "consumables and tooling", "qty": None,
             "cost_usd": A["consumables_per_unit"]},
            {"item": "hardware", "qty": 0, "cost_usd": 0.0},
        ],
        "total_per_unit_usd": round(material, 2),
        "note": ("There is no hardware line because kigumi has no fasteners. The timber "
                 "yield does the damage instead: rough stock is "
                 f"{rough_bf / finished_bf:.2f}x the finished volume."),
    }

    # ---------------------------------------------------------------- 2. process
    mode = ASSEMBLY_MODES[A["assembly_mode"]]
    cycles = dict(A["cycle_minutes"])
    if mode["station"]:
        nm, mach, hand = mode["station"]
        cycles[nm] = {"machine": mach, "handling": hand}
    stations = []
    for name, c in cycles.items():
        total = (c["machine"] + c["handling"]) * (1 + A["changeover_allowance"])
        stations.append({"station": name, "machine_min": c["machine"],
                         "handling_min": c["handling"],
                         "cycle_min_per_unit": round(total, 2),
                         "is_machine_station": c["machine"] > 0})
    bottleneck = max(stations, key=lambda s: s["cycle_min_per_unit"])
    takt = bottleneck["cycle_min_per_unit"]
    hours = A["shifts"] * A["machine_hours_per_shift"] * A["operating_days_per_year"]
    nameplate = hours * 60 / takt * A["oee"]
    for s in stations:
        s["utilisation_at_takt"] = round(s["cycle_min_per_unit"] / takt, 3)
    save_csv("factory_stations", stations)
    out["process"] = {
        "stations": stations, "bottleneck": bottleneck["station"],
        "takt_min_per_unit": round(takt, 2),
        "machine_hours_per_year": hours,
        "nameplate_units_per_year": round(nameplate),
        "units_per_order": A["units_per_order"],
        "nameplate_orders_per_year": round(nameplate / A["units_per_order"]),
        "units_per_shift": round(nameplate / (A["operating_days_per_year"] * A["shifts"])),
        "basis": (f"{A['shifts']} shifts x {A['machine_hours_per_shift']}h x "
                  f"{A['operating_days_per_year']} days at {A['oee']:.0%} OEE, "
                  f"gated by the slowest station"),
        "note": ("No assembly station exists. The plant machines, finishes, test-fits and "
                 "flat-packs; the customer assembles by hand."),
    }

    # ---------------------------------------------------------------- 3. equipment
    eq_rows = [{"phase": p, "category": c, "item": it, "qty": q,
                "unit_cost_usd": u, "total_usd": q * u, "basis": b}
               for p, c, it, q, u, b in EQUIPMENT]
    save_csv("factory_equipment", eq_rows)
    ref = ROOT / "data" / "reference"
    ref.mkdir(parents=True, exist_ok=True)
    with (ref / "equipment.csv").open("w", newline="") as fh:
        w = _csv.DictWriter(fh, fieldnames=list(eq_rows[0]))
        w.writeheader()
        w.writerows(eq_rows)
    by_phase: dict[int, float] = {}
    for r in eq_rows:
        by_phase[r["phase"]] = by_phase.get(r["phase"], 0.0) + r["total_usd"]
    equipment_p1 = by_phase.get(1, 0.0) + mode["capex"]
    if mode["capex"]:
        eq_rows.append({"phase": 1, "category": "Robotics", "item": mode["label"],
                        "qty": 1, "unit_cost_usd": mode["capex"],
                        "total_usd": mode["capex"],
                        "basis": "assembly-mode scenario; see assembly_scenarios"})

    # ---------------------------------------------------------------- 4. facility
    scen = A["building_scenario"]
    rate = A["building_cost_per_sqft"][scen]
    building = A["building_sqft"] * rate
    out["facility"] = {
        "building_sqft": A["building_sqft"], "scenario": scen,
        "cost_per_sqft": rate, "building_cost_usd": round(building),
        "land_cost_usd": A["land_cost"],
        "power_connection_cost_usd": A["power_connection_cost"],
        "alternatives": {k: round(A["building_sqft"] * v)
                         for k, v in A["building_cost_per_sqft"].items()},
        "note": ("Land and three-phase service are owned, so both are zero. Solid timber "
                 "needs more building than panel work: rough stock, the kiln and the "
                 "conditioning room all take floor before a single part is cut."),
    }
    capex_p1 = equipment_p1 + building

    # ---------------------------------------------------------------- 5. opex
    wage, wage_period = latest(prices, "Average hourly earnings, production employees")
    if wage is None:
        wage, wage_period = 25.08, "assumed"
        out["notes"].append("wage series missing — using a fallback rate")
    loaded = wage * A["wage_burden"]
    hourly_heads = {k: v for k, v in A["headcount"].items()
                    if k not in A["salaried_roles"]}
    hourly_fte = sum(hourly_heads.values()) * A["shifts"]
    direct_labour = hourly_fte * loaded * A["machine_hours_per_shift"] \
        * A["operating_days_per_year"]
    salaries = sum(A["salaried_roles"][k] * v for k, v in A["headcount"].items()
                   if k in A["salaried_roles"]) * A["wage_burden"]
    kwh = A["connected_load_kw"] * A["load_duty_factor"] * hours
    power = kwh * A["electricity_usd_per_kwh"]
    fixed = {
        "direct labour (hourly, loaded)": direct_labour,
        "salaried": salaries,
        "electricity": power,
        "maintenance, tooling and spares": equipment_p1 * A["maintenance_pct_of_equipment"],
        "software subscription": A["software_subscription_per_year"],
        "insurance": capex_p1 * A["insurance_pct_of_capex"],
        "equipment depreciation": equipment_p1 / A["equipment_life_years"],
        "building depreciation": building / A["building_life_years"],
    }
    out["opex"] = {
        "wage_basis": (f"BLS average hourly earnings, furniture production employees, "
                       f"{wage_period}: ${wage:,.2f}/h, loaded to ${loaded:,.2f} at "
                       f"{A['wage_burden']:.2f}x"),
        "hourly_fte": hourly_fte, "kwh_per_year": round(kwh),
        "annual": {k: round(v) for k, v in fixed.items()},
        "annual_total": round(sum(fixed.values())),
    }

    # ---------------------------------------------------------------- 6. unit cost
    variable = material + mode["packaging"] + mode["freight"]
    annual_fixed = sum(fixed.values())

    def unit_cost_at(volume: float) -> dict:
        return {"units": round(volume),
                "orders": round(volume / A["units_per_order"]),
                "variable_per_unit": round(variable, 2),
                "fixed_per_unit": round(annual_fixed / volume, 2) if volume else 0,
                "total_per_unit": round(variable + annual_fixed / volume, 2)
                if volume else 0}

    volumes = [2000, 4000, 6000, 8000, 12000, 16000, nameplate]
    curve = [unit_cost_at(v) for v in sorted(set(round(v) for v in volumes))]
    out["unit_cost"] = {
        "variable_breakdown": {
            "timber and finish": round(material, 2),
            "packaging": A["packaging_per_unit"],
            "freight": A["freight_per_unit"],
        },
        "curve": curve,
        "variable_per_unit_usd": round(variable, 2),
        "annual_fixed_usd": round(annual_fixed),
        "annual_fixed_cash_usd": round(annual_fixed - fixed["equipment depreciation"]
                                       - fixed["building depreciation"]),
        "units_per_order": A["units_per_order"],
        "basis": ("unit cost is per chair and full-absorption: it carries depreciation on "
                  "both the equipment and the building. annual_fixed_cash_usd strips "
                  "depreciation out, and is the number that matters for runway."),
    }

    # --------------------------------------------------------- assembly-mode comparison
    scen = []
    base_equipment = by_phase.get(1, 0.0) - mode["capex"] if mode["capex"] else by_phase.get(1, 0.0)
    for key, m in ASSEMBLY_MODES.items():
        cyc = dict(A["cycle_minutes"])
        if m["station"]:
            nm, mach, hand = m["station"]
            cyc[nm] = {"machine": mach, "handling": hand}
        takt_m = max((c["machine"] + c["handling"]) * (1 + A["changeover_allowance"])
                     for c in cyc.values())
        cap_m = hours * 60 / takt_m * A["oee"]
        mat_m = (timber + A["finish_per_unit"] + A["consumables_per_unit"]) \
            * (1 + A["scrap_rate"] + m["scrap_delta"])
        var_m = mat_m + m["packaging"] + m["freight"]
        eq_m = base_equipment + m["capex"]
        capex_m = eq_m + building
        fixed_m = (annual_fixed
                   - equipment_p1 * A["maintenance_pct_of_equipment"]
                   - capex_p1 * A["insurance_pct_of_capex"]
                   - equipment_p1 / A["equipment_life_years"]
                   + eq_m * A["maintenance_pct_of_equipment"]
                   + capex_m * A["insurance_pct_of_capex"]
                   + eq_m / A["equipment_life_years"])
        scen.append({
            "mode": key, "label": m["label"], "note": m["note"],
            "takt_min": round(takt_m, 2),
            "nameplate_units_per_year": round(cap_m),
            "variable_per_unit_usd": round(var_m, 2),
            "freight_per_unit_usd": m["freight"],
            "added_capex_usd": m["capex"],
            "phase_1_capex_usd": round(capex_m),
            "annual_fixed_usd": round(fixed_m),
            "cost_per_unit_at_4500": round(var_m + fixed_m / 4500, 2),
            "selected": key == A["assembly_mode"],
        })
    out["assembly_scenarios"] = scen
    out["assembly_mode"] = {"selected": A["assembly_mode"], "label": mode["label"],
                            "note": mode["note"]}

    out["capital_plan"] = {
        "phase_1_equipment_usd": round(equipment_p1),
        "phase_1_building_usd": round(building),
        "phase_1_total_usd": round(capex_p1),
        "phase_2_usd": round(by_phase.get(2, 0)),
        "phase_3_usd": round(by_phase.get(3, 0)),
        "all_phases_usd": round(capex_p1 + by_phase.get(2, 0) + by_phase.get(3, 0)),
    }

    (PROC / "factory_model.json").write_text(json.dumps(out, indent=2, default=str))
    record("analysis", "factory-model", "scripts/build_factory.py", len(eq_rows),
           note=f"kigumi solid-timber cell; phase-1 capex ${capex_p1:,.0f}, "
                f"nameplate {nameplate:,.0f} chairs/yr")

    log(f"  Timber            {rough_bf:,.1f} rough bf/chair "
        f"({finished_bf:,.1f} finished, {A['rough_to_finished_yield']:.0%} yield)")
    log(f"  Materials         ${material:,.2f}/chair — no hardware, {joinery_ops} joinery ops")
    log(f"  Bottleneck        {bottleneck['station']} at {takt:.1f} min")
    log(f"  Nameplate         {nameplate:,.0f} chairs/yr "
        f"({out['process']['nameplate_orders_per_year']:,} orders of "
        f"{A['units_per_order']})")
    log(f"  Phase-1 capex     ${capex_p1:,.0f} "
        f"(equipment ${equipment_p1:,.0f} + building ${building:,.0f})")
    log(f"  Annual fixed      ${annual_fixed:,.0f}")
    log(f"  Variable          ${variable:,.2f}/chair")
    for r in curve:
        log(f"    {r['units']:>7,} chairs  ${r['total_per_unit']:>8,.0f}/chair")
    log("  assembly modes, cost per chair at 4,500/yr:")
    for sc in scen:
        mark = "*" if sc["selected"] else " "
        log(f"   {mark} {sc['label'][:44]:<44} ${sc['cost_per_unit_at_4500']:>7,.0f}"
            f"  takt {sc['takt_min']:>5.1f}  cap {sc['nameplate_units_per_year']:>6,}"
            f"  capex ${sc['phase_1_capex_usd']:>10,.0f}")


if __name__ == "__main__":
    main()
