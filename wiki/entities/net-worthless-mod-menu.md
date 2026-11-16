---
title: Net Worthless Mod Menu
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/N00bPrograms__net-worthless-mod-menu.md
updated: 2026-11-16
confidence: medium
---

# Net Worthless Mod Menu

**Net Worthless Mod Menu** (N00bPrograms/net-worthless-mod-menu) is an open-source **in-game cheat overlay** for the Godot **4.7** life-simulation title *Net Worthless*. Toggled with **Insert**, the menu is implemented in **GDScript** and wires into the shipped game’s **autoloads** and **orchestrator** APIs rather than patching the executable. Install drops an `override.cfg` **autoload hook** into the game folder so the menu runs as a persistent `Node` alongside stock systems—illustrating **client-side Godot mod injection** without binary edits. Player tabs expose economy and simulation cheats (cash grants/locks, health and happiness controls, skill sliders, month skip with automatic event choices, age edits, free housing moves, marketplace rerolls). Settings can **disconnect the achievement system** from month-end and game-over signals to block **Steam and local achievement recording**; optional dev mode reads scripted commands from a text file for automation and screenshots. Primary audience: researchers and private-play users studying Godot runtime UI layering, autoload override mechanics, and how single-player cheats interact with platform achievements. (source: wiki/sources/descriptions/N00bPrograms__net-worthless-mod-menu.md)

Sits in the Godot offensive lane beside Cheat Engine runtime dumpers such as [[gddumper]] and native injector mod loaders such as [[gdpatch]]—here the integration surface is **engine-native autoload configuration** and direct calls into title orchestrator code rather than external memory tools or process injection.

## Links

- Repo: https://github.com/N00bPrograms/net-worthless-mod-menu

## Related

[[godot]] · [[gddumper]] · [[gdpatch]] · [[godot-sandbox]] · [[overviews/game-hacking]] · [[overviews/game-engine]]