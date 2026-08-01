---
title: AutoAttach
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/legendabrn__AutoAttach.md
updated: 2026-08-01
confidence: medium
---

# AutoAttach

x64dbg plugin that automatically attaches to a configured target process. Written in C/C++; aimed at plugin development and modding in the Cheat / x64dbg Plugins lane. Useful when game-security researchers need hands-off debugger attach to a named executable (e.g. `dota2.exe`) under [[x64dbg]]. (source: wiki/sources/descriptions/legendabrn__AutoAttach.md)

Commands are entered in the x64dbg command bar:

- `AutoAttachStatus 0|1` — disable or enable auto-attach
- `AutoAttachProcess <name>` — set target process name (e.g. `AutoAttachProcess dota2.exe`)
- `AutoAttachSleep <ms>` — delay in milliseconds before attach (e.g. `AutoAttachSleep 1000`)

Not a standalone debugger—extends [[x64dbg]] attach workflow for timed or process-name–driven sessions.

## Links

- Repo: https://github.com/legendabrn/AutoAttach

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[steam-anti-anti-debug]]
