---
title: RX25 DMA Reader
kind: entity
topics: [dma-attack, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Guosstar__rx25-dma-reader.md
updated: 2026-11-18
confidence: medium
---

# RX25 DMA Reader

**Two-board FPGA stack** for high-throughput PCIe DMA reads of host physical memory: a target-side PCIe initiator (no Windows driver on the gaming or forensics target) and an analysis-side board linked over a **25G optical Ethernet** path. Custom **SystemVerilog** RTL with Vivado build flows pairs deep **PCIe TLP and BAR** plumbing (ordered reads, sessions, diagnostics) with **Corundum-style 25G** transport. The initiator runs a **KMDF** kernel driver exposing batched capture, transport, snapshot, and completion-queue interfaces; the analysis machine loads a **LeechCore device plugin** (`device rx25`) so [[pcileech]] / MemProcFS workflows consume the remote physical-memory stream without in-target software. (source: wiki/sources/descriptions/Guosstar__rx25-dma-reader.md)

Suited to game security and anti-cheat research, forensic imaging, and reverse engineering that need reliable **out-of-band** memory acquisition rather than in-process hooks—same [[memory-acquisition-path]] topology as M.2 [[pcileech-fpga]] cards, with optical decoupling between target and operator host. (source: wiki/sources/descriptions/Guosstar__rx25-dma-reader.md)

## Architecture

- **Target board:** PCIe bus master issuing ordered memory-read TLPs; no target-OS driver footprint.
- **Initiator / analysis path:** 25G optical link; Windows KMDF driver for batched DMA capture and completion queues.
- **Host tooling:** LeechCore `rx25` plugin → standard [[pcileech]] / VMM analysis stack on the second PC.

## Links

- Repo: https://github.com/guosstar/rx25-dma-reader

## Related

[[pcileech]] · [[pcileech-fpga]] · [[cyclone-v-pcie-avmm-dma]] · [[litepcie]] · [[memory-acquisition-path]] · [[dma-pe-dumper]] · [[volk-dma]] · [[overviews/dma-attack]] · [[concepts/dma]]