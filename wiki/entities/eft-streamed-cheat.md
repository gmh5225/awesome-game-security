---
title: eft-streamed-cheat
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/fcancelog__EftStreamedCheat.md
updated: 2026-08-15
confidence: medium
---

# eft-streamed-cheat

**Escape From Tarkov** cheat using a **streaming/external** architecture: a driver reads EFT **Unity** game memory out-of-process and renders radar, player positions, loot, and other ESP data on a **separate display or overlay** outside the game window. The design avoids **in-process injection** detection on **BattlEye**-protected clients. Aimed at game security researchers studying external/streaming cheat architectures for Unity titles. (source: wiki/sources/descriptions/fcancelog__EftStreamedCheat.md)

Complements driver-backed externals such as [[eft-external]], separate-screen DMA radars such as [[meatyeftrelease]] and [[eft-dma-radar-1]], and dual-path public radars such as [[nathans-tarkov-radar-public]] by emphasizing off-window streaming output rather than in-client overlays.

## Links

- Repo: https://github.com/fcancelog/EftStreamedCheat

## Related

[[eft-external]] · [[meatyeftrelease]] · [[eft-dma-radar-1]] · [[nathans-tarkov-radar-public]] · [[eft-internal]] · [[simple-eft-base]] · [[battleye]] · [[il2cpp]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
