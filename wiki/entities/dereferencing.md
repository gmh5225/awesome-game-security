---
title: deREferencing
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/danigargu__deREferencing.md
  - wiki/sources/README-categories.md
updated: 2026-09-03
confidence: medium
---

# deREferencing

**deREferencing** is a Python IDA Pro plugin that adds enhanced register and stack debugger windows for live binary analysis. Dereferences pointers, applies color-coded memory annotations, and surfaces contextual values in a PEDA/GEF/pwndbg-like workflow inside IDA. Supports x86, x86-64, ARM, ARM64, MIPS32, and MIPS64 with configurable settings. (source: wiki/sources/descriptions/danigargu__deREferencing.md)

## Capabilities

- **Register view** — dereferenced pointer chains with color-coded annotations.
- **Stack view** — richer stack contents during live debugging sessions.
- **Multi-arch** — x86/x64, ARM/ARM64, MIPS32/MIPS64.
- **Configurable** — settings module tunes display and dereference depth.

Complements IDA debugger UX plugins such as [[lazyida]], [[happyida]], and [[idaref]]; pairs with MCP-assisted RE stacks such as [[ida-pro-mcp]] and agent-native labs such as [[open-reverselab]].

## Links

- Repo: https://github.com/danigargu/deREferencing

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-mcp]] · [[lazyida]] · [[idaref]] · [[open-reverselab]]
