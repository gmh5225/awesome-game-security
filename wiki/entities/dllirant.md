---
title: DLLirant
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/redteamsocietegenerale__DLLirant.md
  - wiki/sources/descriptions/Sh0ckFR__DLLirant.md
updated: 2026-08-21
confidence: medium
---

# DLLirant

Automated Windows DLL hijacking discovery tool: generates proxy DLLs, places them in candidate directories, and monitors whether a target executable loads them — surfacing missing dependencies and unsafe search-order paths for pen-test / audit privilege-escalation and persistence research. (source: wiki/sources/descriptions/redteamsocietegenerale__DLLirant.md)

The curated list also tracks **Sh0ckFR/DLLirant** under Hijacking researches — a lightweight historical placeholder with no implementation in the snapshot; it redirects readers to the maintained project rather than hosting active source. (source: wiki/sources/descriptions/Sh0ckFR__DLLirant.md)

Companion discovery tooling beside catalog DBs [[windows-dll-hijacking]] and [[hijacklibs]] in the Cheat → DLL Hijack lane (not a game-specific cheat); useful for AC/EDR researchers mapping image-load / search-order abuse. Export stub generation: [[dll-hijack-export-dumper]].

## Links

- Repo (maintained): https://github.com/redteamsocietegenerale/DLLirant
- Historical mirror: https://github.com/Sh0ckFR/DLLirant

## Related

[[windows-dll-hijacking]] · [[hijacklibs]] · [[dll-hijack-export-dumper]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injectors]]
