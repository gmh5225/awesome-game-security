---
title: pcileech-wifi (ekknod)
kind: entity
topics: [dma-attack, anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ekknod__pcileech-wifi.md
updated: 2026-08-16
confidence: medium
---

# pcileech-wifi (ekknod)

[[pcileech-fpga]]-based **DMA firmware** variant that emulates a **wireless (Wi‑Fi) network adapter** on PCIe instead of presenting stock placeholder or storage-class identities. Targets game-security researchers and reverse engineers studying offensive PCIe camouflage and anti-cheat detection in the cheat / DMA lane. (source: wiki/sources/descriptions/ekknod__pcileech-wifi.md)

## Detection relevance

Wireless NIC class presentation shifts fingerprinting toward **network-controller** probes—BAR MMIO register layouts, MSI/MSI-X interrupt patterns, and driver-loaded behavioral baselines—rather than trivial Tier-0/1 Xilinx placeholder IDs. Compare other class-emulation forks such as [[pcileech-fpga-dma-vmd]], [[pcileech-dma-nvme-vmd]], and the tier ladder in [[overviews/dma-attack]].

## Forks

[[pcileech-wifi-v2]] (dom0ng) extends this baseline with Verilog PCIe 7x IP integration and customizable device-ID generation scripts for multiple FPGA boards. (source: wiki/sources/descriptions/dom0ng__pcileech-wifi-v2.md)

## Links

- Repo: https://github.com/ekknod/pcileech-wifi

## Related

[[pcileech-wifi-v2]] · [[pcileech]] · [[pcileech-fpga]] · [[vm]] · [[pcileech-fpga-dma-vmd]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-dma-fullstealth]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
