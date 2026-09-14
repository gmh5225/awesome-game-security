---
title: HOOZi CS2 DMA
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/orphannn__hoozi-cs2-dma.md
  - wiki/sources/README-categories.md
updated: 2026-09-14
confidence: medium
---

# HOOZi CS2 DMA

External **Counter-Strike 2** tool that reads game memory over an **FPGA DMA** link from a second PC without injecting into or writing to the game process. Current capability is player ESP with boxes, skeletons, health/armor bars, and name/weapon/distance overlays, plus teammate filtering and **map-aware visibility checks** backed by collision geometry for 21 official maps. Offsets resolve at attach time through pattern scanning and Source 2 schema traversal, with hourly signature sync and per-build caching. Ships a configurable menu framework with multi-profile settings, localization, and planned aim assist, radar, item ESP, and Lua scripting. (source: wiki/sources/descriptions/orphannn__hoozi-cs2-dma.md)

Useful for DMA security researchers studying read-only external overlays, Source 2 schema/offset automation, map-collision visibility gating, and anti-cheat evasion beside stacks such as [[cs2-dma]], [[cs2-dma-radar]], and [[luminary-dma]].

## Stack

| Layer | Component |
|-------|-----------|
| Hardware | FPGA DMA via LeechCore/VMM |
| Host | Separate PC (read-only external) |
| Offsets | Pattern scan + Source 2 schema; hourly sync; per-build cache |
| Visibility | Map collision geometry (21 maps) |
| UI | Configurable menu; multi-profile settings |

## Links

- Repo: https://github.com/orphannn/hoozi-cs2-dma

## Related

[[dma]] · [[pcileech]] · [[world-to-screen]] · [[cs2-dma]] · [[cs2-dma-radar]] · [[cs2-dma-cheat]] · [[luminary-dma]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
