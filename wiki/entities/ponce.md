---
title: Ponce
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Ponce.md
updated: 2026-08-11
confidence: medium
---

# Ponce

IDA Pro plugin for symbolic and taint execution. Integrates the Triton dynamic binary analysis framework into IDA, enabling symbolic execution from within the disassembler to solve path constraints, track tainted data flow, and generate inputs that reach specific code paths. Aimed at vulnerability researchers and reverse engineers using symbolic execution for automated analysis in IDA Pro. (source: wiki/sources/descriptions/gmh5225__Ponce.md)

In-IDA symbolic-exec peer to radare2-backed [[radius2]] and standalone Triton workflows such as [[novmpy]] / [[rumba]]; complements in-IDA Unicorn emulation via [[sk3wldbg]] and CFF deflattening via [[idadeflat]] rather than replacing them.

## Links

- Repo: https://github.com/gmh5225/Ponce

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[sk3wldbg]] · [[radius2]] · [[idadeflat]] · [[novmpy]] · [[qsynthesis]]
