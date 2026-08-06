---
title: GH Offset Dumper
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/guided-hacking__GH-Offset-Dumper.md
updated: 2026-08-06
confidence: medium
---

# GH Offset Dumper

**Windows offset dumper** from Guided Hacking that scans **running game processes** with **pattern (signature) scanning** to locate structures, entity lists, client/engine **interface pointers**, and **netvars**, then exports results as **C++ headers** or **JSON**. The C++ tool is commonly used with **Source engine** titles so game hackers and modders can refresh memory layouts after patches without hand-updating every offset. (source: wiki/sources/descriptions/guided-hacking__GH-Offset-Dumper.md)

Complements maintained header dumps such as [[cs2-offsets]] and [[dota2dumped]], static SDK trees such as [[sdk]], and the [[source-netvars]] parsing workflow.

## Links

- Repo: https://github.com/guided-hacking/GH-Offset-Dumper

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-netvars]] · [[gh-entity-list-finder]] · [[guided-hacking-injector]] · [[gh-d3d11-hook]] · [[cs2-offsets]] · [[dota2dumped]] · [[sdk]] · [[offsets]]
