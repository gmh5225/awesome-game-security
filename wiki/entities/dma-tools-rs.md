---
title: dma-tools-rs
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/sh1ftd__dma-tools-rs.md
updated: 2026-07-31
confidence: medium
---

# dma-tools-rs

Windows desktop application (Rust, **egui**/**eframe**) for programming SPI flash **bitstreams** and reading device **DNA** on Xilinx **Artix-7** FPGAs (35T, 75T, 100T) over **JTAG** in DMA hardware setups. Orchestrates bundled **OpenOCD** builds with project-specific TAP, flash, and DNA scripts for **CH347** and **FTDI RS232** JTAG adapters; the UI parses flash progress and discovers firmware payloads. Capabilities include bitstream programming, unique device DNA extraction, elevated driver-install helpers for FTDI and CH347 stacks, runtime validation of bundled OpenOCD/tools payloads, and a **PCILeech** sanity check via **memflow-base**. Aimed at operators configuring and maintaining FPGA-based DMA cards in game-security research, reverse engineering, and related hardware workflows. (source: wiki/sources/descriptions/sh1ftd__dma-tools-rs.md)

## Links

- Repo: https://github.com/sh1ftd/dma-tools-rs

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[fpga-dma-multi-tool]] · [[dma-speedtest-memflow-rs]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
