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

Default keybinds: **K** prints a ranked cheat report for flagged nearby players; **J** clears stored flags. README notes results are **heuristic** and can false-positive on lag or unusual mechanics. (source: wiki/sources/descriptions/3iden-del__fasds-anti-cheat.md)

## Operations

Local-only ranked reports with optional violation **decay**—no server plugin, outbound telemetry, or automatic sanctions. Treat accumulated violation levels as review hints corroborated with independent signals, not authoritative verdicts.

## Positioning

Same **passive client observer** lane as [[iustitia]] and [[rain-injectable]]—lightweight cheat awareness for multiplayer players, moderators, or researchers, not authoritative server anti-cheat.

## Links

- Repo: https://github.com/3iden-del/fasds-anti-cheat

## Related

[[overviews/anti-cheat]] · [[concepts/detector-operations]] · [[iustitia]] · [[anticheat-qa]]
