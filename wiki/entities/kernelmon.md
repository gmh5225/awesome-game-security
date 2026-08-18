---
title: KernelMon
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/alal4465__KernelMon.md
updated: 2026-08-18
confidence: medium
---

# KernelMon

Virtualization-based Windows monitoring framework that traces kernel activity in a ProcMon-like workflow. Hooks selected kernel-mode APIs and forwards logs to a user-mode desktop UI, covering file system, registry, process, and thread operations. Implementation combines a kernel driver with VMX/EPT-style low-level interception and a companion GUI — aimed at kernel security research, behavior analysis, and anti-cheat or malware investigation in controlled VM environments. (source: wiki/sources/descriptions/alal4465__KernelMon.md)

Complements ETW/minifilter Procmon-style monitors such as [[openprocmon]], process explorers such as [[systeminformer]], and kernel event-stream tools such as [[fibratus]] / [[dbgviewex]].

## Links

- Repo: https://github.com/alal4465/KernelMon

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[openprocmon]] · [[systeminformer]] · [[fibratus]] · [[dbgviewex]] · [[hidden-syscall-monitoring]] · [[etw-explorer]]
