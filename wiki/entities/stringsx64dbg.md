---
title: Strings x64dbg
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/horsicq__stringsx64dbg.md
updated: 2026-08-05
confidence: medium
---

# Strings x64dbg

[[x64dbg]] plugin that adds a dedicated tab for searching and browsing strings inside a debugged process or module. Written in C++ with a Qt-based UI; integrates through the x64dbg plugin SDK and exposes a `SearchStringsWidget` for listing and filtering extracted strings. Supports 32-bit and 64-bit builds via standard x64dbg bridge APIs for GUI tabs and debugger interaction. Aimed at reverse engineers and game-security analysts who need richer string discovery while debugging with [[x64dbg]]. (source: wiki/sources/descriptions/horsicq__stringsx64dbg.md)

Not a standalone static analyzer—live-process/module string extraction inside the debugger, complementary to peers such as [[xfindout]] (memory access tracing) and [[manytypes]] (type/structure parsing).

## Links

- Repo: https://github.com/horsicq/stringsx64dbg

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[x64dbg-plugin-manager]] · [[manytypes]] · [[xfindout]]
