---
title: BinSync
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__binsync.md
updated: 2026-08-09
confidence: medium
---

# BinSync

Collaborative reverse engineering platform that synchronizes analysis data—function names, comments, types, and structs—across multiple users and disassemblers. Supports IDA Pro, Ghidra, Binary Ninja, and angr; stores shared annotations in a Git repository so teams can push and pull analysis, merge contributions, and track change history. Aimed at reverse engineering teams collaborating on large binary analysis projects across different tools. (source: wiki/sources/descriptions/gmh5225__binsync.md)

Complements single-tool live co-editing via [[idarling]] and BN↔Ghidra Server bridging via [[ghidra-svr-bridge]]—BinSync targets Git-backed, cross-disassembler annotation sync rather than real-time IDB sharing or Ghidra Server RMI alone.

## Links

- Repo: https://github.com/gmh5225/binsync

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[idarling]] · [[ghidra-svr-bridge]] · [[binexport]] · [[smallworld]]
