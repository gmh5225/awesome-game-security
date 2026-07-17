---
title: Symbridge
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/xp987__symbridge.md
updated: 2026-07-17
confidence: medium
---

# Symbridge

Live annotation sync bridge between IDA Pro and x64dbg so names, comments, and C struct/type definitions stay aligned when switching between static and dynamic analysis. Sync is bidirectional, keyed by module and RVA (ASLR / differing image bases do not break matching). A Python broker holds canonical state over localhost TCP with newline-delimited JSON; thin adapters (IDAPython via IDB_Hooks, native C++ x64dbg plugin) push local edits and apply remote ones without echo loops. Optional persistence survives restarts; the protocol is designed for additional tool adapters. Aimed at RE workflows that use both IDA and x64dbg on the same binary. (source: wiki/sources/descriptions/xp987__symbridge.md)

Not a debugger or disassembler—bridges annotation state between the two tools.

## Links

- Repo: https://github.com/xp987/symbridge

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[xrefsext]] · [[idadeflat]]
