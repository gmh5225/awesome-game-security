---
title: Reverse Engineering
kind: overview
topics: [reverse-engineering]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zx0CF1__shredder-rs.md
  - wiki/sources/descriptions/zodiacon__TotalPE2.md
  - wiki/sources/descriptions/zodiacon__QuickAsm.md
  - wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md
  - wiki/sources/descriptions/zhuzhu-Top__deobf.md
  - wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md
  - wiki/sources/descriptions/zeroxjf__lightsaber.md
  - wiki/sources/descriptions/zengfr__XrefsExt.md
  - wiki/sources/descriptions/zboralski__unflutter.md
  - wiki/sources/descriptions/za233__IDADeflat.md
  - wiki/sources/descriptions/z1ko__mutaben.md
updated: 2026-07-17
confidence: high
---

# Reverse Engineering

Workflows for protected game clients and anti-cheat components across user mode, kernel, and hypervisor-aware environments: debug/disassemble, DBI, deobfuscation, dump analysis, and IOCTL/callback mapping. (source: wiki/sources/skills/reverse-engineering.md)

## Key sub-areas

- **Tools:** IDA/Ghidra/Binary Ninja, x64dbg/WinDbg/HyperDbg, Cheat Engine, dnSpy, [[frida]]; PE triage viewers such as [[totalpe2]] (headers/imports/exports/.NET metadata) (source: wiki/sources/descriptions/zodiacon__TotalPE2.md); quick x86/x64 assemble-and-run via [[quickasm]] (Keystone) (source: wiki/sources/descriptions/zodiacon__QuickAsm.md); IDA xref-extension plugin [[xrefsext]] (source: wiki/sources/descriptions/zengfr__XrefsExt.md); Android apktool via [[apktool-mcp-server]] (MCP suite) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md); Android HTTP/HTTPS capture + NL query via [[android-proxy-mcp]] (mitmdump/SQLite) (source: wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md)
- **DBI:** Frida, DynamoRIO, Pin; trap-and-emulate CFT; WHP user-mode hypervisor tracing
- **Obfuscation:** MBA, OLLVM CFF, opaque predicates, VMProtect/Themida virtualization; MBA sample generation via [[mutaben]] (Python MBA generator) (source: wiki/sources/descriptions/z1ko__mutaben.md); [[shredder-rs]] for x86_64 instruction-level polymorphic shredding vs static analysis (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md); OLLVM fix / plugin-hook work on `libtprt.so` via [[deobf]] (source: wiki/sources/descriptions/zhuzhu-Top__deobf.md); IDA CFF deflattening via [[idadeflat]] (angr symbolic exec → recover CFG / patch) (source: wiki/sources/descriptions/za233__IDADeflat.md)
- **Game engines:** [[il2cpp]] dumps, Unreal SDK generators, native PE/pattern workflows; Flutter/Dart AOT snapshot static analysis via [[unflutter]] (source: wiki/sources/descriptions/zboralski__unflutter.md)
- **Anti-analysis:** ScyllaHide/TitanHide/HyperHide vs IsDebuggerPresent/Kd* / timing checks
- **Mobile / iOS:** userland exploit-chain study via [[lightsaber]] (iOS 18.4–18.6.2 JS injection into SpringBoard and other processes) (source: wiki/sources/descriptions/zeroxjf__lightsaber.md)

## Related concepts

[[il2cpp]] · [[frida]] · [[unflutter]] · [[kernel-callbacks]] · [[patchguard]] · [[mutaben]] · [[shredder-rs]] · [[deobf]] · [[idadeflat]] · [[totalpe2]] · [[quickasm]] · [[xrefsext]] · [[apktool-mcp-server]] · [[android-proxy-mcp]] · [[lightsaber]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/mobile-security]]

## README map

Cheat Debugging/RE Tools/DBI/Fix VMP|Themida|OLLVM; Anti Cheat Anti Debugging/Disassembly/Dump Fix; large IDA/BN/Ghidra/x64dbg plugin ecosystems. (source: wiki/sources/README-categories.md)
