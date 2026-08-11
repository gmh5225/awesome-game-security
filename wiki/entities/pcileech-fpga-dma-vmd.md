---
title: PCILeech-FPGA-DMA-VMD
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md
updated: 2026-07-29
confidence: medium
---

# PCILeech-FPGA-DMA-VMD

[[pcileech]] FPGA **firmware** for **Xilinx Artix-7 XC7A75T** that emulates an **Intel RST VMD** (Volume Management Device) controller (**Device ID 9A0B**) for DMA-based host memory access. Implements multi-function PCI device simulation, **MSI-X** interrupt handling, **NVMe command processing**, configurable **BAR** addressing, and TLP-level **PCIe config-space shadowing** in **SystemVerilog**—a class-behavioral fork above stock [[pcileech-fpga]] placeholder IDs. (source: wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md)

## Detection relevance

VMD-class emulation targets **Tier 4–5** firmware sophistication: BAR MMIO, MSI-X, and storage-controller behavioral probes rather than trivial `10EE:0666` blacklist hits. AC PCIe integrity checks should still validate donor-consistent config capabilities, NVMe register layouts, interrupt accounting, and completion-latency baselines—not VID/DID alone. See [[overviews/dma-attack]] firmware tiers.

## Links

- Repo: https://github.com/mltpig/PCILeech-FPGA-DMA_VMD

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-dma-fullstealth]] · [[pcileech-dma-nvme-vmd]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
