---
title: Le Chiffre
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Blaumaus__le_chiffre.md
updated: 2026-08-30
confidence: medium
---

# Le Chiffre

Lightweight **external** Counter-Strike: Global Offensive cheat **proof of concept** from Blaumaus, written in **C++**. Implements common gameplay automation features—**bunnyhop**, **triggerbot**, **aimbot**, **glow ESP**, and **radar hacks**—via out-of-process memory-based game manipulation. Structured as an **educational codebase** to demonstrate memory hacking and reverse-engineering fundamentals for learners studying low-level Windows game hacking techniques, not production use. (source: wiki/sources/descriptions/Blaumaus__le_chiffre.md)

Treat as a compact CS:GO external PoC for studying classic usermode feature modules and offset-driven workflows—not a maintained cheat product.

## Feature modules

| Module | Role |
|--------|------|
| Bunnyhop | Automated jump timing |
| Triggerbot | Fire-on-target automation |
| Aimbot | Aim assistance |
| Glow ESP | Entity highlight visuals |
| Radar hacks | Minimap-style awareness helpers |

See [[csgo-cheats]] for tutorial-oriented external examples and [[csgo-external-cheat]] for RPM/driver-backed external patterns in the same lane.

## Links

- Repo: https://github.com/Blaumaus/le_chiffre

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[csgo-external-cheat]] · [[csgo-cheats]] · [[external-cheat-v3]] · [[heck-csgo-external]] · [[echinoidea]] · [[csgo-external-esp]]
