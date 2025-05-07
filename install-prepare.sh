#!/bin/bash
set -euo pipefail

if [[ "$EUID" -ne 0 ]]; then
  echo "Error: Please run as root (sudo ./install-prepare.sh)" >&2
  exit 1
fi

for dep in python3 git; do
  if ! command -v "$dep" >/dev/null 2>&1; then
    echo "Error: '$dep' is required but not found in \$PATH." >&2
    exit 1
  fi
done

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_PATH="/usr/bin/prepare"

if [[ -f "$INSTALL_PATH" ]]; then
  cp "$SRC_DIR/prepare.py" "$INSTALL_PATH"
  chmod +x "$INSTALL_PATH"
  echo "Updated existing 'prepare' at $INSTALL_PATH"
else
  cp "$SRC_DIR/prepare.py" "$INSTALL_PATH"
  chmod +x "$INSTALL_PATH"
  echo "Installed new 'prepare' at $INSTALL_PATH"
fi
