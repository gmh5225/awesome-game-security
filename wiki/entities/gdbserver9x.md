---
title: gdbserver9x
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/robert-yates__gdbserver9x.md
updated: 2026-07-24
confidence: medium
---

# gdbserver9x

Minimal GDB remote stub (RSP) server for debugging 32-bit executables on legacy Windows (Win98SE/XP). Implements breakpoints, memory reads, register queries, and thread support; builds with VC6 and pairs with Binary Ninja’s GDB adapter for retro-Windows RE. (source: wiki/sources/descriptions/robert-yates__gdbserver9x.md)

Not a full debugger UI—scoped to a primitive GDB RSP stub so modern RE tools can attach to 32-bit targets on old Windows hosts.

## Links

- Repo: https://github.com/robert-yates/gdbserver9x

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[mcp-gdb]] · [[x64dbg]] · [[x64dbgbinja]] · [[ariadne]]
