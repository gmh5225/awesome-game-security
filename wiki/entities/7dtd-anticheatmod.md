---
title: 7DTD AntiCheatMod
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/majimaakane__7dtd-AntiCheatMod.md
updated: 2026-08-16
confidence: medium
---

# 7DTD AntiCheatMod

Server-side anti-cheat **mod for 7 Days to Die (7DTD) dedicated multiplayer servers** that detects and blocks common cheating by non-administrative players. Written in C# for **.NET Framework 4.8**, it targets server operators running 7DTD **without Easy Anti-Cheat ([[easy-anti-cheat]])** who need lightweight, configurable server-side protection. (source: wiki/sources/descriptions/majimaakane__7dtd-AntiCheatMod.md)

## Detection and enforcement

- **Command blocking** — unauthorized console and chat cheat commands
- **Movement monitoring** — fly, teleport, speed hack, and god mode via configurable distance, speed, and duration thresholds
- **Admin exemption** — players at or below a defined admin permission level are skipped
- **Escalating penalties** — warnings through kicks to bans
- **Operator visibility** — online administrator notifications and detailed detections written to a dedicated log file

Sits in the server-authoritative dedicated-host lane beside [[cs2ac]], [[windfall-anticheatf]], and [[model-anti-cheat]], rather than kernel AC products.

## Links

- Repo: https://github.com/majimaakane/7dtd-AntiCheatMod

## Related

[[easy-anti-cheat]] · [[cs2ac]] · [[windfall-anticheatf]] · [[model-anti-cheat]] · [[gamesoftacs]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
