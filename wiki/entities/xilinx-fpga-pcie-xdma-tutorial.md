---
title: Xilinx FPGA PCIe XDMA Tutorial
kind: entity
topics: [dma-attack, reverse-engineering]
sources:
  - wiki/sources/descriptions/WangXuan95__Xilinx-FPGA-PCIe-XDMA-Tutorial.md
updated: 2026-08-19
confidence: medium
---

# Xilinx FPGA PCIe XDMA Tutorial

Hands-on **Xilinx Vivado** tutorial for building **PCIe communication systems** with the **XDMA IP core**: step-by-step **BRAM read/write** designs, **AXI** integration, **Linux-side C** host software, and a larger **MPEG2 acceleration** workflow. Material mixes Vivado projects, Verilog/AXI logic, and host bring-up guidance (driver loading and test procedures). Aimed at FPGA and hardware-security practitioners, including **DMA-oriented game-security research**. (source: wiki/sources/descriptions/WangXuan95__Xilinx-FPGA-PCIe-XDMA-Tutorial.md)

## Role in the DMA stack

Educational **XDMA endpoint bring-up** lane—not a turnkey [[pcileech-fpga]] firmware fork. Useful before adapting Artix-7 silicon toward custom DMA endpoints or studying how host drivers, AXI bridges, and PCIe DMA engines interact. Complements reference cores such as [[litepcie]], custom board HDL like [[dma-pcie-board-75t]], and Vivado/SystemVerilog stacks in [[pcileech-fpga]].

## Links

- Repo: https://github.com/WangXuan95/Xilinx-FPGA-PCIe-XDMA-Tutorial

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[litepcie]] · [[dma-pcie-board-75t]] · [[fpga-dma-multi-tool]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
