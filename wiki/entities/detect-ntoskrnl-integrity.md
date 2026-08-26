---
title: DetectNtoskrnlIntegrity
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/DejavuSecure__DetectNtoskrnlIntegrity.md
updated: 2026-08-26
confidence: medium
---

# DetectNtoskrnlIntegrity

Windows **kernel integrity research project** (DejavuSecure) focused on validating **in-memory `ntoskrnl.exe` against its on-disk image**. Presents C++ code and methodology for detecting kernel tampering while accounting for practical complications such as **SSDT-related transformations**, **page-table randomization**, and **retpoline-era behavior changes** on modern Windows builds. Primarily useful for **anti-rootkit**, **anti-cheat**, and **defensive kernel security** research workflows. (source: wiki/sources/descriptions/DejavuSecure__DetectNtoskrnlIntegrity.md)

Complements export-trampoline scanners such as [[driver-detect-nullshit]] and `IRP_MJ_DEVICE_CONTROL` dispatch auditors such as [[device-control-hooks-scanner]] by targeting **whole-kernel image consistency** rather than isolated hook sites. Offline symbol/offset tooling such as [[ntoskrnlwalker]], live inspection via [[ntoskrnl-viewer]], and pre-collected build corpora such as [[ntoskrnl-file-collection]] support the same ntoskrnl analysis lane from adjacent angles.

## Links

- Repo: https://github.com/DejavuSecure/DetectNtoskrnlIntegrity [Memory Integrity Verification with Disk Verification of ntoskrnl.exe]

## Related

[[driver-detect-nullshit]] · [[device-control-hooks-scanner]] · [[ntoskrnl-viewer]] · [[ntoskrnlwalker]] · [[ntoskrnl-file-collection]] · [[hygieia]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
