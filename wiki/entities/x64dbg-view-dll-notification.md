---
title: X64DBG ViewDllNotification
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__X64DBG-ViewDllNotification.md
updated: 2026-08-09
confidence: medium
---

# X64DBG ViewDllNotification

[[x64dbg]] plugin (C++/C++) that surfaces DLL load-notification activity inside the debugger—useful when tracing injectors, manual mappers, or anti-cheat modules that register `LdrRegisterDllNotification` callbacks to observe module load/unload events. Listed under Cheat / x64dbg Plugins; plugin-development focus for game-security researchers and reverse engineers. (source: wiki/sources/descriptions/gmh5225__X64DBG-ViewDllNotification.md)

Complements other in-debugger DLL introspection such as [[expomon]] (live export-table monitoring) and [[disable-parallel-loader]] (sequential load-order debugging).

## Links

- Repo: https://github.com/gmh5225/X64DBG-ViewDllNotification

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[expomon]] · [[disable-parallel-loader]]
