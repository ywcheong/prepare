#!/usr/bin/env bash
set -euo pipefail

if [[ "$EUID" -ne 0 ]]; then
  echo "Error: Please run as root (sudo ./remove-prepare.sh)" >&2
  exit 1
fi

INSTALL_PATH="/usr/bin/prepare"

if [[ -f "$INSTALL_PATH" ]]; then
  rm "$INSTALL_PATH"
  echo "Removed 'prepare' from $INSTALL_PATH"
else
  echo "'prepare' is not installed at $INSTALL_PATH"
fi
