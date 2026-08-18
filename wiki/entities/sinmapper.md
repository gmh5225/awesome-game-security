---
title: sinmapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/armvirus__SinMapper.md
updated: 2026-08-18
confidence: medium
---

# sinmapper

User-mode **manual mapper** that places a custom kernel image into a **section of an already signed driver** rather than allocating fresh kernel pool. It uses physical-memory read/write primitives and page-table permission changes to make the target section executable and writable before mapping, then runs trace-cleaning steps such as clearing common kernel bookkeeping artifacts. Includes an example driver entry format. Primary use case is Windows kernel and anti-cheat evasion research focused on **stealthy driver loading** — hiding payload code inside legitimate signed-driver image bounds. (source: wiki/sources/descriptions/armvirus__SinMapper.md)

README tags the project under **Manual Map In Signed Driver** (armvirus). Complements pool-alloc mappers such as [[kdmapper]] and post-map cleanup tools such as [[nullmap]] and [[revert-mapper]]. Recon for oversized host sections via [[driver-dll-finder]].

## Links

- Repo: https://github.com/armvirus/SinMapper

## Related

[[driver-dll-finder]] · [[kdmapper]] · [[nullmap]] · [[revert-mapper]] · [[saturn-mapper]] · [[known-driver-mappers]] · [[kernel-pool-scanning]] · [[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
