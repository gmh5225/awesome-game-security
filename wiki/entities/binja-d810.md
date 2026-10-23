---
title: binja-d810
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MZHeader__binja-d810.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: high
---

# binja-d810

Binary Ninja plugin (Python) that deobfuscates protected native code at **MLIL/HLIL** lift time—simplifying mixed boolean-arithmetic expressions, folding opaque predicates, and recovering OLLVM-style control-flow flattening without rewriting the on-disk binary. Uses D-810-style MBA rules, a built-in linear MBA simplifier, and optional Trail of Bits [[cobra]]; **Z3** proofs gate condition folding and rule application. Targets OLLVM substitution, Hikari indirect branches, scratch-slot and allocation round trips, flag-based comparisons, and flattened dispatchers on **x86, x64, and ARM64** PE, ELF, and Mach-O. Primary audience: reverse engineers and game-security analysts who need clearer HLIL through commercial packers, anti-tamper, and similar obfuscation in malware or protected game clients. Cheat / Fix OLLVM lane. (source: wiki/sources/descriptions/MZHeader__binja-d810.md)

## Capabilities

- Verified rewrites in **MLIL** and **HLIL** passes (in-memory IR only; no patched binaries).
- MBA simplification via D-810-style rule sets plus a built-in **linear MBA** reducer; optional [[cobra]] integration.
- **Opaque-predicate** folding and **CFF** recovery aligned with OLLVM-style flattening and Hikari-style indirect control flow.
- **Z3-backed** checks before applying condition folds and rewrite rules (fail-closed rule application).

## Use cases

Pair with Binary Ninja headless or GUI workflows when IDA/Hex-Rays [[d810]] / [[d810-ng]] or [[oo0l1ivvmm]] are unavailable but the analyst needs D-810-class lift-time deobfuscation on packed or anti-tamper game modules. Complements [[mixed-boolean-arithmetic]] and [[control-flow-flattening]] concept pages; see [[overviews/reverse-engineering]] obfuscation recovery table.

## Links

- Repo: https://github.com/MZHeader/binja-d810

## Related

[[d810]] · [[d810-ng]] · [[oo0l1ivvmm]] · [[cobra]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
