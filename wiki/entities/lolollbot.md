---
title: lolollbot
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Sasha-cyn__lolollbot.md
updated: 2026-11-24
confidence: medium
---

# lolollbot

**Geode** client mod for **Geometry Dash** (Sasha-cyn/lolollbot; **C++**; **CMake**) that **records and replays frame-accurate click macros** in the spirit of classic **xDBot** tooling. Hooks core layers such as `PlayLayer`, `PlayerObject`, and menu/input dispatchers to capture inputs in record mode and inject them during playback; persists per-level macro data on disk and supports **practice-mode checkpoint rewinds**. Ships a configurable overlay with cheats including **noclip**, **speedhack**, FPS/TPS overrides, and several player/level-effect bypasses—useful for studying rhythm-game automation, client-side modification, and how unofficial tooling interacts with in-game checks such as **spike-based death validation**. (source: wiki/sources/descriptions/Sasha-cyn__lolollbot.md)

## Mechanism

- **Record / playback**: frame-aligned input capture and reinjection through Geode hooks on play and input paths.
- **Persistence**: per-level macro files on disk; checkpoint rewind in practice mode.
- **Overlay menu**: in-game cheat toggles (noclip, speedhack, timing overrides, effect bypasses).

## Security research angles

- **Input provenance**: replayed clicks are **client-injected**—not corroborated by server or raw HID telemetry; see [[input-provenance]].
- **Client-only AC**: spike/death validation runs in-process; macro + bypass modules illustrate limits of local integrity checks versus networked titles.
- **Ecosystem**: contrasts with assist mods such as [[earlybuffering-gd]] and integrity tooling such as [[level-hash]] on the same Geode/Geometry Dash stack.

## Links

- Repo: https://github.com/Sasha-cyn/lolollbot

## Related

[[earlybuffering-gd]] · [[level-hash]] · [[gd-internal]] · [[input-provenance]] · [[cheat-attack-surface]] · [[overviews/game-hacking]]