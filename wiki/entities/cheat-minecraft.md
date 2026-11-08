---
title: cheat-minecraft (SkyOP Client)
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/sky-pixel-Sp__cheat-minecraft.md
  - wiki/sources/README-categories.md
updated: 2026-11-08
confidence: high
---

# cheat-minecraft (SkyOP Client)

**cheat-minecraft** ([sky-pixel-Sp/cheat-minecraft](https://github.com/sky-pixel-Sp/cheat-minecraft)) ships **SkyOP Client**, an open-source **Fabric** mod for **Minecraft Java Edition 26.3**: modular combat, movement, render, inventory, and HUD features behind a searchable **ClickGUI**. (source: wiki/sources/descriptions/sky-pixel-Sp__cheat-minecraft.md)

## Implementation

Java with **Fabric Loader**, **Fabric Loom**, Gradle, and **Minecraft mixins**; JSON profiles, multi-language UI strings, and unit tests for configuration codecs. CI-built releases.

## Notable modules

Combat helpers (**KillAura**, **TriggerBot**, **AutoClicker**), movement (**flight**, speed), **entity ESP**, on-screen HUD panels, and inventory automation (auto eat, armor, tool selection, refill, fishing).

## Multiplayer boundary

Inventory and container changes use vanilla client actions that servers can validate or reject; authors document multiplayer limitations rather than anti-cheat bypass claims.

## Research use

Reference for game security research, anti-cheat evaluation, and reverse engineering of modern Java Edition **Fabric mixin** cheat-client module design—complements JVM attach agents such as [[nocturne-client]] and [[k0t1k-overlay]].

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[leaf-mod-analyzer]] · [[nocturne-client]] · [[k0t1k-overlay]]

## Links

- Repo: https://github.com/sky-pixel-Sp/cheat-minecraft
