---
title: Reverse Engineering
kind: overview
topics: [reverse-engineering]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/README-categories.md
updated: 2026-07-16
confidence: high
---

# Reverse Engineering

Workflows for protected game clients and anti-cheat components across user mode, kernel, and hypervisor-aware environments: debug/disassemble, DBI, deobfuscation, dump analysis, and IOCTL/callback mapping. (source: wiki/sources/skills/reverse-engineering.md)

## Key sub-areas

- **Tools:** IDA/Ghidra/Binary Ninja, x64dbg/WinDbg/HyperDbg, Cheat Engine, dnSpy, [[frida]]
- **DBI:** Frida, DynamoRIO, Pin; trap-and-emulate CFT; WHP user-mode hypervisor tracing
- **Obfuscation:** MBA, OLLVM CFF, opaque predicates, VMProtect/Themida virtualization
- **Game engines:** [[il2cpp]] dumps, Unreal SDK generators, native PE/pattern workflows
- **Anti-analysis:** ScyllaHide/TitanHide/HyperHide vs IsDebuggerPresent/Kd* / timing checks

## Related concepts

[[il2cpp]] · [[frida]] · [[kernel-callbacks]] · [[patchguard]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]

## README map

Cheat Debugging/RE Tools/DBI/Fix VMP|Themida|OLLVM; Anti Cheat Anti Debugging/Disassembly/Dump Fix; large IDA/BN/Ghidra/x64dbg plugin ecosystems. (source: wiki/sources/README-categories.md)
