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

Windows **kernel proof-of-concept** (starfallreverie/pfnwatch) that detects unauthorized kernel-mode reads of a protected process by scanning page table entries for physical page frames owned by that process. Written in C++ for x64 with Visual Studio; aimed at game security and anti-cheat researchers exploring kernel-level cheat detection that is harder to evade than PFN reference-count or pool-tag monitoring alone. README category: Anti Cheat → Detection:Memory Integrity. (source: wiki/sources/descriptions/starfallreverie__pfnwatch.md)

## Capabilities

Build a **PFN bitmap** from the target process page tables; periodically scan kernel page tables for matching PTEs; report kernel virtual addresses, PTE flags, and resolved target addresses. Targets remote memory access paths that must create a PTE mapping — `MmCopyMemory`, `MmMapIoSpace` / `MmMapIoSpaceEx`, and direct PTE manipulation — while filtering prototype and inactive pages to reduce false positives. (source: wiki/sources/descriptions/starfallreverie__pfnwatch.md)

## Architecture

**Kernel driver** plus **C++ usermode console client** communicate over IOCTLs — instrumentation focuses on the page-table mapping surface rather than a single API hook site. (source: wiki/sources/descriptions/starfallreverie__pfnwatch.md)

## Positioning

Complements offensive `MmCopyMemory` bypass study such as [[mm-copy-memory]] and educational hook telemetry such as [[simple-mmcopymemory-hook]] by watching PTE creation instead of export hooks. Pairs disk-vs-memory kernel integrity checks such as [[detect-ntoskrnl-integrity]] and working-set tamper demos such as [[query-working-set-example]] in the Detection:Memory Integrity lane. Contrasts with [[kernel-pool-scanning]] — PFN/page-table walks catch cross-process physical mappings without relying on pool tags or BigPool tables.

## Links

- Repo: https://github.com/starfallreverie/pfnwatch

## Related

[[mm-copy-memory]] · [[simple-mmcopymemory-hook]] · [[detect-ntoskrnl-integrity]] · [[query-working-set-example]] · [[kernel-pool-scanning]] · [[be-injector]] · [[eac-mapper]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
