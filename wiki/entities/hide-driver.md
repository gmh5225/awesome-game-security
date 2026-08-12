---
title: HideDriver
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/nbqofficial__HideDriver.md
updated: 2026-07-28
confidence: medium
---

# HideDriver

Kernel driver-hide sample that unlinks a loaded driver from enumeration by modifying **Flink/Blink** (doubly-linked list unlink). Useful for game-security researchers studying cheat / hide and rootkit-like stealth against anti-cheat driver enumeration. (source: wiki/sources/descriptions/nbqofficial__HideDriver.md)

Pairs with other Detection:Hide-adjacent stealth samples such as [[hide-file]] (file hide) and [[mapped-callback]] (callback hide via codecave JMP). Broader multi-artifact cleanup samples such as [[hide-driver-testing]] (gmh5225; PiDDBCache/MmUnloadedDrivers/PsLoadedModuleList) target the same AC forensics lane. Same author lane as [[norsefire]] / [[kernel-csgo]].

## Links

- Repo: https://github.com/nbqofficial/HideDriver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[hide-file]] · [[hide-driver-testing]] · [[mapped-callback]] · [[norsefire]] · [[kernel-csgo]] · [[openark]]
