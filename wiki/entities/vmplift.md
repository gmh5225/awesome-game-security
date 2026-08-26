---
title: VMPLift
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/sexyiam__VMPLift.md
  - wiki/sources/README-categories.md
updated: 2026-08-26
confidence: medium
---

# VMPLift

**C++** emulation-first tool that walks and lifts virtualized handlers from unpacked **VMProtect 3.8–3.10+** x64 binaries. Traces VIP bytecode, resolves indirect dispatch, and recovers rolling-key state that breaks older static opcode-table devirtualizers. Pipeline scans VM entry points, classifies handler blocks, lifts to intermediate representation, and can emit LLVM IR, pseudo-C, VIP traces, and devirtualized native code when handlers reduce to simple functions. Targets reverse engineers analyzing VMProtect-protected game clients and other executables with newer virtualization features. (source: wiki/sources/descriptions/sexyiam__VMPLift.md)

Listed under Cheat **Fix VMP** beside static VTIL lifts such as [[novmp]] and trace/symbolic paths such as [[titan]] and [[rumba]].

## Links

- Repo: https://github.com/sexyiam/VMPLift

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[novmp]] · [[novmpy]] · [[titan]] · [[vmprotect-devirtualization]] · [[vmprotect]]
