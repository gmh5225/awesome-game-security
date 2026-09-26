---
name: dma-attack-techniques
description: Analyze PCIe DMA threats, host-mediated memory acquisition, FPGA behavior, and IOMMU defenses. Use when the memory initiator or device boundary matters; use kernel security for host-only mechanisms.
---

# DMA attack techniques

Identify the memory initiator, transport, required privilege, isolation boundary, and observable artifacts before classifying a technique as DMA.

## Topic routing

- [Classification and threat model](references/classification-and-threat-model.md) for acquisition-path distinctions and attacker prerequisites.
- [PCIe devices](references/pcie-devices.md) for TLPs, configuration space, programmable endpoints, and emulation limits.
- [IOMMU and defense](references/iommu-and-defense.md) for VT-d/AMD-Vi, ACS, ATS/PASID, domain assignment, hypervisors, and trust anchors.
- [IOMMU state verification](references/iommu-state-verification.md) for separating ACPI advertisement, Windows policy, live unit state, and per-requester coverage.
- [Detection and forensics](references/detection-and-forensics.md) for defensive PCIe inventory, signal correlation, evidence capture, Thunderbolt/USB4, and memory access.
- [Acquisition and transport](references/acquisition-and-transport.md), [assurance boundaries](references/assurance-boundaries.md), and [repository resources](references/repository-resources.md) for focused evidence and source selection.
- [Repository map](references/repository-map.md) when maintaining the collection.

Use `windows-kernel-security` for host driver and kernel internals. Apply `game-security-research-rigor` before turning architecture claims into findings.
