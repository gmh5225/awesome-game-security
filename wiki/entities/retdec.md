---
title: RetDec
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__retdec.md
updated: 2026-08-07
confidence: medium
---

# RetDec

Retargetable machine-code decompiler that lifts compiled binaries toward high-level C for offline static analysis. Listed in the Cheat → Decompiler lane for game security researchers and reverse engineers studying offensive techniques on protected game clients and cheat-related binaries. The upstream project is in limited maintenance due to resource constraints; pull requests are welcomed and reviewed with priority when possible. (source: wiki/sources/descriptions/gmh5225__retdec.md)

Sits in the binary-lifting stack beside McSema, remill, and Binary Ninja MLIL/HLIL workflows—useful when batch decompilation or IR-oriented analysis is needed outside interactive IDA/Ghidra sessions.

## Links

- Repo: https://github.com/gmh5225/retdec

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[oxidizer]] · [[garlic]] · [[ilspy]] · [[windbg-decompile-ext]]
