"""Geometry for the four machined bodies, plus envelopes for the bought parts.

Each body is modelled in its own local frame: local Z = 0 at its own bottom
face, optical axis on Z. The assembly stacks them off the membrane datum.
Every dimension comes from cell_params; there are no literals below that carry
design intent.
"""

from build123d import *

import cell_params as P


# ---------------------------------------------------------------- primitives

def cyl(d: float, z0: float, z1: float):
    """Cylinder from z0 to z1 on the optical axis."""
    return Pos(0, 0, z0) * Cylinder(
        radius=d / 2.0, height=z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN)
    )


def ring(d_in: float, d_out: float, z0: float, z1: float):
    return cyl(d_out, z0, z1) - cyl(d_in, z0, z1)


def gland_down(mean_d: float, cord: float, z_face: float):
    """O-ring gland cut into an upward-facing face (material below it)."""
    w = P.gland_width(cord)
    return ring(mean_d - w, mean_d + w, z_face - P.gland_depth(cord), z_face)


def gland_up(mean_d: float, cord: float, z_face: float):
    """O-ring gland cut into a downward-facing face (material above it)."""
    w = P.gland_width(cord)
    return ring(mean_d - w, mean_d + w, z_face, z_face + P.gland_depth(cord))


def radial_port(sign: int, z: float, bore_d: float, boss_d: float,
                boss_depth: float, inner_d: float):
    """Side port: fitting boss on the outer face, bore through to a central bore.

    sign = -1 for the -X face, +1 for the +X face. Tools overshoot both faces.
    """
    face = P.PLATE / 2.0
    boss = Pos(sign * (face + 1.0), 0, z) * Rot(0, -sign * 90, 0) * Cylinder(
        radius=boss_d / 2.0, height=boss_depth + 1.0,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    reach = face + 1.0 - (inner_d / 2.0 - 1.0)
    bore = Pos(sign * (face + 1.0), 0, z) * Rot(0, -sign * 90, 0) * Cylinder(
        radius=bore_d / 2.0, height=reach,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    return boss + bore


def bolt_holes(d: float, z0: float, z1: float):
    holes = None
    for x, y in P.BOLT_XY:
        h = Pos(x, y, z0) * Cylinder(
            radius=d / 2.0, height=z1 - z0,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        holes = h if holes is None else holes + h
    return holes


def _break_corners(solid, r: float = 3.0):
    """Cosmetic fillet on the four outside vertical corners. Non-critical."""
    try:
        corners = solid.edges().filter_by(Axis.Z).group_by(SortBy.LENGTH)[-1]
        return fillet(corners, radius=r)
    except Exception:
        return solid


# ------------------------------------------------------------ machined parts

def flow_chamber():
    """Upper body: crossflow channel over the membrane, quartz window seat,
    SAMPLE IN and BACKWASH ports, membrane cassette recess."""
    body = Box(P.PLATE, P.PLATE, P.FLOW_T, align=(Align.CENTER, Align.CENTER, Align.MIN))

    body -= cyl(P.CASSETTE_D + 0.5, 0, P.FLOW_CASSETTE_Z)
    body -= cyl(P.EXPOSED_D, P.FLOW_CASSETTE_Z, P.FLOW_CHANNEL_TOP)
    body -= cyl(P.WINDOW_SEAT_D, P.FLOW_CHANNEL_TOP, P.FLOW_T + 1.0)

    body -= gland_down(P.SEAL_WINDOW_D, P.CORD_OPTIC, P.FLOW_CHANNEL_TOP)
    body -= gland_up(P.SEAL_BODY_D, P.CORD_BODY, 0.0)

    port_z = P.FLOW_CASSETTE_Z + P.PORT_Z_IN_CHANNEL
    for sign in (-1, +1):                       # SAMPLE IN / BACKWASH
        body -= radial_port(sign, port_z, P.PORT_BORE_D, P.PORT_BOSS_D,
                            P.PORT_BOSS_DEPTH, P.EXPOSED_D)

    body -= bolt_holes(P.BOLT_CLEAR_D, -1.0, P.FLOW_T + 1.0)

    body = _break_corners(body)
    body.label = "flow_chamber"
    return body


def filtrate_chamber():
    """Lower body: filtrate plenum under the membrane, FILTRATE OUT port,
    polariser seat in the underside."""
    body = Box(P.PLATE, P.PLATE, P.FIL_T, align=(Align.CENTER, Align.CENTER, Align.MIN))

    body -= cyl(P.POLARISER_SEAT_D, -1.0, P.POLARISER_T)
    body -= cyl(P.ILLUM_BORE_D, P.POLARISER_T, P.FIL_T + 1.0)

    body -= gland_down(P.SEAL_POLARISER_D, P.CORD_OPTIC, P.POLARISER_T)
    body -= gland_up(P.SEAL_BASE_D, P.CORD_BODY, 0.0)

    body -= radial_port(+1, P.FIL_PORT_Z, P.FIL_PORT_BORE_D, P.FIL_PORT_BOSS_D,
                        P.FIL_PORT_BOSS_DEPTH, P.ILLUM_BORE_D)

    body -= bolt_holes(P.BOLT_CLEAR_D, -1.0, P.FIL_T + 1.0)

    body = _break_corners(body)
    body.label = "filtrate_chamber"
    return body


def led_base_plate():
    """Base: 530 nm LED array pocket, cable exit, blind tapped holes that the
    whole stack pulls down onto."""
    body = Box(P.PLATE, P.PLATE, P.LED_T, align=(Align.CENTER, Align.CENTER, Align.MIN))

    body -= cyl(P.LED_PCB_D, P.LED_T - P.LED_PCB_T_POCKET, P.LED_T + 1.0)

    cable_z = P.LED_T - P.LED_PCB_T_POCKET - P.CABLE_D / 2.0 + 0.5
    body -= Pos(0, P.PLATE / 2.0 + 1.0, cable_z) * Rot(90, 0, 0) * Cylinder(
        radius=P.CABLE_D / 2.0, height=P.PLATE / 2.0 + 1.0 - (P.LED_PCB_D / 2.0 - 1.0),
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )

    body -= bolt_holes(P.BOLT_TAP_CORE_D, P.LED_T - P.BOLT_TAP_DEPTH, P.LED_T + 1.0)

    body = _break_corners(body)
    body.label = "led_base_plate"
    return body


def window_retainer():
    """Top plate: clamps the quartz window into its seat. The relief is shallower
    than the window stand-proud, so the plate loads the glass, not the aluminium."""
    body = Box(P.PLATE, P.PLATE, P.RET_T, align=(Align.CENTER, Align.CENTER, Align.MIN))

    body -= cyl(P.RET_APERTURE_D, -1.0, P.RET_T + 1.0)
    body -= cyl(P.WINDOW_D + 1.5, -1.0, P.RET_RELIEF)
    body -= bolt_holes(P.BOLT_CLEAR_D, -1.0, P.RET_T + 1.0)

    body = _break_corners(body)
    body.label = "window_retainer"
    return body


# ------------------------------------------------- bought-part envelopes only
# Representative envelopes, NOT catalogue geometry. Present so the stack height,
# the optical path and the clamp chain can be checked visually.

def quartz_window():
    s = cyl(P.WINDOW_D, 0, P.WINDOW_T)
    s.label = "quartz_window:cots_envelope"
    return s


def membrane_cassette():
    s = cyl(P.CASSETTE_D, 0, P.CASSETTE_T)
    s.label = "membrane_cassette_47mm:cots_envelope"
    return s


def polariser(name: str):
    s = cyl(P.POLARISER_D, 0, P.POLARISER_T)
    s.label = f"{name}:cots_envelope"
    return s


def shcs():
    s = cyl(P.BOLT_HEAD_D, 0, P.BOLT_HEAD_T) + cyl(P.BOLT_CLEAR_D - 0.6, -P.BOLT_LEN, 0)
    s.label = "m6x55_shcs:cots_envelope"
    return s


# ------------------------------------------------------ rest of the instrument
# Envelopes for the bought parts above and below the cell. Origins are on the
# face that mates to the cell so the assembly can stack them off one datum.

def _hex_prism(af: float, h: float):
    with BuildPart() as p:
        with BuildSketch():
            RegularPolygon(radius=af / 2.0 / 0.8660254, side_count=6)
        extrude(amount=h)
    return p.part


def macro_lens():
    """Origin at the front face; barrel extends +Z toward the camera."""
    s = cyl(P.LENS_BODY_D, 0, P.LENS_LEN)
    s += cyl(P.LENS_RING_D, P.LENS_RING_Z, P.LENS_RING_Z + P.LENS_RING_T)
    s -= cyl(P.LENS_BODY_D - 6.0, -1.0, 4.0)                 # front element recess
    s.label = "macro_lens_50mm:cots_envelope"
    return s


def analyser():
    """Threaded filter ring with a glass disc; origin at its bottom face."""
    ring = cyl(P.ANALYSER_D, 0, P.ANALYSER_T) - cyl(P.ANALYSER_GLASS_D, -1.0, P.ANALYSER_T + 1.0)
    ring.label = "analyser_ring:cots_envelope"
    glass = cyl(P.ANALYSER_GLASS_D, P.ANALYSER_T / 2.0 - 1.0, P.ANALYSER_T / 2.0 + 1.0)
    glass.label = "analyser_glass:cots_envelope"
    return ring, glass


def camera():
    """C-mount camera; origin at the mount face (bottom), body extends +Z."""
    body = Pos(0, 0, P.CMOUNT_T) * Box(P.CAM_W, P.CAM_W, P.CAM_L, align=(Align.CENTER, Align.CENTER, Align.MIN))
    body = fillet(body.edges().filter_by(Axis.Z), radius=3.0)
    body += cyl(P.CMOUNT_D + 6.0, 0, P.CMOUNT_T)
    body -= cyl(P.CMOUNT_D, -1.0, P.CMOUNT_T + 2.0)
    body.label = "camera:cots_envelope"
    return body


def port_fitting():
    """Hex + barb; origin on the boss face, barb along +Z (outward)."""
    s = _hex_prism(P.FITTING_HEX_AF, P.FITTING_HEX_T)
    s += cyl(P.FITTING_BARB_D, P.FITTING_HEX_T, P.FITTING_HEX_T + P.FITTING_BARB_L)
    s += cyl(P.FITTING_BARB_D + 1.2, P.FITTING_HEX_T + 3.0, P.FITTING_HEX_T + 5.0)
    s += cyl(P.FITTING_BARB_D + 1.2, P.FITTING_HEX_T + 7.5, P.FITTING_HEX_T + 9.5)
    s -= cyl(2.0, -1.0, P.FITTING_HEX_T + P.FITTING_BARB_L + 1.0)
    s.label = "port_fitting:cots_envelope"
    return s


def led_pcb():
    s = cyl(P.LED_PCB_D - 2.0, 0, P.LED_PCB_T)
    s.label = "led_pcb:cots_envelope"
    return s


def led_array():
    """19 domes on a hex grid, origin on the PCB top face."""
    from math import sqrt
    pts = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            x = P.LED_PITCH * (i + 0.5 * j)
            y = P.LED_PITCH * j * sqrt(3) / 2.0
            if x * x + y * y <= (2.05 * P.LED_PITCH) ** 2:
                pts.append((x, y))
    s = None
    for x, y in pts:
        d = Pos(x, y, 0) * Cylinder(radius=P.LED_DOME_D / 2.0, height=P.LED_DOME_H,
                                    align=(Align.CENTER, Align.CENTER, Align.MIN))
        s = d if s is None else s + d
    s.label = f"led_array_{len(pts)}x:cots_envelope"
    return s


def o_ring(mean_d: float, cord: float):
    """Seated (compressed) O-ring; origin at the gland's mid-depth plane."""
    r_minor = P.gland_depth(cord) / 2.0
    s = Torus(major_radius=mean_d / 2.0, minor_radius=r_minor)
    s.label = "o_ring:cots_envelope"
    return s
