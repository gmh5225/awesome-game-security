---
title: Core_ac
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/AmenHermano144__Anti-cheat-Kernel-Driver.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# Core_ac

Modular **Windows x64 WDM kernel anti-cheat reference driver** (AmenHermano144; C; VS 2022 + WDK) aimed at competitive multiplayer games—not a production product. Uses Windows **CNG (BCrypt)** and a hardened usermode **IOCTL** channel sealed with per-session **AES-GCM**. Detection modules cover **BYOVD** and driver timestamp blacklists, kernel module inventory and executable-region scans, **PiDDBCache** and **MmUnloadedDrivers** tamper monitoring, PML4-based process watching, NMI watchdog and environment checks, and mouse/keyboard class input-path integrity. Defers heavy init from `DriverEntry`, applies strict device DACLs, and streams telemetry to a SYSTEM-level companion via an event ring buffer. (source: wiki/sources/descriptions/AmenHermano144__Anti-cheat-Kernel-Driver.md)

## Positioning

Readable open kernel AC baseline beside educational stacks such as [[peregrine-anticheat]], [[saturn-anti-cheat]], [[ringo-ac]], and [[oac]]—emphasizes modular detection code and encrypted usermode comms rather than a full game integration product.

## Links

- Repo: https://github.com/AmenHermano144/Anti-cheat-Kernel-Driver

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[concepts/kernel-callbacks]] · [[concepts/byovd]] · [[concepts/driver-trust-boundaries]] · [[peregrine-anticheat]] · [[ringo-ac]] · [[oac]]
