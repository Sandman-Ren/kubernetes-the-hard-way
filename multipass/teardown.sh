#!/usr/bin/env bash
#
# teardown.sh - Delete and purge the Multipass machines created by provision.sh.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MACHINES=(jumpbox server node-0 node-1)

command -v multipass >/dev/null 2>&1 || { echo "multipass not found" >&2; exit 1; }

for name in "${MACHINES[@]}"; do
  if multipass info "$name" >/dev/null 2>&1; then
    echo "==> Deleting ${name}"
    multipass delete "$name"
  fi
done

echo "==> Purging deleted instances"
multipass purge

rm -f "${SCRIPT_DIR}/machines.txt"
echo "==> Done."
