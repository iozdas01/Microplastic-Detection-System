"""Parameter block for the phone imaging station — the data-collection rig.

A 47 mm filter membrane lies flat under a cover glass on a tray; an LED panel lights it
from below through a polariser; an iPhone with a clip-on macro lens photographs it from
above through a second polariser. Every printed dimension derives from the optics at the
top of this file. Global datum: the MEMBRANE TOP SURFACE at Z = 0, +Z toward the phone.
Each printed part is modelled with local Z = 0 at its own bottom face; the assembly
stacks them.

NUMBERS TAGGED [GUESS] ARE ASSUMED. Replace each with the measured value from the part
you actually buy; the derived geometry follows. The self-checks at the bottom fail the
build rather than let a bad guess reach the printer silently.
"""

from math import hypot

# --------------------------------------------------------------------------
# Camera — iPhone 17 Pro Max main camera. From published specs; verify.
# --------------------------------------------------------------------------
PHONE_F = 6.9                   # real focal length, mm (24 mm equivalent)
PHONE_FNUM = 1.78
PHONE_PIXEL = 0.00122           # mm, 48 MP mode (0.00244 in the 12 MP binned mode)
SENSOR_W = 9.8                  # mm, 1/1.28" class sensor [GUESS: from crop factor]
SENSOR_H = 7.3

PHONE_L = 163.4                 # body, mm (Apple spec sheet; verify against the phone)
PHONE_W = 78.0
PHONE_T = 8.75
PLATEAU_H = 4.5                 # [GUESS] camera plateau proud of the flat back
PLATEAU_L = 45.0                # [GUESS] plateau extent from the top edge, along the length
CAM_FROM_TOP = 15.0             # [GUESS] main-camera axis from the phone's top short edge
CAM_FROM_SIDE = 14.0            # [GUESS] main-camera axis from the nearer long edge

# --------------------------------------------------------------------------
# Clip-on macro lens — the ONE optic we choose. "10x" means f ≈ 25 mm.
# --------------------------------------------------------------------------
CLIP_F = 25.0                   # [GUESS] focal length = working distance; read it off the box
CLIP_BODY_D = 30.0              # [GUESS] outside diameter of the lens housing
CLIP_BELOW = 8.0                # [GUESS] lens front face below the plateau surface

WORKING_DIST = CLIP_F           # lens front -> membrane, phone focused at infinity
MAG = PHONE_F / CLIP_F
FIELD_W = SENSOR_W / MAG        # object field, mm
FIELD_H = SENSOR_H / MAG
UM_PER_PX = PHONE_PIXEL / MAG * 1000.0
NA_OBJ = (PHONE_F / PHONE_FNUM / 2.0) / CLIP_F
RESOLVE_UM = 0.61 * 0.55 / NA_OBJ
DOF_UM = 0.55 / NA_OBJ ** 2

# --------------------------------------------------------------------------
# Sample — bought parts, dimensions are INPUTS
# --------------------------------------------------------------------------
MEMBRANE_D = 47.0               # PCTE filter disc
MEMBRANE_T = 0.02               # 10-25 µm; effectively zero for the stack
GLASS_D = 50.0                  # round cover glass over the membrane
GLASS_T = 1.0                   # [GUESS] 1 mm slide glass; 0.17 mm cover slips are too floppy
GLASS_CLEAR = 0.5               # radial clearance in the seat

# --------------------------------------------------------------------------
# Light — bought parts
# --------------------------------------------------------------------------
LED_W = 50.0                    # [GUESS] square LED panel
LED_T = 4.0                     # [GUESS]
DIFFUSER_T = 2.0                # [GUESS] opal acrylic
POLARISER_T = 0.3               # linear polarising film, each sheet
POLARISER_W = 60.0              # sheet cut to this square
CABLE_W = 6.0                   # cable exit slot
CABLE_H = 4.0

# --------------------------------------------------------------------------
# Printed bodies
# --------------------------------------------------------------------------
BOX_W = 80.0                    # light box block, square, centred on the optical axis
BOX_H = 22.0
BOX_WALL = 3.0
POCKET_W = LED_W + 1.0          # LED + diffuser pocket
POCKET_DEPTH = LED_T + DIFFUSER_T + 1.0
RAIL_H = 4.0                    # tray rails on the box top, along Y (tray slides in from -Y)
RAIL_W = 4.0

