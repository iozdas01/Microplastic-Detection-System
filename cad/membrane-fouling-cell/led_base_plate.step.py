"""Entry generator for the led_base_plate body. Geometry lives in cell_parts.py;
dimensions in cell_params.py. Build with scripts/gen led_base_plate.step.py --write"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cell_parts  # noqa: E402


def gen_step():
    return cell_parts.led_base_plate()
