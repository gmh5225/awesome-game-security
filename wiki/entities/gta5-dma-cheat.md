---
title: GTA5-DMA-CHEAT
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/fmc999__GTA5-DMA-CHEAT.md
updated: 2026-08-15
confidence: medium
---

# GTA5-DMA-CHEAT

**Grand Theft Auto V** DMA-based cheat and memory tool that reads and writes game state through **external PCIe DMA hardware** rather than injecting into the game process. Implemented in **C++** as a Visual Studio Win32 application using **MemProcFS/VMMDLL (LeechCore)** for below-OS memory access and **ImGui with DirectX 11** for the overlay menu. Feature modules cover god mode, teleport, no wanted level, health/armor control, vehicle editing, weapon inspection, invisibility, no collision, player speed, ragdoll, time control, and related player/heist helpers, with support for both **Legacy and Enhanced GTA5** executables. Ships **Cheat Engine offset tables** for those builds, including **BattlEye-related patches**, making it useful for DMA cheat development, GTA V reverse engineering, and anti-cheat research around out-of-process memory manipulation. (source: wiki/sources/descriptions/fmc999__GTA5-DMA-CHEAT.md)

Contrasts with in-process GTA V samples such as [[gta5cheat]], [[grandtheftautov-cheat]], and [[phake]] by keeping attacker logic off the gaming OS; complements other title-specific DMA stacks such as [[cs2-dma-radar]] and [[eft-dma-radar-1]] in the cheat / game:gta5 `[DMA]` lane.

## Links

- Repo: https://github.com/fmc999/GTA5-DMA-CHEAT

## Related

[[gta5cheat]] · [[gta5cheat-qt]] · [[grandtheftautov-cheat]] · [[phake]] · [[gta-5-sigs-1.59]] · [[cs2-dma-radar]] · [[eft-dma-radar-1]] · [[battleye]] · [[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
