---
title: Dani's Nightmare
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/PlinKuuu__DanisNightmare.md
updated: 2026-08-22
confidence: medium
---

# Dani's Nightmare

**BepInEx** mod for the Unity survival game **Muck** that adds a runtime debug and chat-command suite for manipulating nearly every aspect of gameplay. Written in **C#** with **Harmony** IL patches, it hooks player stats, mob scaling, loot drops, chest mechanics, day/night cycles, and item spawning without recompiling the game. Chat commands such as `/player`, `/enemy`, `/powerup`, and `/items` expose god mode, enemy wave control, powerup and item injection, peaceful mode, and time travel; Tab-key autocomplete reads live in-memory game data. Aimed at mod developers, reverse engineers, and security researchers who need a practical tool for probing and stress-testing Muck's engine behavior at runtime. (source: wiki/sources/descriptions/PlinKuuu__DanisNightmare.md)

## Command surface

| Command area | Capabilities |
|--------------|--------------|
| `/player` | Player stat manipulation, god mode |
| `/enemy` | Mob scaling, enemy wave control |
| `/powerup` | Powerup injection |
| `/items` | Item spawning |
| Other | Peaceful mode, time travel, Tab autocomplete from live memory |

## Links

- Repo: https://github.com/PlinKuuu/DanisNightmare

## Related

[[bepinex-il2cppbase]] · [[sts2-kitlib]] · [[unityexplorer]] · [[wellsanticheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
