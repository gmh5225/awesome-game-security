---
title: atmosphere
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Atmosphere-NX__Atmosphere.md
updated: 2026-09-01
confidence: medium
---

# atmosphere

Custom firmware platform for the Nintendo Switch that replaces or patches boot and runtime system components. Built mostly in C and C++ with low-level loaders, TrustZone behavior, sysmodules, and emulated NAND support. Organized into modular parts such as Fusee, Exosphere, Stratosphere, and related development libraries. Used by console security researchers and homebrew developers who need deep system-level control. (source: wiki/sources/descriptions/Atmosphere-NX__Atmosphere.md)

Provides the runtime stack behind homebrew memory tooling such as [[se-tools]] (`dmnt:cht` cheat services) and is often booted via payload chains from [[hekate]]. Cheat formats imported by [[opensw]] trace back to Atmosphere/Eden conventions.

## Links

- Repo: https://github.com/Atmosphere-NX/Atmosphere (README tag: Customized firmware)

## Related

[[hekate]] · [[se-tools]] · [[opensw]] · [[nstool]] · [[xci-explorer]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
