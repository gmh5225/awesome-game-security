---
title: hygieia
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Deputation__hygieia.md
updated: 2026-08-26
confidence: medium
---

# hygieia

Windows **kernel driver** for investigating **traces left by vulnerable drivers**. Implemented in **C/C++** with **WDK-style** driver tooling, it **scans paging structures** to locate known **driver artifacts** and supports **1 GB, 2 MB, and 4 KB** page mappings. Aimed at **low-level memory forensics** for **anti-cheat** and **kernel security research** focused on detecting or understanding **prior unsigned driver activity**. (source: wiki/sources/descriptions/Deputation__hygieia.md)

Complements object-enumeration scanners such as [[memscanner]] and load-artifact cleanup research such as [[clear-driver-traces]] by focusing on **page-table / paging-structure** residue rather than pool tags or PiDDBCache entries alone. Pairs with [[kernel-pool-scanning]] and [[byovd]] threat-modeling when correlating BYOVD mapper footprints with post-load forensic sweeps.

## Links

- Repo: https://github.com/Deputation/hygieia

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[memscanner]] · [[clear-driver-traces]] · [[kernel-pool-scanning]] · [[byovd]] · [[instrumentation-callbacks]]
