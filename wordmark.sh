#!/usr/bin/env bash
# wordmark.sh --name "NAME"
# Generates a futuristic ASCII wordmark using the pyfiglet "future" font.
NAME="SWOKINGZ"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name) NAME="$2"; shift 2 ;;
    *) shift ;;
  esac
done
python3 -c "import pyfiglet; print(pyfiglet.Figlet(font='future').renderText('$NAME'))"
