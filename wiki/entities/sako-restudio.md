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

**Sako RE Studio** is a mobile-first Android reverse-engineering suite that packs disassembler, decompiler, debugger, and APK analysis into a single offline app. Targets reverse engineers, mobile security researchers, and analysts who need IDA Pro or Ghidra-like capabilities on a phone or tablet without sending binaries off-device. (source: wiki/sources/descriptions/Maxamedxasa__SakoREStudio.md)

## Capabilities

- **Interactive disassembler** — Capstone-backed assembly views with control-flow graphs on ARM64 and x86-64.
- **IR-based decompiler** — pseudo-C output from an internal intermediate representation.
- **Call-graph explorer** — navigate inter-procedural relationships across loaded binaries.
- **ptrace debugger** — attach and step native code on-device.
- **APK analyzer** — inspect Android packages alongside native formats.
- **SakoScript plugins** — built-in automation for security auditing, ARM analysis, DEX inspection, and string hunting; extensible plugin system.
- **Project persistence** — SQLite-backed project storage via Jetpack Compose UI.
- **Optional AI assistant** — explain functions locally or via OpenAI-compatible endpoints.

## Architecture

Native **C++17** engine handles binary parsing and analysis; **Kotlin Jetpack Compose** UI provides assembly, decompilation, CFG, and project management. Supports **APK**, **ELF**, **PE**, and **DEX** binaries. Entire workflow runs offline on the device.

Peers with Rust CLI+MCP mobile static analysis via [[glass]] and decode-oriented stacks such as [[jadx]] / [[apktool-mcp-server]]; complements memory-editor lanes such as [[charlyengine]] and desktop IDE stacks such as [[hikarisystem-hexcore]] and [[ghidra]] for field or air-gapped mobile RE.

## Links

- Repo: https://github.com/Maxamedxasa/SakoREStudio

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[charlyengine]] · [[glass]] · [[jadx]] · [[hikarisystem-hexcore]] · [[mobile-re-skill]]
