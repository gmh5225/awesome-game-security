---
title: s4mapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__S4Mapper.md
updated: 2026-08-10
confidence: medium
---

# s4mapper

Windows kernel **driver manual mapper** that abuses Samsung's S4 vulnerable signed driver **`SignalRgbDriver.sys`**. Memory-access IOCTLs to the loaded driver supply kernel R/W primitives for a full PE manual-map pipeline: pool allocation, section copy, relocation fixups, import resolution, and entry-point invocation—loading unsigned drivers without the normal signed-driver install path. (source: wiki/sources/descriptions/gmh5225__S4Mapper.md)

Complements Samsung S4 access-primitive research such as [[s4killer]] (`probmon.sys`; phys/virt kernel R/W via crafted IOCTLs) in the same OEM signed-driver backend lane. Sits in the broader driver-mapper research lane as [[lenovo-mapper]], [[imxyvimapper]], [[ucmapper]], [[saturn-mapper]], [[kdu]], and [[nullmap]].

## Links

- Repo: https://github.com/gmh5225/S4Mapper

## Related

[[byovd]] · [[s4killer]] · [[lenovo-mapper]] · [[imxyvimapper]] · [[ucmapper]] · [[saturn-mapper]] · [[kdu]] · [[nullmap]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
