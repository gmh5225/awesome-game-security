---
title: Dynamic Binary Instrumentation
kind: concept
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/beehive-lab__mambo.md
  - wiki/sources/descriptions/bitdefender__river.md
  - wiki/sources/descriptions/googleprojectzero__TinyInst.md
  - wiki/sources/descriptions/momo5502__vmtrace.md
  - wiki/sources/descriptions/ZehMatt__CovCane.md
  - wiki/sources/descriptions/WaterlooBridge__adbi.md
  - wiki/sources/descriptions/GJDuck__e9patch.md
  - wiki/sources/descriptions/GlacierW__MBA.md
updated: 2026-08-25
confidence: high
---

# Dynamic Binary Instrumentation

**DBI** modifies or observes program behavior at runtime without recompiling the target. In game-security RE, DBI supports API hooking, coverage measurement, fuzz harness creation, behavioral analysis, and tracing of driver IOCTLs and kernel callbacks. (source: wiki/sources/skills/reverse-engineering.md)

Offline **static binary rewriting** on Linux ELF via [[e9patch]] can insert jumps, trampolines, and probes at arbitrary instructions without reassembly—useful when runtime DBI is blocked or when preparing instrumented binaries ahead of execution. (source: wiki/sources/descriptions/GJDuck__e9patch.md)

## Full frameworks

| Tool | Notes |
|------|-------|
| [[frida]] | Cross-platform; mobile + desktop hooking |
| DynamoRIO / Pin / QBDI | Research-grade code manipulation |
| [[tinyinst]] | Lightweight module-selective DBI; hooking / debugging |
| [[river]] | Bitdefender DBI + custom ELF/PE loader (x86; external mapping, import resolution) |
| [[mambo]] | ARM/AArch64 Linux DBI; software code cache; instruction/block/function hooks |
| [[pyda]] | QEMU user-mode Python DBI |
| [[panda]] | Whole-system QEMU DBI |
| [[glacierw-mba]] | QEMU Malware Behavior Analyzer; memory forensics, API tracing, behavioral monitoring (Windows/Linux guests) |
| [[covcane]] | Experimental Windows x86-64 DBI; loader + runtime; Zydis + AsmJIT |
| [[adbi]] | Android ARM/Thumb DBI; hijack injector + inline entry hooks; NDK sample instruments |

Corpus frameworks: [[w1tn3ss]], [[smallworld]] (multi-emulator harness).

## Trap-and-emulate (exception-driven CFT)

Replace branch instructions with fault-generating sentinels; on exception, emulate the original branch and log register context:

- **Sentinels:** HLT (`0xF4`) for `ret`, SALC (`0xD6`) for jmp/jcc/call — avoids INT3 (`0xCC`) integrity scans.
- **Capture:** VEH/SEH or KiUserExceptionDispatcher hooks; handler dispatches by exception code.
- **Emulation:** 16-condition jcc table; direct/indirect call and ret with stack semantics.
- **Patch strategies:** bounded bulk (detectable) → branch chasing → CFG-guided (best coverage/safety balance).
- **Integrity evasion:** PAGE_GUARD + trap flag single-step through original insn without persistent `.text` patches.

Illustrative: [[cpp-veh-dbi]]. Exception-per-branch designs can be orders of magnitude slower — benchmark on target and account for timing checks.

## User-mode hypervisor-assisted tracing

WHP API runs guest code snippets with EPT-equivalent page traps (R/W/X), CPUID interception, and syscall emulation — pure user mode, no driver signing. Composable with disassemblers; limited to snippet/function scope unless full OS modeling is added. WHP trap libraries such as [[vmtrace]] (host-backed guest memory, page traps, VM-exit single-step tracing; asmjit codegen) complement full PE emulators like [[winvisor]]. (source: wiki/sources/descriptions/momo5502__vmtrace.md)

## Related

[[e9patch]] · [[frida]] · [[adbi]] · [[tinyinst]] · [[river]] · [[mambo]] · [[covcane]] · [[cpp-veh-dbi]] · [[w1tn3ss]] · [[pyda]] · [[panda]] · [[glacierw-mba]] · [[vmtrace]] · [[winvisor]] · [[hyper-rev]] · [[ripr]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
