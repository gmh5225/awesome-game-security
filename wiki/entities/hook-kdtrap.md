---
title: Hook KdTrap
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Hook-KdTrap.md
updated: 2026-08-12
confidence: medium
---

# Hook KdTrap

Kernel-mode hook for **KdTrap**, the Windows global exception handler invoked first on any exception. Patches **`HalpStallCounter`** and related variables to hijack control flow, installing a custom exception handler that safely intercepts **null pointer dereferences** and **reserved CR3 bit faults**. Useful for studying low-level first-chance kernel exception dispatch, HAL-global variable abuse, and CR3-related fault handling beside PTE/page-table hook research. (source: wiki/sources/descriptions/gmh5225__Hook-KdTrap.md)

## Links

- Repo: https://github.com/gmh5225/Hook-KdTrap

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[windows-kernel-pagehook]] · [[pteditor]] · [[eac-cr3-bypass]] · [[query-shadow-stack]]
