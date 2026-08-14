---
title: DLL-Hijack-ExportDumper
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__DLL-Hijack-ExportDumper.md
updated: 2026-08-14
confidence: medium
---

# DLL-Hijack-ExportDumper

PE export-table dumper that generates proxy-DLL source code for DLL hijacking: automates export forwarding stubs so researchers can sideload malicious code via legitimate DLL search-order paths without hand-writing every forwarded export. (source: wiki/sources/descriptions/gmh5225__DLL-Hijack-ExportDumper.md)

Sits in the Cheat → DLL Hijack lane beside catalog DBs [[windows-dll-hijacking]] and [[hijacklibs]], discovery tooling [[dllirant]], and workflow automation [[impulsive-dll-hijack]] (not a game-specific cheat); complements PE triage viewers when building proxy DLLs for load-path / sideload research.

## Links

- Repo: https://github.com/gmh5225/DLL-Hijack-ExportDumper

## Related

[[windows-dll-hijacking]] · [[hijacklibs]] · [[dllirant]] · [[impulsive-dll-hijack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
