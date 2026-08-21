---
title: CBS
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Reodus__CBS.md
updated: 2026-08-21
confidence: medium
---

# CBS

**CBS** (Reodus) is an **IDA Pro plugin** that sets, enables, disables, or removes breakpoints based on **instruction patterns**. Implemented in Python with regular expressions, it scans disassembly lines and applies breakpoint actions across functions. A **PyQt** interface lets reverse engineers manage opcode patterns interactively. The tool targets analysts who need fast, repeatable breakpoint automation during binary analysis—useful when triaging large game or protected binaries before live debugging. (source: wiki/sources/descriptions/Reodus__CBS.md)

Complements static-to-debug helpers such as [[copy-rva]] (RVA clipboard for WinDbg) and CE/IDA bridges such as [[ce-tracer-ida]] when preparing IDA sessions for dynamic follow-up.

## Links

- Repo: https://github.com/Reodus/CBS

## Related

[[copy-rva]] · [[ce-tracer-ida]] · [[lazyida]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
