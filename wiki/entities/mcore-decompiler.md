---
title: mcore-decompiler
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/Siesta__MCORE-Decompiler.md
updated: 2026-08-21
confidence: medium
---

# mcore-decompiler

Self-contained decompiler for Motorola M·CORE binaries, shipped as an IDA Pro 9.4 plugin (C++17). Lifts disassembly from IDA's built-in MCORE processor into a custom intermediate representation, then runs optimization, control-flow structuring, stack-frame recovery, and call-argument analysis before emitting readable C pseudocode bound to F5. Because Hex-Rays provides no M·CORE decompiler backend, the project implements an independent pipeline without relying on Hex-Rays decompiler APIs. Targets reverse engineers analyzing embedded firmware and feature-phone binaries—such as Motorola E1000—where M·CORE was commonly used but native decompilation was previously unavailable. (source: wiki/sources/descriptions/Siesta__MCORE-Decompiler.md)

Complements IoT/firmware audit tooling such as [[firmeye]] and embedded RE courses such as [[embedded-hacking]] when lifting obscure embedded ISAs to structured pseudocode inside IDA. Listed alongside other IDA plugin indexes such as [[list-of-ida-plugins]]; distinct from pseudocode SAST on Hex-Rays output via [[ida-security-scanner]].

## Links

- Repo: https://github.com/siesta/mcore-decompiler

## Related

[[overviews/reverse-engineering]] · [[list-of-ida-plugins]] · [[firmeye]] · [[embedded-hacking]] · [[ida-security-scanner]]
