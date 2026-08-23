---
title: MapleStoryUnity
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MapleStoryUnity__MapleStoryUnity.md
updated: 2026-08-23
confidence: medium
---

# MapleStoryUnity

**MapleStoryUnity** is a **Unity-based reimplementation of the MapleStory game client** that loads official **WZ asset archives** and connects to MapleStory-compatible servers. Written primarily in C#, it integrates **WzLib** (via UnityWzLib) for parsing encrypted WZ files, **MapleCryptoLib** for AES and custom MapleStory packet encryption, and the **JCSUnity** framework for 2D character control, UI, and client-side networking with packet encoders, decoders, and login handlers. The project includes map and sound loading, character stat management, and core gameplay systems to reproduce MapleStory client behavior inside Unity. (source: wiki/sources/descriptions/MapleStoryUnity__MapleStoryUnity.md)

Aimed at reverse engineers, private server developers, and game-security researchers studying MapleStory client architecture, network protocols, and asset formats—not live official-client anti-cheat bypass.

Complements NX-format v83 reimplementations such as [[maple-unity]], WZ-first Unity clients such as [[unistory]], WZ tooling such as [[wzcomparerr2]], and client-internals write-ups such as [[maple-research]].

## Links

- Repo: https://github.com/MapleStoryUnity/MapleStoryUnity (README tag: Unity framework for MapleStory-style MMORPGs; C#; WZ via UnityWzLib; GPL-3.0)

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[maple-unity]] · [[unistory]] · [[wzcomparerr2]] · [[maplenecrocer]] · [[maple-research]]
