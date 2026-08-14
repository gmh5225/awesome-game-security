---
title: DDMA-1
kind: entity
topics: [dma-attack, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__DDMA-1.md
updated: 2026-08-14
confidence: medium
---

# DDMA-1

**Disk-based DMA** game-cheating framework using **PCIe hardware** for direct host memory access. Reads and writes game process memory over DMA with **no software footprint on the target system**, aiming to bypass kernel-level anti-cheat that monitors processes, drivers, and injections on the gaming OS. README categorizes it as **disk-based DMA for ATA and SCSI** — a storage-controller camouflage lane distinct from NVMe/VMD forks such as [[pcileech-dma-nvme-vmd]]. (source: wiki/sources/descriptions/gmh5225__DDMA-1.md)

## Role in the DMA stack

Sits in the **class-emulation / stealth firmware** tier alongside [[pcileech-fpga-dma-vmd]] and [[pcileech-dma-nvme-vmd]]: the endpoint presents as a legacy disk controller (ATA/SCSI) while a separate cheat PC issues Memory Read/Write TLPs via the usual [[pcileech]]/LeechCore host stack. Detection shifts toward BAR MMIO, MSI/MSI-X, and storage-class behavioral baselines rather than process/handle signals — see the tier ladder in [[overviews/dma-attack]].

## Links

- Repo: https://github.com/gmh5225/DDMA-1

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-fpga-dma-vmd]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
