---
title: Hardened-qemu
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/batusan__Hardened-qemu.md
updated: 2026-08-18
confidence: medium
---

# Hardened-qemu

Stealth-patched **QEMU/KVM** build that hides common VirtualBox, VMware, Bochs, and QEMU/KVM artifacts from guest software. Based on an upstream QEMU git snapshot with anti-VM fingerprint mitigations for analyzing VM-hostile or anti-cheat software—not intended as a daily-driver hypervisor. (source: wiki/sources/descriptions/batusan__Hardened-qemu.md)

Mainly useful for game-security researchers studying anti-VM checks and running analysis VMs against protected titles. Sibling focus to [[qemu-patched]] (CPUID / SMBIOS / ACPI spoof), [[qemu-anti-detection]] (device-string spoof), and [[proxmox-ve-anti-detection]] (hidden PVE / kernel-oriented).

## Links

- Repo: https://github.com/batusan/Hardened-qemu (README tag: Hidden QEMU)

## Related

[[qemu-patched]] · [[qemu-anti-detection]] · [[proxmox-ve-anti-detection]] · [[vmware-hardened-loader]] · [[awesome-anti-virtualization]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
