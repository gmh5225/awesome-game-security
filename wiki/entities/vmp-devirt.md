---
title: VMP_DEVIRT
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# VMP_DEVIRT

Integrated **research framework** for analyzing, unpacking, and devirtualizing **64-bit** binaries protected by commercial VM obfuscators including **VMProtect 3.x**, **Themida 3.x**, and **Tigress**. Combines Chosen-Instruction Attack knowledge extraction, VPC-sensitive symbolic tracing, **Triton** concolic execution, and **MBA** simplification to recover handler semantics and virtual control flow. The AETHER pipeline applies algebraic pre-reduction, virtual stack elimination, and **LLVM IR** lifting with compiler optimization passes to emit readable native x64 code. Python and C++ (CMake), **Z3** SMT proofs, optional CIA automation and benchmarking submodules. (source: wiki/sources/descriptions/Aetherx86__VMP_DEVIRT.md)

Listed under Cheat **Fix VMP** beside static VTIL lifts ([[novmp]]), emulation-first handler walkers ([[vmplift]]), and trace/symbolic paths ([[titan]], [[vmprotect-devirtualization]]).

## Links

- Repo: https://github.com/Aetherx86/VMP_DEVIRT

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[novmp]] · [[vmplift]] · [[titan]] · [[vmprotect-devirtualization]] · [[vmp-devirtualization-lab]] · [[mixed-boolean-arithmetic]]
