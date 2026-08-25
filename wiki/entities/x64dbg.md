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
  - wiki/sources/descriptions/horsicq__nfdx64dbg.md
  - wiki/sources/descriptions/gmh5225__X64DBG-ViewDllNotification.md
  - wiki/sources/descriptions/gmh5225__X64DBG-MapLdr.md
  - wiki/sources/descriptions/dariushoule__x64dbg-rippy.md
  - wiki/sources/descriptions/dariushoule__x64dbg-automate-pyclient.md
  - wiki/sources/descriptions/bromoket__x64dbg_mcp.md
  - wiki/sources/descriptions/codecat__ClawSearch.md
  - wiki/sources/descriptions/adde88__WoWDumpFix.md
  - wiki/sources/descriptions/ZehMatt__x64dbgPlaytime.md
  - wiki/sources/descriptions/ElvisBlue__x64dbgpython.md
  - wiki/sources/descriptions/VenTaz__Themidie.md
  - wiki/sources/descriptions/Kwansy98__ApiBreakpoint.md
  - wiki/sources/descriptions/Kwansy98__x64dbgCallFinder.md
updated: 2026-08-25
confidence: medium
---

# x64dbg

Open-source Windows debugger for x86/x64 with a large feature set and a comprehensive plugin system for extensions. Widely used by game-security researchers and reverse engineers studying cheat / debugging workflows. (source: wiki/sources/descriptions/x64dbg__x64dbg.md)

Core user-mode debugger—not a kernel debugger or static disassembler; plugin ecosystem bridges to tools such as [[x64dbgbinja]], [[symbridge]], AI-assisted interactive debugging via [[x64dbg-rippy]] (WebView2 in-debugger chat; LLM tool-use for memory/disasm/breakpoints/step; Anthropic/OpenAI APIs) (source: wiki/sources/descriptions/dariushoule__x64dbg-rippy.md), external Python Automate RPC + optional MCP server via [[x64dbg-automate-pyclient]] (ZeroMQ/msgpack; breakpoints/memory/registers/disasm/session/GUI; scripted and agent-assisted workflows) (source: wiki/sources/descriptions/dariushoule__x64dbg-automate-pyclient.md), dedicated TypeScript MCP server with native REST plugin via [[x64dbg-mcp]] (23 mega-tools / 151 REST endpoints; stepping/breakpoints/memory/disasm/tracing/anti-debug bypass/CFA/PE dump; Zod-typed TypeScript + `.dp64`/`.dp32` bridge; Claude/Cursor/Windsurf MCP clients) (source: wiki/sources/descriptions/bromoket__x64dbg_mcp.md), plugin lifecycle management via [[x64dbg-plugin-manager]] (source: wiki/sources/descriptions/horsicq__x64dbg-Plugin-Manager.md), dedicated string search/browse via [[stringsx64dbg]] (source: wiki/sources/descriptions/horsicq__stringsx64dbg.md), in-debugger compiler/packer/protector static ID via [[nfdx64dbg]] (source: wiki/sources/descriptions/horsicq__nfdx64dbg.md), ChaiScript scripting via [[chaiscript-plugin]] (source: wiki/sources/descriptions/jdavidberger__chaiScriptPlugin.md), Lua scripting via [[x64dbg-playtime]] (embedded runtime; memory/registers/breakpoints/labels/modules/assembler; autorun scripts; ZehMatt) (source: wiki/sources/descriptions/ZehMatt__x64dbgPlaytime.md), Python 3 scripting via [[x64dbgpython]] (C++ plugin; Python wrappers mirroring plugin SDK APIs; memory/assembly/module/GUI example scripts; ElvisBlue; Running python3 script) (source: wiki/sources/descriptions/ElvisBlue__x64dbgpython.md), process auto-attach via [[auto-attach]] (source: wiki/sources/descriptions/legendabrn__AutoAttach.md), collaborative breakpoint management via [[slothbp]] (source: wiki/sources/descriptions/x64dbg__SlothBP.md), GUI API breakpoint setup via [[api-breakpoint]] (C++; visual configure/manage workflow; x86/x64; Kwansy98) (source: wiki/sources/descriptions/Kwansy98__ApiBreakpoint.md), managed .NET/C# plugins via [[dotx64dbg]] (source: wiki/sources/descriptions/x64dbg__DotX64Dbg.md), OOP class documentation via [[classroom]] (source: wiki/sources/descriptions/x64dbg__Classroom.md), live DLL export-table monitoring via [[expomon]] (source: wiki/sources/descriptions/milcert__ExpoMon.md), DLL load-notification callback inspection via [[x64dbg-view-dll-notification]] (source: wiki/sources/descriptions/gmh5225__X64DBG-ViewDllNotification.md), memory write/access tracing via [[xfindout]] (source: wiki/sources/descriptions/morsisko__xFindOut.md), runtime call-frequency profiling via [[x64dbg-call-finder]] (conditional breakpoints + per-function counters; filter by call count after in-app actions; UI/gameplay handler discovery; Kwansy98) (source: wiki/sources/descriptions/Kwansy98__x64dbgCallFinder.md), Cheat Engine–style memory value scanning via [[clawsearch]] (source: wiki/sources/descriptions/codecat__ClawSearch.md), Blizzard WoW anti-dump / attach helper via [[wowdumpfix]] (source: wiki/sources/descriptions/adde88__WoWDumpFix.md), Themida anti-analysis bypass via [[themidie]] (C++ MinHook; anti-debug/anti-VM/monitoring neutralization on x64 attach; attach-and-debug vs full unpack; VenTaz) (source: wiki/sources/descriptions/VenTaz__Themidie.md), offline `.trace64` parse/filter via [[x64dbg-trace-reader]] (source: wiki/sources/descriptions/mibho__x64dbgTraceReader.md), XFG call-signature marking via [[x64dbg-xfg-marker]] (source: wiki/sources/descriptions/m417z__x64dbg-xfg-marker.md), multiline assemble/disassemble via [[multiline-ultimate-assembler]] (source: wiki/sources/descriptions/m417z__Multiline-Ultimate-Assembler.md), sequential DLL load-order debugging via [[disable-parallel-loader]] (source: wiki/sources/descriptions/mrexodia__DisableParallelLoader.md), live static-library function ID via [[idenlibx]] (source: wiki/sources/descriptions/secrary__idenLibX.md), linker/IDA `.MAP` symbol import via [[x64dbg-mapldr]] (source: wiki/sources/descriptions/gmh5225__X64DBG-MapLdr.md), and Windows type parsing via [[manytypes]] (source: wiki/sources/descriptions/notpidgey__ManyTypes.md).

## Links

- Repo: https://github.com/x64dbg/x64dbg

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg-rippy]] · [[x64dbg-automate-pyclient]] · [[x64dbg-mcp]] · [[x64dbgbinja]] · [[x64dbg-plugin-manager]] · [[stringsx64dbg]] · [[nfdx64dbg]] · [[chaiscript-plugin]] · [[x64dbg-playtime]] · [[x64dbgpython]] · [[auto-attach]] · [[slothbp]] · [[api-breakpoint]] · [[dotx64dbg]] · [[classroom]] · [[expomon]] · [[x64dbg-view-dll-notification]] · [[x64dbg-mapldr]] · [[xfindout]] · [[x64dbg-call-finder]] · [[clawsearch]] · [[wowdumpfix]] · [[themidie]] · [[x64dbg-trace-reader]] · [[x64dbg-xfg-marker]] · [[multiline-ultimate-assembler]] · [[disable-parallel-loader]] · [[idenlibx]] · [[manytypes]] · [[symbridge]] · [[quickasm]]
