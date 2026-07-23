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
  - wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md
  - wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md
updated: 2026-07-23
confidence: high
---

# HVCI

Hypervisor-Enforced Code Integrity (Memory Integrity): VBS feature where the Secure Kernel (VTL1) and hypervisor EPT/SLAT enforce that kernel pages are not simultaneously writable and executable without re-validation. (source: wiki/sources/skills/windows-kernel.md)

## Game-security role

Raises the cost of classic kernel code patches and some [[byovd]] patterns; baseline assumption alongside Secure Boot/TPM in serious AC and [[dma]] threat models. Does not stop pure external DMA by itself—IOMMU/attestation still required. Research framed as HVCI bypass via PFN swapping (call arbitrary kernel functions from user mode) appears in [[bustercall]]. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

Early-boot / native-subsystem research such as [[bootbypass]] targets DSE and Memory Integrity together via boot-manager checks, CI.dll validation, and `SeCiCallbacks` patching (`subsystem:native`). (source: wiki/sources/descriptions/wesmar__BootBypass.md)

Operator tooling such as [[solemn]] automates adding drivers to the HVCI `HvciDisallowedImages` custom blocklist (Windows Security Features / Ring3 research lane). (source: wiki/sources/descriptions/unkvolism__Solemn.md)

LOLdriver / vulnerable-driver inventory checks under HVCI appear in PowerShell research such as [[hvci-loldrivers-check]] (Trail of Bits; cheat / vulnerable-driver lane). (source: wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md) General LOLdriver scan clients such as [[loldrivers-client]] (Go/PowerShell) cover the same inventory lane without an HVCI-specific framing. (source: wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md)

## Related

[[patchguard]] · [[byovd]] · [[iommu]] · [[bustercall]] · [[bootbypass]] · [[solemn]] · [[hvci-loldrivers-check]] · [[loldrivers-client]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]

