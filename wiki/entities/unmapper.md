---
title: unmapper
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/t3ssellate__unmapper.md
updated: 2026-07-21
confidence: medium
---

# unmapper

Automatic PE dump-fix tool: rewrites headers on dumped PE files so decompilers and other static-analysis tools can load them without errors. Aimed at anti-cheat engineers and defensive researchers in the Dump Fix lane. (source: wiki/sources/descriptions/t3ssellate__unmapper.md)

Useful after memory dumps of AC / game modules when raw dumps fail IDA/Ghidra import—not a packer or live dumper.

## Links

- Repo: https://github.com/t3ssellate/unmapper

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[totalpe2]] · [[veh-dumper]] · [[vac3-dumper]]
