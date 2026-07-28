---
title: ReClass.NET-DriverReader
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/niemand-sec__ReClass.NET-DriverReader.md
updated: 2026-07-28
confidence: medium
---

# ReClass.NET-DriverReader

ReClass.NET plugin that reads target process memory through a kernel driver instead of user-mode `ReadProcessMemory`. A C#/C++ bridge lets ReClass.NET reconstruct structures on processes where anti-cheat blocks standard RPM, for game-security memory-layout research. (source: wiki/sources/descriptions/niemand-sec__ReClass.NET-DriverReader.md)

## Links

- Repo: https://github.com/niemand-sec/ReClass.NET-DriverReader

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[umpmlib]] · [[eupmaccess]] · [[ntmemory]] · [[cheat-driver]]
