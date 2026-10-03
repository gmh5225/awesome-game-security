---
title: Kenshi Automation Harness
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/shaylanger__Kenshi-Automation-Harness.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# Kenshi Automation Harness

**Kenshi Automation Harness** (shaylanger/Kenshi-Automation-Harness) is an in-game **test automation framework** for **Kenshi** mod development. Scripts and AI agents drive a live game session through a **file-based command interface** implemented as a **C++ DLL plugin** built with the **KenshiLib SDK** and **Ogre/MyGUI**, paired with a **Python client** and **PowerShell** tooling to launch the game, send commands, and run **scenario-based tests**. Dozens of built-in commands cover spawning NPCs, manipulating world state, issuing AI orders, controlling UI, and verifying game state; other mods can register **custom commands** via a **C extension API**. Targets mod developers and automated testers who need repeatable, scriptable control without manual playthroughs — README **Game Testing** lane beside UE Gauntlet integration tests such as [[ue4-test-automation]] and Unity instrumentation-first QA samples such as [[games-test-automation-example]]. (source: wiki/sources/descriptions/shaylanger__Kenshi-Automation-Harness.md)

## Links

- Repo: https://github.com/shaylanger/Kenshi-Automation-Harness

## Related

[[ue4-test-automation]] · [[automation-examples]] · [[games-test-automation-example]] · [[overviews/game-engine]]
