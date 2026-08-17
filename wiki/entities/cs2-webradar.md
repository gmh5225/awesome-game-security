---
title: cs2-webradar
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__cs2_webradar.md
  - wiki/sources/descriptions/clauadv__cs2_webradar.md
updated: 2026-08-17
confidence: medium
---

# cs2-webradar

Browser-based **Counter-Strike 2** radar cheats share this name in the curated list—C++/JavaScript stacks that read game memory and stream entity positions to a **web client** for a map overlay instead of drawing radar in-process or via a native external overlay. Both forks center on asset pipelines, modding, and memory analysis for the cheat / game:cs2 lane and are aimed at game security researchers and reverse engineers studying external radar architectures and how offset-driven entity state is consumed outside the game process.

## gmh5225/cs2_webradar

Counter-Strike 2 browser-based radar cheat (C++ and JavaScript) that reads game memory and streams entity positions to a web client for a map overlay. (source: wiki/sources/descriptions/gmh5225__cs2_webradar.md)

## clauadv/cs2_webradar

Undetected browser-based CS2 radar cheat (C++ and JavaScript) centered on asset pipelines, modding, and Unity. Useful for researchers studying offensive techniques in the cheat / game:cs2 area. (source: wiki/sources/descriptions/clauadv__cs2_webradar.md)

Complements native external CS2 samples such as [[cs2-ext]] and [[proext]] (in-process or native-overlay radar) by illustrating a web-fronted radar stack that depends on the same [[cs2-offsets]] / netvar artifacts as overlay cheats.

## Links

- Repo (gmh5225): https://github.com/gmh5225/cs2_webradar
- Repo (clauadv): https://github.com/clauadv/cs2_webradar

## Related

[[cs2-offsets]] · [[cs2-offsets-ro0ti]] · [[cs2-ext]] · [[proext]] · [[cs2-external-cheat]] · [[cs2-dma-radar]] · [[source-netvars]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
