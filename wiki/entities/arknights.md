---
title: Arknights
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Saukiya__Arknights.md
updated: 2026-08-21
confidence: medium
---

# Arknights

**Arknights** (Saukiya) is a **Unity-style reimplementation of Arknights gameplay code** without bundled original game assets. Written primarily in C#, it organizes systems for characters, monsters, dungeons, UI flows, events, and core game-state management, with manager layers for resources, audio, shop logic, and Lua script integration points. (source: wiki/sources/descriptions/Saukiya__Arknights.md)

Aimed at developers and researchers studying Unity project architecture and prototyping tower-defense RPG mechanics—not a live-client cheat or anti-cheat artifact.

Distinct from IL2CPP/Mono dump-and-hook workflows such as [[il2cpp]] + [[dnspy-unity-mono]] and from asset-first Unity reimplementations such as [[maple-unity]] and [[unistory]] that load official game data; this is a **gameplay-systems reference** lane for tower-defense RPG state machines, UI flows, and Lua scripting boundaries.

## Links

- Repo: https://github.com/Saukiya/Arknights (README tag: [Unity Arknights])

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[maple-unity]] · [[unistory]] · [[unity-cs-reference]] · [[xlua]]
