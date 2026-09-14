# Phone imaging station

The data-collection rig: a 47 mm filter membrane under a cover glass on a tray, lit from
below by an LED panel through a polarising film, photographed from above by an iPhone 17
Pro Max with a 10× clip-on macro lens through a second polarising film. It exists to
produce labelled images of known fibres, fast, so a counting and classification model
can be trained before any inline sensor exists.

Everything derives from `station_params.py`. Change the clip-on lens's focal length there
and the working distance, the post length and the field-of-view checks all follow. Every
number tagged `[GUESS]` in that file is an assumption to replace with the measured part.

## The optics, and how to recompute them

Inputs: phone focal length f = 6.9 mm, f-number N = 1.78, pixel p = 1.22 µm (48 MP),
sensor 9.8 × 7.3 mm, clip-on focal length f₂ (25 mm for a "10×"), wavelength λ = 0.55 µm.
All of these are in `station_params.py`; the derived values below are computed there.

| Quantity | Formula | With f₂ = 25 mm |
|---|---|---|
| Working distance | f₂ (phone at infinity, object at the clip-on's focal plane) | 25 mm |
| Magnification m | f / f₂ | 0.276 |
| Field of view | sensor / m | 35.5 × 26.4 mm |
| Object size per pixel | p / m | 4.4 µm |
| Phone aperture D | f / N | 3.9 mm |
| Numerical aperture NA | D / (2 f₂) | 0.078 |
| Smallest resolvable detail | 0.61 λ / NA | 4.3 µm |
| Depth of field | λ / NA² | 0.09 mm |
| Fine focus from the phone's autofocus | f₂² / nearest focus distance | 625 / 200 ≈ 3 mm |
| Retardation of a fibre (crossed polarisers) | Δn × thickness | polyester 0.17 × 20 µm = 3.4 µm; cotton 0.045 × 15 µm = 0.7 µm |
| Exposure time | N² × 12.5 / (L × ISO) | one 1621 slab, L ≈ 200 cd/m², ISO 100: ≈ 1/500 s |

So one frame covers most of the membrane's exposed area, a 25 µm fibre is about 6 pixels
wide, and the sample has to be flat to a tenth of a millimetre — which is why the cover
glass presses the membrane and the tray floor prints on the bed. Change f₂ and the first
eight rows move together; that is the one parameter that matters.

## Parts

Printed (FDM, PLA or PETG, 0.2 mm layers; the tray floor down on the bed):

| file | what | notes |
|---|---|---|
| `base_plate.step` / `stl/base_plate.stl` | base plate with the light box on it | LED + diffuser pocket open to the top, cable slot on +X, tray rails, four post screw holes |
| `post.step` / `stl/post.stl` | square post, print four | 60 mm; M3 pilot holes both ends |
| `tray.step` / `stl/tray.stl` | sample tray | 50 mm glass seat over a 47 mm membrane; ticks every 5 mm; crosshair on the axis; grip tab |
| `cradle.step` / `stl/cradle.stl` | phone cradle | 213 × 129 mm: fits a 220 mm bed, just; pocket for the phone, opening under the camera plateau, ribs underneath |
| `wet_cell.step` / `stl/wet_cell.stl` | wet mount | two 25 mm cover glasses 1 mm apart; drops into the tray rails; print in resin or seal the seats |

`imaging_station.step` is the whole rig assembled, with envelopes for the bought parts.

Bought: 10× clip-on macro lens; two Adafruit 1621 white LED backlights (45 × 86 mm,
~3 V 20 mA each, 100 Ω in series from USB); two 96 × 92 mm linear polarising films; one
full-wave tint sheet (cellophane works); 50 mm round cover glass (1 mm); 25 mm round cover
glass ×2; 47 mm PCTE membranes; 8 × M3 × 10 screws.

## Rebuild

```sh
# once: python3 -m venv .venv-cad && .venv-cad/bin/pip install <text-to-cad>/skills/cad/scripts/packages/cadgen
S=~/.claude/plugins/cache/text-to-cad/cad/0.4.7/skills/cad
cd cad/imaging-station
../../.venv-cad/bin/python $S/scripts/gen *.step.py --write
../../.venv-cad/bin/python $S/scripts/export tray.step.py --stl stl/tray.stl   # etc.
```

## Assumptions to retire, in order

1. Clip-on lens focal length (`CLIP_F`) and body height (`CLIP_BELOW`): read off the lens.
2. Phone camera position (`CAM_FROM_TOP`, `CAM_FROM_SIDE`) and plateau height: measure
   the phone with calipers. These set where the optical axis is under the cradle.
3. LED panel size and thickness: from the panel bought.
4. Cover glass thickness: 1 mm slide glass assumed; 0.17 mm slips would sag.

## First experiments

1. Stage micrometer on the tray, photograph, get pixels per micrometre.
2. Known count of cut polyester fibres in clean water, filtered onto a membrane, count.
3. Same with cotton; then both with the polarisers crossed.
4. Mixed, unknown ratio.
5. One real sample.
