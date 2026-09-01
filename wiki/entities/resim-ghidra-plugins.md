---
title: RESimGhidraPlugins
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mfthomps__RESimGhidraPlugins.md
  - wiki/sources/README-categories.md
updated: 2026-09-01
confidence: medium
---

# RESimGhidraPlugins

Ghidra **Debugger extension plugins** (Java) that integrate Ghidra with the **RESim** reverse-engineering simulator, using Ghidra as the disassembler/debugger front end for simulation-backed analysis. Adds RESim-specific debugger windows for bookmarks, watchmarks, stack inspection, an interactive console, and listing hover helpers; connects to RESim targets via **gdb-multiarch** remote debugging, including **Simics** full-system sessions on port 9123. Mirrors much of the functionality previously available in RESim's IDA Pro plugins. (source: wiki/sources/descriptions/mfthomps__RESimGhidraPlugins.md)

Listed under README **Cheat > RE Tools** (Ghidra Plugins lane). Targets reverse engineers and security researchers who need **dynamic, simulation-backed** binary analysis rather than static disassembly alone.

Complements live GDB↔Ghidra bridges such as [[gdbghidra]] by wiring Ghidra Debugger to **RESim**-driven targets (including **Simics** full-system sessions) instead of a conventional attached process.

## Links

- Repo: https://github.com/mfthomps/RESimGhidraPlugins

## Related

[[ghidra]] · [[gdbghidra]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dynamic-binary-instrumentation]]
