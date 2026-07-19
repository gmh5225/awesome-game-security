---
title: Certael
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/violetweather__Certael.md
updated: 2026-07-19
confidence: medium
---

# Certael

Open-source, cross-engine anti-cheat foundation for authoritative online games. Provides a secure action protocol, a memory-safe Rust native client runtime with a versioned C ABI, and adapters for Godot, Unity, and Unreal, plus a .NET server SDK and self-hosted ASP.NET Core control plane. (source: wiki/sources/descriptions/violetweather__Certael.md)

Sessions use short-lived, single-use bootstrap tickets and signed action intents so clients send typed requests while only the trusted game server validates rules and commits state. Portable signed rule packs, explainable evidence, economy and relationship analysis workers, and an optional agent probe support inventories, progression, social systems, and competitive play without genre-specific heuristics. Aimed at studios building self-hosted, server-authoritative multiplayer security rather than proprietary kernel AC products such as [[easy-anti-cheat]] or [[vanguard]].

## Links

- Repo: https://github.com/violetweather/Certael

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[easy-anti-cheat]] · [[vanguard]]
