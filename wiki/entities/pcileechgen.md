---
title: PCILeechGen
kind: entity
topics: [dma-attack, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
updated: 2026-08-04
confidence: medium
---

# PCILeechGen

Go-based **custom firmware generator** for [[pcileech-fpga]] DMA boards that **clones the PCIe identity** of a real PCI/PCIe donor device and outputs a **ready-to-flash Vivado bitstream**. Reads donor hardware on Linux through **VFIO** and **IOMMU**, captures config space, BAR layouts, and capabilities, then emits **SystemVerilog** and **COE** artifacts for Xilinx synthesis. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Pipeline

1. **Donor capture (Linux):** VFIO/IOMMU access to real PCIe hardware; dump config space, BAR layouts, and extended capabilities.
2. **Codegen:** SystemVerilog modules and `.coe` init data for shadow config, BAR profiles, and MSI-X tables.
3. **Synthesis:** Xilinx Vivado produces a flash-ready bitstream for supported [[pcileech-fpga]] boards.

## Emulation features

NVMe controller behavior, MSI-X tables, config-space scrubbing, BAR profiling, MMIO tracing, and timing-oriented TLP latency tuning — features that help move firmware beyond stock Tier-0/1 [[pcileech-fpga]] fingerprints toward donor-matched behavioral emulation. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Anti-cheat relevance

Automates **hardware identity spoofing** for external DMA cheat hardware; donor-aligned config/BAR/MSI-X and latency tuning raise the bar for PCIe fingerprinting and completion-latency baselines in game-security DMA detection pipelines. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Links

- Repo: https://github.com/sercanarga/pcileechgen

## Related

[[dma]] · [[iommu]] · [[pcileech]] · [[pcileech-fpga]] · [[fpga-dma-multi-tool]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
