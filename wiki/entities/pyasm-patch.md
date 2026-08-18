---
title: PyAsmPatch
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/axhlzy__PyAsmPatch.md
updated: 2026-08-18
confidence: medium
---

# PyAsmPatch

**PyAsmPatch** (axhlzy) is a Python-based **inline hooking** tool for **ARM ELF** binaries, targeting Unity IL2CPP shared libraries (`libil2cpp.so`). It uses **LIEF** for ELF manipulation, **Keystone** for assembly, and **Capstone** for disassembly to merge code sections, patch GOT tables, and inject inline hooks with register inspection and LDR instruction fixup. The tool supports hooking InitArray functions, adding breakpoints for IDA debugging, and calling wrapped Android native functions such as `android_log_print` and `mprotect`. It is mainly useful for mobile game security researchers performing static binary patching and inline hook injection on Unity IL2CPP games. (source: wiki/sources/descriptions/axhlzy__PyAsmPatch.md)

Static/offline `.so` patching lane — complements runtime inject/hook stacks such as [[frida]], [[adbi]], and [[dobby]].

## Links

- Repo: https://github.com/axhlzy/PyAsmPatch

## Related

[[il2cpp]] · [[farm64]] · [[adbi]] · [[frida]] · [[il2cpp-hook-scripts]] · [[il2cpp-hookscripts]] · [[fakerandroid]] · [[overviews/mobile-security]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
