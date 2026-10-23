---
title: binja-d810
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MZHeader__binja-d810.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: medium
---

# binja-d810

Binary Ninja plugin (Python) that deobfuscates protected native code at **MLIL/HLIL** lift time—simplifying mixed boolean-arithmetic expressions, folding opaque predicates, and recovering OLLVM-style control-flow flattening without rewriting the on-disk binary. Uses D-810-style MBA rules, a built-in linear MBA simplifier, and optional Trail of Bits [[cobra]]; Z3 proofs gate condition folding and rule application. Targets OLLVM substitution, Hikari indirect branches, scratch-slot round trips, flag-based comparisons, and flattened dispatchers on x86/x64/ARM64 PE, ELF, and Mach-O. Cheat / Fix OLLVM lane for game-security analysts working through commercial packers and anti-tamper in protected clients. (source: wiki/sources/descriptions/MZHeader__binja-d810.md)

## Links

- Repo: https://github.com/MZHeader/binja-d810

## Related

[[d810]] · [[d810-ng]] · [[oo0l1ivvmm]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
