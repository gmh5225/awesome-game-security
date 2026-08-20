---
title: SimpleQuest
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/TheGeebus__SimpleQuest.md
updated: 2026-08-20
confidence: medium
---

# SimpleQuest

Unreal Engine **5.6+** plugin and demo project for authoring and running **graph-based questlines** in games. Written primarily in C++ with Blueprint support; ships editor modules for designing questline graphs, objectives, prerequisites, activation groups, rewards, and related gameplay tags. Runtime pieces include quest giver, trigger, observer, and reward components, plus save/load of quest state and a companion **SimpleCore** signal and world-state fact subsystem. Targets UE game developers who need a structured quest framework with PIE debugging and inspection tools—not anti-cheat or reverse-engineering work. (source: wiki/sources/descriptions/TheGeebus__SimpleQuest.md)

Sits in the Game Engine Plugins:Unreal lane beside other graph-oriented editor plugins such as [[generic-graph]] and gameplay progression samples such as [[trinitycore]] (server-side quest emulation) for contrasting client-side UE authoring vs. MMO server frameworks.

## Links

- Repo: https://github.com/TheGeebus/SimpleQuest (README: Unreal Engine 5.6+ event-driven progression/quest framework with visual graph authoring)

## Related

[[overviews/game-engine]] · [[generic-graph]] · [[luamachine]] · [[simple-fps-template]] · [[unreal-object-model]] · [[unreal-engine-guide]]
