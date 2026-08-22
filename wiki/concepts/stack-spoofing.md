---
title: Stack Spoofing
kind: concept
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/mgeeky__ThreadStackSpoofer.md
  - wiki/sources/descriptions/klezVirus__SilentMoonwalk.md
  - wiki/sources/descriptions/klezVirus__BYOUD.md
  - wiki/sources/descriptions/gmh5225__spoof-stack-SafeCall.md
  - wiki/sources/descriptions/gmh5225__StackSpoofer_Macro.md
  - wiki/sources/descriptions/gmh5225__STB.md
  - wiki/sources/descriptions/gmh5225__Fenrir.md
  - wiki/sources/descriptions/gmh5225__CallStackSpoofer-2.md
  - wiki/sources/descriptions/gabriellandau__ShadowStackWalk.md
  - wiki/sources/descriptions/frkngksl__NimicStack.md
  - wiki/sources/descriptions/fortra__hw-call-stack.md
  - wiki/sources/descriptions/evilashz__ProxyAPICall.md
  - wiki/sources/descriptions/danielkrupinski__x86RetSpoof.md
  - wiki/sources/descriptions/cryotb__RASD.md
  - wiki/sources/descriptions/WithSecureLabs__CallStackSpoofer.md
  - wiki/sources/descriptions/Sizeable-Bingus__BingusLdr.md
  - wiki/sources/descriptions/Peribunt__Ret-Spoofing.md
updated: 2026-08-22
confidence: medium
---

# Stack Spoofing

Techniques that **fabricate or rewrite call-stack frames** so thread stack walks see return addresses inside expected modules (`ntdll`, `kernel32`, game binaries) instead of cheat or manually mapped code. Used to evade anti-cheat stack inspection, ETW stack traces, and unwind-based hook detection. (source: wiki/sources/skills/game-hacking.md)

## Return-address spoofing

Before calling a sensitive API, replace the stack slot that holds the return address with a gadget or module address; restore after return. Evades naive `RtlWalkFrameChain` scans that flag returns outside loaded images. WithSecure Labs syscall stack-spoof PoCs such as [[callstackspoofer]] (C++; selectable stack profiles mimicking common process behavior; telemetry/debugger validation notes; EDR/stack-detection research) illustrate arbitrary stack fabrication at syscall time. (source: wiki/sources/descriptions/WithSecureLabs__CallStackSpoofer.md) Reusable libraries such as [[spoof-stack-safecall]] (gmh5225/SafeCall) package this pattern for red-team and game-security research. (source: wiki/sources/descriptions/gmh5225__spoof-stack-SafeCall.md) Custom-stack-call API proxies such as [[proxy-api-call]] (evilashz/ProxyAPICall; C/C++; proxy sensitive API calls through fabricated stacks; Cheat Spoof Stack / Custom stack call) extend that lane with explicit API-call proxying. (source: wiki/sources/descriptions/evilashz__ProxyAPICall.md) Macro-based helpers such as [[stack-spoofer-macro]] (gmh5225; easy-to-use C/C++ preprocessor macros for stack spoofing) offer a lightweight alternative in the same lane. (source: wiki/sources/descriptions/gmh5225__StackSpoofer_Macro.md) x64 trampoline implementations such as [[callstackspoofer-2]] (gmh5225; custom assembly trampolines forge return addresses and stack frames for EDR/AC stack-walk evasion; MSVC inline ASM) illustrate the same pattern with hand-written assembly stubs. (source: wiki/sources/descriptions/gmh5225__CallStackSpoofer-2.md) Minimal x64 return-address spoofing without exception handlers such as [[ret-spoofing]] (Peribunt; C++ + ASM stubs; low-overhead fake return targets; documents Windows x64 nonvolatile-register assumptions; Cheat Spoof Stack) offers a lightweight alternative for simple call redirection. (source: wiki/sources/descriptions/Peribunt__Ret-Spoofing.md) x86 (32-bit) header-only libraries such as [[x86-ret-spoof]] (danielkrupinski; `JMP DWORD PTR [EBX]` gadget dispatch in a target module; stdcall/cdecl/fastcall/thiscall) extend the same return-address spoofing pattern to legacy 32-bit Windows game clients. (source: wiki/sources/descriptions/danielkrupinski__x86RetSpoof.md) Kernel/driver-framework samples such as [[fenrir]] (gmh5225; `jmp rdi` gadget dispatch for stack spoofing inside a broader rootkit framework) extend that lane from Ring0. (source: wiki/sources/descriptions/gmh5225__Fenrir.md) Compile-time helpers such as [[stb-gmh5225]] (gmh5225/STB; IDA-style string-to-array conversion for stack-trace building / spoof-stack research) support embedding frame or gadget bytes without static plaintext. (source: wiki/sources/descriptions/gmh5225__STB.md) Nim implementations such as [[nimic-stack]] (frkngksl; pure Nim call-stack spoofing from the WithSecure Labs PoC lineage; mimic legitimate program stacks) illustrate the same pattern outside C/C++ toolchains. (source: wiki/sources/descriptions/frkngksl__NimicStack.md)

