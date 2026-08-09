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
  - wiki/sources/descriptions/mattifestation__WDACTools.md
  - wiki/sources/descriptions/gmh5225__ZeroHVCI.md
updated: 2026-08-09
confidence: high
---

# HVCI

Hypervisor-Enforced Code Integrity (Memory Integrity): a **Virtualization-Based Security (VBS)** feature where the Secure Kernel (VTL1) and hypervisor EPT/SLAT enforce that kernel pages are not simultaneously writable and executable without re-validation. VBS splits the machine into VTL0 (normal Windows kernel + user mode) and VTL1 (Secure Kernel + policy enforcement) via the Windows hypervisor; HVCI is the memory-protection bucket within that stack. (source: wiki/sources/skills/windows-kernel.md)

## Enforcement model

- **W→X transition restriction:** enforced code pages are not intended to stay writable from VTL0; executability is granted only after configured code-integrity checks pass.
- **Pipeline:** CI policy defines trust → hypervisor second-stage translation (EPT/SLAT) → strict execution rules on validated kernel pages.
- **Driver requirement:** drivers must be HVCI-compatible (no self-modifying kernel code paths that violate W→X).

## Game-security role

Raises the cost of classic kernel code patches and some [[byovd]] patterns; baseline assumption alongside Secure Boot/TPM in serious AC and [[dma]] threat models. Does not stop pure external DMA by itself—IOMMU/attestation still required. Research framed as HVCI bypass via PFN swapping (call arbitrary kernel functions from user mode) appears in [[bustercall]]. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

Early-boot / native-subsystem research such as [[bootbypass]] targets DSE and Memory Integrity together via boot-manager checks, CI.dll validation, and `SeCiCallbacks` patching (`subsystem:native`). (source: wiki/sources/descriptions/wesmar__BootBypass.md)

Operator tooling such as [[solemn]] automates adding drivers to the HVCI `HvciDisallowedImages` custom blocklist (Windows Security Features / Ring3 research lane). (source: wiki/sources/descriptions/unkvolism__Solemn.md)

LOLdriver / vulnerable-driver inventory checks under HVCI appear in PowerShell research such as [[hvci-loldrivers-check]] (Trail of Bits; cheat / vulnerable-driver lane). (source: wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md) General LOLdriver scan clients such as [[loldrivers-client]] (Go/PowerShell) cover the same inventory lane without an HVCI-specific framing. (source: wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md)

WDAC policy build/deploy tooling such as [[wdactools]] (PowerShell; base/supplemental CI policies, UMCI/WHQL/audit options, CIPolicyParser, CiTool.exe) helps study the user-mode side of the same code-integrity trust pipeline [[hvci]] enforces at the hypervisor. (source: wiki/sources/descriptions/mattifestation__WDACTools.md)

HVCI bypass PoCs such as [[zero-hvci]] (gmh5225; policy edge cases + vulnerable signed-driver primitives → unsigned kernel code under Memory Integrity) sit in the same kernel trust-feature research lane. (source: wiki/sources/descriptions/gmh5225__ZeroHVCI.md)

## Related

[[patchguard]] · [[byovd]] · [[iommu]] · [[bustercall]] · [[bootbypass]] · [[zero-hvci]] · [[solemn]] · [[wdactools]] · [[hvci-loldrivers-check]] · [[loldrivers-client]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]

