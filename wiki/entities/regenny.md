---
title: regenny
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/cursey__regenny.md
updated: 2026-08-16
confidence: medium
---

# regenny

**Interactive live-memory struct reconstruction tool** (cursey; C++). Reads live process memory and maps raw bytes to user-defined struct layouts in a real-time memory viewer, supporting nested structs, arrays, pointers, enums, and bitfields. Enables iterative refinement of struct definitions and header export—aimed at game hackers and reverse engineers reconstructing unknown data structures from running processes, especially for SDK generation. (source: wiki/sources/descriptions/cursey__regenny.md)

Complements cursey's SDK codegen stack—[[sdkgenny]] (general C++ SDK emit library) and [[ue4genny]] (runtime UE4 reflection SDK generator)—and external structure-recon workflows such as [[reclass-dma]].

## Links

- Repo: https://github.com/cursey/regenny

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[sdkgenny]] · [[ue4genny]] · [[reclass-dma]] · [[luagenny]]