TRAY_W = BOX_W - 2 * RAIL_W - 0.4     # between the rails, X
TRAY_L = BOX_W                        # Y; flush with the box
TRAY_FLOOR = 3.0                      # under the membrane
TRAY_T = TRAY_FLOOR + 3.0             # glass seat is 3 deep; 1 mm glass sits 2 mm below the top
GRIP_L = 12.0                         # tab on the -Y end to pull the tray
TICK_PITCH = 5.0                      # index ticks along the tray edges
TICK_DEPTH = 0.4
TICK_W = 0.6

PLATE_T = 5.0                   # base plate under everything
POST_SQ = 10.0                  # square posts
POST_SCREW_D = 2.5              # M3 self-tap / heat-set pilot in the post ends
SCREW_CLEAR_D = 3.4             # M3 clearance through plate and cradle
CRADLE_T = 6.0
CRADLE_POCKET = 3.0             # phone sits this deep in the cradle
CRADLE_MARGIN = 10.0            # plate beyond the phone outline
PHONE_CLEAR = 0.6               # pocket clearance on length and width
CAM_CUTOUT_L = PLATEAU_L + 6.0  # opening under the plateau + clip, from the top edge
CAM_CUTOUT_W = PHONE_W - 6.0    # nearly full width: the plateau spans the back

WET_WELL_D = 20.0               # wet cell: water column
WET_GLASS_D = 25.0              # round cover glass, top and bottom
WET_GLASS_T = 1.0               # [GUESS]
WET_GAP = 1.0                   # water thickness between the glasses
WET_T = TRAY_T                  # same plate as the tray, drops into the same rails

# --------------------------------------------------------------------------
# Global Z of every face, stacked off the membrane datum (membrane top = 0)
# --------------------------------------------------------------------------
Z_TRAY_BOT = -TRAY_FLOOR
Z_BOX_TOP = Z_TRAY_BOT - POLARISER_T          # polariser 1 lies on the box top
Z_BOX_BOT = Z_BOX_TOP - BOX_H
Z_PLATE_TOP = Z_BOX_BOT                       # box is printed on the plate
Z_PLATE_BOT = Z_PLATE_TOP - PLATE_T
Z_LENS_FRONT = WORKING_DIST
Z_PLATEAU = Z_LENS_FRONT + CLIP_BELOW         # plateau surface (clip sits on it)
Z_PHONE_BACK = Z_PLATEAU + PLATEAU_H          # flat back of the phone = cradle pocket floor
Z_CRADLE_BOT = Z_PHONE_BACK - (CRADLE_T - CRADLE_POCKET)
Z_CRADLE_TOP = Z_CRADLE_BOT + CRADLE_T
POST_L = Z_CRADLE_BOT - Z_PLATE_TOP

# Phone placement: long axis along X, top edge toward +X, camera on the optical axis.
PHONE_CX = -(PHONE_L / 2.0 - CAM_FROM_TOP)    # phone centre, global X
PHONE_CY = -(PHONE_W / 2.0 - CAM_FROM_SIDE)   # phone centre, global Y (camera near +Y edge)
PHONE_X0, PHONE_X1 = PHONE_CX - PHONE_L / 2.0, PHONE_CX + PHONE_L / 2.0
PHONE_Y0, PHONE_Y1 = PHONE_CY - PHONE_W / 2.0, PHONE_CY + PHONE_W / 2.0

# Cradle plate outline and the four posts under it. The camera sits near the phone's
# corner, so on the +X and +Y sides the plate must reach past the light box for the
# posts to stand clear of it; on the other sides the phone outline sets the edge.
POST_INSET = POST_SQ / 2.0 + 3.0
REACH = BOX_W / 2.0 + POST_SQ / 2.0 + 2.0 + POST_INSET   # edge that puts a post clear of the box
CRADLE_X0, CRADLE_X1 = PHONE_X0 - CRADLE_MARGIN, max(PHONE_X1 + CRADLE_MARGIN, REACH)
CRADLE_Y0, CRADLE_Y1 = min(PHONE_Y0 - CRADLE_MARGIN, -REACH), max(PHONE_Y1 + CRADLE_MARGIN, REACH)
CRADLE_L, CRADLE_W = CRADLE_X1 - CRADLE_X0, CRADLE_Y1 - CRADLE_Y0
CRADLE_CX, CRADLE_CY = (CRADLE_X0 + CRADLE_X1) / 2.0, (CRADLE_Y0 + CRADLE_Y1) / 2.0

