---
title: Faultline
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/svespalec__faultline.md
updated: 2026-07-21
confidence: medium
---

# Faultline

Windows usermode anti-cheat proof of concept (C++23 / CMake) that detects code executing from manually mapped or otherwise unregistered memory by watching **working-set page faults**. Uses `InitializeProcessForWsWatch`, `GetWsChangesEx`, and `QueryWorkingSet` to find `FaultingPc` or resident executable pages outside PEB-listed modules; on a hit, suspends the offending thread and walks its call stack. Ships a host process, a manual-map injector (remote thread or `SetThreadContext` hijack), and a test payload for shellcode-style and manual-map demos. Aimed at researchers studying usermode detection of memory-based cheats and injection. (source: wiki/sources/descriptions/svespalec__faultline.md)

Complements region-walk heuristics such as [[battleye-region-walking]] and offensive manual-map samples such as [[modexmap]].

## Links

- Repo: https://github.com/svespalec/faultline

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[battleye-region-walking]] · [[modexmap]] · [[anticheat-poc]] · [[injectors]]
