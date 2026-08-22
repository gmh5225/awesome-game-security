---
title: Source2Gen
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/praydog__Source2Gen.md
  - wiki/sources/descriptions/neverlosecc__source2gen.md
  - wiki/sources/descriptions/gmh5225__CS2-SDK-Source2Gen.md
  - wiki/sources/descriptions/NotOfficer__cs2-sdk.md
updated: 2026-08-22
confidence: medium
---

# Source2Gen

Source 2 SDK generators (C/C++) that emit class/enum headers for exposed Source 2 layouts—cheat / game engine explorer:source tooling for SDK generation and memory analysis. (source: wiki/sources/descriptions/neverlosecc__source2gen.md)

- **neverlosecc/source2gen** — maintained SDK Generator; pairs with generated multi-game dumps in [[source2sdk]]. (source: wiki/sources/descriptions/neverlosecc__source2gen.md)
- **praydog/Source2Gen** — earlier SDK generator that emits C++ headers for many exposed Source 2 classes and enumerators. (source: wiki/sources/descriptions/praydog__Source2Gen.md)

CS2-specific generated output such as [[cs2-sdk-source2gen]] (gmh5225; auto-generated C++ headers for animation, client, engine2, network, scene, schema, and other Source 2 modules; cheat / game:cs2 [SDK]) and [[cs2-sdk]] (NotOfficer; source2gen-produced class/enum headers for client, server, rendering, networking, and schema systems with version patch metadata; cheat / game:cs2 [SDK]) illustrate title-scoped dumps beside multi-game output in [[source2sdk]]. (source: wiki/sources/descriptions/gmh5225__CS2-SDK-Source2Gen.md) (source: wiki/sources/descriptions/NotOfficer__cs2-sdk.md)

Complements Source 1 header dumps such as [[sdk]] and CS2 offset/netvar feeds such as [[cs2-offsets]] / [[cs2-offsets-ro0ti]] in the Source → Source 2 SDK CodeGen path.

## Links

- Repo (neverlosecc): https://github.com/neverlosecc/source2gen
- Repo (praydog): https://github.com/praydog/Source2Gen

## Related

[[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[source2sdk]] · [[cs2-sdk-source2gen]] · [[cs2-sdk]] · [[sdk]] · [[luagenny]] · [[cs2-offsets]] · [[cs2-offsets-ro0ti]] · [[cs2-internal]] · [[cs2-cheat-cpp]]
