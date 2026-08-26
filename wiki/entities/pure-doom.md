---
title: PureDOOM
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Daivuk__PureDOOM.md
updated: 2026-08-26
confidence: medium
---

# PureDOOM

**PureDOOM** is a header-only, dependency-free **DOOM source port** implemented in pure C. It packages idTech 1 engine logic into a single portable interface that avoids standard-library dependencies and supports both 32-bit and 64-bit targets. Practical gameplay options and a minimal integration model make it suitable for embedding DOOM into unusual or constrained environments. Primarily useful for engine experimentation, low-level runtime research, and developers who want a compact retro game core. (source: wiki/sources/descriptions/Daivuk__PureDOOM.md)

Sits in the README **Game Engine → Source** lane — a stdlib-free idTech 1 core for embedding and runtime study, distinct from feature-rich ports such as [[doomretro]], [[gzdoom]], and [[uzdoom]]. Adapted as the engine base for kernel research demos such as [[ntdoom]].

## Links

- Repo: https://github.com/Daivuk/PureDOOM (README tag: [DOOM])

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[doomretro]] · [[gzdoom]] · [[uzdoom]] · [[ntdoom]] · [[devilution]] · [[game-design-documents]]
