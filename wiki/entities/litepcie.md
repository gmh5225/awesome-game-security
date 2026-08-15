---
title: LitePCIe
kind: entity
topics: [dma-attack, reverse-engineering]
sources:
  - wiki/sources/descriptions/enjoy-digital__litepcie.md
updated: 2026-08-15
confidence: medium
---

# LitePCIe

Lightweight **Python/Migen** PCIe **endpoint core** for FPGA development: a complete PCIe implementation with **DMA engines**, **LTSSM tracing**, and **user-space driver** interfaces. Supports Xilinx KC705, KCU105, XCU1525, and Acorn boards with benchmark scripts and example configurations. (source: wiki/sources/descriptions/enjoy-digital__litepcie.md)

## Role in the DMA stack

Educational/reference **PCIe endpoint design** lane—not a turnkey [[pcileech]] firmware fork. Useful for FPGA developers and DMA security researchers studying endpoint architecture, DMA engine implementation, and hardware-level TLP/link behavior before adapting silicon toward attack or defense prototypes. Complements Vivado/SystemVerilog stacks such as [[pcileech-fpga]] and custom board designs like [[dma-pcie-board-75t]].

## Links

- Repo: https://github.com/enjoy-digital/litepcie

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[dma-pcie-board-75t]] · [[fpga-dma-multi-tool]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
