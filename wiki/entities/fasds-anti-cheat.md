---
title: fasd's Anti Cheat
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/3iden-del__fasds-anti-cheat.md
updated: 2026-10-18
confidence: medium
---

# fasd's Anti Cheat

Fabric client mod for **Minecraft Java 1.21.11** (3iden-del/fasds-anti-cheat; Java; Fabric Loader + Fabric API; Gradle Loom; CI-built jar) that heuristically flags suspicious **nearby players** using only data the server already sends to the local client—no server plugin and no outbound reporting. (source: wiki/sources/descriptions/3iden-del__fasds-anti-cheat.md)

## Checks

Accumulates violation levels for categories such as speed, flight/hover, high jump, water walking, extended reach, kill aura / aim snapping, and autoclicker swing rates. Optional decay reduces stale alerts over time.

## UX

Press a key to print a ranked cheat report; another key clears stored flags. README notes results are **heuristic** and can false-positive on lag or unusual mechanics.

## Positioning

Same **passive client observer** lane as [[iustitia]] and [[rain-injectable]]—local awareness for multiplayer players, moderators, or researchers, not authoritative server anti-cheat.

## Links

- Repo: https://github.com/3iden-del/fasds-anti-cheat
- Overview: [[overviews/anti-cheat]]
