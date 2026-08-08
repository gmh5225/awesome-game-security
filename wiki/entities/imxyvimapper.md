---
title: imxyvimapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__imxyviMapper.md
updated: 2026-08-08
confidence: medium
---

# imxyvimapper

Windows kernel **driver mapper** that loads unsigned drivers by abusing a specific vulnerable signed driver — README tags **`AsUpIO.sys`**. The manual-mapping pipeline uses the signed driver's kernel access primitive to copy PE sections, resolve imports, apply relocations, and invoke the mapped driver's entry point without the normal signed-driver install path. Aimed at kernel researchers studying [[byovd]]-based driver mapping implementations. (source: wiki/sources/descriptions/gmh5225__imxyviMapper.md)

Sits in the same driver-mapper research lane as [[saturn-mapper]], [[lenovo-mapper]], [[kdu]], and [[nullmap]].

## Links

- Repo: https://github.com/gmh5225/imxyviMapper

## Related

[[byovd]] · [[saturn-mapper]] · [[lenovo-mapper]] · [[kdu]] · [[nullmap]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
