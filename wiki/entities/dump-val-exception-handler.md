---
title: dump-val-exception-handler
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Dump-val-exception-handler.md
updated: 2026-08-13
confidence: medium
---

# dump-val-exception-handler

**Valorant exception-handler dumper** (gmh5225). Dumps Valorant's exception handler registration and **vectored exception handler (VEH) chains**, extracting and logging the anti-cheat's custom exception-handling setup for reverse engineering [[vanguard]] runtime protection mechanisms. README tag: `[RtlpCallVectoredHandlers Dump]`. Aimed at anti-cheat researchers studying Vanguard's user-mode exception dispatch and VEH registration under a live Valorant process. (source: wiki/sources/descriptions/gmh5225__Dump-val-exception-handler.md)

Sits beside [[val-exception-handler]] in the Vanguard exception-dispatch RE lane, but as **registration/chain enumeration** via `RtlpCallVectoredHandlers` rather than a `ZwRaiseException`-focused PoC. Complements generic VEH tooling such as [[veh-dumper]] and [[custom-veh]] for mapping handler order under [[vanguard]].

## Links

- Repo: https://github.com/gmh5225/Dump-val-exception-handler

## Related

[[vanguard]] · [[val-exception-handler]] · [[veh-dumper]] · [[custom-veh]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
