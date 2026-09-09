---
title: Dragons vs VMs
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Fare9__Dragons-vs-VMs.md
  - wiki/sources/README-categories.md
updated: 2026-09-09
confidence: medium
---

# Dragons vs VMs

Research project and toolkit (Fare9) for analyzing and **devirtualizing VMProtect-protected x64 binaries**, demonstrated on a serial-check sample protected with VMProtect. Python scripts integrate with **Binary Ninja** to trace the virtual machine, catalog and rename all **256 VM handlers**, lift handler semantics through the **dragon-tales** pipeline into **IGNIL** and **LLVM IR**, and run **symbolic execution with Z3** to recover simplified effects. Ships devirtualized LLVM output, handler documentation with x86, intermediate, and symbolic views, and utilities for recompilation and constraint solving. Targets reverse engineers and game security researchers who need to unpack, understand, or bypass commercial VM-based code protection. (source: wiki/sources/descriptions/Fare9__Dragons-vs-VMs.md)

Listed under Cheat **Fix VMP** beside emulation-first lifts such as [[vmplift]], static VTIL devirtualizers such as [[novmp]], and trace/symbolic paths such as [[titan]] and [[vmprotect-devirtualization]].

## Pipeline

1. Trace the VMProtect virtual machine in Binary Ninja.
2. Catalog and rename all 256 handler slots.
3. Lift handler semantics via dragon-tales into IGNIL and LLVM IR.
4. Run Z3 symbolic execution to recover simplified handler effects.
5. Emit devirtualized LLVM, handler docs (x86 / intermediate / symbolic views), and recompilation utilities.

## Links

- Repo: https://github.com/fare9/dragons-vs-vms

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmplift]] · [[novmp]] · [[titan]] · [[vmprotect-devirtualization]] · [[vmp-devirtualization-lab]] · [[mixed-boolean-arithmetic]]
