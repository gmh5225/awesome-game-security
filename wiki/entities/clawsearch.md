---
title: ClawSearch
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/codecat__ClawSearch.md
updated: 2026-08-16
confidence: medium
---

# ClawSearch

[[x64dbg]] plugin (C++; Visual Studio) that adds **Cheat Engine–style memory value scanning** for the currently debugged process—first/next scans over integer and floating-point types (8–64-bit, float, double) with comparison modes such as exact match, bigger/smaller than, changed/unchanged, and increased/decreased values. Uses the x64dbg plugin SDK for memory-map access and reads, plus the IUP toolkit for its search dialog UI. Optional features include hex input, fast-scan alignment stepping, float truncate/round matching, pause-while-scanning, and jumping from result addresses into the debugger dump view. Aimed at reverse engineers and game-security researchers who need iterative value finding while debugging Windows binaries in [[x64dbg]]. (source: wiki/sources/descriptions/codecat__ClawSearch.md)

Complements [[xfindout]] (memory write/access tracing) and generic Cheat Engine workflows for live variable discovery inside a debugger session—not a standalone scanner.

## Links

- Repo: https://github.com/codecat/ClawSearch

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[xfindout]] · [[x64dbg-plugin-manager]]
