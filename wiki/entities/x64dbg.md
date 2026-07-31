---
title: x64dbg
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/x64dbg__x64dbg.md
  - wiki/sources/descriptions/x64dbg__SlothBP.md
  - wiki/sources/descriptions/x64dbg__DotX64Dbg.md
  - wiki/sources/descriptions/x64dbg__Classroom.md
  - wiki/sources/descriptions/secrary__idenLibX.md
  - wiki/sources/descriptions/notpidgey__ManyTypes.md
  - wiki/sources/descriptions/mrexodia__DisableParallelLoader.md
  - wiki/sources/descriptions/morsisko__xFindOut.md
  - wiki/sources/descriptions/milcert__ExpoMon.md
  - wiki/sources/descriptions/mibho__x64dbgTraceReader.md
  - wiki/sources/descriptions/m417z__x64dbg-xfg-marker.md
updated: 2026-07-31
confidence: medium
---

# x64dbg

Open-source Windows debugger for x86/x64 with a large feature set and a comprehensive plugin system for extensions. Widely used by game-security researchers and reverse engineers studying cheat / debugging workflows. (source: wiki/sources/descriptions/x64dbg__x64dbg.md)

Core user-mode debugger—not a kernel debugger or static disassembler; plugin ecosystem bridges to tools such as [[x64dbgbinja]], [[symbridge]], collaborative breakpoint management via [[slothbp]] (source: wiki/sources/descriptions/x64dbg__SlothBP.md), managed .NET/C# plugins via [[dotx64dbg]] (source: wiki/sources/descriptions/x64dbg__DotX64Dbg.md), OOP class documentation via [[classroom]] (source: wiki/sources/descriptions/x64dbg__Classroom.md), live DLL export-table monitoring via [[expomon]] (source: wiki/sources/descriptions/milcert__ExpoMon.md), memory write/access tracing via [[xfindout]] (source: wiki/sources/descriptions/morsisko__xFindOut.md), offline `.trace64` parse/filter via [[x64dbg-trace-reader]] (source: wiki/sources/descriptions/mibho__x64dbgTraceReader.md), XFG call-signature marking via [[x64dbg-xfg-marker]] (source: wiki/sources/descriptions/m417z__x64dbg-xfg-marker.md), sequential DLL load-order debugging via [[disable-parallel-loader]] (source: wiki/sources/descriptions/mrexodia__DisableParallelLoader.md), live static-library function ID via [[idenlibx]] (source: wiki/sources/descriptions/secrary__idenLibX.md), and Windows type parsing via [[manytypes]] (source: wiki/sources/descriptions/notpidgey__ManyTypes.md).

## Links

- Repo: https://github.com/x64dbg/x64dbg

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbgbinja]] · [[slothbp]] · [[dotx64dbg]] · [[classroom]] · [[expomon]] · [[xfindout]] · [[x64dbg-trace-reader]] · [[x64dbg-xfg-marker]] · [[disable-parallel-loader]] · [[idenlibx]] · [[manytypes]] · [[symbridge]] · [[quickasm]]
