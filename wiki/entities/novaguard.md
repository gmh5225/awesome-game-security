---
title: NovaGuard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Novastudio953__NovaGuard.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# NovaGuard

**NovaGuard** (Novastudio953/NovaGuard) is a high-performance **server-side anti-cheat plugin** for **Minecraft Paper 1.21** servers. Written in **Kotlin**, it targets **server administrators** who need server-side cheat detection and moderation for multiplayer Minecraft worlds without client installs. (source: wiki/sources/descriptions/Novastudio953__NovaGuard.md)

README category: Anti Cheat / game:minecraft.

## Detection

44 individually toggleable checks span five domains, each with its own violation-level thresholds, punishments, and ban commands:

- **Movement** — speed, flight, and related locomotion heuristics.
- **Combat** — reach, kill aura, and combat automation signals.
- **World exploits** — scaffold, fast break/place, and interaction abuse.
- **Macro-style automation** — repetitive input and automation patterns.
- **X-ray mining** — honeypot-style ore-exposure traps for underground mining cheats.

## Operations and staff tooling

Built-in moderation includes a suspects GUI, player freeze, ban waves, violation history, player reports, and Discord webhook alerts. Grace periods, lag shields, Bedrock exemptions, and VPN blocking help limit false positives during load spikes and cross-platform play.

## Positioning

Production-oriented **Paper 1.21** modular AC with granular per-check tuning and integrated staff workflows—beside Java modular plugins such as [[h-ac]], heuristic Paper plugins such as [[bs-anticheat]], and client-mod fingerprinting plugins such as [[chanhne-dev-anticheat]].

## Peers

[[h-ac]] · [[bs-anticheat]] · [[nova-anticheat]] · [[chanhne-dev-anticheat]] · [[ultimate-meteor-anticheat]]

## Links

- Repo: https://github.com/Novastudio953/NovaGuard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]]
