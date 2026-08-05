---
title: VmwareHardenedLoader
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hzqst__VmwareHardenedLoader.md
updated: 2026-08-05
confidence: medium
---

# VmwareHardenedLoader

**VMware anti-detection hardening** tool that patches VMware virtual machines to evade VM detection used by malware and anti-cheat systems. Modifies **CPUID leaves**, **SMBIOS** tables, **ACPI** data, registry keys, **MAC addresses**, and other hardware fingerprints so the guest appears as a physical machine. C/C++ loader operates at the **hypervisor level** with **Windows and Linux** guest support. Aimed at malware analysts and game-security researchers who need to hide virtualization from VM-aware software—not a production AC component. (source: wiki/sources/descriptions/hzqst__VmwareHardenedLoader.md)

README lane: VMware guest fingerprint spoof under `Cheat > QEMU/KVM/PVE/VBOX` / `Detection:Virtual Environments` evasion research. Sibling focus to [[qemu-patched]] / [[proxmox-ve-anti-detection]] (QEMU/PVE spoof) and defensive counterpart [[vmaware]] (100+ VM detection techniques).

## Links

- Repo: https://github.com/hzqst/VmwareHardenedLoader

## Related

[[qemu-patched]] · [[qemu-anti-detection]] · [[proxmox-ve-anti-detection]] · [[vmaware]] · [[awesome-anti-virtualization]] · [[unicorn-pe]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
