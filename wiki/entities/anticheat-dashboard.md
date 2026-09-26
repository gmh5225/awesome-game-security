---
title: AntiCheat Dashboard
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# AntiCheat Dashboard

**AntiCheat Dashboard** (severrir/AntiCheat-Dashboard) is a **Roblox server-side anti-cheat system** paired with a web-based staff console for monitoring and enforcement. Listed under README **Anti Cheat > Open Source Anti Cheat System**. Targets Roblox developers and moderation teams who need production-grade cheat detection, live tuning without republishing, and **human-in-the-loop banning** rather than fully automated punishment. (source: wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md)

## Detection surface

Luau **server-side** module runs movement, character, combat, network, timing, and client-integrity checks through a **trust-scoring engine** that requires **corroboration before kicks**, plus honeypots, bait traps, and optional cheater isolation. (source: wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md)

## Staff console

React + Vite + Tailwind + Three.js front-end backed by **Supabase** for live telemetry ingest, global bans, Discord alerts, **3D kick replays**, mission-control radar, case files, and appeal workflows. Operators can tune detection live without republishing the game module. (source: wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md)

## Positioning

**Trust-scored enforcement with staff dashboard** — unlike auto-kick Luau AC such as [[volcano-ac]] or telemetry-only [[bloxdesk]], pairs corroborated server-side scoring with a full moderation console. Adjacent to [[shprotect-ac]], [[advanced-anticheat]], and [[encryptic-roblox-anti-cheat]] in the Roblox Luau server-side lane; illustrates [[detector-operations]] corroboration-before-sanction patterns on [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/severrir/AntiCheat-Dashboard

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[volcano-ac]] · [[bloxdesk]] · [[guard-game]] · [[detector-operations]]
