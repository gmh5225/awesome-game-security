---
title: PCILeechFWGenerator
kind: entity
topics: [dma-attack, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/VoltCyclone__PCILeechFWGenerator.md
updated: 2026-11-20
confidence: medium
---

# PCILeechFWGenerator

Linux **Python toolchain** that builds custom **PCIe DMA FPGA bitstreams** for [[pcileech-fpga]] hardware by cloning the configuration and behavior of a real **donor PCI device**. A three-stage pipeline captures identity, BARs, capabilities, and MSI-X through **VFIO** (with optional MMIO tracing), renders **Jinja2** templates into **SystemVerilog** and board support files, and synthesizes with **Xilinx Vivado** for common DMA boards. Features include MSI-X emulation, register learning from native drivers, **Podman**-based builds, a **Textual** TUI, and flashing helpers. (source: wiki/sources/descriptions/VoltCyclone__PCILeechFWGenerator.md)

## Pipeline

1. **Donor profiling (Linux):** VFIO access; device identity, BAR layout, extended capabilities, MSI-X tables; optional MMIO trace for register behavior.
2. **Codegen:** Jinja2 → SystemVerilog and board files; config-space shadow, MSI-X, and donor-aligned BAR emulation.
3. **Build & flash:** Vivado synthesis; Podman-isolated build option; helpers for widely used PCILeech-class boards.

## Research audience

Aimed at security researchers and developers studying **PCIe DMA**, hardware-assisted memory access, **anti-cheat evasion** threat models, and firmware or reverse-engineering work on isolated lab systems—not in-process game modification. (source: wiki/sources/descriptions/VoltCyclone__PCILeechFWGenerator.md)

## Links

- Repo: https://github.com/VoltCyclone/PCILeechFWGenerator — README: VFIO-based pipeline that profiles a real PCIe donor and generates customized PCILeech FPGA firmware (config shadow, MSI-X, Vivado build)

## Related

[[dma]] · [[iommu]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileechgen]] · [[fpga-dma-multi-tool]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]