POST_XY = [
    (CRADLE_X0 + POST_INSET, CRADLE_Y0 + POST_INSET),
    (CRADLE_X0 + POST_INSET, CRADLE_Y1 - POST_INSET),
    (CRADLE_X1 - POST_INSET, CRADLE_Y0 + POST_INSET),
    (CRADLE_X1 - POST_INSET, CRADLE_Y1 - POST_INSET),
]
PLATE_X0, PLATE_X1 = CRADLE_X0, CRADLE_X1     # base plate matches the cradle footprint
PLATE_Y0, PLATE_Y1 = CRADLE_Y0, CRADLE_Y1
PLATE_L, PLATE_W = PLATE_X1 - PLATE_X0, PLATE_Y1 - PLATE_Y0
PLATE_CX, PLATE_CY = CRADLE_CX, CRADLE_CY

MATERIALS = {
    "base_plate":  ("PLA or PETG, FDM, 0.2 mm layers",             "#3a3f44"),
    "post":        ("PLA or PETG, FDM",                              "#3a3f44"),
    "tray":        ("PLA or PETG, FDM, first layer on glass",        "#4a5157"),
    "cradle":      ("PLA or PETG, FDM, ribbed",                      "#3a3f44"),
    "wet_cell":    ("resin preferred; FDM sealed with silicone",     "#4a5157"),
    "phone":       ("iPhone 17 Pro Max (bought)",                    "#1c2024"),
    "clip_lens":   ("10x clip-on macro lens (bought)",               "#111315"),
    "led_panel":   ("50 mm white LED panel, USB (bought)",           "#f2c94c"),
    "diffuser":    ("opal acrylic (bought)",                          "#f4f4f0"),
    "polariser":   ("linear polarising film (bought)",               "#6e7f8a"),
    "membrane":    ("47 mm PCTE, 5 µm (consumable)",                 "#f6f2e8"),
    "cover_glass": ("round cover glass (bought)",                    "#bfe0f7"),
}


def material_of(label: str):
    return MATERIALS.get(label.split(":")[0])


# --------------------------------------------------------------------------
# Self-checks — the couplings a sketch cannot hold for you.
# --------------------------------------------------------------------------
def check_optics() -> list[str]:
    notes = [
        f"field {FIELD_W:.1f} x {FIELD_H:.1f} mm at {UM_PER_PX:.1f} um/px; "
        f"resolves {RESOLVE_UM:.1f} um; depth of field {DOF_UM:.0f} um",
    ]
    if hypot(FIELD_W, FIELD_H) > LED_W:
        raise ValueError(
            f"field diagonal {hypot(FIELD_W, FIELD_H):.1f} mm is wider than the {LED_W} mm "
            f"LED panel; the corners of every photo will be dark"
        )
    if hypot(FIELD_W, FIELD_H) > POLARISER_W:
        raise ValueError("polariser sheet is smaller than the field diagonal")
    exposed = MEMBRANE_D - 6.0          # typical filtration funnel leaves a 6 mm rim
    notes.append(f"membrane exposed area ~{exposed:.0f} mm across; "
                 f"{'one frame covers it' if FIELD_W >= exposed else 'needs tiling'}")
    if DOF_UM < 60:
        notes.append("WARNING depth of field under 60 um: the tray floor must be printed on a "
                     "flat bed and the glass must press the membrane")
    return notes


def check_stack() -> list[str]:
    notes = []
    if POST_L <= 20:
        raise ValueError(f"posts would be {POST_L:.1f} mm; the stack does not close")
    gap = Z_LENS_FRONT - (Z_TRAY_BOT + TRAY_T)
    if gap < 5.0:
        raise ValueError(f"only {gap:.1f} mm between the tray top and the lens front")
    notes.append(f"posts {POST_L:.1f} mm; lens front {gap:.1f} mm above the tray top")
    if GLASS_T > TRAY_T - TRAY_FLOOR:
        raise ValueError("cover glass stands proud of the tray")
    return notes


def check_cradle() -> list[str]:
    notes = []
    # the clip-on lens must fit through the camera cutout
    if CLIP_BODY_D / 2.0 > CAM_CUTOUT_L - CAM_FROM_TOP:
        raise ValueError("camera cutout does not reach past the clip-on lens body")
    # posts must not stand inside the light box footprint
    for x, y in POST_XY:
        if abs(x) < BOX_W / 2.0 + POST_SQ / 2.0 and abs(y) < BOX_W / 2.0 + POST_SQ / 2.0:
            raise ValueError(f"post at ({x:.0f},{y:.0f}) collides with the light box")
    notes.append(f"cradle {CRADLE_L:.0f} x {CRADLE_W:.0f} mm; plate the same; "
                 f"phone spans x {PHONE_X0:.0f}..{PHONE_X1:.0f}")
    if max(CRADLE_L, CRADLE_W) > 220:
        notes.append("WARNING cradle exceeds a 220 mm print bed")
    return notes


def validate() -> list[str]:
    return check_optics() + check_stack() + check_cradle()


validate()
