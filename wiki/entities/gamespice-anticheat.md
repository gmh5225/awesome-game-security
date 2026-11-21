---
title: GameSpice Anticheat
kind: entity
topics: [game-engine, anti-cheat, game-server-security]
sources:
  - wiki/sources/descriptions/gamespice-platform__anticheat.md
updated: 2026-11-21
confidence: medium
---

# GameSpice Anticheat

**Godot 4.7+ server-side anti-cheat addon** in the GameSpice addon family: GDScript modules for dedicated multiplayer hosts that score per-player suspicion and sanity-check untrusted client commands without installing client drivers or kernel hooks. Complements [[dot-server-security]]-style rule engines by turning detector reports into decaying scores and escalation *signals* the game or moderation stack applies—warn, kick, and ban thresholds are configurable but punishment is not enforced inside the addon itself. (source: wiki/sources/descriptions/gamespice-platform__anticheat.md)

**DotCommandSanity** validates movement, look rates, ranges, and command rates on client-submitted input. **DotSuspicionWatch** aggregates speed, teleport, and aim-snap hits (including feeds from GameSpice Server Security) into decaying suspicion scores and emits escalation events for host-defined enforcement. Headless dedicated servers are a first-class target; configuration uses YAML and environment variables. Listed under README **Anti Cheat → Open Source Anti Cheat System**.

## Components

| Module | Role |
|--------|------|
| DotCommandSanity | Movement, look-rate/range, and command-rate limits on untrusted input |
| DotSuspicionWatch | Aggregates detector reports into decaying per-player suspicion scores |
| Escalation hooks | Warn / kick / ban threshold signals—host or moderation stack enforces |

## Design notes

- **Server-authoritative scoring layer** — not a full client anti-tamper suite
- **Composable with GameSpice Server Security** — ingests speed/teleport/aim-snap detector output
- **No kernel or client driver footprint** — GDScript on the dedicated server

## Links

- Repo: https://github.com/gamespice-platform/anticheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[dot-server-security]] · [[void-engine]] · [[rearguard]] · [[guard-game]] · [[input-provenance]] · [[godot]]