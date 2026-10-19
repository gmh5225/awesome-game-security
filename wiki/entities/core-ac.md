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

Modular **Windows x64 WDM kernel anti-cheat reference driver** (AmenHermano144; C; Visual Studio 2022 + WDK) aimed at competitive multiplayer games—not a production product. Uses Windows **CNG (BCrypt)** and a hardened usermode **IOCTL** channel sealed with per-session **AES-GCM**. (source: wiki/sources/descriptions/AmenHermano144__Anti-cheat-Kernel-Driver.md)

## Detection modules

| Area | Mechanism |
|------|-----------|
| **BYOVD / drivers** | BYOVD and driver timestamp blacklists; kernel module inventory; executable-region scans |
| **Load-artifact integrity** | **PiDDBCache** and **MmUnloadedDrivers** tamper monitoring (see [[byovd]]) |
| **Process watch** | PML4-based process watching |
| **Environment** | NMI watchdog and environment checks |
| **Input path** | Mouse and keyboard class driver integrity |

## Architecture

Defers heavy initialization out of `DriverEntry`, applies strict device **DACLs** on the IOCTL device, and streams detection telemetry to a **SYSTEM**-level user-mode companion through an **event ring buffer**. Usermode comms rely on CNG (BCrypt) with per-session AES-GCM sealing on the IOCTL channel. (source: wiki/sources/descriptions/AmenHermano144__Anti-cheat-Kernel-Driver.md)

## Audience

Game security engineers and authorized anti-cheat researchers who want readable, verifiable kernel detection modules and a baseline for studying how modern kernel anti-cheats are structured.

## Positioning

Readable open kernel AC baseline beside educational stacks such as [[peregrine-anticheat]], [[saturn-anti-cheat]], [[ringo-ac]], and [[oac]]—emphasizes modular detection code and encrypted usermode comms rather than a full game integration product.

## Links

- Repo: https://github.com/AmenHermano144/Anti-cheat-Kernel-Driver

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[concepts/kernel-callbacks]] · [[concepts/byovd]] · [[concepts/driver-trust-boundaries]] · [[peregrine-anticheat]] · [[ringo-ac]] · [[oac]]
