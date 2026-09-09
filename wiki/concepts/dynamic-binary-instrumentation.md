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
  - wiki/sources/descriptions/DynamoRIO__drmemory.md
updated: 2026-09-09
confidence: high
---

# Dynamic Binary Instrumentation

**DBI** modifies or observes program behavior at runtime without recompiling the target. In game-security RE, DBI supports API hooking, coverage measurement, fuzz harness creation, behavioral analysis, and tracing of driver IOCTLs and kernel callbacks. (source: wiki/sources/skills/reverse-engineering.md)

Offline **static binary rewriting** on Linux ELF via [[e9patch]] can insert jumps, trampolines, and probes at arbitrary instructions without reassembly—useful when runtime DBI is blocked or when preparing instrumented binaries ahead of execution. (source: wiki/sources/descriptions/GJDuck__e9patch.md)

## Full frameworks

| Tool | Notes |
|------|-------|
| [[frida]] | Cross-platform; mobile + desktop hooking |
| DynamoRIO / Pin / QBDI | Research-grade code manipulation; [[drmemory]] adds DynamoRIO-based dynamic memory debugging (UAF, OOB, leaks; unmodified binaries) |
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

### Evidence limits (exception-driven)

Exception-driven instrumentation observes selected execution points while changing some combination of code, memory permissions, exception handling, state, or timing. Treat the resulting trace as an **observation under those conditions**—a static control-flow graph or smaller modification footprint does not establish a universally safer or more complete strategy. (source: wiki/sources/skills/reverse-engineering.md)

For owned test programs, assess before generalizing:

| Dimension | What to record |
|-----------|----------------|
| **Semantic fidelity** | Registers, memory effects, error handling, synchronization, and program results vs an uninstrumented baseline under supported conditions |
| **Coverage** | Measured unit (instruction/block/edge/function), denominator, input set, thread scope, missing intervals; an observed edge ≠ every feasible path; a page event ≠ an instruction trace |
| **Observation cost** | Runtime overhead, exception volume, termination, instability, scheduling changes; distinguish application defects from collection artifacts |
| **Scope** | Unsupported instructions, generated code, external calls, collector limitations before transferring results across versions |

DynamoRIO transparency documentation covers state, resource, synchronization, and timing concerns for its clients—it supports these review dimensions but does not validate ad hoc exception instrumentation designs.

## User-mode hypervisor-assisted tracing

WHP API runs guest code snippets with EPT-equivalent page traps (R/W/X), CPUID interception, and syscall emulation — pure user mode, no driver signing. A user-mode application manages guest partitions through Windows Hypervisor Platform; this is **not** the same as running the hypervisor inside that process, forcing all guest code to user mode, or gaining arbitrary host-kernel control. (source: wiki/sources/skills/reverse-engineering.md)

For an analysis trace, record host/guest boundaries, guest execution state, modeled memory/devices, enabled capabilities, and the actual exit reason. A page-access exit supports a finding about that access under the configured policy—it does not provide complete instruction or edge coverage. The documented exit enumeration has no generic syscall exit: do not assume every guest system call automatically transfers control to the analysis application. Match OS/SDK/architecture and nested-environment support; preserve unmodeled scheduler, device, timing, and concurrency effects plus unsupported instructions and missing trace intervals. Review semantic fidelity against an owned baseline before drawing conclusions from modeled execution.

WHP trap libraries such as [[vmtrace]] (host-backed guest memory, page traps, VM-exit single-step tracing; asmjit codegen) complement full PE emulators like [[winvisor]]. (source: wiki/sources/descriptions/momo5502__vmtrace.md)

## Related

[[binary-evidence]] · [[e9patch]] · [[frida]] · [[adbi]] · [[tinyinst]] · [[drmemory]] · [[river]] · [[mambo]] · [[covcane]] · [[cpp-veh-dbi]] · [[w1tn3ss]] · [[pyda]] · [[panda]] · [[glacierw-mba]] · [[vmtrace]] · [[winvisor]] · [[hyper-rev]] · [[ripr]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
