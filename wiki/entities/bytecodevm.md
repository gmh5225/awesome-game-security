---
title: BytecodeVM
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/NHCM-dev__BytecodeVM.md
  - https://github.com/NHCM-dev/BytecodeVM
updated: 2026-08-22
confidence: medium
---

# BytecodeVM

**Java bytecode virtualizing obfuscator** (NHCM-dev) that rewrites selected methods into custom virtual bytecode, injects a generated pure-Java interpreter, and runs protected logic through that VM at runtime — no native code or dynamic libraries. Written in Java and built with Gradle; uses **ASM** for bytecode transformation. A **CLI** accepts YAML configuration; an optional annotation SDK (`@Virtualize`, `@DoNotVirtualize`, `@ProtectClass`) gives per-class and per-method virtualization control; `inspect`/`protect` emit JSON planning reports for CI. (source: wiki/sources/descriptions/NHCM-dev__BytecodeVM.md)

Supports many VM execution architectures — simple dispatch and threaded interpreters through polymorphic, register-based, data-flow, and finite-state-machine designs — plus layered protections: encrypted operands, dynamic constant decryption, shuffled control-flow graphs, super-instruction fusion, and optional runtime VM integrity checks over generated VM/CodePool class bytes. Cross-platform because the VM itself is emitted as JVM bytecode.

Primarily an **educational and research platform** for bytecode virtualization and Java application hardening — protecting sensitive logic from static analysis and reverse engineering — rather than a production-grade commercial obfuscator. Author notes hot-path virtualization can slow execution by orders of magnitude.

## Links

- Repo: https://github.com/NHCM-dev/BytecodeVM
- Demo video: https://youtu.be/hnDbwdsGjBU

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[deobfuscator]] · [[bytecode-viewer]] · [[dprotect]] · [[nocturne]] · [[binary-shield]]
