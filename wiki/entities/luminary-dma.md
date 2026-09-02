---
title: LuminaryDMA
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/TheAustinUS__LuminaryDMA.md
  - wiki/sources/README-categories.md
updated: 2026-09-02
confidence: medium
---

# LuminaryDMA

**Call of Duty** read-only DMA cheat framework (TheAustinUS) that reads game memory from a **separate Windows host** via **PCILeech FPGA** (LeechCore + DMALibrary) or **MockDMA** test mode without hardware. Provides ESP, radar, and player-info overlays through an **ImGui** menu (Visual Studio 2022). Features GamePass/BattleNet platform auto-detection, BattleNet pointer decryption, configurable **BO6 offsets**, and client-info decryption workflows. (source: wiki/sources/descriptions/TheAustinUS__LuminaryDMA.md)

Useful for DMA security researchers studying read-only external overlays, platform-specific pointer decryption, anti-cheat evasion techniques, and protected-memory structure RE on Call of Duty titles—beside Unreal DMA samples such as [[arc-raiders-radar-dma-radar]] and Source-2 stacks such as [[cs2-dma]].

## Stack

| Layer | Component |
|-------|-----------|
| Hardware | [[pcileech]] FPGA via LeechCore, or MockDMA (no hardware) |
| Memory API | [[dmalibrary]] wrapper |
| Host | Separate Windows machine (Visual Studio 2022) |
| UI | ImGui overlay menu |
| Targets | GamePass and BattleNet (auto-detected); configurable BO6 offsets |

## Links

- Repo: https://github.com/TheAustinUS/LuminaryDMA

## Related

[[dma]] · [[pcileech]] · [[dmalibrary]] · [[world-to-screen]] · [[arc-raiders-radar-dma-radar]] · [[cs2-dma]] · [[apex-dma-cheat-updated]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
