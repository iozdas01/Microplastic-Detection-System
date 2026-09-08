"""Fable/cadgen entry point for the detailed, assembled instrument."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from instrument import assembly, make_instrument


def gen_step():
    return assembly(make_instrument())

