---
title: NexusForge
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Sylnar__NexusForge.md
updated: 2026-10-18
confidence: medium
---

# NexusForge

Standalone **Windows** desktop utility (C# on **.NET 8**, **Avalonia** UI) for operating **FPGA-based DMA boards** without **Xilinx Vivado**. Auto-detects **Artix-7** and **Kintex-7** devices over **CH347 JTAG** using bundled **OpenOCD** configs, reads 57-bit factory **DNA**, and flashes DNA-locked **SPI** or volatile bitstream firmware with live erase/write/verify progress. Installs and manages **CH347 JTAG** and **FTDI FT601** USB3 drivers, enumerates **PCIe BARs**, and runs **DMA read speed tests** to confirm host-side physical memory access. Targets operators and researchers who set up, update, and validate commercial DMA hardware in game-security, anti-cheat, and reverse-engineering workflows. (source: wiki/sources/descriptions/Sylnar__NexusForge.md)

## Links

- Repo: https://github.com/Sylnar/NexusForge

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[fpga-dma-multi-tool]] · [[dma-tools-rs]] · [[mewtools]] · [[dma-speedtest-memflow-rs]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
