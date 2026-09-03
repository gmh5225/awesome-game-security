---
title: HikariSystem HexCore
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AkashaCorporation__HikariSystem-HexCore.md
updated: 2026-09-03
confidence: medium
---

# HikariSystem HexCore

**VS Code-based integrated development environment** for binary analysis, malware research, and reverse engineering. Bundles dozens of HexCore extensions—primarily TypeScript with C++ Node-API native engines—including Capstone disassembly, Unicorn CPU emulation, Remill lifting to LLVM IR, Rellic decompilation, Souper superoptimization, and YARA scanning with built-in anti-debug and obfuscation rules. Covers PE and ELF parsing, hex editing, string and XOR decryption, entropy analysis, minidump inspection, IOC extraction, and an HQL semantic query layer for anti-analysis patterns such as API hashing and VM checks. Headless automation via `.hexcore_job.json` supports batch disassembly, emulation, and reporting; includes agent integration. Aimed at malware analysts, reverse engineers, and security researchers who want one desktop environment from static inspection through dynamic emulation and decompilation. (source: wiki/sources/descriptions/AkashaCorporation__HikariSystem-HexCore.md)

Unified RE workbench rather than a single-purpose plugin; complements disassembler hosts such as [[ghidra]] and [[x64dbg]], headless IDA automation such as [[headless-ida]], YARA authoring tools such as [[yarka]] and [[yara4ida]], and Unicorn-based emulation samples such as [[unicorn-pe]].

## Links

- Repo: https://github.com/AkashaCorporation/HikariSystem-HexCore

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[headless-ida]] · [[yarka]] · [[unicorn-pe]] · [[awesome-ghidra]]
