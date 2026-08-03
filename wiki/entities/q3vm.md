---
title: q3vm
kind: entity
topics: [anti-cheat, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/jnz__q3vm.md
updated: 2026-08-03
confidence: medium
---

# q3vm

Lightweight, embeddable **Quake III virtual machine** implementation: a single-file (`vm.c`) interpreter for compiled `.qvm` bytecode, plus an included **LCC**-based C compiler toolchain that turns restricted C source into `.qvm` modules. Derived from the classic id Tech 3 script VM used for game logic sandboxing. (source: wiki/sources/descriptions/jnz__q3vm.md)

Aimed at **anti-cheat engineers** and defensive security researchers building or studying **dynamic script** and sandboxed bytecode execution in AC products—prototyping detection logic that runs inside a controlled VM rather than as native code. Complements historical AC bytecode VMs such as [[valveanticheat1]] (GoldSrc VAC1 ModuleC/ModuleS) and kernel dynamic-script experiments such as [[ntphp]] on the prototyping side; differs from commercial packer VMs ([[nocturne]], VMProtect/Themida) which obfuscate native code.

## Links

- Repo: https://github.com/jnz/q3vm

## Related

[[valveanticheat1]] · [[ntphp]] · [[godot-sandbox]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
