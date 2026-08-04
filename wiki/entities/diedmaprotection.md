---
title: DieDMAProtection
kind: entity
topics: [dma-attack, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/iqrw0__DieDMAProtection.md
updated: 2026-08-04
confidence: medium
---

# DieDMAProtection

Windows proof-of-concept kernel driver that disables DMA protection (IOMMU / VT-d) by manipulating DMA remapping configuration, re-enabling direct physical memory access from external PCIe devices such as FPGA-based [[pcileech]] hardware. Demonstrates the attack surface of OS DMA protection implementations for researchers studying IOMMU bypass and containment boundaries—not a production anti-cheat component. (source: wiki/sources/descriptions/iqrw0__DieDMAProtection.md)

Complements defensive IOMMU programming samples like [[helloiommupkg]] and firmware hardening such as [[x670e-tomahawk-anticheat-update]]; pairs with [[byovd]]-class kernel table reprogramming in the bypass catalog on [[iommu]].

## Links

- Repo: https://github.com/iqrw0/DieDMAProtection

## Related

[[iommu]] · [[dma]] · [[pcileech]] · [[helloiommupkg]] · [[byovd]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
