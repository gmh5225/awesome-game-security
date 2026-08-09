---
title: cs2-webradar
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__cs2_webradar.md
updated: 2026-08-09
confidence: medium
---

# cs2-webradar

**Counter-Strike 2** browser-based radar cheat (C++ and JavaScript) that reads game memory and streams entity positions to a **web client** for a map overlay instead of drawing radar in-process or via a native external overlay. Centers on asset pipelines, modding, and memory analysis for the cheat / game:cs2 lane. Aimed at game security researchers and reverse engineers studying external radar architectures and how offset-driven entity state is consumed outside the game process. (source: wiki/sources/descriptions/gmh5225__cs2_webradar.md)

Complements native external CS2 samples such as [[cs2-ext]] and [[proext]] (in-process or native-overlay radar) by illustrating a web-fronted radar stack that depends on the same [[cs2-offsets]] / netvar artifacts as overlay cheats.

## Links

- Repo: https://github.com/gmh5225/cs2_webradar

## Related

[[cs2-offsets]] · [[cs2-offsets-ro0ti]] · [[cs2-ext]] · [[proext]] · [[cs2-external-cheat]] · [[source-netvars]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
