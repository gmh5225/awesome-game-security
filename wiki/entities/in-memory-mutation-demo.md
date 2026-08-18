---
title: in-memory-mutation-demo
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/alekzandren__in-memory-mutation-demo.md
updated: 2026-08-18
confidence: medium
---

# in-memory-mutation-demo

Educational C++23 demonstration of in-memory polymorphic **data** mutation: a payload is decrypted, used, and re-encrypted entirely within process memory. Cross-platform page protection via Windows `VirtualProtect` and Linux `mprotect` with page-boundary alignment; unified API built on `std::span` and `std::expected` for type-safe errors. The `ProtectedData` class applies position-dependent XOR with dynamic key rotation from a PRNG, restores original permissions, and zeroizes the buffer before exit. Intended for researchers studying binary mechanics, memory layout manipulation, and defense-in-depth relevant to anti-cheat and game security engineering. CMake build; requires C++23-capable compilers. (source: wiki/sources/descriptions/alekzandren__in-memory-mutation-demo.md)

Complements instruction-level polymorphism samples such as [[shredder-rs]] and page-protection fluctuation PoCs such as [[shellcode-fluctuation]]; differs by mutating encrypted **data blobs** rather than code bytes.

## Links

- Repo: https://github.com/alekzandren/in-memory-mutation-demo

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[shellcode-fluctuation]] · [[shredder-rs]] · [[memory-guard]] · [[crystr]] · [[encrypted-value]]
