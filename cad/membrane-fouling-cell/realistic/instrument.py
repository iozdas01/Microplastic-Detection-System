"""Detailed, editable B-rep model of the membrane imaging instrument.

Run build.py for STEP assemblies, GLBs, the parts manifest and geometric checks.
Millimetres; membrane surface is Z=0; camera looks down -Z. Original dimensions
come from ../cell_params.py. Detail/packaging assumptions are collected below.
Purchased parts are representative geometry, not vendor-certified CAD.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from functools import lru_cache
from math import cos, pi, sin, sqrt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import cell_params as P
import cell_parts as C
from build123d import (
    Align, Axis, Box, Color, Compound, Cone, Cylinder, Ellipse, Plane,
    Pos, RegularPolygon, Rot, Sphere, chamfer, extrude, fillet, revolve,
)


# Packaging/detail assumptions. No new pressure rating or optical specification.
ILLUMINATION_GAP = 13.0       # dry gap; leaves 1.1 mm below nominal clamp screw tips
Z_LED = P.Z_LED - ILLUMINATION_GAP
CAMERA_HEIGHT = 34.0         # representative housing; original width retained
CAMERA_Z = P.LENS_FRONT_STANDOFF + P.LENS_LEN
MEMBRANE_THICKNESS = 0.15
WINDOW_PAD_T = 0.30
WINDOW_RELIEF = P.WINDOW_PROUD + WINDOW_PAD_T
LOWER_WINDOW_D = P.POLARISER_D
LOWER_WINDOW_T = P.POLARISER_T
POLARISER_Z = P.Z_FIL - 8.7
POLARISER_OD = 58.0
SCREW_LENGTH = 70.0          # increased to span dry illumination gap
WASHER_T = 1.6
PORT_TAP_CORE = 4.2          # nominal 10-32 envelope, thread not manufacturing data
PORT_THREAD_OD = 4.7
FIL_PORT_Z = P.Z_FIL + P.FIL_PORT_Z
FILAMENTS_ARE_ILLUSTRATIVE = True

MATERIALS = {
    "aluminium": {"color": "#bfc6cb", "metalness": 0.82, "roughness": 0.29},
    "edge_metal": {"color": "#d9dfe2", "metalness": 0.91, "roughness": 0.19},
    "black_anodised": {"color": "#23272b", "metalness": 0.65, "roughness": 0.29},
    "rubber_grip": {"color": "#141719", "metalness": 0.05, "roughness": 0.66},
    "stainless": {"color": "#bfc6cd", "metalness": 0.97, "roughness": 0.21},
    "seal": {"color": "#a84922", "metalness": 0.0, "roughness": 0.69},
    "quartz": {"color": "#dcf2f4", "metalness": 0.0, "roughness": 0.06,
               "transmission": 0.93, "ior": 1.46, "opacity": 0.27},
    "optical_glass": {"color": "#81afa9", "metalness": 0.12, "roughness": 0.07,
                     "transmission": 0.8, "ior": 1.5, "opacity": 0.55},
    "polarising_glass": {"color": "#64767c", "metalness": 0.10, "roughness": 0.09,
                        "transmission": 0.70, "ior": 1.5, "opacity": 0.60},
    "ptfe": {"color": "#f2f0e6", "metalness": 0.0, "roughness": 0.80},
    "membrane": {"color": "#e8e4d7", "metalness": 0.0, "roughness": 0.95},
    "pcb": {"color": "#e1e5dd", "metalness": 0.05, "roughness": 0.50},
    "green_pcb": {"color": "#184a3c", "metalness": 0.05, "roughness": 0.55},
    "gold": {"color": "#b9954e", "metalness": 0.80, "roughness": 0.3},
    "ceramic": {"color": "#deddd4", "metalness": 0.0, "roughness": 0.48},
    "led": {"color": "#bff696", "metalness": 0.05, "roughness": 0.14,
            "emissive": "#60e426", "emissiveIntensity": 1.6},
    "diffuser": {"color": "#e5efd9", "metalness": 0.0, "roughness": 0.78,
                 "transmission": 0.35, "opacity": 0.63},
    "silicone": {"color": "#c9e0df", "metalness": 0.0, "roughness": 0.15,
                 "transmission": 0.82, "ior": 1.41, "opacity": 0.32},
    "label": {"color": "#30383c", "metalness": 0.30, "roughness": 0.50},
}


@dataclass
class Component:
    name: str
    shape: object
    material: str
    group: str
    explode: tuple[float, float, float] = (0, 0, 0)
    description: str = ""
    section: bool = False

    def as_shape(self, exploded=False):
        shape = copy.copy(self.shape)
        if exploded:
            shape = Pos(*self.explode) * shape
        shape.label = self.name
        material = MATERIALS[self.material]
        shape.color = Color(material["color"])
        return shape


def cylinder(d, z0, z1):
    return Pos(0, 0, z0) * Cylinder(d / 2, z1 - z0,
                                   align=(Align.CENTER, Align.CENTER, Align.MIN))


def annulus(di, do, z0, z1):
    return cylinder(do, z0, z1) - cylinder(di, z0 - 0.1, z1 + 0.1)


def cone(d0, d1, z0, z1):
    return Pos(0, 0, z0) * Cone(d0 / 2, d1 / 2, z1 - z0,
                               align=(Align.CENTER, Align.CENTER, Align.MIN))


def block(w, d, z0, z1):
    return Pos(0, 0, z0) * Box(w, d, z1 - z0,
                              align=(Align.CENTER, Align.CENTER, Align.MIN))


def plate(w, d, t, radius=3.0, edge=0.35):
    body = block(w, d, 0, t)
    body = fillet(body.edges().filter_by(Axis.Z), radius)
    if edge:
        body = chamfer(body.edges().filter_by(Axis.Z, reverse=True), edge)
    return body


def hexagon(af, z0, z1):
    return Pos(0, 0, z0) * extrude(
        RegularPolygon(af / sqrt(3), 6, rotation=30), amount=z1 - z0
    )


def bore_breaks(body, positions, diameter, z0, z1, depth=0.35):
    for x, y in positions:
        body -= Pos(x, y) * cone(diameter + 2 * depth, diameter, z0, z0 + depth)
        body -= Pos(x, y) * cone(diameter, diameter + 2 * depth, z1 - depth, z1)
    return body


def outer_ring(di, do, z0, z1, bevel=0.25):
    body = annulus(di, do, z0, z1)
    if bevel:
        body = chamfer(body.edges(), bevel)
    return body


@lru_cache(maxsize=None)
def grip_ring(di, do, height, grooves, width=0.5):
    """Real scalloped edge geometry, including the chamfered end faces."""
    body = outer_ring(di, do, 0, height, 0.22)
    cuts = []
    for i in range(grooves):
        angle = 2 * pi * i / grooves
        r = do / 2 + width * 0.22
        cuts.append(Pos(r * cos(angle), r * sin(angle)) *
                    cylinder(width * 2, 0.45, height - 0.45))
    return body.cut(*cuts)


@lru_cache(maxsize=None)
def socket_screw(d, length, head_d, head_h, socket_af, pitch=1.0):
    """Nominal socket screw. Annular thread crests are cosmetic, not helical."""
    head = cylinder(head_d, 0, head_h)
    head = chamfer(head.edges(), min(0.35, head_h * 0.10))
    head -= hexagon(socket_af, head_h - socket_af * 0.62, head_h + 0.1)
    head -= cone(socket_af, socket_af + 0.55, head_h - 0.24, head_h + 0.01)
    threaded = min(length - 1.0, 17.0 if d >= 5 else 6.0)
    root_d = d - 0.72 * pitch
    shaft = cylinder(root_d, -length + 0.45, 0.08)
    shaft += cone(root_d - 0.6, root_d, -length, -length + 0.45)
    if length > threaded:
        shaft += cylinder(d, -length + threaded, 0.08)
    ridges = []
    count = int((threaded - 0.8) / pitch)
    for i in range(count):
        z = -length + 0.60 + i * pitch
        ridges.append(cone(root_d, d, z, z + pitch * 0.27))
        ridges.append(cone(d, root_d, z + pitch * 0.27, z + pitch * 0.65))
    return head + shaft.fuse(*ridges)


def seated_seal(mean_d, cord, z_bottom):
    depth = P.gland_depth(cord)
    cross_section = Plane.XZ * Pos(mean_d / 2, z_bottom + depth / 2) * Ellipse(
        cord * 0.64, depth / 2
    )
    return revolve(cross_section, axis=Axis.Z)


def glass_lens(d, z_mid, thickness=4.3, curvature=95):
    lower = Pos(0, 0, z_mid + curvature - thickness / 2) * Sphere(curvature)
    upper = Pos(0, 0, z_mid - curvature + thickness / 2) * Sphere(curvature)
    return lower & upper & cylinder(d, z_mid - thickness, z_mid + thickness)


def detailed_flow():
    body = plate(P.PLATE, P.PLATE, P.FLOW_T, 4, 0.45)
    body -= C.cyl(P.CASSETTE_D + 0.5, -0.1, P.FLOW_CASSETTE_Z)
    body -= C.cyl(P.EXPOSED_D, P.FLOW_CASSETTE_Z, P.FLOW_CHANNEL_TOP + 0.1)
    body -= C.cyl(P.WINDOW_SEAT_D, P.FLOW_CHANNEL_TOP, P.FLOW_T + 0.1)
    body -= C.gland_down(P.SEAL_WINDOW_D, P.CORD_OPTIC, P.FLOW_CHANNEL_TOP)
    body -= C.gland_up(P.SEAL_BODY_D, P.CORD_BODY, 0)
    for sign in (-1, 1):
        body -= C.radial_port(sign, P.FLOW_CASSETTE_Z + P.PORT_Z_IN_CHANNEL,
                              P.PORT_BORE_D, PORT_TAP_CORE, 5, P.EXPOSED_D)
    body -= C.bolt_holes(P.BOLT_CLEAR_D, -0.1, P.FLOW_T + 0.1)
    body = bore_breaks(body, P.BOLT_XY, P.BOLT_CLEAR_D, 0, P.FLOW_T)
    # Shallow recessed identification area, facing the operator.
    body -= Pos(0, -P.PLATE / 2 + 0.15, 8.8) * Box(47, 0.5, 5.6)
    return body


def detailed_filtrate():
    body = plate(P.PLATE, P.PLATE, P.FIL_T, 4, 0.45)
    body -= cylinder(P.POLARISER_SEAT_D, -0.1, LOWER_WINDOW_T)
    body -= cylinder(P.ILLUM_BORE_D, LOWER_WINDOW_T, P.FIL_T + 0.1)
    body -= C.gland_up(P.SEAL_POLARISER_D, P.CORD_OPTIC, LOWER_WINDOW_T)
    body -= C.radial_port(1, P.FIL_PORT_Z, P.FIL_PORT_BORE_D,
                          PORT_TAP_CORE, 5, P.ILLUM_BORE_D)
    body -= C.bolt_holes(P.BOLT_CLEAR_D, -0.1, P.FIL_T + 0.1)
    body = bore_breaks(body, P.BOLT_XY, P.BOLT_CLEAR_D, 0, P.FIL_T)
    # Four blind mounting holes for the separate lower-window retainer.
    for x, y in ((32, 0), (-32, 0), (0, 32), (0, -32)):
        body -= Pos(x, y) * cylinder(2.5, -0.1, 6)
    body -= Pos(0, -P.PLATE / 2 + 0.15, 11) * Box(47, 0.5, 6.2)
    return body


def detailed_retainer():
    body = plate(P.PLATE, P.PLATE, P.RET_T, 4, 0.45)
    body -= cylinder(P.RET_APERTURE_D, -0.1, P.RET_T + 0.1)
    body -= cylinder(P.WINDOW_D + 1.5, -0.1, WINDOW_RELIEF)
    body -= cone(P.RET_APERTURE_D, P.RET_APERTURE_D + 3.2, P.RET_T - 1.6, P.RET_T + 0.01)
    body -= C.bolt_holes(P.BOLT_CLEAR_D, -0.1, P.RET_T + 0.1)
    body = bore_breaks(body, P.BOLT_XY, P.BOLT_CLEAR_D, 0, P.RET_T)
    # Recesses for washer seats, remain shallow so the clamp chain is explicit.
    return body


def detailed_led_base():
    body = plate(P.PLATE, P.PLATE, P.LED_T, 4, 0.55)
    body -= cylinder(P.LED_PCB_D, P.LED_T - P.LED_PCB_T_POCKET, P.LED_T + 0.1)
    body -= C.bolt_holes(P.BOLT_TAP_CORE_D, P.LED_T - P.BOLT_TAP_DEPTH, P.LED_T + 0.1)
    # Broad parallel heat-sink channels, integral to the base, below the PCB bed.
    for y in (-29, -20, -11, 0, 11, 20, 29):
        body -= Pos(0, y, 1.4) * Box(56, 3.6, 3.0)
    body -= Pos(0, P.PLATE / 2, P.LED_T - 5.5) * Rot(90, 0, 0) * cylinder(7.8, 0, 24)
    for x, y in ((0, 20.5), (0, -20.5)):
        body -= Pos(x, y) * cylinder(2, P.LED_T - 7, P.LED_T - 3.9)
    body -= Pos(0, -P.PLATE / 2 + 0.15, 9.2) * Box(47, 0.5, 6.2)
    return body


def cassette_ring():
    body = outer_ring(P.EXPOSED_D, P.CASSETTE_D, -P.CASSETTE_T, 0, 0.15)
    body -= cylinder(41.2, -0.4, 0.1)
    for angle in (45, 135, 225, 315):
        r = 22.8
        body -= Pos(r * cos(angle * pi / 180), r * sin(angle * pi / 180)) * cylinder(1.6, -0.8, 0.1)
    return body


def membrane_support():
    body = annulus(37.6, 41, -0.35, -MEMBRANE_THICKNESS)
    bars = []
    radius = 19.3
    for v in range(-17, 18, 2):
        length = 2 * sqrt(radius * radius - v * v)
        bars.append(Pos(v, 0) * block(0.13, length, -0.25, -MEMBRANE_THICKNESS))
        bars.append(Pos(0, v) * block(length, 0.13, -0.25, -MEMBRANE_THICKNESS))
    return body.fuse(*bars)


@lru_cache(maxsize=None)
def fitting():
    # Side-fitting local Z is outward from the chamber wall.
    body = hexagon(9.0, 0.6, 5.4)
    body = chamfer(body.edges().filter_by(Axis.Z, reverse=True), 0.3)
    body += cylinder(7.6, 0, 0.65)
    body += cylinder(PORT_TAP_CORE, -4.7, 0.1)
    for i in range(6):
        z = -4.5 + i * 0.69
        body += cone(PORT_TAP_CORE, PORT_THREAD_OD, z, z + 0.2)
        body += cone(PORT_THREAD_OD, PORT_TAP_CORE, z + 0.2, z + 0.48)
    body += cylinder(5.9, 5.3, 7.5)
    body += cylinder(3.8, 7.4, 18.0)
    for z in (8.0, 11.0, 14.0):
        body += cone(4.95, 3.8, z, z + 1.75)
    body += cone(3.8, 3.3, 18, 18.7)
    body -= cylinder(2.0, -4.8, 18.8)
    return body


def make_instrument():
    parts: list[Component] = []

    def add(name, shape, material, group, explode=(0, 0, 0), description="", section=False):
        parts.append(Component(name, shape, material, group, explode, description, section))

    # Machined cell and optical windows. Dry lower polariser is independently retained.
    add("01_flow_chamber", Pos(0, 0, P.Z_FLOW) * detailed_flow(), "aluminium", "cell",
        (0, 0, 28), "90 mm body; 5 mm crossflow gap; two nominal 10-32 side ports", True)
    add("02_filtrate_chamber", Pos(0, 0, P.Z_FIL) * detailed_filtrate(), "aluminium", "cell",
        (0, 0, -17), "40 mm optical plenum, separate pressure window and outlet", True)
    add("03_window_retainer", Pos(0, 0, P.Z_RET) * detailed_retainer(), "aluminium", "cell",
        (0, 0, 64), "Chamfered viewing aperture and recessed compliant window pad", True)
    add("04_upper_quartz_window", cylinder(P.WINDOW_D, P.CHANNEL_H,
        P.CHANNEL_H + P.WINDOW_T), "quartz", "windows", (0, 0, 48),
        "63.5 × 6.35 mm fused-silica envelope", True)
    add("05_window_cushion", annulus(P.RET_APERTURE_D + 0.2, P.WINDOW_D,
        P.CHANNEL_H + P.WINDOW_T, P.CHANNEL_H + P.WINDOW_T + WINDOW_PAD_T),
        "ptfe", "seals", (0, 0, 57), "0.30 mm nominal compliant clamp pad", True)
    add("06_membrane_carrier", cassette_ring(), "ptfe", "membrane", (0, 0, 7),
        "47 mm carrier with a separate membrane and support screen", True)
    add("07_membrane_sheet", cylinder(41, -MEMBRANE_THICKNESS, 0), "membrane", "membrane",
        (0, 0, 12), "Representative sheet; 25 × 25 mm observation area fits the clear aperture", True)
    add("08_membrane_support_screen", membrane_support(), "stainless", "membrane",
        (0, 0, 4), "Illustrative 2 mm pitch support screen; pore/support design unverified", True)
    add("09_lower_quartz_window", cylinder(LOWER_WINDOW_D, P.Z_FIL, P.Z_FIL + LOWER_WINDOW_T),
        "quartz", "windows", (0, 0, -29), "Pressure window separates filtrate from dry polariser", True)

    # A small annular retainer catches the lower glass, with four actual screws.
    lower_ret = outer_ring(43, 70, -1.2, 0, 0.15)
    retention_xy = ((32, 0), (-32, 0), (0, 32), (0, -32))
    for x, y in retention_xy:
        lower_ret -= Pos(x, y) * cylinder(3.4, -1.3, 0.1)
    add("10_lower_window_retainer", Pos(0, 0, P.Z_FIL) * lower_ret,
        "black_anodised", "windows", (0, 0, -36), section=True)
    for i, (x, y) in enumerate(retention_xy):
        add(f"lower_retainer_screw_{i+1}", Pos(x, y, P.Z_FIL - 1.2) * Rot(180, 0, 0) *
            socket_screw(3, 6, 5.3, 2.5, 2.5, 0.5), "stainless", "fasteners", (0, 0, -41))

    seal_defs = (
        ("window_seal", P.SEAL_WINDOW_D, P.CORD_OPTIC,
         P.CHANNEL_H - P.gland_depth(P.CORD_OPTIC), 37),
        ("cell_face_seal", P.SEAL_BODY_D, P.CORD_BODY, P.Z_FLOW, 20),
        ("lower_window_seal", P.SEAL_POLARISER_D, P.CORD_OPTIC,
         P.Z_FIL + LOWER_WINDOW_T, -23),
    )
    for name, d, cord, z, dz in seal_defs:
        add(name, seated_seal(d, cord, z), "seal", "seals", (0, 0, dz),
            "Nominal compressed cross-section; seal chemistry and squeeze need specification", True)

    # Three individually labelled hollow fittings, including compliant tubing stubs.
    port_defs = (
        ("sample_in", -P.PLATE / 2, P.PORT_Z_IN_CHANNEL, -90, (-25, 0, 28)),
        ("backwash", P.PLATE / 2, P.PORT_Z_IN_CHANNEL, 90, (25, 0, 28)),
        ("filtrate_out", P.PLATE / 2, FIL_PORT_Z, 90, (25, 0, -17)),
    )
    for name, x, z, angle, delta in port_defs:
        loc = Pos(x, 0, z) * Rot(0, angle, 0)
        add(f"fitting_{name}", loc * fitting(), "stainless", "fluidics", delta,
            "Hex shoulder, cosmetic male thread, hollow tapered barb", True)
        add(f"tube_{name}", loc * annulus(4.5, 6.6, 9.0, 37.0), "silicone", "tubing",
            delta, "Flexible silicone tube stub; interference over barbs is intentional")

    # Dry illumination: the gap makes polariser adjustment accessible.
    add("11_led_heat_sink", Pos(0, 0, Z_LED) * detailed_led_base(), "aluminium", "illumination",
        (0, 0, -90), "Machined LED carrier with integral underside heat-sink channels", True)
    for i, (x, y) in enumerate(P.BOLT_XY):
        add(f"dry_gap_spacer_{i+1}", Pos(x, y) * outer_ring(6.6, 11.0,
            Z_LED + P.LED_T, P.Z_FIL, 0.35), "stainless", "fasteners", (0, 0, -74))

    polariser_ring = Pos(0, 0, POLARISER_Z) * grip_ring(43, POLARISER_OD, 6.6, 100, 0.48)
    polariser_ring -= Pos(0, -31, POLARISER_Z + 3.3) * Rot(90, 0, 0) * cylinder(2.85, -3.05, 0)
    add("12_polariser_rotation_ring", polariser_ring,
        "black_anodised", "polariser", (0, 0, -53), "Scalloped rotating holder; mounted in dry optical gap", True)
    add("13_polariser", cylinder(43, POLARISER_Z + 2.7, POLARISER_Z + 3.5),
        "polarising_glass", "polariser", (0, 0, -53), "Representative laminated linear polariser", True)
    add("polariser_bezel_top", annulus(40.8, 43, POLARISER_Z + 3.5, POLARISER_Z + 4.3),
        "black_anodised", "polariser", (0, 0, -53), section=True)
    add("polariser_bezel_bottom", annulus(40.8, 43, POLARISER_Z + 1.9, POLARISER_Z + 2.7),
        "black_anodised", "polariser", (0, 0, -53), section=True)
    add("polariser_index_pin", Pos(0, -31, POLARISER_Z + 3.3) * Rot(90, 0, 0) * cylinder(2.8, -3, 3),
        "stainless", "polariser", (0, 0, -53))
    # Four spring clips capture the rotating ring against the window retainer.
    # The cardinal positions stay clear for the window-retainer socket heads.
    clip_top = P.Z_FIL - 1.2
    clip_bottom = POLARISER_Z - 0.8
    for angle in (45, 135, 225, 315):
        clip = Pos(34.9, 0) * block(2.0, 4.0, clip_bottom, clip_top)
        clip += Pos(31.7, 0) * block(8.4, 4.0, clip_bottom, POLARISER_Z)
        clip += Pos(31.7, 0) * block(8.4, 4.0, POLARISER_Z + 6.6, clip_top)
        add(f"polariser_retention_clip_{angle}", Rot(0, 0, angle) * clip,
            "stainless", "polariser", (0, 0, -45),
            "Representative spring retention clip; attachment detail to be specified")

    pcb_z = Z_LED + P.LED_T - P.LED_PCB_T_POCKET
    pcb = cylinder(P.LED_PCB_D - 2, pcb_z, pcb_z + P.LED_PCB_T)
    for y in (-20.5, 20.5):
        pcb -= Pos(0, y) * cylinder(2.6, pcb_z - 0.1, pcb_z + 2)
    add("14_led_array_board", pcb, "pcb", "illumination", (0, 0, -84), section=True)
    led_i = 0
    for row in range(-2, 3):
        for col in range(-2, 3):
            x = P.LED_PITCH * (col + row * 0.5)
            y = P.LED_PITCH * row * sqrt(3) / 2
            if x*x + y*y > (P.LED_PITCH * 2.05)**2:
                continue
            led_i += 1
            z = pcb_z + P.LED_PCB_T
            add(f"led_ceramic_{led_i:02d}", Pos(x, y, z) * plate(3.5, 3.5, 0.55, 0.25, 0.08),
                "ceramic", "illumination", (0, 0, -84))
            dome = (Pos(x, y, z + 0.53) * Sphere(1.38)) & Pos(x, y) * cylinder(2.76, z+0.53, z+2.0)
            add(f"led_dome_{led_i:02d}", dome, "led", "illumination", (0, 0, -84))
            for sign in (-1, 1):
                add(f"led_pad_{led_i:02d}_{sign}", Pos(x + sign * 2.15, y) *
                    block(0.8, 2.5, z, z + 0.06), "gold", "illumination", (0, 0, -84))
    for i, y in enumerate((-20.5, 20.5)):
        add(f"pcb_screw_{i+1}", Pos(0, y, pcb_z + P.LED_PCB_T) * socket_screw(2.5, 4, 4.4, 1.7, 2, 0.45),
            "stainless", "fasteners", (0, 0, -84))
    add("15_diffuser", cylinder(44, Z_LED + P.LED_T + 0.55, Z_LED + P.LED_T + 1.55),
        "diffuser", "illumination", (0, 0, -69), "1 mm diffuser envelope above the 19 green emitters", True)
    add("diffuser_carrier", outer_ring(42, 48, Z_LED + P.LED_T + 0.05,
        Z_LED + P.LED_T + 0.55, 0.08), "black_anodised", "illumination", (0, 0, -69), section=True)
    gland_z = Z_LED + P.LED_T - 5.5
    add("led_power_gland", Pos(0, 45, gland_z) * Rot(-90, 0, 0) *
        grip_ring(4.5, 11, 8, 24, 0.4), "black_anodised", "illumination", (0, 0, -90))
    add("led_power_lead", Pos(0, 45, gland_z) * Rot(-90, 0, 0) * cylinder(4.4, 0, 28),
        "rubber_grip", "tubing", (0, 0, -90))

    # Optical train: separate focus/iris rings, stepped barrel and curved elements.
    front_z = P.LENS_FRONT_STANDOFF
    analyzer_z = front_z - P.ANALYSER_T
    add("16_analyser_rotation_ring", Pos(0, 0, analyzer_z) * grip_ring(34.5, 42, 8, 78, 0.36),
        "black_anodised", "analyser", (0, 0, 82), "Knurled, independently rotatable analyser", True)
    add("17_analyser", cylinder(34.5, analyzer_z + 3, analyzer_z + 5), "polarising_glass", "analyser",
        (0, 0, 82), section=True)
    add("analyser_retaining_bezel", annulus(32.5, 34.5, analyzer_z + 1.8, analyzer_z + 3),
        "black_anodised", "analyser", (0, 0, 82), section=True)

    barrel_defs = (
        ("18_lens_front_cell", 35, 41.5, 0, 7),
        ("lens_forward_barrel", 33, 39.8, 7, 22),
        ("lens_focus_end_ring", 33, 43.6, 22, 23.2),
        ("lens_scale_barrel", 31, 40.8, 40, 50),
        ("lens_rear_barrel", 26, 37.8, 57, 68.5),
        ("lens_mount_adapter", 25.4, 31.5, 68.5, 72),
    )
    for name, di, do, z0, z1 in barrel_defs:
        add(name, outer_ring(di, do, front_z + z0, front_z + z1, 0.22),
            "black_anodised", "lens", (0, 0, 97), section=True)
    focus_ring = Pos(0, 0, front_z + 23.2) * grip_ring(33, 46, 16.8, 112, 0.42)
    focus_ring -= Pos(0, -22.9, front_z + 33) * Rot(90, 0, 0) * cylinder(2.1, -4, 0.6)
    add("19_focus_ring", focus_ring,
        "rubber_grip", "lens", (0, 0, 97), "112 real machined/grip scallops", True)
    add("20_aperture_ring", Pos(0, 0, front_z + 50) * grip_ring(28, 42.8, 7, 72, 0.39),
        "black_anodised", "lens", (0, 0, 97), section=True)
    for n, z, d in (("focus", 40.15, 40.82), ("aperture", 57.15, 37.82)):
        add(f"lens_silver_witness_{n}", annulus(d, d + 0.08, front_z + z, front_z + z + 0.22),
            "edge_metal", "lens", (0, 0, 97))
    add("lens_front_element", glass_lens(34.8, front_z + 4), "optical_glass", "lens", (0, 0, 97),
        "Curved representative front optical element; not an optical prescription", True)
    add("lens_element_retainer", annulus(32, 35, front_z + 1.1, front_z + 2.1),
        "black_anodised", "lens", (0, 0, 97), section=True)
    add("lens_internal_baffle", annulus(15, 28, front_z + 49.2, front_z + 49.8),
        "black_anodised", "lens", (0, 0, 97), section=True)
    add("lens_rear_element", glass_lens(24.8, front_z + 65, 2.6, 85),
        "optical_glass", "lens", (0, 0, 97), section=True)
    add("focus_lock_screw", Pos(0, -22.9, front_z + 33) * Rot(90, 0, 0) *
        socket_screw(2.5, 3.5, 4.5, 2.5, 2, 0.45), "stainless", "lens", (0, 0, 97))

    # Machined machine-vision housing, service covers and rear connectors.
    cz = CAMERA_Z
    add("camera_mount_flange", outer_ring(25.4, 32, cz, cz + P.CMOUNT_T, 0.3),
        "stainless", "camera", (0, 0, 119), section=True)
    cam_bottom = cz + P.CMOUNT_T
    lower = plate(P.CAM_W, P.CAM_W, 3.0, 2.8, 0.25)
    lower -= cylinder(25.4, -0.1, 3.1)
    add("21_camera_front_cover", Pos(0, 0, cam_bottom) * lower, "aluminium", "camera", (0, 0, 119), section=True)
    main = plate(P.CAM_W, P.CAM_W, CAMERA_HEIGHT - 6.0, 2.8, 0.35)
    main -= block(36, 36, -0.1, CAMERA_HEIGHT - 5.9)
    for x, y in ((-17, -17), (17, -17), (-17, 17), (17, 17)):
        main += Pos(x, y) * cylinder(6.3, 0, CAMERA_HEIGHT - 6.0)
    # Cooling channels in the two sidewalls, shallow enough to retain the housing.
    for sign in (-1, 1):
        for z in (5, 8, 11, 14, 17, 20, 23):
            main -= Pos(sign * 21.7, 0, z) * Box(1.1, 30, 0.9)
    # Two rear connector recesses; no arbitrary electronic internals are claimed.
    main -= Pos(-7.8, 20.6, 10) * Box(12.8, 4, 6.0)
    main -= Pos(9.4, 22.5, 10) * Rot(90, 0, 0) * cylinder(8.2, 0, 6)
    for x, y in ((-17, -17), (17, -17), (-17, 17), (17, 17)):
        main -= Pos(x, y) * cylinder(2.1, CAMERA_HEIGHT - 13, CAMERA_HEIGHT - 5.8)
    add("22_camera_housing", Pos(0, 0, cam_bottom + 3) * main, "aluminium", "camera", (0, 0, 119),
        "Separate covers, rounded edges, side cooling slots and connector openings", True)
    top_z = cam_bottom + CAMERA_HEIGHT - 3
    top = plate(P.CAM_W, P.CAM_W, 3, 2.8, 0.25)
    for x, y in ((-17, -17), (17, -17), (-17, 17), (17, 17)):
        top -= Pos(x, y) * cylinder(2.8, -0.1, 3.1)
        top -= Pos(x, y) * cylinder(5.0, 1.2, 3.1)
    add("23_camera_rear_cover", Pos(0, 0, top_z) * top, "aluminium", "camera", (0, 0, 134), section=True)
    for i, (x, y) in enumerate(((-17, -17), (17, -17), (-17, 17), (17, 17))):
        add(f"camera_cover_screw_{i+1}", Pos(x, y, top_z + 1.2) * socket_screw(2.5, 7, 4.4, 1.7, 2, 0.45),
            "stainless", "camera", (0, 0, 141))
    add("camera_id_plate", Pos(0, -22.02, cam_bottom + 17) * Box(26, 0.2, 13),
        "label", "camera", (0, 0, 119))
    usb_loc = Pos(-7.8, 21.25, cam_bottom + 13) * Rot(-90, 0, 0)
    usb_shell = block(12.3, 5.4, 0, 2.4) - block(10.8, 3.9, -0.1, 2.5)
    add("camera_usb_shell", usb_loc * usb_shell, "stainless", "camera", (0, 0, 119))
    add("camera_usb_insulator", usb_loc * block(10.7, 3.8, 0, 1.4), "rubber_grip", "camera", (0, 0, 119))
    add("camera_usb_tongue", usb_loc * block(8.2, 0.6, 1.4, 2), "green_pcb", "camera", (0, 0, 119))
    io_loc = Pos(9.4, 20.5, cam_bottom + 13) * Rot(-90, 0, 0)
    add("camera_io_shell", io_loc * outer_ring(5.8, 8.0, 0, 4.8, 0.15), "stainless", "camera", (0, 0, 119))
    add("camera_io_insulator", io_loc * cylinder(5.7, 0, 3), "rubber_grip", "camera", (0, 0, 119))
    for i in range(6):
        angle = 2 * pi * i / 6
        add(f"camera_io_pin_{i+1}", io_loc * Pos(1.7 * cos(angle), 1.7 * sin(angle)) *
            cylinder(0.65, 3, 4.3), "gold", "camera", (0, 0, 119))

    # Four main clamp screws with washers; they engage the LED plate blind holes.
    head_z = P.Z_RET + P.RET_T + WASHER_T
    for i, (x, y) in enumerate(P.BOLT_XY):
        add(f"clamp_washer_{i+1}", Pos(x, y) * outer_ring(6.4, 12.8,
            head_z - WASHER_T, head_z, 0.18), "stainless", "fasteners", (0, 0, 64))
        add(f"clamp_screw_m6x70_{i+1}", Pos(x, y, head_z) * socket_screw(6, SCREW_LENGTH, 10, 6, 5),
            "stainless", "fasteners", (0, 0, 127), "5 mm hex socket; cosmetic annular thread crests")

    return parts


def assembly(parts, exploded=False):
    return Compound(label="membrane_fouling_cell_realistic", children=[p.as_shape(exploded) for p in parts])


def cutaway_parts(parts):
    """Actual B-rep half-section at Y=0; complete hidden rear halves retained."""
    keep = Pos(0, 125, 65) * Box(350, 250, 420)
    result = []
    for p in parts:
        if p.section:
            shape = p.shape & keep
            if shape is None or not shape.solids():
                continue
            result.append(Component(p.name, shape, p.material, p.group,
                                    p.explode, p.description, False))
        elif p.group in ("fasteners", "illumination"):
            if p.shape.bounding_box().max.Y < -0.2:
                continue
            result.append(p)
        elif p.group == "tubing":
            continue
        else:
            result.append(p)
    return result
