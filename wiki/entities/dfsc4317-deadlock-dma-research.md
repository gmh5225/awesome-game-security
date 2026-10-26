---
title: DFSC4317 Deadlock DMA Research
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/Lagrossa__DFSC4317-Obfuscating-Game-Hacking-Through-Hardware.md
  - wiki/sources/README-categories.md
updated: 2026-10-26
confidence: medium
---

# DFSC4317 Deadlock DMA Research

Course research repository (Lagrossa; **DFSC4317**) documenting **hardware-obfuscated** game cheating via **FPGA DMA**: external host memory reads for Valve **Deadlock**, entity data extraction, and **minimap overlay** plotting—without running cheat code on the game PC. (source: wiki/sources/descriptions/Lagrossa__DFSC4317-Obfuscating-Game-Hacking-Through-Hardware.md)

Primarily explanatory material (paper/slides) rather than a full DMA software stack; illustrates how external [[memory-acquisition-path]] initiators can bypass in-process anti-cheat and conventional software instrumentation when IOMMU/containment policy is weak.

## Links

- Repo: https://github.com/Lagrossa/DFSC4317-Obfuscating-Game-Hacking-Through-Hardware

[[cyclone-v-pcie-avmm-dma]] · [[luminary-dma]] · [[hoozi-cs2-dma]] · [[memory-acquisition-path]] · [[assurance-boundaries]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
