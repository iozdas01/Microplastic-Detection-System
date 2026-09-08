# Detailed membrane imaging cell

Open **viewer.html** directly in a browser. It is self-contained and works offline.
Use Assembled / Exploded / Cutaway, drag to rotate, and click a component to inspect it.

## Files

- `fouling_cell_realistic.step` — assembled CAD, 166 named solid components.
- `fouling_cell_exploded.step` — separated assembly.
- `fouling_cell_cutaway.step` — actual solid half-section at Y=0.
- `fouling_cell_realistic.step.py` — editable Fable/cadgen entry point.
- `instrument.py` — geometry and detail assumptions; base dimensions derive from `../cell_params.py`.
- `*.glb` — the same geometry with physical material definitions.
- `renders/assembled.png`, `renders/cutaway.png` — renders of the exported CAD geometry.
- `parts.json`, `validation.json`, `fit_audit.json` — component inventory and geometric checks.

The original model is preserved in the parent directory.

## What changed

Separate camera covers, socket screws, cooling slots and connector geometry;
stepped lens cells, curved elements and scalloped adjustment rings; hollow tapered
fittings and tube stubs; separate membrane, carrier and support screen; machined
edge breaks; compressed seal geometry; a 19-package LED board and heat sink.

The lower pressure window is now separate from the dry rotating polariser. A
13 mm illumination gap, retention clips and longer nominal M6 × 70 clamp screws
accommodate it. The lower window gland faces the glass correctly. PCB screws
clear the LED packages. Nominal clamp screw tips have 1.1 mm bottom clearance.

## Scope and verification

This is detailed **concept CAD**, not a qualified manufacturing design. The 90 mm
footprint, 47 mm cassette and 25 × 25 mm field are retained. Purchased parts,
camera height, material finishes and added details are representative assumptions.
The reference's compact layout omits an external camera stand and focus stage.
Pressure rating, seal chemistry, tolerances, optical prescription, sensor/field
compatibility, working distance, support-screen effects and heat removal remain
unverified. Camera and lens geometry are not vendor-approved catalogue parts.
Screw and fitting threads use cosmetic annular crests, not production helices.
Lettering and microscopic finishes in the renders are surface presentation layers.

All 166 assembled solids passed B-rep validity checks. The full fit audit checked
228 overlapping bounding-box pairs and found no unexplained positive solid overlap.
Nominal threads, flexible tubing over barbs, seated LED encapsulant and the bonded
camera label have documented intentional contacts. Cutaway solids were also checked.
GLBs load in Three.js; the viewer's geometry/assembly transforms are checked offline.
Interactive browser QA was unavailable in this session.

## Rebuild

Use Python with build123d 0.11.1 installed:

```sh
python build.py
python audit_fits.py
node package_viewer.mjs /path/to/node_modules
```

The Node module directory needs `three` and `esbuild`. Blender 4.5 LTS can render
the geometry with `--background --factory-startup --python render.py -- --view assembled`.
Choose `cutaway`, `exploded` or `detail` for other cameras. `--save-blend` saves
the configured scene. The packaged HTML embeds Three.js under its MIT license.
