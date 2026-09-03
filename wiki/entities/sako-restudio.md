---
title: Sako RE Studio
kind: entity
topics: [reverse-engineering, mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Maxamedxasa__SakoREStudio.md
  - wiki/sources/README-categories.md
updated: 2026-09-03
confidence: medium
---

# Sako RE Studio

Mobile-first Android reverse-engineering suite combining an interactive disassembler, IR-based decompiler, call-graph explorer, ptrace debugger, APK analyzer, and extensible SakoScript plugin system in a single offline app. Native C++17 engine (Capstone) supports APK, ELF, PE, and DEX on ARM64 and x86-64; Kotlin Jetpack Compose UI provides assembly views, pseudo-C decompilation, control-flow graphs, and SQLite-backed project persistence. Built-in plugins automate security auditing, ARM analysis, DEX inspection, and string hunting; optional AI assistant explains functions locally or via OpenAI-compatible endpoints. Targets analysts who need IDA/Ghidra-like capabilities on a phone or tablet without sending binaries off-device. (source: wiki/sources/descriptions/Maxamedxasa__SakoREStudio.md)

Peers with Rust CLI+MCP mobile static analysis via [[glass]] and decode-oriented stacks such as [[jadx]] / [[apktool-mcp-server]]; complements desktop IDE lanes such as [[hikarisystem-hexcore]] and [[ghidra]] for field or air-gapped mobile RE.

## Links

- Repo: https://github.com/Maxamedxasa/SakoREStudio

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[glass]] · [[jadx]] · [[hikarisystem-hexcore]] · [[mobile-re-skill]]
