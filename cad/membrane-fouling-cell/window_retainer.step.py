"""Entry generator for the window_retainer body. Geometry lives in cell_parts.py;
dimensions in cell_params.py. Build with scripts/gen window_retainer.step.py --write"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cell_parts  # noqa: E402


def gen_step():
    return cell_parts.window_retainer()
