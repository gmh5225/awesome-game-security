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
  - wiki/sources/descriptions/m417z__Multiline-Ultimate-Assembler.md
  - wiki/sources/descriptions/legendabrn__AutoAttach.md
  - wiki/sources/descriptions/jdavidberger__chaiScriptPlugin.md
  - wiki/sources/descriptions/horsicq__x64dbg-Plugin-Manager.md
  - wiki/sources/descriptions/horsicq__stringsx64dbg.md
updated: 2026-08-05
confidence: medium
---

# x64dbg

Open-source Windows debugger for x86/x64 with a large feature set and a comprehensive plugin system for extensions. Widely used by game-security researchers and reverse engineers studying cheat / debugging workflows. (source: wiki/sources/descriptions/x64dbg__x64dbg.md)

Core user-mode debugger—not a kernel debugger or static disassembler; plugin ecosystem bridges to tools such as [[x64dbgbinja]], [[symbridge]], plugin lifecycle management via [[x64dbg-plugin-manager]] (source: wiki/sources/descriptions/horsicq__x64dbg-Plugin-Manager.md), dedicated string search/browse via [[stringsx64dbg]] (source: wiki/sources/descriptions/horsicq__stringsx64dbg.md), ChaiScript scripting via [[chaiscript-plugin]] (source: wiki/sources/descriptions/jdavidberger__chaiScriptPlugin.md), process auto-attach via [[auto-attach]] (source: wiki/sources/descriptions/legendabrn__AutoAttach.md), collaborative breakpoint management via [[slothbp]] (source: wiki/sources/descriptions/x64dbg__SlothBP.md), managed .NET/C# plugins via [[dotx64dbg]] (source: wiki/sources/descriptions/x64dbg__DotX64Dbg.md), OOP class documentation via [[classroom]] (source: wiki/sources/descriptions/x64dbg__Classroom.md), live DLL export-table monitoring via [[expomon]] (source: wiki/sources/descriptions/milcert__ExpoMon.md), memory write/access tracing via [[xfindout]] (source: wiki/sources/descriptions/morsisko__xFindOut.md), offline `.trace64` parse/filter via [[x64dbg-trace-reader]] (source: wiki/sources/descriptions/mibho__x64dbgTraceReader.md), XFG call-signature marking via [[x64dbg-xfg-marker]] (source: wiki/sources/descriptions/m417z__x64dbg-xfg-marker.md), multiline assemble/disassemble via [[multiline-ultimate-assembler]] (source: wiki/sources/descriptions/m417z__Multiline-Ultimate-Assembler.md), sequential DLL load-order debugging via [[disable-parallel-loader]] (source: wiki/sources/descriptions/mrexodia__DisableParallelLoader.md), live static-library function ID via [[idenlibx]] (source: wiki/sources/descriptions/secrary__idenLibX.md), and Windows type parsing via [[manytypes]] (source: wiki/sources/descriptions/notpidgey__ManyTypes.md).

## Links

- Repo: https://github.com/x64dbg/x64dbg

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbgbinja]] · [[x64dbg-plugin-manager]] · [[stringsx64dbg]] · [[chaiscript-plugin]] · [[auto-attach]] · [[slothbp]] · [[dotx64dbg]] · [[classroom]] · [[expomon]] · [[xfindout]] · [[x64dbg-trace-reader]] · [[x64dbg-xfg-marker]] · [[multiline-ultimate-assembler]] · [[disable-parallel-loader]] · [[idenlibx]] · [[manytypes]] · [[symbridge]] · [[quickasm]]
