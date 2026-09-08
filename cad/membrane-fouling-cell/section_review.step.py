"""Review aid: the full assembly with the +Y half removed, so the optical path,
channel, seals, window seat and ports read in one XZ cutaway. Not a part."""

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build123d import Align, Box, Compound, Pos  # noqa: E402


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.step.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gen_step():
    asm = _load("fouling_cell").gen_step()
    knife = Pos(0, 100, 0) * Box(400, 200, 400, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    cut = []
    for child in asm.children:
        piece = child - knife
        piece.label = child.label
        cut.append(piece)
    return Compound(label="fouling_cell_section", children=cut)
