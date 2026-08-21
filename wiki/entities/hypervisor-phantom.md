---
title: Hypervisor-Phantom
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Scrut1ny__Hypervisor-Phantom.md
updated: 2026-08-21
confidence: medium
---

# Hypervisor-Phantom

**Hypervisor-Phantom** (Scrut1ny) is a **Bash-driven automation toolkit** for building **Linux virtualization labs** with **anti-detection-oriented patches**. Setup modules cover **QEMU**, **EDK2**, **kernel patching**, **VFIO passthrough**, and deployment helpers, plus maintained patch sets and auxiliary scripts for **host and guest identifier** handling. Primary use is reproducible VM environments for **anti-cheat behavior testing** and **virtualization security** experiments—not a production anti-cheat component. (source: wiki/sources/descriptions/Scrut1ny__Hypervisor-Phantom.md)

Distinct from single-purpose fingerprint spoof repos such as [[qemu-anti-detection]] (device-string spoof) and [[qemu-patched]] (CPUID/SMBIOS/ACPI masking): Hypervisor-Phantom orchestrates an end-to-end **lab provisioning pipeline** (build, patch, deploy). Sibling focus to [[hardened-qemu]] (stealth-patched QEMU/KVM build) and [[proxmox-ve-anti-detection]] (hidden PVE / kernel-oriented). Same maintainer as guest-side identifier tooling [[windows-spoofer]].

Sits in the `Cheat > QEMU/KVM/PVE/VBOX` lane and the defensive counterpart `Detection:Virtual Environments`.

## Links

- Repo: https://github.com/Scrut1ny/Hypervisor-Phantom (README tag: Hidden QEMU)

## Related

[[qemu-anti-detection]] · [[qemu-patched]] · [[hardened-qemu]] · [[proxmox-ve-anti-detection]] · [[kvm-performance]] · [[windows-spoofer]] · [[awesome-anti-virtualization]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
