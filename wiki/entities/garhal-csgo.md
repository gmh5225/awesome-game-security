---
title: GarHal CSGO
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/dretax__GarHal_CSGO.md
updated: 2026-08-16
confidence: medium
---

# GarHal CSGO

**CS:GO kernel-mode cheat driver** (dretax) with a **companion usermode controller** that demonstrates game manipulation from **kernel space via IOCTL communication**. Implements **kernel-level memory read/write** for game entity data access, with stated plans for **kernel-level DirectX hooking** and drawing overlays without usermode injection. Mainly useful for game security researchers studying **kernel-driver-based cheat architectures** and how anti-cheat systems must defend against **ring-0 threats**. (source: wiki/sources/descriptions/dretax__GarHal_CSGO.md)

Sits beside other CS:GO KM samples such as [[kernel-csgo]] (hook-based KM↔UM comm) and [[ec]] (ekknod kernel/driver CS:GO), driver-backed externals such as [[csgo-cheat-external]], and planned kernel DirectX overlay lanes such as [[kernel-cheat-for-directx3d]].

## Links

- Repo: https://github.com/dretax/GarHal_CSGO

## Related

[[kernel-csgo]] · [[ec]] · [[csgo-cheat-external]] · [[kernel-cheat-for-directx3d]] · [[cheat-driver]] · [[csgo-ac]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
