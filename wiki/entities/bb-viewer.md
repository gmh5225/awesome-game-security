---
title: bb-viewer
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/cristeigabriela__bb-viewer.md
updated: 2026-08-16
confidence: medium
---

# bb-viewer

**bb-viewer** is a web-based viewer for Windows kernel structure datasets produced by [[bb]] (Benowin Blanc). It browses **ntoskrnl**, **hal**, and related Windows SDK/PHNT output: functions, types, typedefs, constants, IRQL annotations, and type-relationship graphs, with search, filtering, and dataset switching across user/kernel modes and **amd64** / **x86** / **arm** / **arm64** targets. (source: wiki/sources/descriptions/cristeigabriela__bb-viewer.md)

Complements [[bb]]’s CLI/TUI and JSON export with an interactive explorer for cheat / Windows kernel explorer and RE workflows that need quick struct/type navigation without WinDbg attach.

## Links

- Repo: https://github.com/cristeigabriela/bb-viewer

## Related

[[bb]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[ntoskrnlwalker]] · [[ntkernelwalkerlib]] · [[windbg-scripts]] · [[systeminformer]]
