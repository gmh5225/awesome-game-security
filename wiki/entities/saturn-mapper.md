---
title: saturn-mapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/paysonism__saturn-mapper.md
updated: 2026-07-26
confidence: medium
---

# saturn-mapper

Windows kernel **manual mapper** (“Saturn”) that loads unsigned drivers into kernel memory by mapping PE sections, resolving imports, and applying relocations. C++ / WDK with prebuilt driver binaries and signature-scanning helpers; README tags the classic Intel vulnerable driver `iqvw64e.sys` (BYOVD / kdmapper-style lane). Useful for studying unsigned kernel load paths without the normal signed-driver install path. (source: wiki/sources/descriptions/paysonism__saturn-mapper.md)

Companion research lane to mapper catalogs such as [[known-driver-mappers]], kdmapper ports such as [[kdmapper-rs]], trusted-process hosts such as [[lsass-extend-mapper]], and post-map cleanup such as [[revert-mapper]].

## Links

- Repo: https://github.com/paysonism/saturn-mapper

## Related

[[known-driver-mappers]] · [[kdmapper-rs]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
