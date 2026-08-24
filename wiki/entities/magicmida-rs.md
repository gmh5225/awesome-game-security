---
title: magicmida-rs
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/guoxing2024__magicmida-rs.md
updated: 2026-08-06
confidence: medium
---

# magicmida-rs

Rust modular reimplementation of the original Pascal [[magicmida]] automatic Themida unpacker. Detects and unpacks Themida v1/v2/v3 protected executables (x86 and x64) by launching the target under a Win32 Debug API debugger, discovering the original entry point, dumping process memory, and rebuilding PE import and section tables. Key capabilities include runtime IAT reconstruction via live memory tracing, OEP discovery with MSVC CRT and Go/Delphi heuristics, optional ScyllaHide integration to bypass anti-debugging on newer builds, and a verify mode that diffs unpacked output against a known-good reference. Aimed at reverse engineers and game-security researchers analyzing Themida-protected binaries. (source: wiki/sources/descriptions/guoxing2024__magicmida-rs.md)

Companion surface to Cheat → Fix Themida work ([[themida-research]] VM internals, [[tde]] IDA devirtualization): debugger-driven automatic unpack + IAT/OEP rebuild rather than VM handler lifting or plugin recovery.

## Links

- Repo: https://github.com/guoxing2024/magicmida-rs

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[magicmida]] · [[themida-research]] · [[tde]] · [[vmpunpacker]] · [[xvolkolak]] · [[unmapper]]
