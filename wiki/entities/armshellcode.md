---
title: ArmShellCode
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/IIIImmmyyy__ArmShellCode.md
updated: 2026-08-24
confidence: medium
---

# ArmShellCode

**ArmShellCode** (IIIImmmyyy) is an **ARM64 shellcode framework for Android** that builds **position-independent** native payloads for **arm64-v8a**. The C codebase includes **ELF parsing**, **`/proc/maps` parsing**, **syscall wrappers**, and a **modular shellcode loader** with **custom linker scripts** for generating standalone shellcode blobs. Uses **[[dobby]]**-based symbol resolution at runtime. Targets Android security researchers and exploit developers studying **ARM64 shellcode construction** and **runtime code injection**. README tag: `[Android arm arm64-v8a ShellCode Generate]`. (source: wiki/sources/descriptions/IIIImmmyyy__ArmShellCode.md)

Complements offline ARM64 ELF patch/hook tooling such as [[elf-got-patcher]] and [[pyasm-patch]], and runtime inject frameworks such as [[adbi]] and [[android-super-inject]].

## Links

- Repo: https://github.com/IIIImmmyyy/ArmShellCode

## Related

[[dobby]] · [[elf-got-patcher]] · [[pyasm-patch]] · [[adbi]] · [[and64-inline-hook]] · [[android-super-inject]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
