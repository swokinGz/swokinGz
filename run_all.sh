#!/usr/bin/env bash
# Regenerates every animated/static SVG panel in this README from scratch.
# Requires: figlet (or pyfiglet), python3, and the "common.py" module alongside this script.
set -e
python3 make_wordmark.py
python3 panel_identity.py
python3 panel_core_stack.py
python3 panel_telemetry.py
python3 panel_deployed.py
python3 panel_uplink.py
echo "Done. Regenerated: wordmark.svg identity.svg core_stack.svg telemetry.svg deployed.svg uplink.svg"
