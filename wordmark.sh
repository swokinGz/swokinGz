#!/usr/bin/env bash
# wordmark.sh --name "NAME"
NAME="swokingz"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name) NAME="$2"; shift 2 ;;
    *) shift ;;
  esac
done
figlet -f big "$NAME"
