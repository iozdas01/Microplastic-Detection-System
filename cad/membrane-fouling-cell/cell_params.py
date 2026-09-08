"""Parameter block for the polarised-light membrane fouling cell.

Every dimension in the four machined bodies derives from this file. Datum for
the whole stack is the MEMBRANE TOP SURFACE at global Z = 0, +Z along the
optical path toward the camera. Each part is modelled in its own local frame
with local Z = 0 at its own bottom face; the assembly stacks them.

NUMBERS ARE ASSUMED, not measured off the reference render. Anything tagged
[GUESS] should be replaced with the real value; the derived geometry follows.
"""

from math import hypot

# --------------------------------------------------------------------------
# Optics — the imaging side. These drive every bore above the membrane.
# --------------------------------------------------------------------------
ACTIVE_W = 25.0                 # imaged active area, mm (from the reference)
ACTIVE_H = 25.0
ACTIVE_DIAG = hypot(ACTIVE_W, ACTIVE_H)      # 35.355 mm — the real field size

LENS_FOCAL = 50.0               # "MACRO 1:1  f = 50 mm" from the reference
LENS_MAG = 1.0                  # 1:1
LENS_FNUM = 4.0                 # [GUESS] working aperture
WORKING_DIST = LENS_FOCAL * (1.0 + 1.0 / LENS_MAG)   # object -> front principal plane
ENTRANCE_PUPIL_D = LENS_FOCAL / LENS_FNUM
OPTICAL_MARGIN = 1.5            # radial mm of slop added to every clear bore


def clear_aperture_d(z: float) -> float:
    """Minimum clear bore diameter at height z above the membrane.

    Envelope of every ray from the corner of the active area to the edge of the
    lens entrance pupil. Shrinks with height because the bundle converges on the
    pupil. A bore smaller than this vignettes the corners of the image -- and you
    do not find that out until the parts are machined and you take a picture.
    """
    r_obj = ACTIVE_DIAG / 2.0
    r_pup = ENTRANCE_PUPIL_D / 2.0
    t = min(max(z / WORKING_DIST, 0.0), 1.0)
    return 2.0 * (r_obj + (r_pup - r_obj) * t + OPTICAL_MARGIN)


# Illumination side (below the membrane) wants to be generous, not tight:
# uniformity matters more than stray light here.
ILLUM_BORE_D = 40.0

# --------------------------------------------------------------------------
# O-ring glands (ISO 3601 / AS568 static face seal)
#   depth = cord * (1 - squeeze)      width = cord * 1.3   (fill <= 90%)
# Change a cord size and every groove, land and stack height follows.
# --------------------------------------------------------------------------
SQUEEZE = 0.25                  # 20-30% for a static face seal

CORD_BODY = 2.62                # AS568 0.103" — body-to-body pressure seals
CORD_OPTIC = 1.78               # AS568 0.070" — light seals onto glass


def gland_depth(cord: float) -> float:
    return cord * (1.0 - SQUEEZE)


def gland_width(cord: float) -> float:
    return cord * 1.30


# Mean seal diameters
SEAL_WINDOW_D = 52.0            # quartz window -> flow chamber
SEAL_BODY_D = 56.0              # flow chamber -> filtrate chamber
SEAL_BASE_D = 60.0              # filtrate chamber -> LED base plate
SEAL_POLARISER_D = 46.0         # polariser -> filtrate chamber (retains filtrate)

# --------------------------------------------------------------------------
# Purchased parts — dimensions are INPUTS, never modelled guesses
# --------------------------------------------------------------------------
WINDOW_D = 63.5                 # [GUESS] 2.5" stock quartz disc
WINDOW_T = 6.35                 # 0.25"
WINDOW_SEAT_D = WINDOW_D + 0.5  # radial clearance in the seat
WINDOW_PROUD = 0.35             # sits above the flow-chamber top face; the
                                # retainer clamps the glass, not the aluminium

CASSETTE_D = 47.0               # "47 mm membrane cassette" from the reference
CASSETTE_T = 3.5                # [GUESS]

POLARISER_D = 50.8              # 2". A 25 mm polariser would vignette a
POLARISER_T = 3.0               # 35.4 mm field -- see check_optics() below.
POLARISER_SEAT_D = POLARISER_D + 0.5

LED_PCB_D = 48.0                # [GUESS] 530 nm array carrier
LED_PCB_T_POCKET = 4.0          # pocket depth for the PCB + domes

# --------------------------------------------------------------------------
# Plate footprint and fasteners
# --------------------------------------------------------------------------
PLATE = 90.0                    # [GUESS] square footprint
BOLT_OFFSET = 34.0              # 4x at (+/-34, +/-34)
BOLT_CLEAR_D = 6.6              # M6 normal clearance
BOLT_TAP_CORE_D = 5.0           # M6 tapping drill
BOLT_TAP_DEPTH = 14.0
BOLT_LEN = 55.0                 # M6 x 55 SHCS
BOLT_HEAD_D = 10.0
BOLT_HEAD_T = 6.0

