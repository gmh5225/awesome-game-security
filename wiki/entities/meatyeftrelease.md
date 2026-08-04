---
title: meatyeftrelease
kind: entity
topics: [dma-attack, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/paul01784__MeatyEFTRelease.md
updated: 2026-08-04
confidence: medium
---

# meatyeftrelease

Open-source **Escape From Tarkov** external radar and overlay client (Windows C++). Reads live game state through **DMA hardware** via LeechCore and MemProcFS (VMMDLL), with Unity-oriented modules tracking players, loot, exfil points, quests, explosives, cameras, and other entities. Renders a DirectX 11 / Direct2D **fuser** overlay with ImGui (aim view, map, read-only aim modules) and Makcu device integration; integrates a cloud DogTag API, tarkov.dev queries, and a libcurl auto-updater with SHA-256 verification. Aimed at game-security research, reverse engineering, and studying external DMA cheat techniques vs anti-cheat countermeasures. (source: wiki/sources/descriptions/paul01784__MeatyEFTRelease.md)

Complements internal EFT scaffolds such as [[simple-eft-base]] and discontinued Mono-era trainers such as [[escapefromtarkov-trainer]] by illustrating the below-OS cheat / game:eft [DMA] lane with a full-featured external client stack.

## Links

- Repo: https://github.com/paul01784/MeatyEFTRelease

## Related

[[dma]] · [[pcileech]] · [[csgo-dma-overlay]] · [[fn-dma-cheat]] · [[simple-eft-base]] · [[escapefromtarkov-trainer]] · [[il2cpp]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
