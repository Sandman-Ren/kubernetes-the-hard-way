# Provisioning the machines with Multipass

This directory provides a small kit for standing up the four machines required
by [Kubernetes The Hard Way](../docs/01-prerequisites.md) using
[Multipass](https://multipass.run) — Canonical's lightweight local VM manager.

It is an alternative to provisioning the machines by hand. When it finishes you
have everything the prerequisites and "Provisioning Compute Resources" labs set
up by hand, up to (and including) SSH key distribution and `machines.txt`.

## What you get

| Name    | Role                | CPU | RAM   | Disk |
|---------|---------------------|-----|-------|------|
| jumpbox | Administration host | 1   | 512MB | 10GB |
| server  | Kubernetes server   | 1   | 2GB   | 20GB |
| node-0  | Worker node         | 1   | 2GB   | 20GB |
| node-1  | Worker node         | 1   | 2GB   | 20GB |

These specs come straight from [docs/01-prerequisites.md](../docs/01-prerequisites.md).

On top of the bare VMs the `provision.sh` script also:

- enables **root SSH login** on every machine (via `cloud-init.yaml`),
- generates an SSH keypair on the **jumpbox** and installs its public key in
  `root`'s `authorized_keys` on `server`, `node-0` and `node-1` — i.e. it
  pre-completes the *Generate and Distribute SSH Keys* step,
- generates a `machines.txt` database from the IP addresses Multipass assigned
  and drops it at `/root/machines.txt` on the jumpbox.

So once the script finishes you can jump straight to the **Hostnames** section
of [docs/03-compute-resources.md](../docs/03-compute-resources.md).

## A note on the operating system

The tutorial asks for **Debian 12 (bookworm)**, but Multipass only publishes
**Ubuntu** images — there is no `multipass launch debian`. Every step in
Kubernetes The Hard Way is distro-agnostic (plain `apt` and `systemd`), so this
kit defaults to **Ubuntu 24.04 LTS** and the rest of the tutorial works
unchanged. The only visible difference is the `/etc/os-release` check in the
prerequisites lab, which will report Ubuntu instead of Debian.

If you specifically need Debian 12, Multipass cannot help on its own; use a tool
that can boot a Debian cloud image (Vagrant + libvirt, plain `virt-install`,
Lima, etc.). To point this script at a non-default image (for example a custom
Multipass remote that serves Debian), set the `IMAGE` environment variable:

```bash
IMAGE=debian/12 ./provision.sh   # only works if your Multipass remote has it
```

## Usage

Prerequisites: a working Multipass install (`multipass version`) on your local
machine — macOS, Windows, or Linux. Multipass runs the VMs on a hypervisor on
**your workstation**, not in CI or a container.

```bash
# Create and wire up all four machines
./provision.sh

# ... follow the tutorial ...

# Destroy everything when you're done
./teardown.sh
```

The script is idempotent: re-running it skips machines that already exist and
re-distributes the SSH key / regenerates `machines.txt`.

### Handy commands

```bash
multipass list                 # see all instances and their IPs
multipass shell jumpbox        # open a shell on the jumpbox
multipass info server          # details for one machine
multipass stop --all           # pause every machine (frees CPU/RAM)
multipass start --all          # resume
```

## How it fits the tutorial

1. **Prerequisites** — the four machines and their specs are created by
   `provision.sh` (Ubuntu instead of Debian; see the OS note above).
2. **Provisioning Compute Resources**
   - *Machine Database* — `machines.txt` is generated and placed on the jumpbox.
   - *Configuring SSH Access* / *Generate and Distribute SSH Keys* — done by the
     script (root login enabled, jumpbox key distributed).
   - *Hostnames*, *Host Lookup Table*, `/etc/hosts` — follow the tutorial as
     written from the jumpbox.

From there, every later lab (CA, etcd, control plane, workers, …) proceeds
exactly as documented.
