---
title: cos-mapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/armvirus__CosMapper.md
updated: 2026-08-18
confidence: medium
---

# cos-mapper

Windows **kernel driver mapper** that loads an unsigned payload driver through a **signed helper driver**. The project combines user-mode and kernel-mode components, transfers mapped images through **kernel hooks**, and attempts to clean common forensic traces such as **unloaded-driver** and **cache** artifacts. Includes an example driver entry contract and buildable Visual Studio projects for the full mapping flow. Aimed at low-level game security and kernel research where driver loading behavior and stealth tradeoffs are being studied. (source: wiki/sources/descriptions/armvirus__CosMapper.md)

README tags the project under **Signed Driver Map** (armvirus). Complements section-overlay mappers such as [[sinmapper]], pool-alloc BYOVD mappers such as [[kdmapper]], and post-map cleanup tools such as [[nullmap]] and [[revert-mapper]].

## Links

- Repo: https://github.com/armvirus/CosMapper

## Related

[[sinmapper]] · [[driver-dll-finder]] · [[kdmapper]] · [[nullmap]] · [[revert-mapper]] · [[known-driver-mappers]] · [[byovd]] · [[kernel-pool-scanning]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
