---
title: val-exception-handler
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/lil-skies__val-exception-handler.md
updated: 2026-08-01
confidence: medium
---

# val-exception-handler

Proof-of-concept exploiting Valorant / [[vanguard]] exception handling: analyzes how Vanguard processes hardware exceptions and vectored exception handlers, documenting potential weaknesses in the anti-cheat's exception dispatch flow that could be leveraged for code execution or detection evasion. README tag: `[ZwRaiseException Dump]`. Aimed at anti-cheat researchers studying Vanguard's kernel-level protection and exception handling architecture. (source: wiki/sources/descriptions/lil-skies__val-exception-handler.md)

Sits beside VEH-focused AC research tooling such as [[veh-dumper]] and [[veh]], but scoped to Vanguard's kernel exception-dispatch path rather than generic VEH chain dumping.

## Links

- Repo: https://github.com/lil-skies/val-exception-handler

## Related

[[vanguard]] · [[veh]] · [[veh-dumper]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
