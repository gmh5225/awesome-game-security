---
title: Level Hash
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/urcool626__Level-Hash.md
updated: 2026-10-18
confidence: medium
---

# Level Hash

Geode mod for **Geometry Dash** (urcool626/Level-Hash; C++23; Geode SDK; CMake) that SHA-256 fingerprints a level’s serialized string and shows the digest on the level info screen via an in-game button. Targets community integrity checks—hidden **Level Edit** tweaks, undisclosed nerfs, or other tampering versus published levels—without server authority. (source: wiki/sources/descriptions/urcool626__Level-Hash.md)

## Mechanics

Hashes the level serialization payload clients already use for upload/download; depends on companion Geode mods for level data access. Ships as a shared library for Windows, macOS, iOS, and Android Geometry Dash builds.

## Positioning

**Content-integrity fingerprinting** lane (cryptographic digest of user-generated level bytes) beside behavioral AC; complements manual review and reputation systems rather than kernel or network enforcement.

## Links

- Repo: https://github.com/urcool626/Level-Hash
- Overview: [[overviews/anti-cheat]]
