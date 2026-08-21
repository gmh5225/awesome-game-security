---
title: HVCI
kind: concept
topics: [windows-kernel, anti-cheat, dma-attack]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/zer0condition__BusterCall.md
  - wiki/sources/descriptions/zer0condition__GoodmansKernel.md
  - wiki/sources/descriptions/wesmar__BootBypass.md
  - wiki/sources/descriptions/unkvolism__Solemn.md
  - wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md
  - wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md
  - wiki/sources/descriptions/mattifestation__WDACTools.md
  - wiki/sources/descriptions/gmh5225__ZeroHVCI.md
  - wiki/sources/descriptions/gmh5225__FakeEnclave.md
  - wiki/sources/descriptions/SamuelTulach__SecureGame.md
  - wiki/sources/descriptions/gmh5225__Disabling-Hyper-V.md
  - wiki/sources/descriptions/ghostbyt3__BYOVDFinder.md
  - wiki/sources/descriptions/XaFF-XaFF__BugcheckSuppressor.md
updated: 2026-08-21
confidence: high
---

# HVCI

Hypervisor-Enforced Code Integrity (Memory Integrity): a **Virtualization-Based Security (VBS)** feature where the Secure Kernel (VTL1) and hypervisor EPT/SLAT enforce that kernel pages are not simultaneously writable and executable without re-validation. VBS splits the machine into VTL0 (normal Windows kernel + user mode) and VTL1 (Secure Kernel + policy enforcement) via the Windows hypervisor; HVCI is the memory-protection bucket within that stack. (source: wiki/sources/skills/windows-kernel.md)

## Enforcement model

- **W→X transition restriction:** enforced code pages are not intended to stay writable from VTL0; executability is granted only after configured code-integrity checks pass.
- **Pipeline:** CI policy defines trust → hypervisor second-stage translation (EPT/SLAT) → strict execution rules on validated kernel pages.
- **Driver requirement:** drivers must be HVCI-compatible (no self-modifying kernel code paths that violate W→X). HVCI-oriented research platforms such as [[goodmans-kernel]] (signed WDM driver embedding wasm3 to hot-load unsigned wasm32 modules without per-iteration driver rebuild; SEH-guarded kernel memory access; zer0condition) illustrate updatable kernel logic under Memory Integrity constraints. (source: wiki/sources/descriptions/zer0condition__GoodmansKernel.md)

## Game-security role

Raises the cost of classic kernel code patches and some [[byovd]] patterns; baseline assumption alongside Secure Boot/TPM in serious AC and [[dma]] threat models. Does not stop pure external DMA by itself—IOMMU/attestation still required. Research framed as HVCI bypass via PFN swapping (call arbitrary kernel functions from user mode) appears in [[bustercall]]. (source: wiki/sources/descriptions/zer0condition__BusterCall.md)

Early-boot / native-subsystem research such as [[bootbypass]] targets DSE and Memory Integrity together via boot-manager checks, CI.dll validation, and `SeCiCallbacks` patching (`subsystem:native`). (source: wiki/sources/descriptions/wesmar__BootBypass.md)

Operator tooling such as [[solemn]] automates adding drivers to the HVCI `HvciDisallowedImages` custom blocklist (Windows Security Features / Ring3 research lane). (source: wiki/sources/descriptions/unkvolism__Solemn.md)

LOLdriver / vulnerable-driver inventory checks under HVCI appear in PowerShell research such as [[hvci-loldrivers-check]] (Trail of Bits; cheat / vulnerable-driver lane). (source: wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md) [[byovdfinder]] (ghostbyt3; identifies LOLdrivers not blocked by the active HVCI policy—BYOVD attack-path research under Memory Integrity) targets the same policy-gap inventory lane. (source: wiki/sources/descriptions/ghostbyt3__BYOVDFinder.md) General LOLdriver scan clients such as [[loldrivers-client]] (Go/PowerShell) cover the same inventory lane without an HVCI-specific framing. (source: wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md)

WDAC policy build/deploy tooling such as [[wdactools]] (PowerShell; base/supplemental CI policies, UMCI/WHQL/audit options, CIPolicyParser, CiTool.exe) helps study the user-mode side of the same code-integrity trust pipeline [[hvci]] enforces at the hypervisor. (source: wiki/sources/descriptions/mattifestation__WDACTools.md)

HVCI bypass PoCs such as [[zero-hvci]] (gmh5225; policy edge cases + vulnerable signed-driver primitives → unsigned kernel code under Memory Integrity) sit in the same kernel trust-feature research lane. (source: wiki/sources/descriptions/gmh5225__ZeroHVCI.md)

VBS enclave abuse PoCs such as [[fake-enclave]] (gmh5225; proof-of-concept misusing Enclave isolation within the VBS stack) complement HVCI bypass work when studying virtualization-based security limitations. (source: wiki/sources/descriptions/gmh5225__FakeEnclave.md) Defensive enclave game-logic isolation PoCs such as [[secure-game]] (SamuelTulach; Pong-like sample; host app for render/input + enclave DLL for state/rules; SDL2; trusted execution / anti-cheat research) illustrate isolating sensitive gameplay from usermode tampering within the same VBS stack. (source: wiki/sources/descriptions/SamuelTulach__SecureGame.md)

Lab teardown guides such as [[disabling-hyper-v]] (gmh5225; Win10; Microsoft's Device Guard and Credential Guard hardware readiness tool → disable HVCI, Device Guard, Credential Guard, and related VBS so Hyper-V can be fully removed—not an in-place bypass) document the configuration side of turning Memory Integrity off for research hosts. (source: wiki/sources/descriptions/gmh5225__Disabling-Hyper-V.md)

HVCI/kCET-aware kernel exception research such as [[bugcheck-suppressor]] (XaFF-XaFF; data-only HAL dispatch hook + bugcheck-callback interception + SEH `RtlUnwindEx` recovery; CET-compatible assembly stubs; BSOD suppression PoC) probes how Memory Integrity and shadow-stack enforcement interact with bugcheck handling—not a bypass of W→X policy itself. (source: wiki/sources/descriptions/XaFF-XaFF__BugcheckSuppressor.md)

## Related

[[patchguard]] · [[byovd]] · [[iommu]] · [[bustercall]] · [[bootbypass]] · [[zero-hvci]] · [[fake-enclave]] · [[secure-game]] · [[disabling-hyper-v]] · [[solemn]] · [[wdactools]] · [[hvci-loldrivers-check]] · [[byovdfinder]] · [[loldrivers-client]] · [[goodmans-kernel]] · [[bugcheck-suppressor]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]

