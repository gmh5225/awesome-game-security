---
title: VGK DMA bypass
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/d1skq__vgk-dma-bypass.md
updated: 2026-08-16
confidence: medium
---

# VGK DMA bypass

Modified **[[pcileech-fpga]]** Artix-7 PCIe **configuration-space** SystemVerilog fork aimed at **[[vanguard]]** (VGK) DMA-related research. The archive centers on `pcileech_pcie_cfg_a7.sv` with **CFG-space** and **MSI-X**-oriented changes derived from the PCILeech FPGA stack—not a full cheat stack, but firmware/HDL for studying how Vanguard-class anti-cheat DMA threat models interact with PCIe config and interrupt behavior. (source: wiki/sources/descriptions/d1skq__vgk-dma-bypass.md)

## Detection relevance

Sits in the **firmware tier** lane beside class-emulation forks such as [[pcileech-fpga-dma-vmd]] and [[pcileech-wifi]]: researchers use it to probe whether config-space shadowing, MSI-X layout, and BAR/capability-chain integrity checks differ when the defensive target is Vanguard's PCIe/DMA inventory rather than generic EAC/BattlEye stacks. See [[overviews/dma-attack]] firmware tiers and [[concepts/dma]] anti-cheat detection pipeline.

## Links

- Repo: https://github.com/d1skq/vgk-dma-bypass

## Related

[[vanguard]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileech-fpga-dma-vmd]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
