---
title: PatchGuardEncryptorDriver
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/AmitMoshel1__PatchGuardEncryptorDriver.md
updated: 2026-09-02
confidence: medium
---

# PatchGuardEncryptorDriver

Windows kernel research driver (C++) that implements a custom [[patchguard]]-like integrity monitor rather than bypassing KPP. Periodic **KTIMER** and **KDPC** routines track **SSDT**, **IDT**, and selected **MSR** state; secondary checks verify timer and DPC structures to detect tampering with the monitor itself. Targets low-level security researchers studying kernel integrity defense and anti-tamper techniques. (source: wiki/sources/descriptions/AmitMoshel1__PatchGuardEncryptorDriver.md)

Complements educational PG walkthroughs such as [[demystifying-patchguard]], monitoring tooling such as [[sushi]], and offensive bypass PoCs such as [[patchguard-2023]] — this repo models the **defensive** side of periodic kernel-structure verification.

## Links

- Repo: https://github.com/AmitMoshel1/PatchGuardEncryptorDriver (README tag: Self-implemented PatchGuard)

## Related

[[patchguard]] · [[demystifying-patchguard]] · [[sushi]] · [[patchguard-2023]] · [[gdrv-sys-exploit]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
