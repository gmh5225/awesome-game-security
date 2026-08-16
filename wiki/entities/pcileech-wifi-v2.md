---
title: pcileech-wifi-v2 (dom0ng)
kind: entity
topics: [dma-attack, anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/dom0ng__pcileech-wifi-v2.md
updated: 2026-08-16
confidence: medium
---

# pcileech-wifi-v2 (dom0ng)

[[pcileech-fpga]] **DMA firmware** fork that emulates a **wireless (Wi‑Fi) network adapter** PCIe configuration space so a DMA attack device can masquerade as a WiFi card on the target bus. Builds on [[pcileech-wifi]] (ekknod) with **Verilog-based PCIe 7x IP core** integration and **customizable device ID generation scripts** for multiple FPGA boards. Targets DMA security researchers studying PCIe device impersonation and anti-cheat DMA detection evasion. (source: wiki/sources/descriptions/dom0ng__pcileech-wifi-v2.md)

## Technical notes

Compared to the upstream [[pcileech-wifi]] baseline, the v2 fork emphasizes Xilinx **PCIe 7-series IP** integration in Verilog and board-specific **VID/DID scripting**—useful when tailoring wireless-class fingerprints across CaptainDMA, ScreamerM2, and related Artix-7 boards without hand-editing shadow config alone. Detection relevance matches other **network-controller class** emulation: BAR MMIO register layouts, MSI/MSI-X interrupt patterns, and driver-loaded behavioral baselines rather than stock Tier-0/1 placeholder IDs. (source: wiki/sources/descriptions/dom0ng__pcileech-wifi-v2.md)

## Links

- Repo: https://github.com/dom0ng/pcileech-wifi-v2

## Related

[[pcileech-wifi]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileech-fpga-dma-vmd]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-dma-fullstealth]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
