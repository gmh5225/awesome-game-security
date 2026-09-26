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

**AntiCheat Dashboard** (severrir/AntiCheat-Dashboard) is a **Roblox server-side anti-cheat system** paired with a web-based staff console for monitoring and enforcement. Listed under README **Anti Cheat > Open Source Anti Cheat System**. (source: wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md)

## Game module

Luau server-side checks cover movement, character, combat, network, timing, and client integrity through a **trust-scoring engine** that requires corroboration before kicks, plus honeypots, bait traps, and optional cheater isolation.

## Staff dashboard

React + Vite + Tailwind + Three.js front-end backed by Supabase for live telemetry, global bans, Discord alerts, 3D kick replays, mission-control radar, case files, and appeal workflows. Targets production-grade cheat detection with live tuning without republishing and human-in-the-loop banning.

## Positioning

Adjacent to Luau server-side AC such as [[volcano-ac]], telemetry-first [[bloxdesk]], and client-side watchdog tooling. Pairs with [[detector-operations]] trust-scoring and corroboration patterns on [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/severrir/AntiCheat-Dashboard

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[volcano-ac]] · [[bloxdesk]] · [[guard-game]] · [[detector-operations]]
