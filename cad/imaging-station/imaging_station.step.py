"""Phone imaging station — the whole rig.

Five printed bodies (base plate with the light box on it, four posts, tray, cradle) plus
envelopes for everything bought: phone, clip-on lens, LED panel, diffuser, two polariser
films, membrane and cover glass. The base plate is the fixed root; everything stacks up
from it via face-to-face mates whose offsets come from station_params. The wet cell is a
separate entry (wet_cell.step.py) because it swaps with the tray rather than adding to it.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Color, Location  # noqa: E402
from cadgen.assembly import AssemblyHelper  # noqa: E402

import station_params as P  # noqa: E402
import station_parts as C  # noqa: E402


def gen_step():
    asm = AssemblyHelper("imaging_station")
    _add = asm.add

    def add(shape, name, *details):
        mat = P.material_of(name)
        return _add(shape, name, *details, color=Color(mat[1]) if mat else None)

    asm.add = add
    F = asm.rigid_frame
    Z = lambda z: Location((0, 0, z))  # noqa: E731

    base = asm.add(C.base_plate(), "base_plate")
    seats = []

    def seat(part, name, carrier, location):
        seats.append((F(carrier, f"seat_{name}", location), F(part, "base", Z(0)), name))

    box_top = P.PLATE_T + P.BOX_H                       # local to the base plate
    pocket_floor = box_top - P.POCKET_DEPTH

    # --- light stack in the box --------------------------------------------
    seat(asm.add(C.led_panel(), "led_panel"), "led", base, Z(pocket_floor))
    seat(asm.add(C.diffuser(), "diffuser"), "diffuser", base, Z(pocket_floor + P.LED_T))
    seat(asm.add(C.polariser(), "polariser", "lower"), "polariser_lower", base, Z(box_top))

    # --- tray on the box top, over the polariser ----------------------------
    tray = asm.add(C.tray(), "tray")
    seat(tray, "tray", base, Z(box_top + P.POLARISER_T))
    seat(asm.add(C.membrane(), "membrane"), "membrane", tray, Z(P.TRAY_FLOOR))
    seat(asm.add(C.cover_glass(), "cover_glass"), "glass", tray, Z(P.TRAY_FLOOR + P.MEMBRANE_T))

    # --- posts and cradle ----------------------------------------------------
    names = ("front_left", "rear_left", "front_right", "rear_right")
    for (x, y), corner in zip(P.POST_XY, names):
        seat(asm.add(C.post(), "post", corner), f"post_{corner}", base, Location((x, y, P.PLATE_T)))
    cradle = asm.add(C.cradle(), "cradle")
    seat(cradle, "cradle", base, Z(P.PLATE_T + P.POST_L))

    # --- phone, lens, upper polariser ---------------------------------------
    # phone frame: its flat back at the cradle pocket floor, camera on the optical axis
    phone = asm.add(C.phone(), "phone")
    seat(phone, "phone", cradle, Location((P.PHONE_CX, P.PHONE_CY, P.CRADLE_T - P.CRADLE_POCKET)))
    lens = asm.add(C.clip_lens(), "clip_lens")
    # clip lens frame: lens front is its local Z=0; it hangs CLIP_BELOW under the plateau,
    # which is PLATEAU_H under the phone's flat back, on the optical axis
    seat(lens, "lens", phone, Location((-P.PHONE_CX, -P.PHONE_CY, -P.PLATEAU_H - P.CLIP_BELOW)))
    seat(asm.add(C.polariser(), "polariser", "upper"), "polariser_upper", lens, Z(-P.POLARISER_T))

    for fixed, moving, name in seats:
        asm.face_to_face(fixed, moving, label=name)

    return asm.build()
