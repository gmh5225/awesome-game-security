---
title: lazy_importer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/JustasMasiulis__lazy_importer.md
updated: 2026-08-24
confidence: medium
---

# lazy_importer

Header-only C++ **lazy importer** for resolving Windows modules and API exports at runtime. Designed to avoid static import table entries, avoid plaintext export/module strings, and keep generated code very small. Supports **safe**, **cached**, and **forwarded** resolution modes, and **randomizes hashes per build**. Commonly used in reverse-engineering-resistant tooling and game security research (Anti Cheat → Lazy Importer). (source: wiki/sources/descriptions/JustasMasiulis__lazy_importer.md)

Canonical user-mode lazy-import reference in the README Lazy Importer lane. Complements kernel-mode [[kli]] / [[kli-ex]] and runtime zero-IAT resolver [[noimportz]] (LSTAR→ntoskrnl + `PsLoadedModuleList` export walk for WDK drivers), sibling [[blitz]] (direct-call syntax), compile-time string hiding via [[xorstr]], and direct-syscall stub libraries such as [[inline-syscall]]. Defensive analysts should treat PEB/Ldr hash-walk resolution in `.text` with sparse IAT as potential lazy-import usage.

## Links

- Repo: https://github.com/JustasMasiulis/lazy_importer

## Related

[[blitz]] · [[kli]] · [[kli-ex]] · [[noimportz]] · [[xorstr]] · [[inline-syscall]] · [[ue4-base]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
