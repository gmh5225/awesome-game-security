---
title: dae
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/ejfkdev__dae.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# dae

**dae** (ejfkdev/dae) is a config-driven **Dart AOT snapshot debug-info exporter** written in Rust. It locates embedded snapshots inside Mach-O, ELF, and PE binaries and exports symbols and runtime structures without requiring the Dart SDK or executing the target — aimed at reverse engineers and game security researchers analyzing compiled Dart and Flutter applications. (source: wiki/sources/descriptions/ejfkdev__dae.md)

README category: Cheat / RE Tools.

## Snapshot extraction

Auto-detects Dart versions via embedded SDK profiles, then parses AOT snapshots from Flutter release builds and `dart compile exe` / aot-snapshot artifacts across **Dart 2.7–3.14**. (source: wiki/sources/descriptions/ejfkdev__dae.md)

## Toolchain outputs

Emits IDA, radare2, and Frida scripts plus Capstone-backed ARM64 disassembly, object-pool dumps, class and function indexes, and optional experimental pseudocode decompilation. Output is **blutter-compatible** for workflows that already consume blutter artifacts. (source: wiki/sources/descriptions/ejfkdev__dae.md)

## Positioning

Complements [[unflutter]] Python static snapshot analysis and [[flutter-re-demo]] IDA/reFlutter workflows when researchers need cross-platform (Mach-O/ELF/PE) symbol recovery from compiled Dart/Flutter game clients without installing the Dart SDK.

## Links

- Repo: https://github.com/ejfkdev/dae

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[unflutter]] · [[flutter-re-demo]] · [[frida]]
