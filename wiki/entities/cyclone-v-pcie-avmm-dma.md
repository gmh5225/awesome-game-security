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

## Architecture

- **Host link:** PCIe 2.0 x4 endpoint; up to sixteen independent DMA channels with FIFO buffering between the link and on-chip logic.
- **On-chip bus:** Avalon-MM (AVMM) with hook-up points for custom control/status registers per channel.
- **Interrupts:** MSI-X completion per channel plus one external interrupt source per channel.
- **Tooling:** Intel Quartus Platform Designer integration; Makefile-driven synthesis and programming; Questa or Cocotb simulation testbenches.

## Research use

End-to-end bring-up (RTL → bitstream → Linux kernel module → C userspace) makes channel scheduling, IRQ delivery, and register maps inspectable without a commercial [[pcileech-fpga]] bitstream. Useful for hardware researchers modeling how external PCIe initiators expose host memory access paths that anti-cheat inventory and [[iommu]] policy must reason about—not a cheat product, but a transparent DMA mechanics baseline. (source: wiki/sources/descriptions/apoj-inc__Cyclone-V-PCIe-AVMM-DMA.md)

## Links

- Repo: https://github.com/apoj-inc/Cyclone-V-PCIe-AVMM-DMA

## Related

[[litepcie]] · [[pcileech-fpga]] · [[pcileech]] · [[memory-acquisition-path]] · [[iommu]] · [[overviews/dma-attack]]
