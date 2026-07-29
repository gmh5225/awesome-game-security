---
title: DisableParallelLoader
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__DisableParallelLoader.md
updated: 2026-07-29
confidence: medium
---

# DisableParallelLoader

[[x64dbg]] plugin that disables the Windows 10+ parallel DLL loader by patching `LdrpMapAndSnapWork` and related `ntdll` internals through the Process Hacker Native API (phnt). Forces sequential dependency loading during process creation so researchers can trace and debug DLL load order deterministically. (source: wiki/sources/descriptions/mrexodia__DisableParallelLoader.md)

Useful when reverse-engineering injectors, manual mappers, or anti-cheat modules whose initialization order matters under the default parallel loader.

## Links

- Repo: https://github.com/mrexodia/DisableParallelLoader

## Related

[[overviews/reverse-engineering]] · [[x64dbg]] · [[classroom]] · [[slothbp]] · [[detoursnt]]
