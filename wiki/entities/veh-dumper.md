---
title: veh-dumper
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/xxFURYWOLFxx__veh-dumper.md
updated: 2026-07-17
confidence: medium
---

# veh-dumper

Injectable x64 DLL that enumerates registered VectoredExceptionHandler and VectoredContinueHandler entries in a target process and dumps each handler as a standalone synthetic PE64 that IDA can open. Per handler it extracts function bytes (`RtlLookupFunctionEntry` unwind info or heuristic scan), RIP-relative data, depth-capped direct callees, and resolved indirect-call IAT slots; Windows system-module callees become named imports instead of dumped code. List walking uses a foothold VEH plus dynamic `RtlDecodePointer` offset discovery—aimed at RE of VEH-based protection / anti-cheat logic. (source: wiki/sources/descriptions/xxFURYWOLFxx__veh-dumper.md)

## Links

- Repo: https://github.com/xxFURYWOLFxx/veh-dumper

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
