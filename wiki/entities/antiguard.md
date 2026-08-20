---
title: AntiGuard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/TheMille-Dev__AntiGuard.md
updated: 2026-08-20
confidence: medium
---

# AntiGuard

Self-contained anti-cheat plugin for Minecraft **Paper** and **Purpur** SMP servers. Written primarily in Java and shipped as a single drop-in JAR, it detects common client-side cheats without requiring external services. Physics-based checks cover fly, speed, reach, kill aura, auto-click, no-swing, no-fall, and fast-break behavior, using research-backed thresholds aimed at low false positives. The plugin embeds SQLite-backed storage (or reuses the LuckPerms database when present) to persist flags, bans, and kicks, and exposes a built-in web dashboard and REST API for live monitoring and configuration. Targets server operators and administrators who want lightweight on-server cheat detection and enforcement for multiplayer survival and minigame environments. Legacy Python components—a FastAPI reporting server and a reference agent—support earlier centralized flag-reporting workflows. (source: wiki/sources/descriptions/TheMille-Dev__AntiGuard.md)

## Detection stack

Physics-based movement and combat checks (fly, speed, reach, kill aura, auto-click, no-swing, no-fall, fast-break); research-backed violation thresholds; embedded SQLite persistence with optional LuckPerms DB reuse; built-in web dashboard and REST API for live monitoring and configuration.

## Links

- Repo: https://github.com/TheMille-Dev/AntiGuard

## Related

[[dakotaac]] · [[minecraft-anti-cheat]] · [[cklsit-advanced-anticheat]] · [[windfall-anticheat]] · [[ycbr-anticheat]] · [[minecraft-anticheatai]] · [[phantom-client]] · [[yuri]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
