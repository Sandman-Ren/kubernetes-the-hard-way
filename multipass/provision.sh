#!/usr/bin/env bash
#
# provision.sh - Create the four machines required by "Kubernetes The Hard Way"
# using Multipass, and wire them up the way the prerequisites lab expects.
#
# What this gives you when it finishes:
#   * jumpbox, server, node-0, node-1 running with the CPU/RAM/disk specs
#     from docs/01-prerequisites.md
#   * root SSH login enabled on all machines (via cloud-init.yaml)
#   * an SSH keypair generated on the jumpbox and its public key installed in
#     root's authorized_keys on server, node-0 and node-1 (the "Generate and
#     Distribute SSH Keys" step from docs/03-compute-resources.md)
#   * a machines.txt database, generated from the IPs Multipass assigned, copied
#     to /root/machines.txt on the jumpbox
#
# After running this you can `multipass shell jumpbox`, `sudo su -`, and pick the
# tutorial back up at the "Hostnames" section of docs/03-compute-resources.md.
#
# NOTE ON THE OS: Multipass only publishes Ubuntu images, so there is no Debian
# 12 image to launch. Every KTHW step is plain apt/systemd and works unchanged
# on Ubuntu, so we default to Ubuntu 24.04 LTS. Override with IMAGE=... if you
# have a custom remote that serves Debian.

set -euo pipefail

# --- Configuration -----------------------------------------------------------

IMAGE="${IMAGE:-24.04}"                 # Ubuntu 24.04 LTS (Multipass has no Debian image)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLOUD_INIT="${SCRIPT_DIR}/cloud-init.yaml"

# Machine specs: name|cpus|memory|disk. Straight out of docs/01-prerequisites.md.
MACHINES=(
  "jumpbox|1|512M|10G"
  "server|1|2G|20G"
  "node-0|1|2G|20G"
  "node-1|1|2G|20G"
)

# Pod subnets for the worker nodes, matching the example in
# docs/03-compute-resources.md. The server has no pod subnet.
declare -A POD_SUBNET=(
  ["node-0"]="10.200.0.0/24"
  ["node-1"]="10.200.1.0/24"
)

# --- Helpers -----------------------------------------------------------------

log()  { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m==>\033[0m %s\n' "$*" >&2; }
die()  { printf '\033[1;31mERROR:\033[0m %s\n' "$*" >&2; exit 1; }

require_multipass() {
  command -v multipass >/dev/null 2>&1 || die \
    "multipass not found. Install it from https://multipass.run and re-run."
}

# `multipass info` exposes the instance state; treat "missing" as not-launched.
instance_state() {
  multipass info "$1" 2>/dev/null | awk '/^State:/ {print $2; exit}'
}

mem_flag() {
  # Multipass >= 1.13 uses --memory; older releases use --mem. Pick whatever
  # the installed version advertises so the script works on both.
  if multipass launch --help 2>&1 | grep -q -- '--memory'; then
    echo "--memory"
  else
    echo "--mem"
  fi
}

# --- Launch ------------------------------------------------------------------

require_multipass
[[ -f "$CLOUD_INIT" ]] || die "cloud-init file not found at $CLOUD_INIT"
MEM_FLAG="$(mem_flag)"

log "Launching machines from image '${IMAGE}' (memory flag: ${MEM_FLAG})"
for spec in "${MACHINES[@]}"; do
  IFS='|' read -r name cpus mem disk <<<"$spec"
  state="$(instance_state "$name" || true)"
  if [[ -n "$state" ]]; then
    log "Instance '${name}' already exists (state: ${state}); skipping launch."
    continue
  fi
  log "Launching ${name} (${cpus} CPU, ${mem} RAM, ${disk} disk)"
  multipass launch "$IMAGE" \
    --name "$name" \
    --cpus "$cpus" \
    "$MEM_FLAG" "$mem" \
    --disk "$disk" \
    --cloud-init "$CLOUD_INIT"
done

# Make sure cloud-init has fully finished before we start poking at the VMs.
for spec in "${MACHINES[@]}"; do
  IFS='|' read -r name _ _ _ <<<"$spec"
  log "Waiting for cloud-init to finish on ${name}"
  multipass exec "$name" -- cloud-init status --wait >/dev/null
done

# --- Distribute the jumpbox's SSH key ---------------------------------------

log "Generating an SSH keypair on the jumpbox (if one does not exist)"
multipass exec jumpbox -- sudo bash -c '
  set -e
  if [ ! -f /root/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 4096 -N "" -f /root/.ssh/id_rsa
  fi
'
JUMPBOX_PUBKEY="$(multipass exec jumpbox -- sudo cat /root/.ssh/id_rsa.pub)"
[[ -n "$JUMPBOX_PUBKEY" ]] || die "failed to read jumpbox root public key"

for host in server node-0 node-1; do
  log "Authorizing the jumpbox key for root@${host}"
  multipass exec "$host" -- sudo bash -c "
    set -e
    install -d -m 0700 /root/.ssh
    touch /root/.ssh/authorized_keys
    chmod 0600 /root/.ssh/authorized_keys
    grep -qxF '${JUMPBOX_PUBKEY}' /root/.ssh/authorized_keys \
      || echo '${JUMPBOX_PUBKEY}' >> /root/.ssh/authorized_keys
  "
done

# --- Build machines.txt ------------------------------------------------------

ip_of() {
  multipass info "$1" --format csv | awk -F, 'NR==2 {print $3}' | awk '{print $1}'
}

log "Generating machines.txt from the assigned IP addresses"
MACHINES_TXT="${SCRIPT_DIR}/machines.txt"
: >"$MACHINES_TXT"
for host in server node-0 node-1; do
  ip="$(ip_of "$host")"
  [[ -n "$ip" ]] || die "could not determine IP address for ${host}"
  if [[ -n "${POD_SUBNET[$host]:-}" ]]; then
    printf '%s %s.kubernetes.local %s %s\n' "$ip" "$host" "$host" "${POD_SUBNET[$host]}" >>"$MACHINES_TXT"
  else
    printf '%s %s.kubernetes.local %s\n' "$ip" "$host" "$host" >>"$MACHINES_TXT"
  fi
done

log "machines.txt:"
cat "$MACHINES_TXT"

log "Copying machines.txt to /root/machines.txt on the jumpbox"
multipass transfer "$MACHINES_TXT" jumpbox:/tmp/machines.txt
multipass exec jumpbox -- sudo install -m 0644 /tmp/machines.txt /root/machines.txt

# --- Done --------------------------------------------------------------------

cat <<EOF

$(log "All four machines are up and the jumpbox can reach them over SSH.")

Next steps:

  1. Open a shell on the jumpbox and become root:
       multipass shell jumpbox
       sudo su -

  2. machines.txt is already at /root/machines.txt. Verify SSH works:
       while read IP FQDN HOST SUBNET; do ssh -n root@\${IP} hostname; done < machines.txt

  3. Continue the tutorial from the "Hostnames" section of
     docs/03-compute-resources.md.

Tear everything down with: ${SCRIPT_DIR}/teardown.sh
EOF
