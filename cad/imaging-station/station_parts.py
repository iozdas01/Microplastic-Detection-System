"""Geometry for the five printed bodies of the imaging station, plus envelopes for the
bought parts. Every body is modelled in its own local frame with local Z = 0 at its
bottom face and the optical axis on global Z; the assembly stacks them off the membrane
datum. All dimensions come from station_params; no literal below carries design intent.
"""

from build123d import *

import station_params as P


# ---------------------------------------------------------------- primitives

def box(l: float, w: float, h: float, x: float = 0.0, y: float = 0.0, z0: float = 0.0):
    """Box centred on (x, y) in plan, from z0 up to z0 + h."""
    return Pos(x, y, z0) * Box(l, w, h, align=(Align.CENTER, Align.CENTER, Align.MIN))


def cyl(d: float, z0: float, z1: float, x: float = 0.0, y: float = 0.0):
    return Pos(x, y, z0) * Cylinder(radius=d / 2.0, height=z1 - z0,
                                    align=(Align.CENTER, Align.CENTER, Align.MIN))


def _break_corners(solid, r: float = 3.0):
    """Cosmetic radius on the outside vertical corners. Non-critical."""
    try:
        corners = solid.edges().filter_by(Axis.Z).group_by(SortBy.LENGTH)[-1]
        return fillet(corners, radius=r)
    except Exception:
        return solid


# ------------------------------------------------------------ printed parts

def base_plate():
    """Base plate with the light box printed on it: LED + diffuser pocket open to the top,
    tray rails on the box top along Y, cable slot out the +X wall, four post sockets."""
    body = box(P.PLATE_L, P.PLATE_W, P.PLATE_T, P.PLATE_CX, P.PLATE_CY)
    body += box(P.BOX_W, P.BOX_W, P.BOX_H, 0, 0, P.PLATE_T)
    top = P.PLATE_T + P.BOX_H

    # LED + diffuser pocket, from the top
    body -= box(P.POCKET_W, P.POCKET_W, P.POCKET_DEPTH + 1.0, 0, 0, top - P.POCKET_DEPTH)
    # cable slot through the +X wall at pocket-floor level
    body -= box(P.BOX_W, P.CABLE_W, P.CABLE_H, P.BOX_W / 2.0, 0, top - P.POCKET_DEPTH)
    # tray rails along Y on the box top, at the ±X edges
    for sx in (-1, +1):
        body += box(P.RAIL_W, P.BOX_W, P.RAIL_H, sx * (P.BOX_W / 2.0 - P.RAIL_W / 2.0), 0, top)
    # rear stop so the tray always lands on the same spot (+Y end)
    body += box(P.BOX_W - 2 * P.RAIL_W, P.RAIL_W, P.RAIL_H, 0, P.BOX_W / 2.0 - P.RAIL_W / 2.0, top)

    # post screw holes through the plate (M3 clearance)
    for x, y in P.POST_XY:
        body -= cyl(P.SCREW_CLEAR_D, -1.0, P.PLATE_T + 1.0, x, y)

    body = _break_corners(body)
    body.label = "base_plate"
    return body


def post():
    """Square post, pilot holes in both ends for M3 screws. Four identical."""
    body = box(P.POST_SQ, P.POST_SQ, P.POST_L)
    body -= cyl(P.POST_SCREW_D, -1.0, 10.0)
    body -= cyl(P.POST_SCREW_D, P.POST_L - 10.0, P.POST_L + 1.0)
    body.label = "post"
    return body


