---
title: HVCI
kind: concept
topics: [windows-kernel, anti-cheat, dma-attack]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/zer0condition__BusterCall.md
updated: 2026-07-17
confidence: high
---

# HVCI

Hypervisor-Enforced Code Integrity (Memory Integrity): VBS feature where the Secure Kernel (VTL1) and hypervisor EPT/SLAT enforce that kernel pages are not simultaneously writable and executable without re-validation. (source: wiki/sources/skills/windows-kernel.md)

## Game-security role

Raises the cost of classic kernel code patches and some [[byovd]] patterns; baseline assumption alongside Secure Boot/TPM in serious AC and [[dma]] threat models. Does not stop pure external DMA by itself—IOMMU/attestation still required. Research framed as HVCI bypass via PFN swapping (call arbitrary kernel functions from user mode) appears in [[bustercall]]. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

## Related

[[patchguard]] · [[byovd]] · [[iommu]] · [[bustercall]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
