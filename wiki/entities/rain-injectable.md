---
title: RainInjectable
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/maximumemails-cmd__RainInjectable.md
  - wiki/sources/README-categories.md
updated: 2026-09-27
confidence: medium
---

# RainInjectable

**RainInjectable** (maximumemails-cmd/RainInjectable) is an injectable **Windows** runtime that loads the **Rain Anti-Cheat** passive observer into **Minecraft 1.8.9** **Forge** and **Badlion Client** processes. It combines a **C++/CMake** native injector and **JNI bootstrap** with a **Java 8** detection runtime that watches other players for killaura, auto-block, scaffold, and aim-related behavior without sending data to servers or changing gameplay. (source: wiki/sources/descriptions/maximumemails-cmd__RainInjectable.md)

README category: Anti Cheat / game:minecraft.

## Architecture

- **Native injector** — C++/CMake Windows loader that attaches to the JVM game process and bootstraps the Java detection runtime via JNI.
- **Observation engine** — temporal analysis over visible players' combat and movement patterns.
- **Evidence pipeline** — local evidence export and configurable GUI overlays that surface review candidates on the operator machine.

## Detection surface

Passive client-side observation for legacy **1.8.9** PvP cheat families:

- Killaura / auto-block
- Scaffold
- Aim-related rotation and targeting anomalies

No server telemetry, no gameplay mutation, and no automatic ban integration—flags remain local for human review.

## Positioning

Targets **defensive game-security research** and **authorized environments** where client-side cheat detection and evidence collection on legacy **1.8.9** multiplayer is needed. Complements Forge mod passive monitors such as [[local-anticheat-1-8-9]] (packet-flow checks without injection) and server-side **1.8.9** plugins such as [[ycbr-anticheat]]; contrasts with offensive JVM-injection clients such as [[phantom-client]] and MCP cheat stacks such as [[yuri]].

## Peers

[[local-anticheat-1-8-9]] · [[ycbr-anticheat]] · [[anticheat-qa]] · [[phantom-client]] · [[yuri]] · [[mcace]]

## Links

- Repo: https://github.com/maximumemails-cmd/RainInjectable

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[input-provenance]]
