---
title: kli-ex
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__kli-ex.md
updated: 2026-08-08
confidence: medium
---

# kli-ex

Extended fork of [[kli]] — a header-only C++ kernel-mode lazy import resolver for WDK drivers. Adds random seeds, resolve caching, hidden global variables, and pluggable hash/encryption over the same `KLI_CALL` macro API; intended as a modification template for the Anti Cheat → Lazy Importer lane. (source: wiki/sources/descriptions/gmh5225__kli-ex.md)

Complements upstream [[kli]] and user-mode **lazy_importer**; defensive analysts should treat per-build seed/caching variants as harder static fingerprints than baseline lazy-import patterns.

## Links

- Repo: https://github.com/gmh5225/kli-ex

## Related

[[kli]] · [[syscalls-cpp]] · [[skcrypter]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
