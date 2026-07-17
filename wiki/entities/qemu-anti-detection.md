---
title: qemu-anti-detection
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/zhaodice__qemu-anti-detection.md
updated: 2026-07-17
confidence: medium
---

# qemu-anti-detection

Research project for **hidden QEMU**: masking guest virtualization fingerprints (e.g. renaming “QEMU keyboard” to “ASUS keyboard”) so a QEMU guest looks less like a VM to anti-cheat and environment checks. (source: wiki/sources/descriptions/zhaodice__qemu-anti-detection.md)

Useful for game-security researchers and reverse engineers studying offensive techniques in the `Cheat > QEMU/KVM/PVE/VBOX` lane and the defensive counterpart `Detection:Virtual Environments`—not a production AC component. Sibling focus to [[proxmox-ve-anti-detection]] (hidden PVE / kernel-oriented).

## Links

- Repo: https://github.com/zhaodice/qemu-anti-detection (README tag: Hidden QEMU)

## Related

[[proxmox-ve-anti-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
