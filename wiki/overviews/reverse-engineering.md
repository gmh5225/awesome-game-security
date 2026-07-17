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
updated: 2026-07-17
confidence: high
---

# Reverse Engineering

Workflows for protected game clients and anti-cheat components across user mode, kernel, and hypervisor-aware environments: debug/disassemble, DBI, deobfuscation, dump analysis, and IOCTL/callback mapping. (source: wiki/sources/skills/reverse-engineering.md)

## Key sub-areas

- **Tools:** IDA/Ghidra/Binary Ninja, x64dbg/WinDbg/HyperDbg, Cheat Engine, dnSpy, [[frida]]; PE triage viewers such as [[totalpe2]] (headers/imports/exports/.NET metadata) (source: wiki/sources/descriptions/zodiacon__TotalPE2.md); quick x86/x64 assemble-and-run via [[quickasm]] (Keystone) (source: wiki/sources/descriptions/zodiacon__QuickAsm.md); Android apktool via [[apktool-mcp-server]] (MCP suite) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md)
- **DBI:** Frida, DynamoRIO, Pin; trap-and-emulate CFT; WHP user-mode hypervisor tracing
- **Obfuscation:** MBA, OLLVM CFF, opaque predicates, VMProtect/Themida virtualization; [[shredder-rs]] for x86_64 instruction-level polymorphic shredding vs static analysis (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md)
- **Game engines:** [[il2cpp]] dumps, Unreal SDK generators, native PE/pattern workflows
- **Anti-analysis:** ScyllaHide/TitanHide/HyperHide vs IsDebuggerPresent/Kd* / timing checks

## Related concepts

[[il2cpp]] · [[frida]] · [[kernel-callbacks]] · [[patchguard]] · [[shredder-rs]] · [[totalpe2]] · [[quickasm]] · [[apktool-mcp-server]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]

## README map

Cheat Debugging/RE Tools/DBI/Fix VMP|Themida|OLLVM; Anti Cheat Anti Debugging/Disassembly/Dump Fix; large IDA/BN/Ghidra/x64dbg plugin ecosystems. (source: wiki/sources/README-categories.md)
