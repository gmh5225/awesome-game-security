---
title: VTD-Bypass
kind: entity
topics: [dma-attack, windows-kernel, anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md
updated: 2026-09-25
confidence: medium
---

# VTD-Bypass

Python tool (kEv1nZ0/VTD-Bypass) that automates bypassing VT-d and IOMMU-related detection by reading and modifying ACPI tables in host physical memory via LeechCore over FPGA DMA hardware. It dumps memory, locates the XSDT table, builds a checksum-valid DMAR table, and patches XSDT so the system reports VT-d as enabled when firmware has it disabled. Techniques include signature-based ACPI table search, 4KB-aligned hole selection, DRHD base placement in high MMIO space, encrypted configuration files, and repeated timed writes during boot. Targets hardware security research, ACPI/IOMMU analysis, and anti-cheat testing where VT-d enforcement is checked. (source: wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md)

## Role in the DMA stack

Offensive **IOMMU/ACPI spoofing** lane beside kernel remapping PoCs such as [[diedmaprotection]] and defensive samples such as [[dmaprotect]]—uses physical DMA writes to fabricate firmware-visible VT-d state rather than driver-mediated table edits. (source: wiki/sources/README-categories.md)

## Requirements

Windows host, Python 3.9–3.11, leechcorepyc, and external DMA libraries. (source: wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md)

## Links

- Repo: https://github.com/kEv1nZ0/VTD-Bypass

## Related

[[pcileech]] · [[pcileech-fpga]] · [[iommu]] · [[diedmaprotection]] · [[dmaprotect]] · [[sewindows]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
