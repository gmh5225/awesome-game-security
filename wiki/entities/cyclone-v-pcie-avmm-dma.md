---
title: Cyclone V PCIe AVMM DMA
kind: entity
topics: [dma-attack, reverse-engineering]
sources:
  - wiki/sources/descriptions/apoj-inc__Cyclone-V-PCIe-AVMM-DMA.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# Cyclone V PCIe AVMM DMA

Configurable **PCIe 2.0 x4 FPGA DMA controller** that moves data between a host PC and on-chip logic through Avalon-MM interfaces and FIFOs. SystemVerilog RTL targets Intel Cyclone V boards with Quartus Platform Designer integration, Makefile-driven synthesis, and Questa or Cocotb simulation. Supports up to sixteen independent DMA channels, MSI-X completion interrupts, per-channel external interrupt sources, and custom control/status registers on the AVMM bus. A Linux kernel module and C userspace examples exercise multi-channel echo, parallel read/write, and IRQ paths. (source: wiki/sources/descriptions/apoj-inc__Cyclone-V-PCIe-AVMM-DMA.md)

Reference stack for custom PCIe DMA FPGA designs and study of DMA attack surfaces relevant to game anti-cheat and low-level containment research. Sits beside [[litepcie]], [[pcileech-fpga]], and [[learn-fpga-programming]] on [[overviews/dma-attack]].

## Links

- Repo: https://github.com/apoj-inc/Cyclone-V-PCIe-AVMM-DMA

## Related

[[litepcie]] · [[pcileech-fpga]] · [[pcileech]] · [[memory-acquisition-path]] · [[iommu]] · [[overviews/dma-attack]]
