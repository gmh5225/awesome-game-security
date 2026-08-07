---
title: VDK
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__vdk.md
updated: 2026-08-07
confidence: medium
---

# VDK

**Vulnerable Driver Kit** — tools and libraries for exploiting signed but vulnerable Windows kernel drivers via [[byovd]]. A unified interface abstracts multiple vulnerable-driver backends (README lists **Speedfan.sys**) so researchers can obtain arbitrary kernel read/write, manipulate processes, and load drivers without reimplementing each IOCTL chain. Aimed at kernel security researchers and red-team operators studying vulnerable-driver exploitation. (source: wiki/sources/descriptions/gmh5225__vdk.md)

Same multi-provider mapper lane as [[kdu]], [[saturn-mapper]], and [[known-driver-mappers]].

## Links

- Repo: https://github.com/gmh5225/vdk

## Related

[[byovd]] · [[kdu]] · [[gdrv-loader-v2]] · [[saturn-mapper]] · [[known-driver-mappers]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
