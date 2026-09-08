"""Inspect every overlapping bounding-box pair for actual positive solid overlap.

Reports nominal threads and flexible-part contacts separately from unexpected
hard-part collisions. Run after editing geometry, before final export.
"""
import json
from itertools import combinations
from pathlib import Path
from instrument import make_instrument

parts = make_instrument()
boxes = {p.name: p.shape.bounding_box() for p in parts}
contacts = []
checked = 0
for a, b in combinations(parts, 2):
    ba, bb = boxes[a.name], boxes[b.name]
    if any(min(tuple(ba.max)[i], tuple(bb.max)[i]) - max(tuple(ba.min)[i], tuple(bb.min)[i]) < 1e-5 for i in range(3)):
        continue
    checked += 1
    common = a.shape & b.shape
    volume = common.volume if common is not None else 0
    if volume < 0.001:
        continue
    names = {a.name, b.name}
    reason = None
    if any(p.material == "silicone" for p in (a, b)) and any(p.name.startswith("fitting_") for p in (a, b)):
        reason = "Flexible tube interference over tapered barbs"
    elif any(p.name.startswith(("fitting_", "clamp_screw_", "lower_retainer_screw_", "pcb_screw_", "camera_cover_screw_")) for p in (a, b)) and any(p.name in ("01_flow_chamber", "02_filtrate_chamber", "11_led_heat_sink", "22_camera_housing") for p in (a, b)):
        reason = "Nominal male thread overlaps mating tap-drill envelope; female helix not modelled"
    elif any(p.name.startswith("led_dome_") for p in (a, b)) and any(p.name.startswith("led_ceramic_") for p in (a, b)):
        reason = "LED encapsulant seats 0.02 mm into its ceramic package"
    elif names == {"camera_id_plate", "22_camera_housing"}:
        reason = "Bonded label plate is seated into housing surface"
    elif names == {"19_focus_ring", "focus_lock_screw"}:
        reason = "Nominal focus-lock screw thread overlaps its tap-drill envelope"
    contact = {"a": a.name, "b": b.name, "intersection_mm3": round(volume, 6), "explanation": reason}
    contacts.append(contact)
    if not reason:
        print("REVIEW", contact, flush=True)
report = {"components": len(parts), "exact_boolean_checks": checked, "positive_contacts": contacts,
          "unexpected": [p for p in contacts if not p["explanation"]]}
Path(__file__).with_name("fit_audit.json").write_text(json.dumps(report, indent=2) + "\n")
print(f"Checked {checked} potential overlaps; {len(report['unexpected'])} need review.", flush=True)
