---
title: SmKernel-CSGO
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/DeiVid-12__SmKernel-CSGO.md
updated: 2026-08-26
confidence: medium
---

# SmKernel-CSGO

Educational **proof-of-concept kernel-driver-assisted CS:GO cheat architecture** (DeiVid-12). Uses **shared-memory communication** between user-mode and kernel-mode components to expose primitives such as **module-base lookup** and **cross-process memory read/write**, plus a **simple triggerbot** example. The project openly discusses **detectability tradeoffs** against stronger kernel anti-cheat systems and is mainly intended for learning **driver-based game hacking** and **anti-cheat threat models**. (source: wiki/sources/descriptions/DeiVid-12__SmKernel-CSGO.md)

Sits beside other CS:GO KM samples such as [[kernel-csgo]] (hook-based KM↔UM comm), [[garhal-csgo]] (IOCTL usermode controller), and [[raybot-zero]] (kernel triggerbot without a traditional usermode controller), and minimal cross-process R/W teaching drivers such as [[cheat-driver]].

## Links

- Repo: https://github.com/DeiVid-12/SmKernel-CSGO

## Related

[[kernel-csgo]] · [[garhal-csgo]] · [[raybot-zero]] · [[cheat-driver]] · [[csgo-full-kernel]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
