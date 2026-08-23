---
title: CS2-DMA-Extrnal
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/MoZiHao__CS2_DMA_Extrnal.md
updated: 2026-08-23
confidence: medium
---

# CS2-DMA-Extrnal

**Counter-Strike 2** external **DMA toolset** (MoZiHao) written mainly in **C++** that reads and acts on game state from a separate host through **PCIe DMA hardware** (LeechCore / VMMDLL-style components) without running cheat software on the target gaming OS. Feature modules include **aimbot**, **trigger bot**, **radar**, **bunny hop**, and **anti-flash**, controlled through an **ImGui** interface. JSON offset tables and configuration utilities support external memory-driven cheat workflows. Aimed at game hacking and anti-cheat researchers studying DMA-assisted external tooling patterns. (source: wiki/sources/descriptions/MoZiHao__CS2_DMA_Extrnal.md)

Complements MoZiHao's browser-radar fork [[cs2-dma-radar]] and fuller CS2 DMA stacks such as [[cs2-dma]] and [[cs2-dma-cheat]] by illustrating a modular below-OS external with combat/movement helpers plus situational awareness on one host.

## Links

- Repo: https://github.com/MoZiHao/CS2_DMA_Extrnal

## Related

[[cs2-dma-radar]] · [[cs2-dma]] · [[cs2-dma-cheat]] · [[cs2-offsets]] · [[cs2-dumper]] · [[proext]] · [[vesta]] · [[pcileech]] · [[memprocfs-analyzer]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
