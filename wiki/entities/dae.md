---
title: dae
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/ejfkdev__dae.md
updated: 2026-09-26
confidence: medium
---

# dae

Config-driven Rust CLI that locates embedded Dart AOT snapshots inside Mach-O, ELF, and PE binaries and exports debug symbols and runtime structures without requiring the Dart SDK or executing the target. Auto-detects Dart versions via embedded SDK profiles and emits IDA, radare2, and Frida scripts plus disassembly, object-pool dumps, class/function indexes, and optional experimental pseudocode decompilation. Supports Flutter release builds and `dart compile exe` / aot-snapshot artifacts across Dart 2.7–3.14 with Capstone-backed ARM64 disassembly and blutter-compatible output. (source: wiki/sources/descriptions/ejfkdev__dae.md)

Complements [[unflutter]] static analysis and [[flutter-re-demo]] IDA workflows when researchers need cross-platform symbol recovery from compiled Dart/Flutter game clients.

## Links

- Repo: https://github.com/ejfkdev/dae

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[unflutter]] · [[flutter-re-demo]] · [[frida]]
