---
title: Pcileech AMDPCI (Herooyyy)
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Herooyyy__Pcileech-AMDPCI.md
updated: 2026-08-24
confidence: medium
---

# Pcileech AMDPCI (Herooyyy)

**[[pcileech]]-class FPGA DMA firmware profile** that emulates an **AMD PCI device model** on PCILeech-compatible hardware. Implemented in **Verilog/SystemVerilog** with **Xilinx Vivado** IP components and build scripts targeting **35T**, **75T**, and **ZDMA** boards. Focuses on **no-interrupt communication behavior** and **hardware identity spoofing** for anti-cheat resilience testing and research into **hardware-signature-based detection**. (source: wiki/sources/descriptions/Herooyyy__Pcileech-AMDPCI.md)

## Anti-cheat context

Curated README positions the release toward **Faceit** and **[[vanguard]] (vgk)** bypass via **MSI/MSI-X absence**—interrupt-driven probes that correlate DMA cards with suspicious interrupt patterns. Contrasts with wired-NIC behavioral releases such as [[pcileech-intel-i226-v-fullemu]] and bridge-identity forks such as [[pcileech-isabridge]] from the same author lane. See PCIe identity and interrupt probes on [[overviews/dma-attack]].

## Links

- Repo: https://github.com/Herooyyy/Pcileech-AMDPCI

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-activator-anti-crack]] · [[pcileech-intel-i226-v-fullemu]] · [[pcileech-isabridge]] · [[dma-pcileech]] · [[pcileechgen]] · [[vgk-dma-bypass]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
