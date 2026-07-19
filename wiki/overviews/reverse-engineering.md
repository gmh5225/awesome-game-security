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
  - wiki/sources/descriptions/xxFURYWOLFxx__veh-dumper.md
  - wiki/sources/descriptions/xtremegamer1__vmdevirt-vtil.md
  - wiki/sources/descriptions/xsj3n__x64-EXE-Packer.md
  - wiki/sources/descriptions/xM0kht4r__2Pack.md
  - wiki/sources/descriptions/xqemu__xqemu.md
  - wiki/sources/descriptions/xkevio__kevboy.md
  - wiki/sources/descriptions/vojty__feather-gb.md
  - wiki/sources/descriptions/xenia-project__xenia.md
  - wiki/sources/descriptions/wmarti__xenia-mac.md
  - wiki/sources/descriptions/xemu-project__xemu.md
  - wiki/sources/descriptions/xp987__symbridge.md
  - wiki/sources/descriptions/xsslize__idarem.md
  - wiki/sources/descriptions/xiaoweime__WProtect.md
  - wiki/sources/descriptions/xaitax__NTSleuth.md
  - wiki/sources/descriptions/x90skysn3k__x260-lenovo-opencore.md
  - wiki/sources/descriptions/x86matthew__WinVisor.md
  - wiki/sources/descriptions/waryas__KACE.md
  - wiki/sources/descriptions/x86byte__sbox.md
  - wiki/sources/descriptions/x86byte__Obfusk8.md
  - wiki/sources/descriptions/x64dbg__x64dbgbinja.md
  - wiki/sources/descriptions/x64dbg__x64dbg.md
  - wiki/sources/descriptions/x64dbg__SlothBP.md
  - wiki/sources/descriptions/x64dbg__DotX64Dbg.md
  - wiki/sources/descriptions/x64dbg__Classroom.md
  - wiki/sources/descriptions/wtsxDev__reverse-engineering.md
  - wiki/sources/descriptions/wiresock__ndisapi.md
  - wiki/sources/descriptions/winsiderss__systeminformer.md
  - wiki/sources/descriptions/wilszdev__SteamAntiAntiDebug.md
  - wiki/sources/descriptions/westfox-5__GhidraMetrics.md
  - wiki/sources/descriptions/wesmar__KvcForensic.md
  - wiki/sources/descriptions/wesmar__FileRecoveryTool.md
  - wiki/sources/descriptions/wesmar__CmdT.md
  - wiki/sources/descriptions/weak1337__ricochet_deobfuscator.md
  - wiki/sources/descriptions/weak1337__NO_ACCESS_Protection.md
  - wiki/sources/descriptions/weak1337__Alcatraz.md
  - wiki/sources/descriptions/waryas__UMPMLib.md
  - wiki/sources/descriptions/waryas__EUPMAccess.md
  - wiki/sources/descriptions/wallds__NoVmpy.md
  - wiki/sources/descriptions/void-stack__VMUnprotect.md
  - wiki/sources/descriptions/void-stack__VMUnprotect.Dumper.md
  - wiki/sources/descriptions/wINfOG__IDA_Easy_Life.md

  - wiki/sources/descriptions/w00tzenheimer__d810-ng.md
  - wiki/sources/descriptions/vxlang__vxlang-page.md
  - wiki/sources/descriptions/vxCrypt0r__Voidmaw.md
  - wiki/sources/descriptions/vsteffen__woody_woodpacker.md
  - wiki/sources/descriptions/volatilityfoundation__volatility3.md
  - wiki/sources/descriptions/volatilityfoundation__volatility.md
  - wiki/sources/descriptions/vmi-rs__ephemera.md
  - wiki/sources/descriptions/vm03__payload_dumper.md
  - wiki/sources/descriptions/vchelaru__FlatRedBall.md
  - wiki/sources/descriptions/uuksu__RPGMakerDecrypter.md
  - wiki/sources/descriptions/urho3d__Urho3D.md
  - wiki/sources/descriptions/utmapp__UTM.md
  - wiki/sources/descriptions/user23333__veh.md
  - wiki/sources/descriptions/user1342__Obfu-DE-Scate.md
  - wiki/sources/descriptions/un4ckn0wl3z__MemMCP.md
updated: 2026-07-19
confidence: high
---




# Reverse Engineering

Workflows for protected game clients and anti-cheat components across user mode, kernel, and hypervisor-aware environments: debug/disassemble, DBI, deobfuscation, dump analysis, and IOCTL/callback mapping. (source: wiki/sources/skills/reverse-engineering.md)

