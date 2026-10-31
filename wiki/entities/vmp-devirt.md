---
title: VMP_DEVIRT
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# VMP_DEVIRT

[Aetherx86/VMP_DEVIRT](https://github.com/Aetherx86/VMP_DEVIRT) — integrated **research framework** for analyzing, unpacking, and devirtualizing **64-bit** binaries protected by commercial VM obfuscators including **VMProtect 3.x**, **Themida 3.x**, and **Tigress**. Aimed at reverse engineers, malware analysts, and security researchers who need automated deobfuscation of virtualization packers in software protection and anti-tamper scenarios. (source: wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md)

## Analysis stack

| Technique | Role |
|-----------|------|
| **Chosen-Instruction Attack (CIA)** | Knowledge extraction from protected VM bytecode |
| **VPC-sensitive symbolic tracing** | Virtual program-counter–aware trace for handler boundaries |
| **Triton concolic execution** | Path exploration and handler semantics recovery |
| **MBA simplification** | Mixed Boolean-Arithmetic reduction on virtualized expressions |
| **Z3 SMT proofs** | Equivalence and constraint validation |

Optional submodules cover CIA automation, benchmarking datasets, and related academic toolchains. (source: wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md)

## AETHER pipeline

Algebraic pre-reduction and **virtual stack elimination** feed **LLVM IR** lifting; compiler optimization passes emit readable native **x64** code from recovered virtual control flow and handler semantics. (source: wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md)

## Implementation

Primarily **Python** and **C++** with **CMake**-built components. (source: wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md)

## Positioning

Listed under Cheat **Fix VMP** beside static VTIL lifts ([[novmp]]), emulation-first handler walkers ([[vmplift]]), Pin/Triton pure-function devirt ([[vmprotect-devirtualization]]), and trace/symbolic paths ([[titan]], [[dragons-vs-vms]]). Broader Themida unpack tooling includes [[themida-unmutate]] and [[unthemidator]].

## Links

- Repo: https://github.com/Aetherx86/VMP_DEVIRT

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[novmp]] · [[vmplift]] · [[titan]] · [[vmprotect-devirtualization]] · [[vmp-devirtualization-lab]] · [[mixed-boolean-arithmetic]] · [[triton]]
