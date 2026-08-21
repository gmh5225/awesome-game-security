---
title: il2cpp-pdb
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/bombaris34__il2cpp-pdb.md
updated: 2026-08-21
confidence: medium
---

# il2cpp-pdb

Il2CppDumper fork with a native Rust PDB generator for x64 PE (`GameAssembly.dll`). Extends standard [[il2cpp]] metadata dumping by emitting Windows PDB debug symbol files that map method addresses and type information back to original .NET symbols — function names, full struct types, and typed prototypes — for debugger integration. Output is auto-loaded by IDA. (source: wiki/sources/descriptions/bombaris34__il2cpp-pdb.md)

Complements cross-platform dump tooling such as [[il2cpp-inspector]] and script-based IDA import: where those produce `script.json` / headers, il2cpp-pdb supplies native PDB symbols in the same lane as synthetic symbol tools ([[fakepdb]]) and general Windows PDB parsers ([[pdb]], [[pdb-rs]]).

## Links

- Repo: https://github.com/bombaris34/il2cpp-pdb

## Related

[[il2cpp]] · [[il2cpp-inspector]] · [[il2cppdumper]] · [[ida-unity-pdb-downloader]] · [[fakepdb]] · [[pdb]] · [[pdb-rs]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
