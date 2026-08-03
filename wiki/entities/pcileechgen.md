---
title: PCILeechGen
kind: entity
topics: [dma-attack, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
updated: 2026-08-03
confidence: medium
---

# PCILeechGen

Go-based **custom firmware generator** for [[pcileech-fpga]] DMA boards that **clones the PCIe identity** of a real donor device and outputs a **ready-to-flash Vivado bitstream**. Reads donor hardware on Linux through **VFIO** and **IOMMU**, captures config space, BAR layouts, and extended capabilities, then emits **SystemVerilog** and **COE** artifacts for Xilinx synthesis. Supports NVMe controller behavior, MSI-X tables, config-space scrubbing, BAR profiling, MMIO tracing, and TLP latency tuning across many supported FPGA boards. Targets security research on PCIe DMA attacks, hardware identity spoofing, and anti-cheat defenses against external memory-access cheat hardware. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Links

- Repo: https://github.com/sercanarga/pcileechgen

## Related

[[dma]] · [[iommu]] · [[pcileech]] · [[pcileech-fpga]] · [[fpga-dma-multi-tool]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
