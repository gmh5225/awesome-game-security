---
title: star-rail
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__star_rail.md
  - wiki/sources/descriptions/gmh5225__Pom-Pom.md
updated: 2026-08-11
confidence: medium
---

# star-rail

C/C++ research repo for **Honkai: Star Rail** centered on **DirectX** and **hooking**. Listed under cheat / game:honkai star rail; aimed at game-security researchers and reverse engineers studying offensive in-process techniques against HoYoverse client-side protection. (source: wiki/sources/descriptions/gmh5225__star_rail.md)

Sits in the same HoYoverse title lane as Genshin Impact reversing samples such as [[genshinjumpfixer2]] and `mhyprot2` bypass research ([[mhynot2]]), but as a gmh5225 DirectX hook scaffold for Star Rail rather than CFG decode or kernel-driver circumvention tooling. Unity/hooking cheat scaffolds such as [[starrail-s-gc]], hooking/overlay samples such as [[pom-pom]], and out-of-process daily automation via screen recognition ([[starrailcopilot]]) cover adjacent offensive lanes for the same title. Tencent ACE reverse-engineering for the Star Rail PC client is documented in [[starrail-ace-b]] (kernel driver, integrity checks, detection/bypass surfaces).

## Links

- Repo: https://github.com/gmh5225/star_rail

## Related

[[starrail-s-gc]] · [[pom-pom]] · [[starrailcopilot]] · [[starrail-ace-b]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[present-hook]] · [[genshinjumpfixer2]] · [[mhynot2]]
