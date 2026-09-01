#!/bin/sh
# Startup Assumption Lab — one-command setup. Run once per clone; safe to rerun.
#
#     scripts/setup.sh
#
# Creates .venv and installs dependencies there rather than system-wide, because a
# Homebrew/system python3 on macOS refuses `pip install` outright (PEP 668) — which
# is why the validators, the generators and the tests all fail on a fresh clone with
# "No module named 'yaml'" until this has run.
#
# Then installs the git hooks, which is what actually enforces single authorship.

set -e

REPO="$(git rev-parse --show-toplevel)"
cd "$REPO"

if [ ! -x .venv/bin/python ]; then
    echo "Creating .venv…"
    python3 -m venv .venv
fi

echo "Installing dependencies…"
.venv/bin/python -m pip install --quiet --upgrade pip
.venv/bin/python -m pip install --quiet -r requirements.txt

scripts/hooks/install.sh

echo ""
echo "Verifying…"
.venv/bin/python scripts/validate_repo.py
.venv/bin/python scripts/validate_skill_catalog.py
.venv/bin/python -m pytest tests -q

echo ""
echo "Ready. Run repo scripts with .venv/bin/python, or activate the venv:"
echo "    source .venv/bin/activate"
