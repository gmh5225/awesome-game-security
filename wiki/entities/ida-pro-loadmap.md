---
title: ida-pro-loadmap
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mefistotelis__ida-pro-loadmap.md
updated: 2026-07-30
confidence: medium
---

# ida-pro-loadmap

IDA Pro plugin that imports symbol names from linker `.MAP` output files into the current database. Parses section:offset notation from VC, Borland, Dede, GCC, and IDA-format MAP files and creates named functions or labels at the corresponding addresses via the IDA SDK's `kernwin` and segment APIs. (source: wiki/sources/descriptions/mefistotelis__ida-pro-loadmap.md)

Useful when a game or anti-cheat client ships without PDBs but a build-time MAP file is available—restores readable function names before deeper static RE. Complements PDB workflows ([[pdb]], [[pdblister]], [[pdb-rs]]) and stripped-binary heuristics such as [[symless]] or [[idenlib]].

## Links

- Repo: https://github.com/mefistotelis/ida-pro-loadmap

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-map-symbol-parser]] · [[x64dbg-mapldr]] · [[pdb]] · [[pdblister]] · [[symless]] · [[idenlib]] · [[idaplugins]]
