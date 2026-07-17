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
  - wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md
  - wiki/sources/descriptions/ytk2128__pe32-password.md
  - wiki/sources/descriptions/yoavst__ida-ios-helper.md
  - wiki/sources/descriptions/ykus4__kagura.md
  - wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md
  - wiki/sources/descriptions/yaxinsn__vermagic.md
  - wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md
updated: 2026-07-17
confidence: high
---



# Reverse Engineering

Workflows for protected game clients and anti-cheat components across user mode, kernel, and hypervisor-aware environments: debug/disassemble, DBI, deobfuscation, dump analysis, and IOCTL/callback mapping. (source: wiki/sources/skills/reverse-engineering.md)

## Key sub-areas

- **Tools:** IDA/Ghidra/Binary Ninja, x64dbg/WinDbg/HyperDbg, Cheat Engine, dnSpy, [[frida]]; JS WinDbg kernel scripts such as [[windbg-scripts]] (Cheat → WinDbg Plugins) (source: wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md); PE triage viewers such as [[totalpe2]] (headers/imports/exports/.NET metadata) (source: wiki/sources/descriptions/zodiacon__TotalPE2.md); quick x86/x64 assemble-and-run via [[quickasm]] (Keystone) (source: wiki/sources/descriptions/zodiacon__QuickAsm.md); IDA xref-extension plugin [[xrefsext]] (source: wiki/sources/descriptions/zengfr__XrefsExt.md); IDA JM Xorstr decrypt attempts via [[ida-jm-xorstr-decrypt-plugin]] (x64) (source: wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md); iOS IDA helper [[ida-ios-helper]] (vtable symbols required) (source: wiki/sources/descriptions/yoavst__ida-ios-helper.md); Android apktool via [[apktool-mcp-server]] (MCP suite) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md); Android HTTP/HTTPS capture + NL query via [[android-proxy-mcp]] (mitmdump/SQLite) (source: wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md)
 (headers/imports/exports/.NET metadata) (source: wiki/sources/descriptions/zodiacon__TotalPE2.md); quick x86/x64 assemble-and-run via [[quickasm]] (Keystone) (source: wiki/sources/descriptions/zodiacon__QuickAsm.md); IDA xref-extension plugin [[xrefsext]] (source: wiki/sources/descriptions/zengfr__XrefsExt.md); IDA JM Xorstr decrypt attempts via [[ida-jm-xorstr-decrypt-plugin]] (x64) (source: wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md); iOS IDA helper [[ida-ios-helper]] (vtable symbols required) (source: wiki/sources/descriptions/yoavst__ida-ios-helper.md); Android apktool via [[apktool-mcp-server]] (MCP suite) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md); Android HTTP/HTTPS capture + NL query via [[android-proxy-mcp]] (mitmdump/SQLite) (source: wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md)
- **DBI:** Frida, DynamoRIO, Pin; trap-and-emulate CFT; WHP user-mode hypervisor tracing
- **Obfuscation:** MBA, OLLVM CFF, opaque predicates, VMProtect/Themida virtualization; MBA sample generation via [[mutaben]] (Python MBA generator) (source: wiki/sources/descriptions/z1ko__mutaben.md); [[shredder-rs]] for x86_64 instruction-level polymorphic shredding vs static analysis (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md); OLLVM fix / plugin-hook work on `libtprt.so` via [[deobf]] (source: wiki/sources/descriptions/zhuzhu-Top__deobf.md); IDA CFF deflattening via [[idadeflat]] (angr symbolic exec → recover CFG / patch) (source: wiki/sources/descriptions/za233__IDADeflat.md); opaque-predicate detection via [[opaque-predicates-detective]] (invariant-expression / BB-local damage model; Binary Ninja plugin lane) (source: wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md); PE32 password packing via [[pe32-password]] (Binary Packer) (source: wiki/sources/descriptions/ytk2128__pe32-password.md); LLVM pass-plugin obfuscation/anti-tamper via [[kagura]] (CFF/bogus CFG, string/data encryption, anti-debug runtime; mobile/desktop/Wasm) (source: wiki/sources/descriptions/ykus4__kagura.md)
- **Game engines:** [[il2cpp]] dumps, Unreal SDK generators, native PE/pattern workflows; Flutter/Dart AOT snapshot static analysis via [[unflutter]] (source: wiki/sources/descriptions/zboralski__unflutter.md)
- **Anti-analysis:** ScyllaHide/TitanHide/HyperHide vs IsDebuggerPresent/Kd* / timing checks
- **Linux LKM metadata:** tools such as [[vermagic]] rewrite vermagic / CRC fields so a module can load across mismatched kernel builds (cheat / RE tools lane). (source: wiki/sources/descriptions/yaxinsn__vermagic.md)
- **Mobile / iOS:** userland exploit-chain study via [[lightsaber]] (iOS 18.4–18.6.2 JS injection into SpringBoard and other processes) (source: wiki/sources/descriptions/zeroxjf__lightsaber.md); iOS project reversing in IDA via [[ida-ios-helper]] (vtable symbols required) (source: wiki/sources/descriptions/yoavst__ida-ios-helper.md)


## Related concepts

[[il2cpp]] · [[frida]] · [[unflutter]] · [[kernel-callbacks]] · [[patchguard]] · [[mutaben]] · [[shredder-rs]] · [[deobf]] · [[idadeflat]] · [[opaque-predicates-detective]] · [[ida-jm-xorstr-decrypt-plugin]] · [[ida-ios-helper]] · [[pe32-password]] · [[kagura]] · [[totalpe2]] · [[quickasm]] · [[xrefsext]] · [[apktool-mcp-server]] · [[android-proxy-mcp]] · [[lightsaber]] · [[vermagic]] · [[windbg-scripts]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/mobile-security]]



## README map

Cheat Debugging / RE Tools / Mixed boolean-arithmetic / DBI / Fix VMP|Themida|OLLVM (plus IDA/BN/Ghidra/x64dbg plugin ecosystems); Anti Cheat Anti Debugging / Disassembly / Dump Fix / Binary Packer; adjacent `Windows Emulator` (~7; WHP trap-driven guests + hybrid kernel-driver emulation for rootkit/AC RE). (source: wiki/sources/README-categories.md)