## Key sub-areas

- **Guides / indexes:** curated RE resource lists such as [[reverse-engineering]] (reversing + networking + editor tooling; cheat/guide lane) (source: wiki/sources/descriptions/wtsxDev__reverse-engineering.md)
- **Network / NDIS:** user-mode packet-filter APIs such as [[ndisapi]] (Windows Packet Filter; NDIS-level inspect/modify) for cheat / packet-sniffer RE. (source: wiki/sources/descriptions/wiresock__ndisapi.md)
- **Tools:** IDA/Ghidra/Binary Ninja, [[x64dbg]]/WinDbg/HyperDbg (Windows x86/x64 debugger + plugins) (source: wiki/sources/descriptions/x64dbg__x64dbg.md), Cheat Engine, dnSpy, [[frida]]; Cheat Engine–like MCP memory tooling via [[memmcp]] (Python; Game Develop / MCP) (source: wiki/sources/descriptions/un4ckn0wl3z__MemMCP.md); usermode process-memory / RPM research libs such as [[umpmlib]] (C/C++; cheat / RPM) (source: wiki/sources/descriptions/waryas__UMPMLib.md); related memory-analysis samples such as [[eupmaccess]] (C/C++; cheat / RPM) (source: wiki/sources/descriptions/waryas__EUPMAccess.md); Ghidra native-code metrics via [[ghidrametrics]] (cyclomatic complexity / function size / call depth; headless + JSON export) (source: wiki/sources/descriptions/westfox-5__GhidraMetrics.md); host process/system explorers such as [[systeminformer]] (formerly Process Hacker; Cheat Windows kernel explorer) (source: wiki/sources/descriptions/winsiderss__systeminformer.md); JS WinDbg kernel scripts such as [[windbg-scripts]] (Cheat → WinDbg Plugins) (source: wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md); PE triage viewers such as [[totalpe2]] (headers/imports/exports/.NET metadata) (source: wiki/sources/descriptions/zodiacon__TotalPE2.md); Windows syscall-table extraction via [[ntsleuth]] (`ntdll`/`win32u` PDB + disasm → JSON/C headers) (source: wiki/sources/descriptions/xaitax__NTSleuth.md); quick x86/x64 assemble-and-run via [[quickasm]] (Keystone) (source: wiki/sources/descriptions/zodiacon__QuickAsm.md); IDA xref-extension plugin [[xrefsext]] (source: wiki/sources/descriptions/zengfr__XrefsExt.md); live IDA ↔ x64dbg annotation/type sync via [[symbridge]] (module+RVA keyed; Python broker) (source: wiki/sources/descriptions/xp987__symbridge.md); remote browser review of a live IDB via [[idarem]] (Flask REST/SSE + React; live follow / optional rename-comment write-back) (source: wiki/sources/descriptions/xsslize__idarem.md); Binary Ninja ↔ x64dbg plugin lane via [[x64dbgbinja]] (Python BN plugin) (source: wiki/sources/descriptions/x64dbg__x64dbgbinja.md); collaborative x64dbg breakpoint management via [[slothbp]] (source: wiki/sources/descriptions/x64dbg__SlothBP.md); .NET 6 / C# x64dbg plugins via [[dotx64dbg]] (live edit + custom commands/expressions) (source: wiki/sources/descriptions/x64dbg__DotX64Dbg.md); OOP class documentation while debugging via [[classroom]] (member funcs/vars; persisted docs) (source: wiki/sources/descriptions/x64dbg__Classroom.md); IDA JM Xorstr decrypt attempts via [[ida-jm-xorstr-decrypt-plugin]] (x64) (source: wiki/sources/descriptions/yubie-re__ida-jm-xorstr-decrypt-plugin.md); iOS IDA helper [[ida-ios-helper]] (vtable symbols required) (source: wiki/sources/descriptions/yoavst__ida-ios-helper.md); Android apktool via [[apktool-mcp-server]] (MCP suite) (source: wiki/sources/descriptions/zinja-coder__apktool-mcp-server.md); ProGuard/R8 APK name recovery + HTML class-hierarchy reports via [[obfu-de-scate]] (source: wiki/sources/descriptions/user1342__Obfu-DE-Scate.md); Android OTA `payload.bin` dumps via [[payload-dumper]] (Python; ROM/RE tools) (source: wiki/sources/descriptions/vm03__payload_dumper.md); Android HTTP/HTTPS capture + NL query via [[android-proxy-mcp]] (mitmdump/SQLite) (source: wiki/sources/descriptions/zhizhuodemao__android_proxy_mcp.md)
- **DBI:** Frida, DynamoRIO, Pin; trap-and-emulate CFT; WHP user-mode hypervisor tracing; WHP-hosted x64 PE emulation such as [[winvisor]] (`Windows Emulator`); RING3 kernel-driver sandboxing such as [[kace]] (self context mapping or Unicorn; AC/driver RE without loading on the host) (source: wiki/sources/descriptions/x86matthew__WinVisor.md) (source: wiki/sources/descriptions/waryas__KACE.md)
- **Obfuscation:** MBA, OLLVM CFF, opaque predicates, VMProtect/Themida virtualization; MBA sample generation via [[mutaben]] (Python MBA generator) (source: wiki/sources/descriptions/z1ko__mutaben.md); [[shredder-rs]] for x86_64 instruction-level polymorphic shredding vs static analysis (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md); OLLVM fix / plugin-hook work on `libtprt.so` via [[deobf]] (source: wiki/sources/descriptions/zhuzhu-Top__deobf.md); Ricochet AC deobfuscation via [[ricochet-deobfuscator]] (C/C++; driver / memory analysis; explore anticheat:ricochet) (source: wiki/sources/descriptions/weak1337__ricochet_deobfuscator.md); IDA CFF deflattening via [[idadeflat]] (angr symbolic exec → recover CFG / patch) (source: wiki/sources/descriptions/za233__IDADeflat.md); IDA deobfuscation plugin work via [[ida-easy-life]] (Python; cheat / IDA Plugins) (source: wiki/sources/descriptions/wINfOG__IDA_Easy_Life.md); decompilation-time deobfuscation via [[d810-ng]] (d810 next-gen; Fix OLLVM lane) (source: wiki/sources/descriptions/w00tzenheimer__d810-ng.md); opaque-predicate detection via [[opaque-predicates-detective]] (invariant-expression / BB-local damage model; Binary Ninja plugin lane) (source: wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md); PE32 password packing via [[pe32-password]] (Binary Packer) (source: wiki/sources/descriptions/ytk2128__pe32-password.md); PE X64 packing via [[x64-exe-packer]] (source: wiki/sources/descriptions/xsj3n__x64-EXE-Packer.md); Rust PE & shellcode packing via [[2pack]] (EXE/DLL + raw shellcode) (source: wiki/sources/descriptions/xM0kht4r__2Pack.md); ELF packing via [[woody-woodpacker]] (outputs “woody”) (source: wiki/sources/descriptions/vsteffen__woody_woodpacker.md); LLVM pass-plugin obfuscation/anti-tamper via [[kagura]] (CFF/bogus CFG, string/data encryption, anti-debug runtime; mobile/desktop/Wasm) (source: wiki/sources/descriptions/ykus4__kagura.md); Obfuscation Engine research via [[wprotect]] (C/C++ WProtect) (source: wiki/sources/descriptions/xiaoweime__WProtect.md); post-compile x64 PE obfuscation via [[alcatraz]] (mutation / CFF / anti-disasm / IAT; Zydis + AsmJit) (source: wiki/sources/descriptions/weak1337__Alcatraz.md); dual-mode Windows protector [[vxlang-page]] (virtualization / flatten / anti-tamper; PE/DLL/SYS + .NET) (source: wiki/sources/descriptions/vxlang__vxlang-page.md); C++17 compile-time+runtime obfuscation library [[obfusk8]] (logic/data protection) (source: wiki/sources/descriptions/x86byte__Obfusk8.md); compile-time AES-128 / S-box string encryption via [[sbox]] (constexpr macros; Obfusk8 spin-off) (source: wiki/sources/descriptions/x86byte__sbox.md); Fix VMP / VTIL demos such as [[vmdevirt-vtil]] (broken VTIL compile path; jmp-around-`vmenter` IDA display idea) (source: wiki/sources/descriptions/xtremegamer1__vmdevirt-vtil.md); Python VMProtect symbolic-exec deobf via [[novmpy]] (handler-chain semantics → original insn reconstruct; Triton) (source: wiki/sources/descriptions/wallds__NoVmpy.md); .NET Harmony instrumentation of VMProtect-virtualized methods via [[vmunprotect]] (trace invokes / params; anti-debug bypass; VMP 3.6.0) (source: wiki/sources/descriptions/void-stack__VMUnprotect.md); dynamic .NET VMProtect unpack/dump via [[vmunprotect-dumper]] (force static ctor restore → AsmResolver PE dump; VMP 3.7.0) (source: wiki/sources/descriptions/void-stack__VMUnprotect.Dumper.md)

