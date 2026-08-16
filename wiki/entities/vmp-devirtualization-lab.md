---
title: vmp-devirtualization-lab
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/tomhamidi97-arch__vmp-devirtualization-lab.md
updated: 2026-08-16
confidence: medium
---

# vmp-devirtualization-lab

Educational guide and hands-on lab for analyzing **Virtual Machine Protection on Android native libraries**—how VMP replaces native code with custom bytecode and how to reverse that process. Includes a reproducible mini-VM in C with a switch-based dispatcher plus Python tooling to disassemble bytecode and lift it back to readable logic. (source: wiki/sources/descriptions/tomhamidi97-arch__vmp-devirtualization-lab.md)

Covers the full devirtualization workflow: locating dispatchers, enumerating handlers, symbolic lifting, trace-driven analysis, and differential testing using QBDI, Unicorn, Triton, Frida, IDA, Ghidra, and angr. Also surveys real-world protectors (VMProtect, OLLVM forks, Tigress, mobile packers) and companion obfuscations such as [[control-flow-flattening]], [[mixed-boolean-arithmetic]], and anti-debug techniques. Aimed at authorized security researchers, reverse engineers, and CTF participants studying native anti-tamper on Android and related game-security targets.

## Links

- Repo: https://github.com/tomhamidi97-arch/vmp-devirtualization-lab

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[vmprotect]] · [[novmpy]] · [[rumba]] · [[vmattack]] · [[control-flow-flattening]] · [[mixed-boolean-arithmetic]] · [[frida]]
