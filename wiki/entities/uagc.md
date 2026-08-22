---
title: UAGC (UltimateAntiGamingChair)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/no1qq__UAGC.md
updated: 2026-08-22
confidence: medium
---

# UAGC (UltimateAntiGamingChair)

Context-aware anti-cheat platform implemented as a Java plugin for PaperMC Minecraft servers. Written in Java 21 (Gradle). Targets PaperMC **1.21** through **1.21.11**.

Modular check engine covering movement, combat, interaction, and protocol violations—including reach hacks, speed modifications, fast break, and timer abuse. Uses a confidence model that weighs legitimate game mechanics and server context to reduce false positives.

Built-in staff tooling includes exemptions, permission-based bypass with visibility for staff, evidence history, alerts, automatic and manual punishments, persistent player freeze, and an integration API for trusted plugins to report authorized behavior. Intended for multiplayer server operators who need server-side detection and enforcement against client-side cheating. (source: wiki/sources/descriptions/no1qq__UAGC.md)

## Detection stack

Modular movement/combat/interaction/protocol checks; confidence scoring with server-context false-positive reduction; staff exemptions and permission bypass audit; evidence history and alerts; automatic and manual punishment workflows; persistent freeze; trusted-plugin integration API.

## Links

- Repo: https://github.com/no1qq/UAGC

## Related

[[minecraft-anti-cheat]] · [[dakotaac]] · [[guardac]] · [[react]] · [[mlanticheat]] · [[antiguard]] · [[windfall-anticheat]] · [[phantom-client]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
