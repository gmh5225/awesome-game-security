---
title: ida_vmx128_helper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Goatman13__ida_vmx128_helper.md
  - wiki/sources/README-categories.md
updated: 2026-10-01
confidence: medium
---

# ida_vmx128_helper

**ida_vmx128_helper** (Goatman13/ida_vmx128_helper) is an **IDA Pro Python plugin** that corrects misinterpreted **VMX128** vector-register operands during disassembly of **PowerPC Xenon** binaries. It hooks IDA's processor module so instructions such as `vaddfp128`, `vperm128`, and `vsldoi128` display accurate **A, B, C, and D** register fields instead of generic VMX decode artifacts. (source: wiki/sources/descriptions/Goatman13__ida_vmx128_helper.md)

## Mechanism

- **Implementation:** IDAPython plugin; hooks the PPC processor module's instruction decode/display path
- **Problem addressed:** stock IDA VMX128 decode often mislabels **A-register** operands and related vector fields on Xenon SIMD opcodes
- **Output:** readable disassembly with correct A/B/C/D register annotations for VMX128-heavy code paths

## Scope

- **Targets:** PowerPC binaries, especially **Xbox 360 XEX** and related executable formats
- **Instructions:** VMX128 opcodes including `vaddfp128`, `vperm128`, `vsldoi128`
- **Activation:** auto-loads when placed in IDA's plugins directory for PPC processor targets
- **Category:** Cheat / RE Tools (README)

Pairs with [[idaxex]] for XEX load/import workflows and static-recomp projects such as [[mcla-pc]] that depend on readable VMX128 disassembly for Xenon shader and SIMD RE. Same author (Goatman13) also maintains console IDA helpers [[ps2-ida-vu-micro]] and [[spu2c]] for PlayStation vector-unit annotation.

## Positioning

For reverse engineers and game security researchers who need trustworthy static disassembly when analyzing VMX128-heavy console game code—especially Xbox 360 titles where SIMD math, shader microcode, and vector permutes dominate hot paths. Complements live modded-console tooling such as [[toastylink]] XBDM memory RE by fixing the static-analysis layer IDA shows before patch authoring.

## Links

- Repo: https://github.com/Goatman13/ida_vmx128_helper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idaxex]] · [[mcla-pc]] · [[toastylink]] · [[recompiler]] · [[ps2-ida-vu-micro]] · [[spu2c]] · [[static-runtime-evidence]]
