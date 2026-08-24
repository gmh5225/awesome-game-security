---
title: Free DMA Firmware pcileech (Herooyyy)
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Herooyyy__Free-DMA-Firmware-pcileech.md
updated: 2026-08-24
confidence: medium
---

# Free DMA Firmware pcileech (Herooyyy)

**[[pcileech]]-class FPGA DMA firmware** for PCILeech-compatible hardware used to **emulate PCIe devices** in security testing. Implemented in **Verilog/SystemVerilog** with **Xilinx Vivado** IP cores and **board-specific build scripts**. Includes logic for **PCIe configuration-space behavior**, **MSI-X interrupt handling patterns**, and **multiple hardware persona profiles**. Primarily used for **low-level anti-cheat evasion research** and experimentation with **DMA-based detection bypass** techniques. (source: wiki/sources/descriptions/Herooyyy__Free-DMA-Firmware-pcileech.md)

## Anti-cheat context

Curated README positions the release toward **[[vanguard]] (VGK)** and **Faceit (FAC)** bypass via **MSI-X interrupt** handling—interrupt-driven probes that correlate DMA cards with suspicious MSI/MSI-X patterns. Contrasts with no-interrupt profiles such as [[pcileech-amdpci]], bridge-identity forks such as [[pcileech-isabridge]], and wired-NIC behavioral releases like [[pcileech-intel-i226-v-fullemu]] from the same author lane. See PCIe interrupt probes and the firmware tier ladder on [[overviews/dma-attack]].

## Links

- Repo: https://github.com/Herooyyy/Free-DMA-Firmware-pcileech

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-activator-anti-crack]] · [[pcileech-amdpci]] · [[pcileech-intel-i226-v-fullemu]] · [[pcileech-isabridge]] · [[vgk-dma-bypass]] · [[dma-pcileech]] · [[pcileechgen]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