- **Game engines:** [[il2cpp]] dumps, Unreal SDK generators, native PE/pattern workflows; Flutter/Dart AOT snapshot static analysis via [[unflutter]] (source: wiki/sources/descriptions/zboralski__unflutter.md); managed .NET 2D engine trees such as [[flatredball]] for inspecting a complete editor/runtime codebase (source: wiki/sources/descriptions/vchelaru__FlatRedBall.md); lightweight cross-platform 2D/3D engine source such as [[urho3d]] (source: wiki/sources/descriptions/urho3d__Urho3D.md); RPG Maker XP/VX/VX Ace encrypted-archive extraction via [[rpgmakerdecrypter]] (CLI; cheat / RE-tools lane) (source: wiki/sources/descriptions/uuksu__RPGMakerDecrypter.md)
- **Anti-analysis:** ScyllaHide/TitanHide/HyperHide vs IsDebuggerPresent/Kd* / timing checks; Steam-specific anti-anti-debug via [[steam-anti-anti-debug]] (patch Steam debug detection so [[x64dbg]] can attach to protected game processes) (source: wiki/sources/descriptions/wilszdev__SteamAntiAntiDebug.md); VEH software debugger (no Debug API) via [[veh]] (breakpoint / single-step / AV handlers; CE plugin for manual-mapped VEH DLLs) (source: wiki/sources/descriptions/user23333__veh.md); VEH/VCH chain dump to IDA-ready PE64 via [[veh-dumper]] (foothold handler + `RtlDecodePointer` list walk) (source: wiki/sources/descriptions/xxFURYWOLFxx__veh-dumper.md); PAGE_NOACCESS code-page anti-tamper via [[no-access-protection]] (VEH restore + `STATUS_SINGLE_STEP` re-protect vs external scanners) (source: wiki/sources/descriptions/weak1337__NO_ACCESS_Protection.md); VEH + `PAGE_GUARD` code-hiding via [[voidmaw]] (AV/AC page-protection research) (source: wiki/sources/descriptions/vxCrypt0r__Voidmaw.md)
- **LSA / dump forensics:** cross-platform LSASS credential extractors such as [[kvcforensic]] recover MSV/WDigest/Kerberos/CredMan/DPAPI secrets from live memory or `lsass.dmp` via signature scan + BCrypt (Win11 24H2–26H1; Windows/Linux). (source: wiki/sources/descriptions/wesmar__KvcForensic.md)
- **Memory forensics (RAM):** frameworks such as [[volatility]] (original Python 2; profile-based; pslist/psscan, modules, rootkit/malware plugins) and [[volatility3]] (Python 3 rewrite; layer translation + automagic profiles) extract process/network/registry/kernel artifacts from offline memory images for IR and malware RE. (source: wiki/sources/descriptions/volatilityfoundation__volatility.md) (source: wiki/sources/descriptions/volatilityfoundation__volatility3.md) WinDbg-flavored multiplatform `MEMORY.DMP` analysis via [[ephemera]] covers crash-dump workflows for AC / kernel dump RE when native WinDbg is too slow. (source: wiki/sources/descriptions/vmi-rs__ephemera.md)

