---
title: IDAComments
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/NoneShell__IDAComments.md
updated: 2026-08-22
confidence: medium
---

# IDAComments

Python **IDA Pro** plugin for managing and organizing **user comments** during reverse engineering. Hooks comment-related actions so new annotations are captured and displayed in a dedicated view, with keyboard and menu access for quick review. Targets **IDA 7.x and 8.x** workflows. Useful when analyzing large binaries—game clients, anti-cheat modules, and other protected targets—where scattered inline notes need centralized triage without leaving the disassembler. (source: wiki/sources/descriptions/NoneShell__IDAComments.md)

Workflow helper only—not decompilation, renaming automation, or collaborative sync. Complements documentation export via [[ida-export-functions]], auto-comment generation from strings via [[ida-function-string-associate]], and multi-user comment sync via [[idarling]].

## Links

- Repo: https://github.com/NoneShell/IDAComments

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-export-functions]] · [[ida-function-string-associate]] · [[idarling]] · [[lazyida]] · [[list-of-ida-plugins]]