def tray():
    """Sample tray: 47 mm membrane on a flat floor under a 50 mm cover glass seat,
    index ticks every 5 mm on the top face, grip tab at the -Y end. Slides between the rails."""
    body = box(P.TRAY_W, P.TRAY_L, P.TRAY_T)
    body += box(P.TRAY_W, P.GRIP_L, P.TRAY_T - 2.0, 0, -(P.TRAY_L / 2.0 + P.GRIP_L / 2.0))

    # glass seat: 3 mm deep, the membrane lies on its floor
    seat_d = P.GLASS_D + P.GLASS_CLEAR
    body -= cyl(seat_d, P.TRAY_FLOOR, P.TRAY_T + 1.0)
    # illumination window under the membrane: leave a 4 mm rim to support the disc edge
    body -= cyl(P.MEMBRANE_D - 8.0, -1.0, P.TRAY_FLOOR + 1.0)
    # two finger notches to lift the glass out
    for sy in (-1, +1):
        body -= box(6.0, 3.0, P.TRAY_T, 0, sy * (seat_d / 2.0), P.TRAY_FLOOR + 1.0)

    # index ticks along both X edges of the top face, every TICK_PITCH
    n = int((P.TRAY_L / 2.0) // P.TICK_PITCH)
    for i in range(-n, n + 1):
        y = i * P.TICK_PITCH
        long = 3.0 if i % 2 == 0 else 1.5
        for sx in (-1, +1):
            body -= box(long, P.TICK_W, P.TICK_DEPTH + 0.1,
                        sx * (P.TRAY_W / 2.0 - long / 2.0), y, P.TRAY_T - P.TICK_DEPTH)
    # crosshair on the seat rim, marks the optical axis
    for ang in (0, 90):
        body -= Rot(0, 0, ang) * box(P.TRAY_W, P.TICK_W, P.TICK_DEPTH + 0.1, 0, 0,
                                     P.TRAY_T - P.TICK_DEPTH)

    body.label = "tray"
    return body


def cradle():
    """Phone cradle: pocket the phone lies in screen-up, opening under the camera plateau
    and clip-on lens, stiffening ribs on the underside, four post screw holes."""
    body = box(P.CRADLE_L, P.CRADLE_W, P.CRADLE_T, P.CRADLE_CX, P.CRADLE_CY)

    # phone pocket, open to the top
    body -= box(P.PHONE_L + P.PHONE_CLEAR, P.PHONE_W + P.PHONE_CLEAR, P.CRADLE_POCKET + 1.0,
                P.PHONE_CX, P.PHONE_CY, P.CRADLE_T - P.CRADLE_POCKET)
    # through-opening under the plateau + clip, from the phone's top (+X) edge inward
    body -= box(P.CAM_CUTOUT_L, P.CAM_CUTOUT_W, P.CRADLE_T + 2.0,
                P.PHONE_X1 - P.CAM_CUTOUT_L / 2.0, P.PHONE_CY, -1.0)
    # the optical axis: a round clearance for the lens body in case the cutout is narrowed
    body -= cyl(P.CLIP_BODY_D + 2.0, -1.0, P.CRADLE_T + 1.0)
    # thumb notch at the -X end to lift the phone out
    body -= cyl(24.0, P.CRADLE_T - P.CRADLE_POCKET - 1.0, P.CRADLE_T + 1.0, P.PHONE_X0, P.PHONE_CY)

    # post screw holes
    for x, y in P.POST_XY:
        body -= cyl(P.SCREW_CLEAR_D, -1.0, P.CRADLE_T + 1.0, x, y)

    # two ribs along X on the underside, outside the phone pocket walls
    rib_h = 6.0
    for y in (P.CRADLE_Y0 + 4.0, P.CRADLE_Y1 - 4.0):
        body += box(P.CRADLE_L - 2 * P.POST_INSET - P.POST_SQ, 3.0, rib_h, P.CRADLE_CX, y, -rib_h)

    body = _break_corners(body, 4.0)
    body.label = "cradle"
    return body


def wet_cell():
    """Wet mount: two 25 mm cover glasses held WET_GAP apart in a plate that drops into the
    tray rails. Lower glass seats from below, upper glass from above; the well between them
    holds the water."""
    body = box(P.TRAY_W, P.TRAY_L, P.WET_T)
    body += box(P.TRAY_W, P.GRIP_L, P.WET_T - 2.0, 0, -(P.TRAY_L / 2.0 + P.GRIP_L / 2.0))
    d = P.WET_GLASS_D + 0.5
    lower_top = P.WET_GLASS_T + 0.2                    # lower glass seat depth from the bottom
    body -= cyl(d, -1.0, lower_top)                    # lower glass seat
    body -= cyl(P.WET_WELL_D, lower_top - 1.0, P.WET_T + 1.0)   # the well, through to the top
    body -= cyl(d, lower_top + P.WET_GAP, P.WET_T + 1.0)        # upper glass seat
    # fill notch: a small side channel into the well at gap level, for the pipette tip
    body -= box(P.TRAY_W / 2.0, 2.0, P.WET_GAP, P.TRAY_W / 4.0 + P.WET_WELL_D / 4.0, 0, lower_top)
    body.label = "wet_cell"
    return body


# ------------------------------------------------------------- bought parts

def phone():
    """iPhone 17 Pro Max envelope: flat slab plus the camera plateau on the back face.
    Local Z = 0 at the FLAT BACK; the plateau hangs below it (negative Z)."""
    slab = box(P.PHONE_L, P.PHONE_W, P.PHONE_T)
    slab = _break_corners(slab, 12.0)
    plateau = box(P.PLATEAU_L, P.PHONE_W - 8.0, P.PLATEAU_H,
                  P.PHONE_L / 2.0 - P.PLATEAU_L / 2.0 - 4.0, 0, -P.PLATEAU_H)
    body = slab + plateau
    body.label = "phone"
    return body


def clip_lens():
    """Clip-on macro lens envelope: a disc on the plateau over the camera, lens front down.
    Local Z = 0 at the LENS FRONT face."""
    body = cyl(P.CLIP_BODY_D, 0.0, P.CLIP_BELOW)
    body -= cyl(P.CLIP_BODY_D * 0.45, -1.0, 1.5)
    body.label = "clip_lens"
    return body


def led_panel():
    body = box(P.LED_W, P.LED_W, P.LED_T)
    body.label = "led_panel"
    return body


def diffuser():
    body = box(P.LED_W, P.LED_W, P.DIFFUSER_T)
    body.label = "diffuser"
    return body


def polariser():
    body = box(P.POLARISER_W, P.POLARISER_W, P.POLARISER_T)
    body.label = "polariser"
    return body


def membrane():
    body = cyl(P.MEMBRANE_D, 0.0, max(P.MEMBRANE_T, 0.05))
    body.label = "membrane"
    return body


def cover_glass(d: float = P.GLASS_D, t: float = P.GLASS_T):
    body = cyl(d, 0.0, t)
    body.label = "cover_glass"
    return body
