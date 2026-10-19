---
title: ORRESS
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/okiedocus__orress.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# ORRESS

**ORRESS** (Okiedocus Rusty Reverse Engineering Software Suite) is a pure-Rust integrated development environment for reverse engineering and binary analysis. It loads PE, ELF, Mach-O, .NET, Java, DEX, WebAssembly, and related formats. (source: wiki/sources/descriptions/okiedocus__orress.md)

## Capabilities

- **Static:** x86/x86-64 and ARM64 disassembly, control-flow graphs, cross-references, and a decompiler that can emit compilable Rust.
- **Dynamic:** native debugging; x86-64 emulator with time-travel tracing; symbolic solving.
- **Triage & patch:** YARA-X malware triage with sandboxing; built-in assembler, patcher, and transform workbench.
- **Automation:** Zed-style extensions and Rhai scripting.
- **Training:** **ORRESS Academy** — guided lessons and crackmes for static/dynamic analysis, including anti-debugging topics.

## Audience

Reverse engineers, malware analysts, CTF players, and anyone who wants a self-contained toolkit for understanding and modifying compiled software — beside GUI-centric suites such as [[ceasta]], [[n0xis]], and [[sako-restudio]]. (source: wiki/sources/descriptions/okiedocus__orress.md)

## Links

- Repo: https://github.com/okiedocus/orress

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[n0xis]] · [[ceasta]] · [[sako-restudio]] · [[disrobe]]
