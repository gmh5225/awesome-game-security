---
title: custom-VEH
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__custom-VEH.md
updated: 2026-08-09
confidence: medium
---

# custom-VEH

Library for registering **custom Vectored Exception Handlers (VEH)** by hooking ntdll's internal `RtlpCallVectoredHandlers`. Handlers registered through this path are faster than standard `AddVectoredExceptionHandler` registrations and run **before** vanilla VEH entries—useful when studying or building Windows Ring3 exception-dispatch / callback ordering in anti-cheat and defensive security research. (source: wiki/sources/descriptions/gmh5225__custom-VEH.md)

Complements standard VEH tooling such as [[veh]] (software debugger without the Debug API), VEH-chain dumpers such as [[veh-dumper]], and page-protection / VEH interception samples such as [[veh-printf-hook]] and [[veh-hide-memory]].

## Links

- Repo: https://github.com/gmh5225/custom-VEH (README: Register VEH by hooking RtlpCallVectoredHandlers)

## Related

[[veh]] · [[veh-dumper]] · [[veh-printf-hook]] · [[veh-hide-memory]] · [[cpp-veh-dbi]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
