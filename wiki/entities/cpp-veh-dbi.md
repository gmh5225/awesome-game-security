---
title: cpp-veh-dbi
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/revsic__cpp-veh-dbi.md
updated: 2026-07-24
confidence: medium
---

# cpp-veh-dbi

C++ **VEH-based dynamic binary instrumentation** sample in the Cheat → DBI lane. Uses Vectored Exception Handling as the instrumentation spine (with PowerShell support scripts) for studying lightweight, exception-driven DBI on Windows rather than full frameworks such as Pin or DynamoRIO. Aimed at game-security and reverse-engineering researchers working offensive DBI / trap-style instrumentation techniques. (source: wiki/sources/descriptions/revsic__cpp-veh-dbi.md)

Pairs with related VEH tooling such as [[veh]] (software debugger without the Debug API) and [[veh-dumper]] (VEH/VCH chain dump to IDA-ready PE64), and with broader DBI harnessing such as [[smallworld]].

## Links

- Repo: https://github.com/revsic/cpp-veh-dbi

## Related

[[veh]] · [[veh-dumper]] · [[smallworld]] · [[frida]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
