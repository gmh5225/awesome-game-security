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

**ida_vmx128_helper** (Goatman13/ida_vmx128_helper) is an **IDA Pro Python plugin** that corrects misinterpreted **VMX128** vector-register operands during disassembly of **PowerPC Xenon** binaries. It hooks IDA's processor module so instructions such as `vaddfp128`, `vperm128`, and `vsldoi128` display accurate **A, B, C, and D** register fields instead of generic VMX decode artifacts. Auto-loads from IDA's plugins directory for PPC targets, especially **Xbox 360 XEX** and related executable formats. (source: wiki/sources/descriptions/Goatman13__ida_vmx128_helper.md)

## Role in the README map

Listed under **Cheat → RE Tools** beside other console-focused IDA helpers such as [[toastylink]] XBDM tooling and Xbox static-recomp projects such as [[mcla-pc]] that also depend on readable VMX128 disassembly for Xenon shader and SIMD RE.

## Links

- Repo: https://github.com/Goatman13/ida_vmx128_helper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[mcla-pc]] · [[toastylink]] · [[recompiler]] · [[static-runtime-evidence]]
