---
title: DMA-PCIE-BOARD-75T
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md
updated: 2026-08-14
confidence: medium
---

# DMA-PCIE-BOARD-75T

Custom **PCIe DMA board design** built around a **Xilinx Artix-7 75T** FPGA for hardware-level host memory access. Ships **firmware and HDL sources** for a bespoke PCIe endpoint that issues DMA reads and writes against system RAM—aimed at game-security research and testing rather than a turnkey host stack. (source: wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md)

## Role in the DMA stack

Sits in the **FPGA bring-up / firmware** lane alongside [[pcileech-fpga]] and board utilities such as [[fpga-dma-multi-tool]] and [[dma-tools-rs]]: researchers flash or adapt the HDL, then drive the card from a separate cheat PC via [[pcileech]]/LeechCore once the endpoint enumerates. Artix-7 **75T** is the same class of silicon used in many consumer DMA boards (Captain, Squirrel, stealth forks such as [[pcileech-dma-fullstealth]]), so config-space and behavioral probes follow the tier ladder in [[overviews/dma-attack]].

## Links

- Repo: https://github.com/gmh5225/DMA-PCIE-BOARD-75T

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[fpga-dma-multi-tool]] · [[dma-tools-rs]] · [[memtools]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