- **Disk / file forensics:** tools such as [[file-recovery-tool]] recover deleted files on NTFS/FAT32/ExFAT via MFT/USN scan, signature carving, and sector-level reassembly (pure Win32; direct disk). (source: wiki/sources/descriptions/wesmar__FileRecoveryTool.md) TrustedInstaller-token launchers such as [[cmdt]] (asm GUI/CLI; TI token duplication) help RE/forensics workflows reach TI-ACL–protected OS components without taking ownership. (source: wiki/sources/descriptions/wesmar__CmdT.md)

- **Linux LKM metadata:** tools such as [[vermagic]] rewrite vermagic / CRC fields so a module can load across mismatched kernel builds (cheat / RE tools lane). (source: wiki/sources/descriptions/yaxinsn__vermagic.md)
- **Mobile / iOS:** userland exploit-chain study via [[lightsaber]] (iOS 18.4–18.6.2 JS injection into SpringBoard and other processes) (source: wiki/sources/descriptions/zeroxjf__lightsaber.md); iOS project reversing in IDA via [[ida-ios-helper]] (vtable symbols required) (source: wiki/sources/descriptions/yoavst__ida-ios-helper.md)
- **Console / QEMU:** original Xbox titles via [[xqemu]] (full-machine software emulation, no hardware VT) for RE in the QEMU/KVM/PVE/VBOX research lane. (source: wiki/sources/descriptions/xqemu__xqemu.md); original Xbox LLE via [[xemu]] (QEMU fork; NV2A/MCPX/NForce/Pentium III; OpenGL + SDL2). (source: wiki/sources/descriptions/xemu-project__xemu.md); Game Boy hardware study via [[kevboy]] (Rust CPU/memory/graphics/input emulator). (source: wiki/sources/descriptions/xkevio__kevboy.md); peer Rust GB emulator [[feather-gb]] for retro handheld / GB-area RE. (source: wiki/sources/descriptions/vojty__feather-gb.md); Xbox 360 HLE via [[xenia]] (PowerPC recompiler, D3D12/Vulkan GPU, XAM/kernel/XEX) for console binary-translation / hardware-abstraction study. (source: wiki/sources/descriptions/xenia-project__xenia.md); macOS port [[xenia-mac]] for the same 360 stack on Apple hosts. (source: wiki/sources/descriptions/wmarti__xenia-mac.md)
- **macOS research hosts:** Hackintosh OpenCore EFI packs such as [[x260-lenovo-opencore]] (ThinkPad X260) give security researchers a non-Apple macOS lab for testing. (source: wiki/sources/descriptions/x90skysn3k__x260-lenovo-opencore.md); QEMU VM host [[utm]] runs Windows/Linux guests on iOS/macOS via Hypervisor.framework or JIT (Apple-device VM lab; `IOS Emulator` lane). (source: wiki/sources/descriptions/utmapp__UTM.md)


