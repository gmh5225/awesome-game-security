---
title: DmaProtect
kind: entity
topics: [dma-attack, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/cutecatsandvirtualmachines__DmaProtect.md
updated: 2026-08-16
confidence: medium
---

# DmaProtect

Windows kernel driver that configures Intel VT-d / AMD-Vi IOMMU DMA remapping to restrict which PCIe devices may access system memory—blocking unauthorized physical reads from FPGA-based [[dma]] attack boards such as [[pcileech]] while leaving legitimate devices in permitted domains. Demonstrates defensive runtime IOMMU table programming for anti-cheat engineers and security researchers building DMA mitigations. (source: wiki/sources/descriptions/cutecatsandvirtualmachines__DmaProtect.md)

Defensive counterpart to bypass PoCs like [[diedmaprotection]]; complements UEFI learning samples [[helloiommupkg]] and firmware hardening such as [[x670e-tomahawk-anticheat-update]]. Not a drop-in production anti-cheat component—policy, ACS topology, and kernel trust boundaries still matter on [[iommu]].

## Links

- Repo: https://github.com/cutecatsandvirtualmachines/DmaProtect

## Related

[[iommu]] · [[dma]] · [[diedmaprotection]] · [[helloiommupkg]] · [[pcileech]] · [[byovd]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
