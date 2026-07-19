---
title: HVCI
kind: concept
topics: [windows-kernel, anti-cheat, dma-attack]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/zer0condition__BusterCall.md
  - wiki/sources/descriptions/wesmar__BootBypass.md
  - wiki/sources/descriptions/unkvolism__Solemn.md
updated: 2026-07-19
confidence: high
---

# HVCI

Hypervisor-Enforced Code Integrity (Memory Integrity): VBS feature where the Secure Kernel (VTL1) and hypervisor EPT/SLAT enforce that kernel pages are not simultaneously writable and executable without re-validation. (source: wiki/sources/skills/windows-kernel.md)

## Game-security role

Raises the cost of classic kernel code patches and some [[byovd]] patterns; baseline assumption alongside Secure Boot/TPM in serious AC and [[dma]] threat models. Does not stop pure external DMA by itself—IOMMU/attestation still required. Research framed as HVCI bypass via PFN swapping (call arbitrary kernel functions from user mode) appears in [[bustercall]]. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

Early-boot / native-subsystem research such as [[bootbypass]] targets DSE and Memory Integrity together via boot-manager checks, CI.dll validation, and `SeCiCallbacks` patching (`subsystem:native`). (source: wiki/sources/descriptions/wesmar__BootBypass.md)

Operator tooling such as [[solemn]] automates adding drivers to the HVCI `HvciDisallowedImages` custom blocklist (Windows Security Features / Ring3 research lane). (source: wiki/sources/descriptions/unkvolism__Solemn.md)

## Related

[[patchguard]] · [[byovd]] · [[iommu]] · [[bustercall]] · [[bootbypass]] · [[solemn]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
