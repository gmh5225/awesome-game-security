---
title: qemu-patched
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/kila58__qemu-patched.md
updated: 2026-08-02
confidence: medium
---

# qemu-patched

Patched **QEMU fork** with anti-detection modifications to hide the virtual machine from guest OS anti-VM checks. Spoofs CPUID responses, SMBIOS/DMI data, ACPI tables, device names, and other VM fingerprints so a QEMU guest appears as physical hardware to malware and anti-cheat environment probes. (source: wiki/sources/descriptions/kila58__qemu-patched.md)

Aimed at malware analysts and game-security researchers who need to run VM-detecting software in QEMU without triggering detection—not a production AC component. Sibling focus to [[qemu-anti-detection]] (device-string spoof) and [[proxmox-ve-anti-detection]] (hidden PVE / kernel-oriented).

## Links

- Repo: https://github.com/kila58/qemu-patched (README tag: Hidden QEMU)

## Related

[[qemu-anti-detection]] · [[proxmox-ve-anti-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
