---
title: Cheat Engine DMA Plugin
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md
updated: 2026-08-02
confidence: medium
---

# Cheat Engine DMA Plugin

Open-source **C/C++ Cheat Engine plugin** that routes memory read/write through **DMA hardware** (PCILeech-compatible FPGA boards) via the **pcileech/LeechCore** library instead of CE's normal in-process APIs. Scanning and editing use physical-memory operations on the target, so the gaming OS does not observe conventional process-memory access from CE. Aimed at DMA game-security researchers and anti-cheat analysts who want CE's familiar scan/edit workflow on an external DMA path. (source: wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md)

## Links

- Repo: https://github.com/kaijia2022/Cheat-Engine-DMA-Plugin

## Related

[[dma]] · [[pcileech]] · [[dma-cheat-engine-loader]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
