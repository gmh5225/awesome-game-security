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

**DFSC4317 — Obfuscating Game Hacking Through Hardware** (Lagrossa/DFSC4317-Obfuscating-Game-Hacking-Through-Hardware) is course research documenting **hardware-obfuscated** cheating: **FPGA DMA** reads game memory from an **external host** so no cheat executable runs on the gaming PC. Target title: Valve **Deadlock**; demonstrated outcome: entity-related data off the machine and **minimap overlay** plotting. README lanes: Cheat / Guide. (source: wiki/sources/descriptions/Lagrossa__DFSC4317-Obfuscating-Game-Hacking-Through-Hardware.md)

## Approach

- **External acquisition:** DMA-capable FPGA board on the target PCIe tree; analysis and visualization on a separate machine.
- **Obfuscation angle:** Bypasses conventional **in-process** anti-cheat and software instrumentation because attacker logic stays off the game OS.
- **Boundary:** Effectiveness still depends on [[iommu]] / containment policy and device attestation—not automatic against all [[assurance-boundaries]].

## Artifacts

- Explanatory **paper and slides**; not a full DMA software stack (contrast [[hoozi-cs2-dma]], [[luminary-dma]], [[cyclone-v-pcie-avmm-dma]] bring-up repos).
- Minimap-style **entity plotting** as the visible cheat surface while reads use [[memory-acquisition-path]] hardware initiators.

## Audience

Game security researchers studying **hardware-assisted cheating**, external memory acquisition, and anti-cheat evasion pedagogy—complements title-specific DMA radars and firmware guides without shipping a maintained cheat product.

## Links

- Repo: https://github.com/Lagrossa/DFSC4317-Obfuscating-Game-Hacking-Through-Hardware

[[cyclone-v-pcie-avmm-dma]] · [[luminary-dma]] · [[hoozi-cs2-dma]] · [[memory-acquisition-path]] · [[assurance-boundaries]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
