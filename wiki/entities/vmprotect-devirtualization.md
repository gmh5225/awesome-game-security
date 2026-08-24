---
title: VMProtect-devirtualization
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JonathanSalwan__VMProtect-devirtualization.md
updated: 2026-08-24
confidence: medium
---

# VMProtect-devirtualization

Experimental **dynamic devirtualization** workflow for recovering the original logic of **pure functions** protected by VMProtect 3.x code virtualization. An Intel Pin-based tracer records execution, then the Triton symbolic execution engine builds path predicates and input–output relations while concretizing VM machinery noise. Recovered expressions can be synthesized and lifted to LLVM IR so LLVM optimizations simplify embedded **MBA-style obfuscation** and emit a cleaner unprotected form. Notes and sample scripts target reverse engineers analyzing virtualized binaries and researching dynamic attacks against commercial protectors. (source: wiki/sources/descriptions/JonathanSalwan__VMProtect-devirtualization.md)

Complements static VTIL lift via [[novmp]], trace-driven handler recovery in [[novmpy]] and [[rumba]], and LLVM-oriented devirt via [[titan]]—here the emphasis is Pin trace capture plus Triton symbolic analysis on VMProtect 3.x pure-function targets rather than full-module static lift or Android lab workflows such as [[vmp-devirtualization-lab]].

## Links

- Repo: https://github.com/JonathanSalwan/VMProtect-devirtualization

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[titan]] · [[novmpy]] · [[novmp]] · [[rumba]] · [[vmp-devirtualization-lab]] · [[mixed-boolean-arithmetic]]
