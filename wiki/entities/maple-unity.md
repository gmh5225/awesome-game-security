---
title: MapleUnity
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ilia810__MapleUnity.md
updated: 2026-08-18
confidence: medium
---

# MapleUnity

**MapleUnity** (ilia810) is a **Unity-based reimplementation of the MapleStory v83 client** that loads official **NX game data** and recreates maps, characters, and gameplay systems in a modern engine. Written primarily in C# with TDD and clean architecture, it parses NX assets through **reNX** and **NXWrapper** bindings, generates playable map scenes with foothold-based collision, and renders layered character sprites using attachment-point math derived from the original C++ client. The modular stack covers physics, inventory, skills, and a network layer with packet serialization and **AES encryption** matching legacy server protocols. Extensive Unity Editor diagnostics support exploring NX node structures, tilesets, equipment layouts, and rendering behavior. (source: wiki/sources/descriptions/ilia810__MapleUnity.md)

Aimed at reverse engineers, private-server developers, and game-security researchers who need a readable, testable reference for MapleStory client mechanics and protocol behavior—not live official-client anti-cheat bypass.

Complements WZ-first Unity reimplementations such as [[unistory]] (TMS v245), C# client emulators such as [[maplenecrocer]], and v83 private-server stacks such as [[maplestory-v83-maplestory-cpp]], [[libremaple-client]], and [[maplestory-heavenclient]].

## Links

- Repo: https://github.com/ilia810/MapleUnity (README tag: Unity reimplementation of MapleStory v83 client; TDD + clean architecture; C#; NX assets)

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[unistory]] · [[maplenecrocer]] · [[maplestory-v83-maplestory-cpp]] · [[libremaple-client]] · [[maplestory-heavenclient]]
