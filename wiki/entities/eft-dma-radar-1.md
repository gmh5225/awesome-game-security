---
title: eft-dma-radar-1
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__eft-dma-radar-1.md
updated: 2026-08-09
confidence: medium
---

# eft-dma-radar-1

**Escape From Tarkov** DMA-based radar cheat that reads game memory through **PCILeech-compatible DMA hardware**. Extracts player positions, loot locations, and map data from EFT's Unity game engine memory and displays them on a **separate screen** as a real-time radar overlay. The below-OS DMA path avoids BattlEye process-level detection on the gaming machine. Aimed at game security researchers studying DMA-based cheat architectures for BattlEye-protected Unity titles. (source: wiki/sources/descriptions/gmh5225__eft-dma-radar-1.md)

Complements fuller external clients such as [[meatyeftrelease]] and in-process samples such as [[eft-internal]] by illustrating a minimal PCILeech-stack EFT radar focused on separate-display overlay and Unity world-state extraction.

## Links

- Repo: https://github.com/gmh5225/eft-dma-radar-1

## Related

[[meatyeftrelease]] · [[eft-internal]] · [[simple-eft-base]] · [[escapefromtarkov-trainer]] · [[dma]] · [[pcileech]] · [[battleye]] · [[il2cpp]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