## Synthetic call stacks

Build multi-frame stacks whose return PCs land in legitimate modules with plausible offsets. Must satisfy **`RtlVirtualUnwind`** and **`.pdata` / UNWIND_INFO`** consistency—spoofed frames that violate unwind metadata fail deeper validation. Crystal Palace–based reflective DLL loaders such as [[bingusldr]] (Sizeable-Bingus; CET-friendly stack spoofing; EAF-compatible API resolution; heap/image masking; mingw-w64; Cobalt Strike `.cna` integration) combine stack evasion with in-memory payload loading for endpoint-detection and anti-cheat research. (source: wiki/sources/descriptions/Sizeable-Bingus__BingusLdr.md)

## Hardware-breakpoint stack spoofing

Some Windows implementations use **x86 debug registers (DR0–DR7)** to intercept execution and **forge visible call stacks** during syscalls and API calls without classic return-address patching. [[hw-call-stack]] (fortra; C/C++; `Cheat > Spoof Stack` / `[HWBP]`) illustrates this lane for game-security researchers studying HWBP-driven stack presentation. (source: wiki/sources/descriptions/fortra__hw-call-stack.md)

## Unwind-metadata manipulation

Instead of fabricating return addresses on the stack, some frameworks **tamper with or leverage unwind metadata** (`.pdata`, `UNWIND_INFO`, runtime function tables) so stack walks and debugger unwinds skip or misinterpret portions of the real call chain. [[byoud]] (klezVirus; x64 Windows framework) illustrates this inverted approach—hiding arbitrary call-chain segments from debuggers and EDRs rather than patching individual return slots. (source: wiki/sources/descriptions/klezVirus__BYOUD.md)

## Detection surface

Anti-cheat walks thread stacks for non-module returns, validates unwind records, and correlates with shadow-stack / CET where enabled. Defensive implementations such as [[shadow-stack-walk]] (gabriellandau; `CaptureStackBackTrace` / `StackWalk64` augmented with CET/HSP shadow-stack data to catch thread stack spoofing) illustrate hardware-backed detection in the `Detection:Spoof Stack` lane. (source: wiki/sources/descriptions/gabriellandau__ShadowStackWalk.md) R5AC-style `RtlCaptureStackBackTrace` analysis such as [[rasd]] (cryotb; reconstructed Apex Legends stackwalk checks; flags non-`CALL`-generated return addresses, unbacked RWX callers, and common x64 spoof gadgets) shows software-only detection without CET. (source: wiki/sources/descriptions/cryotb__RASD.md) Illustrative corpus samples: [[return-address-spoofer]], [[spoof-stack-safecall]] (gmh5225/SafeCall; fake legitimate return addresses before API calls) (source: wiki/sources/descriptions/gmh5225__spoof-stack-SafeCall.md), [[stack-spoofer-macro]] (gmh5225; C/C++ macro for stack spoofing) (source: wiki/sources/descriptions/gmh5225__StackSpoofer_Macro.md), [[loudsunrun]], [[thread-stack-spoofer]] (PoC thread call-stack spoof for in-process shellcode hiding; bypass thread-based memory examination) (source: wiki/sources/descriptions/mgeeky__ThreadStackSpoofer.md), [[silent-moonwalk]] (klezVirus; TRUE call-stack spoofer from joint stack-spoofing research) (source: wiki/sources/descriptions/klezVirus__SilentMoonwalk.md), [[nimic-stack]] (frkngksl; pure Nim; WithSecure Labs PoC lineage) (source: wiki/sources/descriptions/frkngksl__NimicStack.md), [[callstackspoofer]] (WithSecureLabs; C++ syscall stack-spoof PoC; selectable stack profiles) (source: wiki/sources/descriptions/WithSecureLabs__CallStackSpoofer.md), [[byoud]] (klezVirus; unwind-metadata manipulation to hide call-chain segments) (source: wiki/sources/descriptions/klezVirus__BYOUD.md), [[nocturneldr]], [[callout-poc]]. Defensive context: [[overviews/anti-cheat]] Detection:Spoof Stack lane.

## Related

[[kernel-callbacks]] · [[present-hook]] · [[windows-process-injection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
