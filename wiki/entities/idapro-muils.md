---
title: IDAPro-MuiLs
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/PoP-Lin__IDAPro-MuiLs.md
updated: 2026-09-19
confidence: medium
---

# IDAPro-MuiLs

IDAPython plugin that applies a restrained modern dark theme to **IDA Pro 9.3** while preserving native workspace behavior. Implemented in Python with PySide6 and scoped Qt stylesheets, it restyles menus, toolbars, docks, dialogs, choosers, graph views, scrollbars, and compatible third-party plugin panels. (source: wiki/sources/descriptions/PoP-Lin__IDAPro-MuiLs.md)

## Scope

- **Target:** IDA Pro 9.3 on Windows 11
- **Implementation:** IDAPython, PySide6, scoped Qt stylesheets
- **Category:** Cheat / IDA themes (README)
- **Features:** automatic startup with persistent settings; continuous rounded row selection in Functions/Names/Strings views; customizable fonts, accent colors, density, and corner radius with live preview; smooth Windows resize handling with dark title-bar integration; compatible third-party plugin panel styling

Visual comfort tooling—does not alter disassembly, decompilation, or navigation behavior. Targets reverse-engineering workflows where analysts want a cleaner, more readable IDA interface during long static-analysis sessions.

## Links

- Repo: https://github.com/PoP-Lin/IDAPro-MuiLs

## Related

[[overviews/reverse-engineering]] · [[ida-themer]] · [[ida-dark-plus]] · [[ida-nord-theme]] · [[long-night]] · [[idaskins]] · [[dp701]]
