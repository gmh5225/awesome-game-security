---
title: Icarus
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/dxxxxy__Icarus.md
updated: 2026-11-15
confidence: medium
---

# Icarus

Cross-loader Minecraft mod library that turns **annotated static fields** into in-game settings menus. Mod authors declare pages, groups, sliders, dropdowns, and keybinds with Java annotations; the runtime builds the menu UI, persists **JSON configs**, fires change callbacks, and supports HUD elements and toasts. A **Minecraft-independent Java 8** core ships with thin per-target adapters for **Forge, Fabric, and NeoForge** across many versions (Gradle + Unimined; Jar-in-Jar packaging). Bundled themes closely recreate popular **CS:GO-style cheat-client** menu layouts (skeet/fatality aesthetics), so the project is useful for legitimate mod tooling and for studying cheat-client interface patterns in game-security work. (source: wiki/sources/descriptions/dxxxxy__Icarus.md)

Not a gameplay cheat client itself: a **shared GUI/config substrate** that utility mods and research clients can embed beside full-feature stacks such as [[epsilon]] and [[vortex-client]].

## Links

- Repo: https://github.com/dxxxxy/Icarus

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[epsilon]] · [[jsaclient]] · [[vortex-client]] · [[lenrete-mod]] · [[anticheat-qa]] · [[jaranalyzer]]