---
title: Detection-CheatEngine
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Detection-CheatEngine.md
updated: 2026-08-14
confidence: medium
---

# Detection-CheatEngine

Small **user-mode Cheat Engine artifact detector** built on **`ReadDirectoryChangesW`** directory monitoring. Watches the user profile and `C:\` for file create, rename, and write events, then flags filenames containing markers such as **`ADDRESSES.FIRST`** and **`MEMORY.FIRST`** defined in `CEInfo.h`. Does not scan memory or enumerate processes — a lightweight **filesystem heuristic** focused on CE table and artifact creation behavior, extensible with additional detection strings and directory watches. README category `[CE]`. (source: wiki/sources/descriptions/gmh5225__Detection-CheatEngine.md)

Mainly useful for anti-cheat engineers studying simple user-mode CE detection strategies. Complements multi-vector process/window/driver probes such as [[cedetector]] and the `ReadDirectoryChangesW` wrapper patterns in [[readdirectorychanges]].

## Links

- Repo: https://github.com/gmh5225/Detection-CheatEngine

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cedetector]] · [[readdirectorychanges]]
