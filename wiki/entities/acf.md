---
title: ACF (Anti-cheat)
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/Dalbonden__Anti-cheat.md
updated: 2026-11-20
confidence: medium
---

# ACF (Anti-cheat)

**ACF** is a modular, **server-authoritative anti-cheat framework** for **Roblox** games, written in **Luau**. The core centralizes detection lifecycle, configuration, player sessions, scheduling, and bounded evidence storage so individual detectors only implement their own logic. (source: wiki/sources/descriptions/Dalbonden__Anti-cheat.md)

## Detection surface

Built-in modules cover movement and physics checks, combat validation, behavioral statistics, and **RemoteEvent** protection via schema validators and rate limits. A risk engine aggregates signals before enforcement.

## Enforcement

Tiered enforcement runs from **shadow mode** through kicks and **staff-approved bans**, supporting evidence-driven rollout without trusting client-side code.

## Toolchain

Targets Roblox Studio and live servers; integrates with **Rojo** for placement under `ServerScriptService`. **Lune** scripts provide offline testing and evaluation.

## Audience

Roblox developers and game security engineers who need configurable, evidence-driven cheat detection on a server-authoritative Luau stack—alongside frameworks such as [[encryptic-roblox-anti-cheat]], [[volcano-ac]], and [[anticheat-dashboard]].

## Links

- Repo: https://github.com/Dalbonden/Anti-cheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[encryptic-roblox-anti-cheat]] · [[volcano-ac]] · [[anticheat-dashboard]] · [[cheeto]] · [[bloxdesk]] · [[roblox-speed-tester]] · [[detector-operations]]