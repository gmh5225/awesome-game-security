---
title: un-dma-v2 (Unleashed DMA V2)
kind: entity
topics: [dma-attack, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/RUC601__un-dma-v2.md
updated: 2026-11-18
confidence: medium
---

# un-dma-v2 (Unleashed DMA V2)

**C++ Overwatch 2 companion** that reads game state through **external DMA hardware** on a separate analysis host—no code runs inside the Overwatch process. Windows **CMake** builds integrate **LeechCore** and **VMM** for physical-memory reads; example configs cover **FPGA**, **FT601**, **FT2232H**, kernel driver paths, and other common [[pcileech]]-class backends. V2 adds a **launcher workflow**, **ImGui** UI, fixed **high-rate capture**, and modular features: entity visuals, hitbox overlays, aim smoothing, and skill alerts driven by Overwatch-specific game logic. (source: wiki/sources/descriptions/RUC601__un-dma-v2.md)

Positioned for researchers and defenders studying **DMA-assisted cheating**, remote memory acquisition, and how anti-cheat must reason about **out-of-process read paths** and companion tooling on the [[memory-acquisition-path]]. (source: wiki/sources/descriptions/RUC601__un-dma-v2.md)

## Stack

- **Target:** gaming PC with PCIe DMA initiator (no in-game injector).
- **Analysis host:** LeechCore + VMM scatter reads → game-state reconstruction → ImGui overlay/features.
- **Backends:** PCILeech-compatible FPGA/USB (FT601/FT2232H) or documented kernel-driver configs.

## Links

- Repo: https://github.com/RUC601/un-dma-v2

## Related

[[pcileech]] · [[volk-dma]] · [[dmalibrary]] · [[memory-acquisition-path]] · [[overviews/dma-attack]] · [[concepts/dma]] · [[overviews/anti-cheat]]