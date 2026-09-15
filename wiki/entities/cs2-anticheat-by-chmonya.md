---
title: CS2 AntiCheat by Chmonya
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ChmonyaStudio__cs2-anticheat-by-chmonya.md
  - wiki/sources/README-categories.md
updated: 2026-09-15
confidence: medium
---

# CS2 AntiCheat by Chmonya

Server-side anti-cheat plugin for Counter-Strike 2 built on CounterStrikeSharp (ChmonyaStudio). Written in C# for .NET 8, it analyzes players every server tick with heuristic modules for aim snap/spin, jerk-based AI-aimbot smoothing, DMA hardware mouse emulators (subpixel patterns), grid-snap triggerbot, prefire, wallbang heuristics, bhop scripts, and HvH exploits (pitch anti-aim, spinbot, tickbase abuse). Combines suspicion scoring with decay, persistent JSON ban storage, Discord webhook alerts, and an in-game admin menu for thresholds, whitelists, and moderation. Targets CS2 server administrators who want lightweight plugin-based cheat detection without a client-side anti-cheat install. (source: wiki/sources/descriptions/ChmonyaStudio__cs2-anticheat-by-chmonya.md)

## Capabilities

- **Per-tick heuristics** — aim snap/jerk, DMA subpixel mouse emulation, HvH anti-aim/spinbot, grid-snap triggerbot, prefire, wallbang, bhop.
- **CounterStrikeSharp host** — C#/.NET 8 plugin; no Metamod dependency.
- **Progressive enforcement** — suspicion scoring with decay, JSON ban list, Discord webhooks.
- **Admin menu** — in-game threshold, whitelist, and moderation controls.

Peers with [[sac-the-server-anticheat]], [[anticheatsystem]], [[cs2ac]], and [[cs2guard]] in the Open Source Anti Cheat System lane.

## Links

- Repo: https://github.com/ChmonyaStudio/cs2-anticheat-by-chmonya

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/dma-attack]] · [[sac-the-server-anticheat]] · [[anticheatsystem]] · [[cs2ac]] · [[cs2guard]] · [[detector-operations]] · [[input-provenance]] · [[hardware-input-injection]]
