# Phone imaging station

The data-collection rig: a 47 mm filter membrane under a cover glass on a tray, lit from
below by an LED panel through a polarising film, photographed from above by an iPhone 17
Pro Max with a 10× clip-on macro lens through a second polarising film. It exists to
produce labelled images of known fibres, fast, so a counting and classification model
can be trained before any inline sensor exists.

Everything derives from `station_params.py`. Change the clip-on lens's focal length there
and the working distance, the post length and the field-of-view checks all follow. Every
number tagged `[GUESS]` in that file is an assumption to replace with the measured part.

## What the optics decide

With the 10× clip-on (f ≈ 25 mm) on the phone's main camera, at 48 MP:

| field of view | per pixel | resolves | depth of field | a 25 µm fibre |
|---|---|---|---|---|
| 35.5 × 26.4 mm | 4.4 µm | 4.3 µm | 92 µm | 5.7 px |

So one frame covers most of the membrane's exposed area, a fibre is countable and
measurable in length, and the sample has to be flat to a tenth of a millimetre — which
is why the cover glass presses the membrane and the tray floor prints on the bed.

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

Bought: 10× clip-on macro lens; 50 × 50 mm white LED panel (USB); opal diffuser; two
60 × 60 mm linear polarising films; 50 mm round cover glass (1 mm); 25 mm round cover
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
