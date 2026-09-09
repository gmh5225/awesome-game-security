---
title: Memory Acquisition Path
kind: concept
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/dma-attack.md
updated: 2026-09-09
confidence: high
---

# Memory Acquisition Path

Before evaluating a DMA cheat claim, USB bridge cable, LeechCore workflow, or WinPmem-style capture, classify **who initiates memory access**, **how bytes move**, and **where analysis runs**. A library name or second computer does not settle the threat model. (source: wiki/sources/skills/dma-attack.md)

## Classify first

| Dimension | Record explicitly |
|-----------|-------------------|
| Memory source | PCIe requester (FPGA/card), host kernel driver/interface, hypervisor path, or offline image |
| Access requirements | Physical slot, admin/kernel rights, pre-boot window, authenticated transport |
| Transport endpoints | PCIe link, USB/FT601, Ethernet, bridge cable between two hosts |
| Analysis location | Cheat PC, gaming PC, or offline workstation |
| Write capability | Read-only vs read/write TLPs or host APIs |
| Input path | Separate HID actuator, proxied APIs, or none |

Leave unknowns explicit. Map defenses to the **actual boundary**: device DMA remapping ([[iommu]]), driver/interface security, authenticated transport, or server-side information exposure—not a generic “DMA detected” label.

## Common paths

**Hardware bus initiator (external DMA cheat):** FPGA or other PCIe endpoint in the gaming PC issues Memory Read/Write TLPs as a bus master. Host tools ([[pcileech]], LeechCore, MemProcFS) run on the cheat PC and consume the device transport only. No attacker process need execute on the gaming OS. (source: wiki/sources/skills/dma-attack.md)

**Host-mediated capture:** WinPmem, `/dev/mem`, kernel drivers, or hypervisor interfaces read physical memory through OS/firmware contracts. IOMMU and PCIe fingerprinting apply differently; the initiator is software on (or under) the target, not an arbitrary PCIe requester.

**Mixed / claimed hybrids:** USB transfer cables, two-computer setups, and commercial “DMA kits” may combine host software with hardware. Verify implementation claims against primary sources with [[research-rigor]]—marketing diagrams do not establish that advertised FPGA or bridge components are present or active.

## Detection and mitigation scope

- **PCIe-layer checks** (config integrity, link behavior, BAR probes) apply when the initiator is a visible endpoint.
- **IOMMU policy** governs device IOVA translation when remapping is active on that path.
- **Hypervisor EPT** records CPU guest-physical access under EPT policy—it is **not** direct evidence of a PCIe DMA request; correlate remapping/fault telemetry separately. (source: wiki/sources/skills/dma-attack.md)
- **Attestation** covers selected boot measurements, not every runtime mapping or absent FPGA.

A clean process module list or absent FPGA is not a clean-host finding by itself; artifact availability depends on observer, platform, and collection scope.

## Related

[[dma]] · [[iommu]] · [[pcileech]] · [[research-rigor]] · [[overviews/dma-attack]]
