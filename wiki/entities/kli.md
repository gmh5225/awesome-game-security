---
title: kli
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/hypervisor__kli.md
updated: 2026-08-05
confidence: medium
---

# kli

Simple header-only C++ library for kernel-mode lazy import resolution — a ring-0 alternative to user-mode [[lazy-importer]]. Resolves imports at runtime without a static IAT, reducing import-table fingerprints that AC and EDR scanners target in KM drivers. Aimed at anti-cheat engineers and defensive security researchers in the Anti Cheat → Lazy Importer lane. (source: wiki/sources/descriptions/hypervisor__kli.md)

Complements user-mode compile-time import hiding and direct-syscall stub libraries such as [[syscalls-cpp]]; defensive analysts should treat unresolved-import / hash-walk patterns in driver `.text` as potential lazy-import usage alongside classic IAT anomalies. Extended fork [[kli-ex]] (gmh5225) adds random seeds, resolve caching, hidden globals, and customizable encryption over the same API.

## Links

- Repo: https://github.com/hypervisor/kli

## Related

[[lazy-importer]] · [[kli-ex]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[syscalls-cpp]] · [[ntsleuth]] · [[skcrypter]]