BOLT_XY = [
    (-BOLT_OFFSET, -BOLT_OFFSET),
    (+BOLT_OFFSET, -BOLT_OFFSET),
    (-BOLT_OFFSET, +BOLT_OFFSET),
    (+BOLT_OFFSET, +BOLT_OFFSET),
]

# --------------------------------------------------------------------------
# Hydraulics
# --------------------------------------------------------------------------
CHANNEL_H = 5.0                 # *** THE EXPERIMENTAL VARIABLE ***
                                # crossflow gap over the membrane -> wall shear.
                                # Constrained from below by the port geometry;
                                # see check_channel_vs_port().

EXPOSED_D = round(clear_aperture_d(0.0) * 2) / 2   # membrane area actually imaged
FILTRATE_PLENUM_H = 8.0

PORT_BORE_D = 2.0               # 10-32 flat-bottom fluidic port
PORT_BOSS_D = 6.4
PORT_BOSS_DEPTH = 5.0
PORT_Z_IN_CHANNEL = 2.2         # port axis above the channel floor

FIL_PORT_BORE_D = 3.0           # filtrate side runs bigger, lower velocity
FIL_PORT_BOSS_D = 8.5
FIL_PORT_BOSS_DEPTH = 6.0

# --------------------------------------------------------------------------
# Body heights (local, bottom face = 0)
# --------------------------------------------------------------------------
FLOW_CASSETTE_Z = CASSETTE_T                       # 0 .. 3.5  cassette recess
FLOW_CHANNEL_TOP = FLOW_CASSETTE_Z + CHANNEL_H     # window seats here
FLOW_T = FLOW_CHANNEL_TOP + WINDOW_T - WINDOW_PROUD

FIL_T = 20.0
LED_T = 16.0
RET_T = 8.0

# Global Z of each part's bottom face, stacked off the membrane datum
Z_FLOW = -CASSETTE_T
Z_FIL = Z_FLOW - FIL_T
Z_LED = Z_FIL - LED_T
Z_RET = Z_FLOW + FLOW_T

RET_APERTURE_D = round(clear_aperture_d(Z_RET) + 1.0, 1)


# --------------------------------------------------------------------------
# Self-checks. These are the couplings a GUI cannot hold for you.
# --------------------------------------------------------------------------
def check_optics() -> list[str]:
    """Every bore on the imaging path must clear the ray envelope."""
    notes = []
    checks = [
        ("flow chamber channel", EXPOSED_D, 0.0),
        ("window seat bore", WINDOW_SEAT_D, CHANNEL_H),
        ("window retainer aperture", RET_APERTURE_D, Z_RET),
    ]
    for name, have, z in checks:
        need = clear_aperture_d(z)
        if have < need:
            raise ValueError(
                f"{name} is {have:.2f} mm at z={z:.1f}; needs >= {need:.2f} mm "
                f"or it vignettes the {ACTIVE_W:.0f}x{ACTIVE_H:.0f} mm field"
            )
        notes.append(f"{name}: {have:.2f} >= {need:.2f} mm  (+{have - need:.2f})")

    # Illumination side: the polariser is a bought part and is the usual trap.
    pol_clear = POLARISER_D * 0.90          # typical mounted clear aperture
    if pol_clear < ACTIVE_DIAG:
        raise ValueError(
            f"polariser clear aperture ~{pol_clear:.1f} mm cannot pass the "
            f"{ACTIVE_DIAG:.1f} mm field diagonal"
        )
    notes.append(f"polariser clear ~{pol_clear:.1f} >= {ACTIVE_DIAG:.1f} mm field diagonal")
    return notes


def check_channel_vs_port() -> str:
    """The window seal gland eats into the channel roof from above; the inlet
    port bore comes at it from the side. If they meet, the port breaks into the
    seal groove and the cell leaks. This is what sets the minimum channel height.
    """
    groove_floor = FLOW_CHANNEL_TOP - gland_depth(CORD_OPTIC)
    port_top = FLOW_CASSETTE_Z + PORT_Z_IN_CHANNEL + PORT_BORE_D / 2.0
    clearance = groove_floor - port_top
    if clearance < 0.3:
        min_h = 2.0 * (PORT_BORE_D / 2.0 + gland_depth(CORD_OPTIC) + 0.3)
        raise ValueError(
            f"inlet port breaks into the window seal gland (clearance "
            f"{clearance:.3f} mm). With a {CORD_OPTIC} mm cord and a "
            f"{PORT_BORE_D} mm port, CHANNEL_H must be >= {min_h:.2f} mm."
        )
    return f"port/gland clearance: {clearance:.3f} mm"


