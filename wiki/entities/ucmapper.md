---
title: ucmapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__UCMapper.md
updated: 2026-08-10
confidence: medium
---

# ucmapper

Windows kernel **driver manual mapper** that abuses NVIDIA **`nvaudio.sys`** as the vulnerable signed-driver transport. Includes both a user-mode loader and in-memory PE mapping logic—not a thin wrapper around an existing mapper. (source: wiki/sources/descriptions/gmh5225__UCMapper.md)

The loader enables `SeLoadDriverPrivilege`, installs and starts the vulnerable driver, opens its device, loads **`nvaudio.sys`** into user space to reuse an internal **`EncodePayLoad`** routine, then removes the driver's runtime-list entry so the helper is less visible after use. The mapper implements explicit relocation, import resolution, and image loading adapted to the nvaudio path—useful for studying [[byovd]]-based driver mapping, reuse of vendor helper routines, and post-load cleanup around runtime lists.

Sits in the same driver-mapper research lane as [[imxyvimapper]], [[lenovo-mapper]], [[saturn-mapper]], [[kdu]], and [[nullmap]].

## Links

- Repo: https://github.com/gmh5225/UCMapper

## Related

[[byovd]] · [[imxyvimapper]] · [[lenovo-mapper]] · [[saturn-mapper]] · [[kdu]] · [[nullmap]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
