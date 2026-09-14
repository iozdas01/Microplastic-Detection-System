"""Exploded view of the imaging station — the same parts as imaging_station.step.py, each
lifted by a fixed amount so the stacking order reads. Review only; nothing here is a
manufacturing placement. Offsets come from EXPLODE below, not from station_params."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Color, Location  # noqa: E402
from cadgen.assembly import AssemblyHelper  # noqa: E402

import station_params as P  # noqa: E402
import station_parts as C  # noqa: E402

EXPLODE = 22.0   # mm added between each layer of the stack


def gen_step():
    asm = AssemblyHelper("imaging_station_exploded")

    def add(shape, name, *details):
        mat = P.material_of(name)
        return asm.add(shape, name, *details, color=Color(mat[1]) if mat else None)

    def place(part, x, y, z):
        asm.face_to_face(asm.rigid_frame(base, f"seat_{part.label}", Location((x, y, z))),
                         asm.rigid_frame(part, "base", Location((0, 0, 0))))

    base = add(C.base_plate(), "base_plate")
    box_top = P.PLATE_T + P.BOX_H
    pocket_floor = box_top - P.POCKET_DEPTH
    e = EXPLODE

    for i in range(P.LED_COUNT):
        y = (i - (P.LED_COUNT - 1) / 2.0) * (P.LED_W + P.LED_GAP)
        place(add(C.led_panel(), "led_panel", f"slab_{i + 1}"), 0, y, pocket_floor + 1 * e)
    recess = box_top - P.FILM_RECESS
    place(add(C.polariser(), "polariser", "lower"), 0, 0, recess + 2 * e)
    place(add(C.tint_plate(), "tint_plate"), 0, 0, recess + P.POLARISER_T + 3 * e)
    tray_z = box_top + 4 * e
    place(add(C.tray(), "tray"), 0, 0, tray_z)
    place(add(C.membrane(), "membrane"), 0, 0, tray_z + P.TRAY_FLOOR + 1 * e)
    place(add(C.cover_glass(), "cover_glass"), 0, 0, tray_z + P.TRAY_FLOOR + 2 * e)

    names = ("front_left", "rear_left", "front_right", "rear_right")
    for (x, y), corner in zip(P.POST_XY, names):
        place(add(C.post(), "post", corner), x, y, P.PLATE_T + 2 * e)
    cradle_z = P.PLATE_T + P.POST_L + 7 * e
    place(add(C.cradle(), "cradle"), 0, 0, cradle_z)
    phone_back = cradle_z + P.CRADLE_T - P.CRADLE_POCKET
    place(add(C.polariser(), "polariser", "upper"), 0, 0, phone_back - P.PLATEAU_H - P.CLIP_BELOW - P.POLARISER_T + 0 * e)
    place(add(C.clip_lens(), "clip_lens"), 0, 0, phone_back - P.PLATEAU_H - P.CLIP_BELOW + 1 * e)
    place(add(C.phone(), "phone"), P.PHONE_CX, P.PHONE_CY, phone_back + 2 * e)
    return asm.build()
