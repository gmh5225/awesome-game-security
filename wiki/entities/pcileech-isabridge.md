---
title: Pcileech ISABridge (Herooyyy)
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Herooyyy__Pcileech-ISABridge.md
updated: 2026-08-24
confidence: medium
---

# Pcileech ISABridge (Herooyyy)

**[[pcileech]]-class FPGA DMA firmware** that emulates an **ISA-bridge-style PCIe device profile** for hardware-assisted memory-access research. Implemented in **Verilog/SystemVerilog** with **Xilinx Vivado** project files and **generated bitstream** outputs. Demonstrates **PID/VID spoofing** via bridge-device simulation to study how anti-cheat systems **classify and block suspicious PCIe peripherals**. (source: wiki/sources/descriptions/Herooyyy__Pcileech-ISABridge.md)

## Anti-cheat context

Curated README positions the release toward **Faceit**-class **hardware filtering** that keys on PCIe **vendor/device identity** rather than only stock Xilinx DMA fingerprints. Contrasts with network-controller emulation forks such as [[dma-pcileech]], [[pcileech-wifi]], and wired-NIC behavioral releases like [[pcileech-intel-i226-v-fullemu]] from the same author lane. See PCIe identity probes and the firmware tier ladder on [[overviews/dma-attack]].

## Links

- Repo: https://github.com/Herooyyy/Pcileech-ISABridge

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-activator-anti-crack]] · [[pcileech-intel-i226-v-fullemu]] · [[dma-pcileech]] · [[pcileech-wifi]] · [[pcileech-wifi-v2]] · [[pcileechgen]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
