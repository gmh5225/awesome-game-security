---
title: procmap
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/joaomlneto__procmap.md
updated: 2026-08-03
confidence: medium
---

# procmap

C++14 library that parses Linux `/proc/pid/maps` into structured `MemorySegment` objects exposing address ranges, permission flags, file offsets, and backing file paths. Provides a programmatic interface for live process memory-layout analysis useful in memory forensics and game-security tooling on Linux (and Android hosts exposing the same procfs layout). (source: wiki/sources/descriptions/joaomlneto__procmap.md)

## Links

- Repo: https://github.com/joaomlneto/procmap

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[libmem]] · [[memdumper]] · [[pince]] · [[pwatch]]
