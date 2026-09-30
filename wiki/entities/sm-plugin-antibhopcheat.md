---
title: sm-plugin-AntiBhopCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/srcdslab__sm-plugin-AntiBhopCheat.md
updated: 2026-09-30
confidence: medium
---

# sm-plugin-AntiBhopCheat

**SourceMod plugin** for **Source engine** dedicated servers that detects **bunny hop cheats**, including scripted bhop hacks and **hyperscroll** input patterns. Written in **SourcePawn**, it analyzes player **jump timing**, **velocity**, and **tick-level input** across current and global streak windows to flag suspicious movement with configurable thresholds. (source: wiki/sources/descriptions/srcdslab__sm-plugin-AntiBhopCheat.md)

## Detection and enforcement

Server administrators can review detections via **admin commands**, optionally play **alert sounds**, limit bunny hopping for flagged players through **SelectiveBhop** integration, or **automatically kick** repeat offenders. Targets competitive and community server operators who need server-side anti-cheat enforcement against movement automation on **Counter-Strike** and other SourceMod-supported titles.

## Links

- Repo: https://github.com/srcdslab/sm-plugin-AntiBhopCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[little-anti-cheat]] · [[nocheatz-3]] · [[corner-culling-source-engine]] · [[source-engine]] · [[input-provenance]]
