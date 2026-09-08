"""Membrane fouling cell — the whole instrument.

Four machined bodies bolted on a shared bolt circle and optical axis, plus
envelopes for everything bought: camera, 50 mm macro lens, analyser, quartz
window, membrane cassette, polariser, 530 nm LED array, O-rings, port
fittings and bolts. The LED base plate is the fixed root; everything stacks
up from it via face-to-face mates whose offsets come from cell_params.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Color, Location  # noqa: E402
from cadgen.assembly import AssemblyHelper  # noqa: E402

import cell_params as P  # noqa: E402
import cell_parts as C  # noqa: E402


def gen_step():
    asm = AssemblyHelper("membrane_fouling_cell")
    _add = asm.add

    def add(shape, name, *details):
        mat = P.material_of(name)
        return _add(shape, name, *details, color=Color(mat[1]) if mat else None)

    asm.add = add
    F = asm.rigid_frame
    Z = lambda z: Location((0, 0, z))  # noqa: E731

    # --- machined stack ------------------------------------------------------
    led = asm.add(C.led_base_plate(), "led_base_plate")
    fil = asm.add(C.filtrate_chamber(), "filtrate_chamber")
    flow = asm.add(C.flow_chamber(), "flow_chamber")
    ret = asm.add(C.window_retainer(), "window_retainer")

    led_top, fil_bot = F(led, "top_face", Z(P.LED_T)), F(fil, "bottom_face", Z(0))
    fil_top, flow_bot = F(fil, "top_face", Z(P.FIL_T)), F(flow, "bottom_face", Z(0))
    flow_top, ret_bot = F(flow, "top_face", Z(P.FLOW_T)), F(ret, "bottom_face", Z(0))

    # --- everything bought, with the seat it sits in --------------------------
    # (fixed frame on the carrier, moving frame at the part's own origin)
    seats = []

    def seat(part, name, carrier, location):
        seats.append((F(carrier, f"seat_{name}", location), F(part, "base", Z(0)), name))

    membrane_z = P.CASSETTE_T                       # membrane top, local to flow
    d_body, d_optic = P.gland_depth(P.CORD_BODY), P.gland_depth(P.CORD_OPTIC)

    seat(asm.add(C.polariser("polariser_530nm"), "polariser"), "polariser", fil, Z(0))
    seat(asm.add(C.membrane_cassette(), "membrane_cassette"), "cassette", flow, Z(0))
    seat(asm.add(C.quartz_window(), "quartz_window"), "window", flow, Z(P.FLOW_CHANNEL_TOP))

    seat(asm.add(C.o_ring(P.SEAL_WINDOW_D, P.CORD_OPTIC), "o_ring", "window"),
         "oring_window", flow, Z(P.FLOW_CHANNEL_TOP - d_optic / 2))
    seat(asm.add(C.o_ring(P.SEAL_BODY_D, P.CORD_BODY), "o_ring", "body"),
         "oring_body", flow, Z(d_body / 2))
    seat(asm.add(C.o_ring(P.SEAL_POLARISER_D, P.CORD_OPTIC), "o_ring", "polariser"),
         "oring_polariser", fil, Z(P.POLARISER_T - d_optic / 2))
    seat(asm.add(C.o_ring(P.SEAL_BASE_D, P.CORD_BODY), "o_ring", "base"),
         "oring_base", fil, Z(d_body / 2))

    lens_front = membrane_z + P.LENS_FRONT_STANDOFF
    ring, glass = C.analyser()
    seat(asm.add(ring, "analyser"), "analyser", flow, Z(lens_front - P.ANALYSER_T))
    seat(asm.add(glass, "analyser_glass"), "analyser_glass", flow, Z(lens_front - P.ANALYSER_T))
    seat(asm.add(C.macro_lens(), "macro_lens"), "lens", flow, Z(lens_front))
    seat(asm.add(C.camera(), "camera"), "camera", flow, Z(lens_front + P.LENS_LEN))

    seat(asm.add(C.led_pcb(), "led_pcb"), "led_pcb", led, Z(P.LED_T - P.LED_PCB_T_POCKET))
    seat(asm.add(C.led_array(), "led_array"), "led_array", led,
         Z(P.LED_T - P.LED_PCB_T_POCKET + P.LED_PCB_T))

    port_z = P.FLOW_CASSETTE_Z + P.PORT_Z_IN_CHANNEL
    half = P.PLATE / 2.0
    seat(asm.add(C.port_fitting(), "fitting", "sample_in"), "fit_in", flow,
         Location((-half, 0, port_z), (0, -90, 0)))
    seat(asm.add(C.port_fitting(), "fitting", "backwash"), "fit_bw", flow,
         Location((half, 0, port_z), (0, 90, 0)))
    seat(asm.add(C.port_fitting(), "fitting", "filtrate_out"), "fit_out", fil,
         Location((half, 0, P.FIL_PORT_Z), (0, 90, 0)))

    corners = ("rear_left", "rear_right", "front_left", "front_right")
    for (x, y), corner in zip(P.BOLT_XY, corners):
        seat(asm.add(C.shcs(), "m6_shcs", corner), f"bolt_{corner}", ret, Location((x, y, P.RET_T)))

    # --- mates, root outward ---------------------------------------------------
    asm.face_to_face(led_top, fil_bot, label="filtrate_on_base")
    asm.face_to_face(fil_top, flow_bot, label="flow_on_filtrate")
    asm.face_to_face(flow_top, ret_bot, label="retainer_on_flow")
    for fixed, moving, name in seats:
        asm.face_to_face(fixed, moving, label=name)

    return asm.build()
