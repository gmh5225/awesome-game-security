---
title: CS2-DMA
kind: entity
topics: [dma-attack, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/chao-shushu__CS2-DMA.md
updated: 2026-08-17
confidence: medium
---

# CS2-DMA

Open-source **Counter-Strike 2** external tool in **C++** that uses **FPGA-based DMA hardware** (LeechCore) to read game memory on a **separate machine** and render overlays without injecting into the game process. The public build is **read-only DMA** and focuses on visualization: box and bone ESP, weapon and ammo displays, visibility coloring, bomb and projectile helpers, plus a **LAN-accessible web radar** with grenade-helper support. Stack: **MemProcFS** and LeechCore for DMA access, **ImGui** with **DirectX 11** for the UI, low-latency scatter batch reads, snapshot interpolation, and tiered DMA recovery. Automatic offset updates via **cs2-dumper**, dual-source hotkeys, and troubleshooting utilities. Aimed at game-security researchers studying DMA-based external CS2 analysis and visualization. (source: wiki/sources/descriptions/chao-shushu__CS2-DMA.md)

Complements [[cs2-dma-radar]] and [[cs2-dma-cheat]] by documenting a fuller open-source read-only ESP/radar stack with MemProcFS scatter optimizations and web-radar delivery; contrasts with in-process CS2 samples such as [[cs2-cheat-cpp]] and browser radars such as [[cs2-webradar]] by keeping attacker logic on a second host with zero target-OS software.

## Links

- Repo: https://github.com/chao-shushu/CS2-DMA

## Related

[[cs2-dma-radar]] · [[cs2-dma-cheat]] · [[cs2-webradar]] · [[cs2-offsets]] · [[proext]] · [[volk-dma]] · [[memtools]] · [[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
