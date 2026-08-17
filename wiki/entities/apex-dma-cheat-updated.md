---
title: ApexDmaCheatUpdated
kind: entity
topics: [dma-attack, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/boowampp__ApexDmaCheatUpdated.md
updated: 2026-08-17
confidence: medium
---

# ApexDmaCheatUpdated

**Apex Legends** DMA-based **external** cheat research sample (C++) that reads game memory through **[[pcileech]]/MemProcFS** and **FPGA** hardware rather than injecting into the target process. Features include configurable **aimbot** (FOV and smoothing), **recoil compensation**, **ESP** rendering, **camera calculations**, and a DMA memory library with **input management**, **registry access**, and **shellcode injection** support. Useful for DMA security researchers studying hardware-based game memory access and anti-cheat evasion under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/boowampp__ApexDmaCheatUpdated.md)

Complements title-specific Apex externals such as [[apexd3d-external]] and [[apex-full-cheat]] by illustrating the below-OS DMA lane; sits beside CS2 DMA samples such as [[cs2-dma]] and [[cs2-dma-cheat]] as another open-source title-specific PCILeech/MemProcFS stack with zero target-OS software.

## Links

- Repo: https://github.com/boowampp/ApexDmaCheatUpdated

## Related

[[easy-anti-cheat]] · [[dma]] · [[pcileech]] · [[world-to-screen]] · [[ai-aimbot-detection]] · [[hardware-input-injection]] · [[cs2-dma]] · [[cs2-dma-cheat]] · [[apexd3d-external]] · [[apex-full-cheat]] · [[apex-legends-sdk]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
