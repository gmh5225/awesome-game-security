---
title: ZyvenAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/orglatis-a11y__ZyvenAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-15
confidence: medium
---

# ZyvenAntiCheat

**ZyvenAntiCheat** (orglatis-a11y/ZyvenAntiCheat) is an open-source **Bukkit/Paper 1.21** Minecraft server anti-cheat plugin. It runs entirely server-side—no modified client is required. The project is implemented in **Java** with **Maven** against the Paper API. (source: wiki/sources/descriptions/orglatis-a11y__ZyvenAntiCheat.md)

## Detection stack

- **Event-driven checks** — movement, combat, mining, vehicles, and item use, with violation levels and configurable staff alerts and kick commands.
- **Movement & utility** — fly, speed, no-fall, elytra and boat abuse, reach, kill aura, autoclick, crystal and anchor auras, fast eat, and auto-totem.
- **Mining** — break timing and speed limits.

## Anti-ESP countermeasures

Standout defensive techniques include **line-of-sight entity hiding**, **per-player decoy entities** against ESP and freecam, and **client-only bait blocks** aimed at block-ESP and base-finder clients—overlapping the server-side visibility-mitigation lane beside [[civ-anticheat]] ray-masked ESP handling and honeypot-style plugins such as [[larping-anti-cheat]].

Targets survival and PvP server operators who want lightweight, configurable game security on a standard Bukkit or Paper host.

## Links

- Repo: https://github.com/orglatis-a11y/ZyvenAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[minecraft-anti-cheat]] · [[amber-anticheat]] · [[civ-anticheat]] · [[larping-anti-cheat]] · [[kozy-anticheat]]