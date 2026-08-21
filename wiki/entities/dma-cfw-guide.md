---
title: DMA CFW Guide
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Silverr12__DMA-CFW-Guide.md
updated: 2026-08-21
confidence: medium
---

# DMA CFW Guide

Step-by-step **guide** for building **custom/modified DMA attack firmware** on top of **[[pcileech-fpga]] v4.15** for common FPGA DMA boards (**Squirrel**, **EnigmaX1**, **ZDMA**). Walks through harvesting donor PCIe **device identity and config-space** data with **Arbor** or **Telescan PE**, then patching **SystemVerilog** sources and **Xilinx Vivado** IP settings—vendor/device IDs, **DSN**, **BAR** layouts, and extended capability chains. Also covers **TLP emulation**, interrupt-related notes, **bitstream build and flash** workflows, and an alternate **shadow configuration-space** path using **`.coe` files and writemasks**. Aimed at researchers and practitioners working on PCIe DMA firmware, **anti-cheat evasion threat modeling**, and low-level game-security hardware research. (source: wiki/sources/descriptions/Silverr12__DMA-CFW-Guide.md)

## Workflow highlights

| Stage | Focus |
|-------|--------|
| Donor capture | PCI config space, BAR masks, capability chain, DSN (Arbor / Telescan PE) |
| HDL patch | [[pcileech-fpga]] SystemVerilog + Vivado IP (IDs, BARs, capabilities) |
| Shadow config | `.coe` init + writemask overlay path (tier 2–3 fingerprint hardening) |
| TLP / IRQ | Emulation notes for realistic bus behavior |
| Build/flash | Vivado bitstream for Squirrel / EnigmaX1 / ZDMA |

Broader multi-board coverage than board-specific NIC-cloning guides such as [[dma-attack-firmware-customization]]; complements automated donor pipelines like [[pcileechgen]] when hand-editing **pcileech-fpga 4.15** sources. Detection relevance matches the firmware tier ladder in [[overviews/dma-attack]]—config-space integrity, BAR MMIO probes, MSI/MSI-X patterns, and TLP timing—not just stock Tier-0/1 placeholder IDs.

## Links

- Repo: https://github.com/Silverr12/DMA-CFW-Guide

## Related

[[pcileech-fpga]] · [[pcileech]] · [[pcileechgen]] · [[dma-attack-firmware-customization]] · [[pcileech-wifi]] · [[pcileech-wifi-v2]] · [[dma]] · [[iommu]] · [[easy-anti-cheat]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
