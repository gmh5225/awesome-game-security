---
title: nv-v2 (ekknod)
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ekknod__nv_v2.md
updated: 2026-08-15
confidence: medium
---

# nv-v2 (ekknod)

**nv_v2** is a **sound ESP** research project for CS:GO — offensive tooling that derives positional awareness from game **audio** rather than screen-space overlays or conventional entity-list visuals. It is written in **C** and **C/C++**, centers on **hooking**, and targets game-security researchers and reverse engineers studying cheat / game:csgo techniques. (source: wiki/sources/descriptions/ekknod__nv_v2.md)

Sound ESP sits beside visual ESP samples: it avoids [[world-to-screen]] draw paths but still depends on hooked game audio or engine state to infer enemy locations.

## Links

- Repo: https://github.com/ekknod/nv_v2

## Related

[[csgo-external-esp]] · [[solace-csgo]] · [[present-hook]] · [[vm]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