## Related concepts

[[il2cpp]] · [[frida]] · [[unflutter]] · [[flatredball]] · [[rpgmakerdecrypter]] · [[kernel-callbacks]] · [[patchguard]] · [[mutaben]] · [[ndisapi]] · [[umpmlib]] · [[eupmaccess]] · [[shredder-rs]] · [[deobf]] · [[ricochet-deobfuscator]] · [[idadeflat]] · [[ida-easy-life]] · [[d810-ng]] · [[opaque-predicates-detective]] · [[ida-jm-xorstr-decrypt-plugin]] · [[ida-ios-helper]] · [[pe32-password]] · [[x64-exe-packer]] · [[2pack]] · [[woody-woodpacker]] · [[kagura]] · [[wprotect]] · [[alcatraz]] · [[vxlang-page]] · [[obfusk8]] · [[sbox]] · [[vmdevirt-vtil]] · [[novmpy]] · [[vmunprotect]] · [[vmunprotect-dumper]] · [[totalpe2]]
 · [[ntsleuth]] · [[quickasm]] · [[xrefsext]] · [[symbridge]] · [[idarem]] · [[systeminformer]] · [[cmdt]] · [[x64dbg]] · [[x64dbgbinja]] · [[slothbp]] · [[dotx64dbg]] · [[classroom]] · [[steam-anti-anti-debug]] · [[ghidrametrics]] · [[apktool-mcp-server]] · [[memmcp]] · [[obfu-de-scate]] · [[payload-dumper]] · [[android-proxy-mcp]] · [[lightsaber]] · [[vermagic]] · [[veh]] · [[veh-dumper]] · [[no-access-protection]] · [[voidmaw]] · [[kvcforensic]] · [[volatility]] · [[volatility3]] · [[ephemera]] · [[file-recovery-tool]]
 · [[windbg-scripts]] · [[winvisor]] · [[xqemu]] · [[xemu]] · [[kevboy]] · [[feather-gb]] · [[xenia]] · [[xenia-mac]] · [[x260-lenovo-opencore]] · [[utm]] · [[reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/mobile-security]]




## README map

Cheat (~2554) Debugging / RE Tools / Mixed boolean-arithmetic / DBI / Fix VMP|Themida|OLLVM (plus IDA/BN/Ghidra/x64dbg plugin ecosystems); Anti Cheat Anti Debugging / Disassembly / Dump Fix / Binary Packer; adjacent `Windows Emulator` (~7; WHP trap-driven guests + hybrid kernel-driver emulation for rootkit/AC RE), `Linux Emulator` (~1), and console cats (`Xbox` ~7 / `Game Boy` ~3 / Switch ~7 / `PlayStation` ~5 HV+BD-JB / 3DS LLE) for binary-translation, hypervisor, and hardware-abstraction RE. (source: wiki/sources/README-categories.md)
