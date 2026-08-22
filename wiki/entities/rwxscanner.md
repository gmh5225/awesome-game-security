---
title: RwxScanner
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Oliver-1-1__RwxScanner.md
updated: 2026-08-22
confidence: medium
---

# RwxScanner

Windows **kernel-mode scanner** that enumerates **process page tables** to find **writable and executable (RWX)** memory regions. The driver walks **PML4, PDPT, PD, and PT** structures using **physical memory reads** and logs suspicious mappings in per-process context. It also reports process metadata such as **image name** and **admin-token state** to support investigation. Intended for low-level **anti-cheat** and **malware detection** research around injected or self-modifying code. (source: wiki/sources/descriptions/Oliver-1-1__RwxScanner.md)

README lane: **RWX Memory scanner**.

Contrasts with usermode offensive RWX discovery such as [[rwxfinder]] (`VirtualQueryEx` staging research) and complements cross-platform defensive scanners such as [[ghost]]. Same page-table inspection lane as [[ptview]] and [[page-table-injector]], oriented toward **suspicious PTE protection** rather than general PTE browsing.

## Links

- Repo: https://github.com/Oliver-1-1/RwxScanner (README tag: RWX Memory scanner)

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[rwxfinder]] · [[ghost]] · [[ptview]] · [[page-table-injector]] · [[windows-process-injection]]
