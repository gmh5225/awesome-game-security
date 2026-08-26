---
title: pico_dma
kind: entity
topics: [dma-attack, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Cr4sh__pico_dma.md
updated: 2026-08-26
confidence: medium
---

# pico_dma

**pico_dma** (Cr4sh) is an **FPGA-based platform** for **autonomous pre-boot PCIe DMA attack workflows** on **compact hardware**. It combines **Verilog HDL**, **Vivado** and **Vitis** project assets, and **embedded software** on a **MicroBlaze** soft processor. The stack supports **autonomous payload execution**, **UART-controlled** operation, and **SPI flashing** for flexible deployment. Primary use cases include **hardware-assisted boot and firmware security research** and **DMA implant prototyping**. (source: wiki/sources/descriptions/Cr4sh__pico_dma.md)

## Role in the DMA stack

Compact **pre-boot MicroBlaze** lane from the same author as [[s6-pcie-microblaze]]—targets smaller boards than the legacy **Spartan-6 SP605** toolkit and contrasts with Artix-7 [[pcileech-fpga]] M.2 cheat-hardware stacks. Useful for researchers studying **Option ROM / pre-boot compromise**, **below-OS DMA** threat models, and **firmware implant** workflows before OS-level anti-cheat runs.

## Links

- Repo: https://github.com/Cr4sh/pico_dma

## Related

[[s6-pcie-microblaze]] · [[pcileech]] · [[pcileech-fpga]] · [[litepcie]] · [[xilinx-fpga-pcie-xdma-tutorial]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]]
