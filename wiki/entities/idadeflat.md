---
title: IDADeflat
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/za233__IDADeflat.md
updated: 2026-07-17
confidence: medium
---

# IDADeflat

IDA Pro plugin for semi-automated removal of control-flow flattening (CFF). Python-based; uses angr symbolic execution to find real basic blocks, recover the original CFG, and patch the flattened function back to deobfuscated form. Aimed at RE / malware analysts facing OLLVM-style CFF in protected binaries. (source: wiki/sources/descriptions/za233__IDADeflat.md)

Not a full unpacker—scoped to CFF deflattening inside IDA.

## Links

- Repo: https://github.com/za233/IDADeflat

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[deobf]] · [[xrefsext]]
