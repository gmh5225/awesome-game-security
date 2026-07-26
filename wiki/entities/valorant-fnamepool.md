---
title: VALORANT-FNamePool
kind: entity
topics: [game-engine, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/percpopper__VALORANT-FNamePool.md
updated: 2026-07-26
confidence: medium
---

# VALORANT-FNamePool

C/C++ sample that iterates and decrypts Valorant’s Unreal `FNamePool->Entries` (cheat / game:valorant). Useful for researchers studying how encrypted FName/GNames-style pools are walked under a [[vanguard]]-protected UE title, rather than as a full SDK dumper. (source: wiki/sources/descriptions/percpopper__VALORANT-FNamePool.md)

Sits beside [[valorant-dumper]] in the per-title Valorant Unreal name/object lane; narrower focus on FNamePool entry iteration/decrypt vs broader GObjects/GNames layout dumps.

## Links

- Repo: https://github.com/percpopper/VALORANT-FNamePool

## Related

[[vanguard]] · [[valorant-dumper]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[ts-ue4dumper]] · [[vx-it]]
