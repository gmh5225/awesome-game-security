---
title: pfnwatch
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/starfallreverie__pfnwatch.md
  - wiki/sources/README-categories.md
updated: 2026-10-08
confidence: medium
---

# pfnwatch

Windows **kernel proof-of-concept** (starfallreverie/pfnwatch) that detects unauthorized kernel-mode reads of a protected process by scanning page table entries for physical page frames owned by that process. A kernel driver and C++ usermode console client communicate over IOCTLs to build a PFN bitmap from the target's page tables, periodically scan kernel page tables for matching PTEs, and report kernel virtual addresses, PTE flags, and resolved target addresses. The technique targets remote memory access paths that must create a PTE mapping — including `MmCopyMemory`, `MmMapIoSpace` / `MmMapIoSpaceEx`, and direct PTE manipulation — while filtering prototype and inactive pages to reduce false positives. Aimed at game security and anti-cheat researchers exploring kernel-level cheat detection that is harder to evade than PFN reference-count or pool-tag monitoring alone. README category: Anti Cheat → Detection:Memory Integrity. (source: wiki/sources/descriptions/starfallreverie__pfnwatch.md)

Complements offensive `MmCopyMemory` bypass study such as [[mm-copy-memory]] and educational hook telemetry such as [[simple-mmcopymemory-hook]] by instrumenting the **page-table mapping surface** rather than a single API hook site. Pairs disk-vs-memory kernel integrity checks such as [[detect-ntoskrnl-integrity]] and working-set tamper demos such as [[query-working-set-example]] in the Detection:Memory Integrity lane.

## Links

- Repo: https://github.com/starfallreverie/pfnwatch

## Related

[[mm-copy-memory]] · [[simple-mmcopymemory-hook]] · [[detect-ntoskrnl-integrity]] · [[query-working-set-example]] · [[be-injector]] · [[eac-mapper]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
