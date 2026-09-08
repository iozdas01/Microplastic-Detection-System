"""Generate the three review assemblies and validate the actual B-rep geometry."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import struct
import time

from build123d import export_gltf, export_step
from instrument import (
    MATERIALS, P, SCREW_LENGTH, WASHER_T, WINDOW_PAD_T, Z_LED,
    assembly, cutaway_parts, make_instrument,
)

ROOT = Path(__file__).resolve().parent


def finish_glb(path, component_lookup):
    """Preserve node identities and physical materials in the portable GLB.

    OCCT can give repeated fastener meshes the final occurrence's name. Each
    exported node already has the correct name; mirror it onto its mesh.
    """
    data = path.read_bytes()
    length, kind = struct.unpack_from("<II", data, 12)
    document = json.loads(data[20:20 + length])
    rest = data[20 + length:]
    materials = []
    material_ids = {}
    extensions = set(document.get("extensionsUsed", []))
    for name, spec in MATERIALS.items():
        def linear_color(value):
            rgb = [int(value.lstrip("#")[i:i+2], 16) / 255 for i in (0, 2, 4)]
            return [v / 12.92 if v < 0.04045 else ((v + 0.055) / 1.055)**2.4 for v in rgb]
        material = {"name": name, "doubleSided": True, "pbrMetallicRoughness": {
            "baseColorFactor": linear_color(spec["color"]) + [1],
            "metallicFactor": spec.get("metalness", 0),
            "roughnessFactor": spec.get("roughness", 0.3),
        }}
        if "transmission" in spec:
            material["extensions"] = {
                "KHR_materials_transmission": {"transmissionFactor": spec["transmission"]},
                "KHR_materials_ior": {"ior": spec.get("ior", 1.46)},
            }
        if "emissive" in spec:
            material["emissiveFactor"] = linear_color(spec["emissive"])
            material.setdefault("extensions", {})["KHR_materials_emissive_strength"] = {
                "emissiveStrength": spec.get("emissiveIntensity", 1)
            }
        extensions.update(material.get("extensions", {}))
        material_ids[name] = len(materials)
        materials.append(material)
    document["materials"] = materials
    document["extensionsUsed"] = sorted(extensions)
    for node in document["nodes"]:
        if "mesh" not in node:
            continue
        mesh = document["meshes"][node["mesh"]]
        mesh["name"] = node["name"]
        component = component_lookup[node["name"]]
        node["extras"] = {"cad_component": component.name, "group": component.group,
                          "explode_mm": list(component.explode)}
        for primitive in mesh["primitives"]:
            primitive["material"] = material_ids[component.material]
    payload = json.dumps(document, separators=(",", ":")).encode()
    payload += b" " * (-len(payload) % 4)
    path.write_bytes(struct.pack("<III", 0x46546C67, 2, 20 + len(payload) + len(rest)) +
                     struct.pack("<II", len(payload), kind) + payload + rest)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assembled-only", action="store_true")
    parser.add_argument("--skip-step", action="store_true")
    args = parser.parse_args()
    start = time.monotonic()
    print("Building detailed instrument…", flush=True)
    parts = make_instrument()
    print(f"Built {len(parts)} individually named components in {time.monotonic() - start:.1f}s", flush=True)

    errors = []
    records = []
    by_name = {p.name: p for p in parts}
    for p in parts:
        if not p.shape.is_valid:
            errors.append(f"Invalid B-rep: {p.name}")
        if p.shape.volume <= 1e-7:
            errors.append(f"Non-positive volume: {p.name}")
        bbox = p.shape.bounding_box()
        records.append({
            "name": p.name, "material": p.material, "group": p.group,
            "explode": p.explode, "description": p.description,
            "volume_mm3": round(p.shape.volume, 5), "solids": len(p.shape.solids()),
            "bbox": {"min": list(bbox.min), "max": list(bbox.max)},
        })

    # Check the hard mechanical interfaces. Thread crests/tubes and compressed
    # seals are documented intentional overlaps and are not hard-body fit tests.
    pairs = [
        ("01_flow_chamber", "02_filtrate_chamber"),
        ("01_flow_chamber", "03_window_retainer"),
        ("01_flow_chamber", "04_upper_quartz_window"),
        ("01_flow_chamber", "06_membrane_carrier"),
        ("03_window_retainer", "04_upper_quartz_window"),
        ("03_window_retainer", "05_window_cushion"),
        ("02_filtrate_chamber", "09_lower_quartz_window"),
        ("09_lower_quartz_window", "lower_window_seal"),
        ("06_membrane_carrier", "07_membrane_sheet"),
        ("06_membrane_carrier", "08_membrane_support_screen"),
        ("07_membrane_sheet", "08_membrane_support_screen"),
        ("11_led_heat_sink", "14_led_array_board"),
        ("11_led_heat_sink", "12_polariser_rotation_ring"),
        ("10_lower_window_retainer", "12_polariser_rotation_ring"),
        ("15_diffuser", "12_polariser_rotation_ring"),
    ]
    interference = []
    for a, b in pairs:
        intersection = by_name[a].shape & by_name[b].shape
        volume = intersection.volume if intersection is not None else 0
        interference.append({"a": a, "b": b, "intersection_mm3": round(volume, 7)})
        if volume > 0.01:
            errors.append(f"Hard-part interference: {a} / {b}: {volume:.4f} mm³")
    shaft_end = P.Z_RET + P.RET_T + WASHER_T - SCREW_LENGTH
    blind_floor = Z_LED + P.LED_T - P.BOLT_TAP_DEPTH
    if shaft_end < blind_floor - 0.01:
        errors.append(f"Main screws bottom out by {blind_floor - shaft_end:.3f} mm")
    if P.ACTIVE_DIAG > P.EXPOSED_D:
        errors.append("25 × 25 mm field does not fit clear membrane aperture")

    report = {
        "component_count": len(parts), "solid_count": sum(r["solids"] for r in records),
        "units": "mm", "datum": "Membrane top Z=0; optical axis +Z",
        "all_breps_valid": not any(e.startswith("Invalid") for e in errors),
        "critical_interference_checks": interference,
        "screw_tip_clearance_mm": round(shaft_end - blind_floor, 3),
        "thread_engagement_envelope_mm": round(Z_LED + P.LED_T - shaft_end, 3),
        "nominal_window_pad_mm": WINDOW_PAD_T,
        "errors": errors,
        "limits": [
            "Geometry/packaging review only; no pressure, optical, thermal or seal qualification.",
            "Purchased-part dimensions and cosmetic thread geometry are representative.",
            "Compact reference layout omits an external camera support and focus stage.",
        ],
    }
    (ROOT / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    if errors:
        raise RuntimeError("\n".join(errors))
    print("All B-reps valid; critical fit checks pass.", flush=True)

    manifest = {"materials": MATERIALS, "components": records, "validation": report}
    (ROOT / "parts.json").write_text(json.dumps(manifest, indent=2) + "\n")
    variants = [("fouling_cell_realistic", parts, False)]
    if not args.assembled_only:
        print("Computing physical half-section…", flush=True)
        section_parts = cutaway_parts(parts)
        invalid = [p.name for p in section_parts if not p.shape.is_valid]
        if invalid:
            raise RuntimeError(f"Invalid section components: {invalid}")
        variants.extend([("fouling_cell_exploded", parts, True),
                         ("fouling_cell_cutaway", section_parts, False)])
    for name, variant, exploded in variants:
        model = assembly(variant, exploded)
        if not args.skip_step:
            print(f"Writing {name}.step…", flush=True)
            assert export_step(model, ROOT / f"{name}.step"), f"STEP export failed: {name}"
        # Geometry is the same as STEP; not a separately invented render model.
        print(f"Tessellating {name}.glb…", flush=True)
        assert export_gltf(model, ROOT / f"{name}.glb", binary=True,
                           linear_deflection=0.035, angular_deflection=0.16), f"GLB export failed: {name}"
        finish_glb(ROOT / f"{name}.glb", by_name)
    print(f"Complete in {time.monotonic() - start:.1f}s", flush=True)


if __name__ == "__main__":
    main()
