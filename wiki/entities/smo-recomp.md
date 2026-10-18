---
title: smo-recomp
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Coz-0__smo-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: medium
---

# smo-recomp

Static recompilation of *Super Mario Odyssey* (Switch 1.4.1 AArch64) to native Windows x64 C, linked against a custom host runtime instead of emulating the console CPU. A Python lifter translates functions ahead of time; Clang builds the output while Unicorn differential tests check instruction fidelity. The runtime reimplements Switch system libraries, file I/O, SDL3 input, and NVN-style graphics on Vulkan with a Maxwell-to-SPIR-V shader translator. No game assets ship in the repository—researchers supply their own decrypted dump. Useful for studying Switch binary structure, static recompilation pipelines, and commercial porting without a JIT or interpreter. (source: wiki/sources/descriptions/Coz-0__smo-recomp.md)

## Links

- Repo: https://github.com/Coz-0/smo-recomp

## Related

[[ngbrecomp]] · [[sc2-android-recomp]] · [[static-runtime-evidence]] · [[opensw]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
