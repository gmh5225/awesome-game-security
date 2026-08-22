---
title: rezygisk
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/PerformanC__ReZygisk.md
updated: 2026-08-22
confidence: medium
---

# rezygisk

**ReZygisk** is an open-source standalone implementation of the **Zygisk API stack** for rooted Android environments. Rewritten largely in C, it targets a cleaner architecture, lighter binaries, and compatibility across **Magisk**, **KernelSU**, and **APatch**-based setups. The repository ships module packaging, dependency integration, and operational tooling for stable process injection and runtime hooks on modern Android. Primary audience: Android security researchers and module developers who need a transparent Zygisk-compatible runtime layer. (source: wiki/sources/descriptions/PerformanC__ReZygisk.md)

Contrasts with Magisk-bundled Zygisk and complements module ecosystems built on [[zygisk]] hooks (e.g. [[ksurusda]], [[florida-zygisk]], [[zygisk-frida]]). Framework home: [[magisk]] · [[kernelsu]] · [[zygisk]].

## Links

- Repo: https://github.com/PerformanC/ReZygisk (Transparent implementation of Zygisk)

## Related

[[zygisk]] · [[magisk]] · [[kernelsu]] · [[florida-zygisk]] · [[ksurusda]] · [[zygisk-frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
