---
title: MemScanner
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/FaEryICE__MemScanner.md
updated: 2026-08-25
confidence: medium
---

# MemScanner

Windows **x64 kernel memory layout scanner** that walks kernel memory regions to enumerate **drivers**, **processes**, and **section objects**. Implemented in **C** for **WDK** and **Visual Studio**, it resolves in-memory structures such as **`DRIVER_OBJECT`**, **LDR entries**, and related **file objects** from live kernel layouts. Notes cover behavior differences across **Windows 7 through Windows 10** plus stability fixes. Primary use cases are **kernel forensics** and **anti-cheat-oriented memory structure research** — mapping how kernel objects appear in RAM rather than usermode process scanning. (source: wiki/sources/descriptions/FaEryICE__MemScanner.md)

README lane: **Memory scanner**.

Complements symbol-driven live inspection via [[ntoskrnl-viewer]] and page-table protection scans such as [[rwxscanner]]; pairs with [[kernel-pool-scanning]] / [[pooldump]] when correlating enumerated driver objects with pool or load-artifact forensics.

## Links

- Repo: https://github.com/FaEryICE/MemScanner (README tag: Memory scanner)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[ntoskrnl-viewer]] · [[rwxscanner]] · [[pooldump]] · [[kernel-pool-scanning]] · [[device-control-hooks-scanner]]
