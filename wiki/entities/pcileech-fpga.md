---
title: PCILeech-FPGA
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
updated: 2026-07-19
confidence: medium
---

# PCILeech-FPGA

FPGA **HDL/firmware** and **Vivado** build flows for [[pcileech]] DMA devices that access target system memory over PCIe. Primarily **SystemVerilog/Verilog** with Xilinx IP, constraints, and Tcl for project generation, bitstream builds, and flashing. Covers many board targets (CaptainDMA, PCIeSquirrel, ScreamerM2, EnigmaX1, ZDMA, NeTV2, FT601/FT2232H platforms) plus PCIe TLP handling, BAR control, and configuration-space shadow logic. Used for DMA-based memory acquisition and anti-cheat threat modeling. (source: wiki/sources/descriptions/ufrisk__pcileech-fpga.md)

## Links

- Repo: https://github.com/ufrisk/pcileech-fpga

## Related

[[pcileech]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
