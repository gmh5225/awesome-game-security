---
title: nathans-tarkov-radar-public
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Nathans-Tarkov-Radar-Public.md
updated: 2026-08-11
confidence: medium
---

# nathans-tarkov-radar-public

Public **Escape From Tarkov** radar cheat that reads EFT's **Unity** game memory to extract entity coordinates and game state, rendering a **top-down radar** on a **secondary display** with players, scavs, loot, and extractions. Operates **externally** (Vmread path) or through **DMA hardware**. Aimed at game security researchers studying radar cheat architecture for **BattlEye**-protected games. (source: wiki/sources/descriptions/gmh5225__Nathans-Tarkov-Radar-Public.md)

Complements PCILeech-focused samples such as [[eft-dma-radar-1]] and fuller DMA clients such as [[meatyeftrelease]] by illustrating a public dual-path (Vmread + DMA) EFT radar with separate-screen overlay.

## Links

- Repo: https://github.com/gmh5225/Nathans-Tarkov-Radar-Public

## Related

[[eft-dma-radar-1]] · [[meatyeftrelease]] · [[eft-internal]] · [[escapefromtarkov-trainer]] · [[simple-eft-base]] · [[battleye]] · [[il2cpp]] · [[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
