---
title: Import Wrapper Attack
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Ahora57__import_wrapper_attack.md
updated: 2026-11-20
confidence: medium
---

# Import Wrapper Attack

Windows **research PoC** (C++, Visual Studio) that attacks **import wrappers** used by **VMProtect**, **Themida**, and **WinLicense** instead of hooking transitions from application code into the protector’s VM. It scans protected processes, disassembles wrapper stubs with **Zydis**, and emulates obfuscated decode sequences with **Unicorn** to recover real API targets. Supporting modules handle import detection, protector identification, and x86/x64 analysis of `jmp`/`call` patterns that reference hidden imports. The sample demonstrates hooking shielded imports such as `MessageBoxW` for reverse engineers studying packer import obfuscation and anti-tamper defenses. (source: wiki/sources/descriptions/Ahora57__import_wrapper_attack.md)

Complements live-process import-stub recovery via [[vmpimportfixer]] and broader Fix VMP unpack/devirt tooling ([[vmprotect-unpacker]], [[unlicense]], [[bobalkkagi]]) by targeting wrapper-layer indirection rather than full unpack or handler devirtualization. Same author lane as userland anti-anti-debug timing research [[racecondition]].

## Links

- Repo: https://github.com/Ahora57/import_wrapper_attack (README: research PoC; Zydis + Unicorn; VMProtect / Themida–WinLicense import wrappers)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmpimportfixer]] · [[vmprotect]] · [[unlicense]] · [[bobalkkagi]] · [[racecondition]]