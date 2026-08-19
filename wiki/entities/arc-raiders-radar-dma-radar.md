---
title: ArcRaidersRadar-dma-Radar
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/a0yark__ArcRaidersRadar-dma-Radar.md
updated: 2026-08-19
confidence: medium
---

# ArcRaidersRadar-dma-Radar

**Arc Raiders** DMA-based radar and ESP tool (a0yark) that reads game memory externally through **FPGA hardware** using **MemProcFS**. Uses **Unicorn Engine** to emulate the game's own decryption functions for resolving obfuscated pointers such as **GWorld**, **GameInstance**, **CameraManager**, and **BoneBase** without manually reversing the decryption logic. The C++ codebase covers DMA initialization, process and module discovery, emulation-based pointer decryption, and a framework for player and actor iteration. (source: wiki/sources/descriptions/a0yark__ArcRaidersRadar-dma-Radar.md)

Mainly useful for DMA security researchers studying **emulation-assisted pointer resolution** and hardware-based external memory reading on Unreal Engine titles with encrypted world pointers—complementing title DMA radars such as [[cs2-dma-radar]] and [[eft-dma-radar-1]], and sibling a0yark samples such as [[pubg-demo]].

## Links

- Repo: https://github.com/a0yark/ArcRaidersRadar-dma-Radar

## Related

[[unreal-object-model]] · [[world-to-screen]] · [[cs2-dma-radar]] · [[eft-dma-radar-1]] · [[apex-dma-cheat-updated]] · [[pubg-demo]] · [[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
