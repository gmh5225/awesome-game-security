---
title: SAC The Server AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/IDELd__SAC-The-server-AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-09-15
confidence: medium
---

# SAC The Server AntiCheat

**SAC** (Super Anti Cheat; IDELd) is a server-side algorithmic anti-cheat plugin for Counter-Strike 2 on Metamod:Source and CounterStrikeSharp. Written in C# for .NET 8, it ships with 17 detection modules covering aimbot, silent aim, bhop, DLL injection, invalid input, and related cheat behaviors. Adds in-game player reporting, a four-stage progressive warning and ban system, mass-check sensitivity boosts after multiple reports, optional demo recording, and anonymized event logging. Targets CS2 dedicated server operators who want autonomous, rule-based cheat detection without external services or AI integrations. (source: wiki/sources/descriptions/IDELd__SAC-The-server-AntiCheat.md)

## Capabilities

- **17 algorithmic modules** — aimbot, silent aim, bhop, injection, invalid input, and related behaviors.
- **Dual host support** — Metamod:Source and CounterStrikeSharp.
- **Progressive enforcement** — four-stage warning/ban escalation with in-game reporting.
- **Mass-check mode** — elevated sensitivity after multiple player reports.
- **Optional demo capture** — match recording plus anonymized event logs.

Peers with [[anticheatsystem]], [[cs2ac]], [[cs2guard]], and [[osanticheat]] in the Open Source Anti Cheat System lane.

## Links

- Repo: https://github.com/IDELd/SAC-The-server-AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[anticheatsystem]] · [[cs2ac]] · [[cs2guard]] · [[detector-operations]] · [[input-provenance]]
