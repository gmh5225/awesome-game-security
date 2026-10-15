---
title: Nexora AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/yuonsovann5656-netizen__Nexora-AntiCheat.md
updated: 2026-10-15
confidence: medium
---

# Nexora AntiCheat

**Nexora AntiCheat** (yuonsovann5656-netizen/Nexora-AntiCheat) is a lag-compensated anti-cheat plugin for modern **Paper** and **Folia** Minecraft servers. It targets movement, combat, world, and protocol cheats with modular checks (speed, fly, kill aura, reach, scaffold, x-ray) and emphasizes low false positives via statistical analysis, vector ray-tracing, ping-aware reach math, velocity validation, and Bedrock/**Geyser** tolerance where appropriate. (source: wiki/sources/descriptions/yuonsovann5656-netizen__Nexora-AntiCheat.md)

## Server plugin

- **Stack** — Java **21**, **Maven** server-side core on the authoritative host.
- **Checks** — Modular movement/combat/world/protocol modules with lag compensation.
- **Persistence** — Async violation storage in **SQLite** or **MySQL**.
- **Enforcement** — Progressive kick-to-ban escalation; staff GUI and commands; **Discord** punishment webhooks.
- **Licensing** — Optional license heartbeat integration for commercial deployments. (source: wiki/sources/descriptions/yuonsovann5656-netizen__Nexora-AntiCheat.md)

## Operator panel

Bundled **React** + **Node.js** web panel backed by **Supabase PostgreSQL** for license issuance, fleet telemetry, and remote server management—aimed at survival or minigame network operators running multiple protected instances. (source: wiki/sources/descriptions/yuonsovann5656-netizen__Nexora-AntiCheat.md)

## Positioning

On-server heuristic + ops tooling on Paper/Folia—beside modular plugins such as [[bs-anticheat]] and [[h-ac]], physics simulation AC such as [[grim]], and cloud-review telemetry plugins such as [[pluginskers-shield]] and [[thorium-minecraft-plugin]]. Operational patterns: [[detector-operations]]. Catalog: [[minecraft-anticheat-list]].

## Links

- Repo: https://github.com/yuonsovann5656-netizen/Nexora-AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[bs-anticheat]] · [[h-ac]] · [[grim]] · [[pluginskers-shield]] · [[thorium-minecraft-plugin]] · [[detector-operations]] · [[minecraft-anticheat-list]]
