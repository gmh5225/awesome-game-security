---
title: DMA FW Guide 2.0
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JPShag__DMA-FW-Guide-2.0.md
updated: 2026-08-24
confidence: medium
---

# DMA FW Guide 2.0

Comprehensive **firmware development guide** for building **custom PCIe DMA device emulation** on **FPGA** platforms. Documents end-to-end workflow steps: **donor device profiling**, **PCIe configuration-space cloning**, **BAR** and **interrupt** handling, and **firmware flashing**. Bundles tooling references and multi-language materials around **PCILeech-style** hardware stacks and **Xilinx Vivado**-based development. Primary audience is hardware security and game **anti-cheat researchers** studying DMA attack simulation and low-level PCIe behavior. (source: wiki/sources/descriptions/JPShag__DMA-FW-Guide-2.0.md)

## Workflow highlights

| Stage | Focus |
|-------|--------|
| Donor profiling | Harvest real PCIe device identity, BAR layout, and capability chain |
| Config clone | Shadow donor config space into FPGA firmware |
| BAR / IRQ | BAR MMIO layout and interrupt handling for realistic endpoint behavior |
| Build / flash | Vivado bitstream generation and programming workflows |

Sits alongside other curated **Guide**-lane firmware walkthroughs such as [[dma-cfw-guide]] (Silverr12; **pcileech-fpga v4.15** hand-edit path) and [[entities/dma]] (Rakeshmonkee; Vivado customization + Python/Tcl auto-generation). Complements automated donor pipelines like [[pcileechgen]] when researchers need documented manual steps before adapting [[pcileech-fpga]] sources. Detection relevance matches the firmware tier ladder in [[overviews/dma-attack]]—config-space integrity, BAR probes, MSI/MSI-X patterns, and TLP behavior—not stock Tier-0/1 placeholder IDs alone.

## Links

- Repo: https://github.com/JPShag/DMA-FW-Guide-2.0

## Related

[[pcileech-fpga]] · [[pcileech]] · [[pcileechgen]] · [[dma-cfw-guide]] · [[entities/dma]] · [[dma-attack-firmware-customization]] · [[xilinx-fpga-pcie-xdma-tutorial]] · [[learn-fpga-programming]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
