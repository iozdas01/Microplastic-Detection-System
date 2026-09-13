"""Entry generator for the post body. Geometry lives in station_parts.py; dimensions in
station_params.py. Build with scripts/gen post.step.py --write"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import station_parts  # noqa: E402


def gen_step():
    return station_parts.post()