def check_lands() -> list[str]:
    """Every gland needs metal either side of it to seal against."""
    notes = []
    beds = [
        ("window seal", SEAL_WINDOW_D, CORD_OPTIC, EXPOSED_D, WINDOW_SEAT_D),
        ("body seal", SEAL_BODY_D, CORD_BODY, CASSETTE_D, PLATE),
        ("base seal", SEAL_BASE_D, CORD_BODY, POLARISER_SEAT_D, PLATE),
        ("polariser seal", SEAL_POLARISER_D, CORD_OPTIC, ILLUM_BORE_D, POLARISER_SEAT_D),
    ]
    for name, mean_d, cord, inner_d, outer_d in beds:
        half_w = gland_width(cord) / 2.0
        land_in = (mean_d - 2 * half_w - inner_d) / 2.0
        land_out = (outer_d - mean_d - 2 * half_w) / 2.0
        if min(land_in, land_out) < 0.8:
            raise ValueError(
                f"{name} gland has {min(land_in, land_out):.2f} mm of land; "
                f"needs >= 0.8 mm inboard and outboard"
            )
        notes.append(f"{name}: land {land_in:.2f} in / {land_out:.2f} out")
    return notes


def check_bolts() -> str:
    """Bolt holes must miss the largest bore and stay off the plate edge."""
    from math import sqrt
    radius = sqrt(2) * BOLT_OFFSET
    inner = radius - BOLT_CLEAR_D / 2.0
    biggest_bore_r = WINDOW_SEAT_D / 2.0
    if inner <= biggest_bore_r:
        raise ValueError(
            f"bolt holes reach r={inner:.1f} mm, into the {WINDOW_SEAT_D} mm seat"
        )
    edge = PLATE / 2.0 - BOLT_OFFSET - BOLT_CLEAR_D / 2.0
    if edge < 3.0:
        raise ValueError(f"only {edge:.1f} mm of material outboard of the bolt holes")
    return f"bolts: {inner - biggest_bore_r:.1f} mm off the seat, {edge:.1f} mm to the edge"


def validate() -> list[str]:
    notes = []
    notes += check_optics()
    notes.append(check_channel_vs_port())
    notes += check_lands()
    notes.append(check_bolts())
    return notes


validate()

# Late additions referenced by cell_parts
FIL_PORT_Z = FIL_T - 6.0        # filtrate port axis, local to the filtrate body
CABLE_D = 8.0                   # LED cable exit
RET_RELIEF = 0.2                # retainer relief over the window seat face

# --------------------------------------------------------------------------
# Rest of the instrument — bought-part envelopes only, all [GUESS]
# --------------------------------------------------------------------------
LENS_FRONT_STANDOFF = 70.0      # membrane top -> front face of the lens/analyser stack
LENS_BODY_D = 40.0              # 50 mm 1:1 macro barrel
LENS_LEN = 72.0
LENS_RING_D = 46.0              # focus ring
LENS_RING_T = 14.0
LENS_RING_Z = 22.0              # ring position from the lens front
ANALYSER_D = 42.0               # threaded filter ring on the lens front
ANALYSER_T = 8.0
ANALYSER_GLASS_D = 34.0
CAM_W = 44.0                    # boxy machine-vision camera, C-mount
CAM_L = 50.0
CMOUNT_D = 25.4
CMOUNT_T = 5.0
FITTING_HEX_AF = 9.0            # push-in / barb fittings on the ports
FITTING_HEX_T = 6.0
FITTING_BARB_D = 4.5
FITTING_BARB_L = 12.0
LED_PCB_T = 1.6                 # aluminium-core PCB in the pocket
LED_DOME_D = 4.0
LED_DOME_H = 2.0
LED_PITCH = 8.0                 # 19-up hex array

# --------------------------------------------------------------------------
# Materials — one author for the colour written into the STEP and the name
# that goes on the drawing / BOM. Keyed by the part label's first token.
# --------------------------------------------------------------------------
MATERIALS = {
    # label            (material / finish,                          STEP colour)
    "led_base_plate":   ("6082-T6 aluminium, clear anodised",         "#c9cfd4"),
    "filtrate_chamber": ("6082-T6 aluminium, clear anodised",         "#c9cfd4"),
    "flow_chamber":     ("6082-T6 aluminium, clear anodised",         "#c9cfd4"),
    "window_retainer":  ("6082-T6 aluminium, clear anodised",         "#c9cfd4"),
    "quartz_window":    ("UV fused silica, 60/40 scratch-dig",         "#bfe0f7"),
    "analyser_glass":   ("linear polariser, glass laminated",          "#bfe0f7"),
    "polariser":        ("linear polariser, glass laminated",          "#3a4b5c"),
    "membrane_cassette":("PTFE membrane in PP cassette (consumable)",  "#efece2"),
    "o_ring":           ("FKM (Viton) 75 Shore A",                     "#d0602a"),
    "m6_shcs":          ("A2-70 stainless, ISO 4762",                  "#b4b9bd"),
    "fitting":          ("nickel-plated brass, 10-32 barb",            "#c2c6c7"),
    "camera":           ("machine-vision camera, C-mount (bought)",    "#8e959c"),
    "macro_lens":       ("50 mm 1:1 macro, black anodised (bought)",   "#202429"),
    "analyser":         ("filter ring, black anodised (bought)",       "#1a1d21"),
    "led_pcb":          ("aluminium-core PCB, white solder mask",      "#f2f2ee"),
    "led_array":        ("530 nm LED, 4 mm dome, 19-up",               "#3ef06a"),
}


def material_of(label: str):
    return MATERIALS.get(label.split(":")[0])
