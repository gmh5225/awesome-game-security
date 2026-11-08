---
title: dma-attacks (xairy)
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/xairy__dma-attacks.md
updated: 2026-11-08
confidence: high
---

# dma-attacks (xairy)

Curated **reference collection** and companion materials for an introductory talk on **PCI Express** and **direct memory access (DMA)** attacks—not an application codebase. Organizes **slides**, **videos**, and a large **annotated bibliography** spanning PCIe fundamentals, **FPGA device emulation**, Thunderbolt and hotplug issues, and real-world attack write-ups. Topics include PCILeech-style DMA hardware, **IOMMU** and kernel DMA protection bypasses, BitLocker and enterprise countermeasures, and recent research on **detecting PCIe DMA-based cheating**. Entry point for security researchers, penetration testers, and professionals in **game security**, **anti-cheat**, and hardware-assisted reverse engineering who need a structured DMA threat-model and defense reading list. (source: wiki/sources/descriptions/xairy__dma-attacks.md)

## Scope

| Layer | Content |
|-------|--------|
| Education | PCIe/DMA talk decks and recordings |
| Bibliography | Annotated links: hardware cheats, bypass research, enterprise mitigations |
| Audience | AC engineers, pentesters, hardware-assisted RE |

Complements hands-on **Guide** lanes ([[dma-fw-guide-2.0]], [[pcileech-dma-firmware-guide]], [[entities/dma]]) and tool entities ([[pcileech]], [[pcileech-fpga]]) with curated background reading rather than firmware or host tooling.

## Links

- Repo: https://github.com/xairy/dma-attacks

## Related

[[concepts/dma]] · [[iommu]] · [[pcileech]] · [[pcileech-fpga]] · [[dma-fw-guide-2.0]] · [[assurance-boundaries]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
