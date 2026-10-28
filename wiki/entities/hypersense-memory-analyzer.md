---
title: HyperSense Memory Analyzer
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/hypersenseindia__hypersense-memory-analyzer.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# HyperSense Memory Analyzer

Windows x64 **live usermode memory analysis** GUI (hypersenseindia/hypersense-memory-analyzer) wrapping the open-source **Moneta** engine. C++17 Win32 front-end plus optional classic Moneta-style CLI layout scans a selected process for injection-like regions, suspicious mappings, unsigned modules, metadata anomalies, and CLR-related heaps across IOC, ALL, REGION, and REFERENCED modes. Emits TXT/HTML reports and optional VirusTotal lookups on file paths. README category: Anti Cheat → Detection:Memory Integrity. (source: wiki/sources/descriptions/hypersenseindia__hypersense-memory-analyzer.md)

## Positioning

Complements kernel PTE walk PoCs such as [[pfnwatch]] and disk-vs-memory kernel checks such as [[detect-ntoskrnl-integrity]] by giving analysts a **usermode live-process** Moneta workflow without driver install. Pairs cheat-side injection labs such as [[process-injection-detection-lab]] for contrasting offensive telemetry with defensive memory-region triage on authorized hosts.

## Links

- Repo: https://github.com/hypersenseindia/hypersense-memory-analyzer

## Related

[[pfnwatch]] · [[detect-ntoskrnl-integrity]] · [[query-working-set-example]] · [[process-injection-detection-lab]] · [[kernel-pool-scanning]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
