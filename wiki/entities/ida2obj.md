---
title: IDA2Obj
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__IDA2Obj.md
updated: 2026-08-12
confidence: medium
---

# IDA2Obj

Tool that **exports IDA Pro database content back into linkable object files**. Reconstructs **COFF/ELF** objects from IDA analysis data—relocations, symbols, and section content—for **binary patching** and **recompilation** workflows. Listed under the cheat / RE lane with a `[COFF Relink]` tag. (source: wiki/sources/descriptions/gmh5225__IDA2Obj.md)

Bridges static analysis in IDA to a relinkable object artifact; complements PE-level editors such as [[kitsupe]] and patch-script generators such as [[genpatch]] when the goal is to round-trip analyzed code into a linkable `.obj` rather than raw byte patches.

## Links

- Repo: https://github.com/gmh5225/IDA2Obj

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[kitsupe]] · [[genpatch]] · [[ida2llvm]] · [[levo]] · [[list-of-ida-plugins]]
