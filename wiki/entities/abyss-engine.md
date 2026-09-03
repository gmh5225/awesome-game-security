---
title: AbyssEngine
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/AbyssEngine__AbyssEngine.md
updated: 2026-09-03
confidence: medium
---

# AbyssEngine

**AbyssEngine** (AbyssEngine/AbyssEngine) is a clean-room **C** reimplementation of a classic action RPG engine. Cross-platform components cover rendering, audio, scene management, **MPQ asset handling**, and media decoding via SDL2, FFmpeg, zlib, and libarchive. The project prioritizes portability and extensibility over reusing original proprietary game code — a transparent foundation for engine developers and modding-oriented researchers studying and extending legacy game behavior. (source: wiki/sources/descriptions/AbyssEngine__AbyssEngine.md)

Sits in the Game Engine / source lane beside reverse-engineered classic RPG codebases such as [[devilution]] (Diablo 1 retail binary reconstruction) and other ARPG engine sources such as [[spark-engine]], but as an independent clean-room stack rather than a decompilation artifact.

## Links

- Repo: https://github.com/AbyssEngine/AbyssEngine (README: `[ARPG]`)

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[devilution]] · [[spark-engine]] · [[research-rigor]]
