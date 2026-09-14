#!/usr/bin/env bash
# Open Blender with the MCP bridge listening, so a Claude Code session can drive it.
#
#   scripts/blender_mcp.sh                      # empty scene
#   scripts/blender_mcp.sh path/to/scene.blend  # open a scene
#
# One-time setup per machine (already done on the first founder's Mac, 2026-09-13):
#   brew install uv
#   install and enable the "MCP for Blender" add-on (github.com/ahujasid/blender-mcp, addon.py)
#   claude mcp add --scope user blender -- "$(command -v uvx)" blender-mcp
# The add-on auto-starts its socket server on port 9876 whenever Blender opens with a GUI;
# it cannot serve in `blender --background`, so this script opens the normal app.
set -euo pipefail
PORT=9876
if nc -z 127.0.0.1 "$PORT" 2>/dev/null; then
  echo "Blender MCP bridge already listening on $PORT"; exit 0
fi
# Launch the binary directly: `open -a Blender` came up without the bridge on the first try.
BLENDER=/Applications/Blender.app/Contents/MacOS/Blender
LOG="${TMPDIR:-/tmp}/blender_mcp.log"
nohup "$BLENDER" "$@" > "$LOG" 2>&1 &
echo "Blender starting (log: $LOG)"
for _ in $(seq 1 120); do
  if nc -z 127.0.0.1 "$PORT" 2>/dev/null; then echo "Blender MCP bridge listening on $PORT"; exit 0; fi
  sleep 1
done
echo "Blender opened but nothing is listening on $PORT after 120 s. In Blender: press N, BlenderMCP tab, Connect to Claude." >&2
exit 1
