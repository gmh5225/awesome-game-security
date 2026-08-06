---
title: GH Entity List Finder
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/guided-hacking__GH-Entity-List-Finder.md
updated: 2026-08-06
confidence: medium
---

# GH Entity List Finder

**Windows entity-list discovery tool** from Guided Hacking that scans **running game processes** to surface the most likely **entity list addresses**. Supports both **x64 and x86** targets. Aimed at game security researchers and reverse engineers studying offensive cheat / RE tooling when ESP, aimbot, or entity enumeration needs a stable list pointer before deeper offset work. (source: wiki/sources/descriptions/guided-hacking__GH-Entity-List-Finder.md)

Complements signature-based offset dumpers such as [[gh-offset-dumper]] and the [[source-netvars]] / `IClientEntityList` workflow for Source-engine titles.

## Links

- Repo: https://github.com/guided-hacking/GH-Entity-List-Finder

## Related

[[overviews/game-hacking]] · [[source-netvars]] · [[gh-offset-dumper]] · [[guided-hacking-injector]] · [[gh-d3d11-hook]] · [[overviews/reverse-engineering]]
