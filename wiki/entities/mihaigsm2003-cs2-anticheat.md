---
title: CS2 AntiCheat (mihaigsm2003)
kind: entity
topics: [anti-cheat, game:cs2]
sources:
  - wiki/sources/descriptions/mihaigsm2003__CS2-AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: medium
---

# CS2 AntiCheat (mihaigsm2003)

Open-source **Metamod:Source** plugin for Counter-Strike 2 dedicated servers (mihaigsm2003). Analyzes player aim, shots, movement, inputs, and **client-reported settings** on the authoritative host—no client install. Implementation is primarily C++ against the Source 2 SDK (hooks, detours, movement analysis, client cvar queries); Python and shell scripts drive AMBuild packaging for Linux and Windows. (source: wiki/sources/descriptions/mihaigsm2003__CS2-AntiCheat.md)

## Architecture

- **Native server module** — Metamod:Source load on dedicated CS2 Linux/Windows hosts; server-side observation of combat and movement telemetry.
- **Hook/detour layer** — Source 2 SDK integration for movement, firing, and input paths plus client cvar integrity probes—label cvar-derived fields **client-reported** until validated ([[input-provenance]]).
- **AMBuild toolchain** — reproducible dedicated-server binaries across platforms.

## Detection surface

Eighteen **independently configurable** detection modules cover aim assistance, trigger and silent aim, bunnyhop and autostrafe, subtick manipulation, invalid cvars and inputs, suspicious DLL-related client events, and related rage behaviors. Operators enable subsets and tune sensitivity before tying hits to sanctions—rehearse with [[detector-operations]] shadow/canary discipline on representative traffic. (source: wiki/sources/descriptions/mihaigsm2003__CS2-AntiCheat.md)

## Enforcement and reporting

`AntiCheat.cfg` and console commands configure punishments, player whitelists, and optional **Discord** or **JSON webhook** reporting for staff review and external case tooling.

## Catalog

Listed under README **Anti Cheat** → **Open Source Anti Cheat System**. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/mihaigsm2003/CS2-AntiCheat

## Related

[[overviews/anti-cheat]] · [[detector-operations]] · [[input-provenance]] · [[ai-aimbot-detection]] · [[anticheatsystem]] · [[plugify-cs2ac]] · [[cs2ac]] · [[sac-the-server-anticheat]] · [[cs2-anticheat-by-chmonya]] · [[aegis-ac-cs2]]
