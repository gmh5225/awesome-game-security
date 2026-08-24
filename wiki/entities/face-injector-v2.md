---
title: face-injector-v2
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/KANKOSHEV__face-injector-v2.md
updated: 2026-08-24
confidence: medium
---

# face-injector-v2

C++ **injector framework** that uses a **mapped kernel driver** to inject payloads into game processes (KANKOSHEV). The repository bundles payload-dropper logic, privilege-elevation helpers, randomized staging paths, and a mapper execution flow for loading the kernel component. It explicitly names multiple game targets and warns that using this approach can lead to bans. Primarily an educational sample for studying driver-backed injection techniques in game security research—not a maintained bypass product. (source: wiki/sources/descriptions/KANKOSHEV__face-injector-v2.md)

README lane: Injection/ Testing.

## Links

- Repo: https://github.com/KANKOSHEV/face-injector-v2

## Related

[[kdmapper]] · [[kernelmode-dll-injector]] · [[stealthy-kernelmode-injector]] · [[eac-injector-driver]] · [[memmap]] · [[guided-hacking-injector]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
