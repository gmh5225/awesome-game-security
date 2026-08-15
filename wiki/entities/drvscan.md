---
title: drvscan (ekknod)
kind: entity
topics: [dma-attack, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/ekknod__drvscan.md
updated: 2026-08-15
confidence: medium
---

# drvscan (ekknod)

**drvscan** is a Windows **DMA/PCIe device scanner and memory forensics** tool written in **C**. It enumerates PCI Express devices, flags suspicious or unknown endpoints that may be DMA attack hardware (FPGA boards), and scans physical memory through direct PCIe access for known cheat or rootkit signatures. Supports **pcileech-style memory acquisition** and device fingerprinting for anti-cheat engineers and security researchers in the Detection:DMA lane. (source: wiki/sources/descriptions/ekknod__drvscan.md)

## Detection relevance

Complements kernel config-space inventory such as [[pcie-detector]] by pairing **PCIe enumeration** with **physical-memory signature scans** over the same DMA read path offensive stacks use via [[pcileech]]. Useful when studying how class-emulation firmware such as [[pcileech-wifi]] or donor-cloned [[pcileech-fpga]] builds appear in a live bus inventory versus known cheat/rootkit residue in RAM.

## Links

- Repo: https://github.com/ekknod/drvscan

## Related

[[pcileech]] · [[pcie-detector]] · [[pcileech-fpga]] · [[pcileech-wifi]] · [[vm]] · [[volk-dma]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
