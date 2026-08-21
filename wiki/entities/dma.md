---
title: DMA (Rakeshmonkee)
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Rakeshmonkee__DMA.md
updated: 2026-08-21
confidence: medium
---

# DMA (Rakeshmonkee)

Practical **guide and toolkit** for building and customizing **PCIe DMA firmware** on **FPGA-based boards**. Combines Markdown documentation with **Python** and **Tcl** utilities for automated project generation and firmware preparation. Covers step-by-step **Xilinx Vivado** customization, **config-space cloning**, automatic firmware-generation scripts, and **bitstream flash** workflows. Primary use case is game-security research on DMA hardware behavior and **anti-cheat evasion testing** in controlled environments. (source: wiki/sources/descriptions/Rakeshmonkee__DMA.md)

## Workflow highlights

| Stage | Focus |
|-------|--------|
| Vivado customization | Hand-edited IP/project settings for FPGA DMA endpoints |
| Config-space clone | Donor PCI identity harvest → firmware shadow config |
| Auto-generation | Python/Tcl scripts for project and firmware prep |
| Flash | Bitstream build and programming workflows |

Complements hand-edit guides such as [[dma-cfw-guide]] and [[dma-attack-firmware-customization]] with scripted generation paths; pairs with automated donor pipelines like [[pcileechgen]] when moving from donor capture to flash-ready [[pcileech-fpga]] bitstreams.

## Links

- Repo: https://github.com/Rakeshmonkee/DMA

## Related

[[pcileech-fpga]] · [[pcileech]] · [[pcileechgen]] · [[dma-cfw-guide]] · [[dma-attack-firmware-customization]] · [[concepts/dma]] · [[iommu]] · [[easy-anti-cheat]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
