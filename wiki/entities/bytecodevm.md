---
title: BytecodeVM
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - https://github.com/NHCM-dev/BytecodeVM
updated: 2026-08-04
confidence: medium
---

# BytecodeVM

**Java bytecode virtualizing obfuscator** that rewrites selected methods into compact virtual bytecode programs, injects a generated pure-Java VM, and executes protected logic through that interpreter at runtime. The VM itself is emitted as JVM bytecode (no native code or dynamic libraries), so protection stays cross-platform. YAML + optional Maven Central annotation SDK (`@Virtualize`, `@DoNotVirtualize`, `@ProtectClass`) drive method selection; `inspect`/`protect` emit JSON planning reports for CI.

Features multiple VM structure tiers (simple dispatch through data-flow / register-based / polymorphic handlers), per-method opcode maps, encrypted operands and dynamic constant decryption, virtual control-flow graphs, super-instruction fusion, and optional second-stage VM integrity checks over generated VM/CodePool class bytes. Author notes it is demonstration-oriented — virtualization can slow hot paths by orders of magnitude and is not positioned as production-grade vs commercial JVM/native protectors.

## Links

- Repo: https://github.com/NHCM-dev/BytecodeVM
- Demo video: https://youtu.be/hnDbwdsGjBU

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[deobfuscator]] · [[dprotect]] · [[nocturne]]
