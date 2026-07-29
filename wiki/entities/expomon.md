---
title: ExpoMon
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/milcert__ExpoMon.md
updated: 2026-07-29
confidence: medium
---

# ExpoMon

x64dbg plugin with a Qt-based GUI that monitors DLL export tables in the debugged process in real time. Built against the x64dbg Plugin SDK (`bridgemain`, TitanEngine, XEDParse). Displays loaded-module export function names, ordinals, and addresses as modules load; includes Windows internals helpers for resolving device names and process information. (source: wiki/sources/descriptions/milcert__ExpoMon.md)

Useful when tracing game or anti-cheat DLLs that expose many exports (hooks, callbacks, RPC stubs) and you need a live view of the export surface without leaving the debugger. Extends [[x64dbg]] in the Cheat / Exports monitoring lane—not a standalone disassembler or static PE viewer.

## Links

- Repo: https://github.com/milcert/ExpoMon

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[slothbp]] · [[classroom]] · [[xfindout]] · [[idenlibx]]
