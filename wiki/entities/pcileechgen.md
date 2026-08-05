---
title: PCILeechGen
kind: entity
topics: [dma-attack, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/sercanarga__pcileechgen.md
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
updated: 2026-08-05
confidence: medium
---

# PCILeechGen

Go-based **custom firmware generator** for [[pcileech-fpga]] DMA boards that **clones the PCIe identity** of a real PCI/PCIe donor device and outputs a **ready-to-flash Vivado bitstream**. Reads donor hardware on Linux through **VFIO**, captures config space, BAR layouts, and capabilities, then emits **SystemVerilog** and **COE** artifacts for Xilinx Vivado synthesis. Automates **scan, check, build, and validate** workflows across many common PCILeech-compatible FPGA boards. (source: wiki/sources/descriptions/sercanarga__pcileechgen.md)

## Pipeline

1. **Donor capture (Linux):** VFIO access to real PCIe hardware; dump config space, BAR layouts, and extended capabilities.
2. **Codegen:** SystemVerilog modules and `.coe` init files with config-space scrubbing, **dynamic BAR emulation**, MSI-X tables, and optional **offline MMIO trace** import to refine register behavior.
3. **Synthesis:** Xilinx Vivado produces a flash-ready bitstream; validate step confirms donor-aligned behavior before deployment.

## Emulation features

**NVMe admin-queue and DMA bridge** support, MSI-X handling, config-space scrubbing, dynamic BAR emulation, MMIO trace import, and **TLP latency and timing emulation** for realistic device behavior — features that help move firmware beyond stock Tier-0/1 [[pcileech-fpga]] fingerprints toward donor-matched behavioral emulation (tiers 2–5). (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Research audience

Aimed at security researchers studying **PCIe and DMA attack surfaces**, FPGA-based memory access techniques, and **anti-cheat or hardware-trust** research in educational settings. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Links

- Repo: https://github.com/sercanarga/pcileechgen — README: Go tool to clone a real PCI/PCIe donor via VFIO and synthesize ready-to-flash PCILeech FPGA bitstreams through Vivado

## Related

[[dma]] · [[iommu]] · [[pcileech]] · [[pcileech-fpga]] · [[fpga-dma-multi-tool]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
