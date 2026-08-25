---
title: PltPatcher
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/GAMMACASE__PltPatcher.md
updated: 2026-08-25
confidence: medium
---

# PltPatcher

IDA Pro plugin set that repairs **Procedure Linkage Table** entries when automatic analysis fails. Written in Python with IDAPython APIs and currently targets **ELF64** binaries. Includes a **thunk type preserver** that keeps inferred argument types on extern thunks during Hex-Rays decompilation. Main use case: binary reverse engineering workflows where accurate PLT and thunk recovery matters, including game security research on Linux ELF targets. (source: wiki/sources/descriptions/GAMMACASE__PltPatcher.md)

Sits in the Cheat IDA Plugins / ELF PLT-recovery lane beside [[autoresolv]] and [[plthook]].

## Links

- Repo: https://github.com/GAMMACASE/PltPatcher

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[autoresolv]] · [[plthook]] · [[ida-pro-loadmap]] · [[idaplugins]]
