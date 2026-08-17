---
title: Mixed Boolean-Arithmetic
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/mizt0__mixed-boolean-transform.md
  - wiki/sources/descriptions/gmh5225__qsynthesis.md
  - wiki/sources/descriptions/fvrmatteo__DrillAndJoin.md
  - wiki/sources/descriptions/dmaivel__covirt.md
  - wiki/sources/descriptions/bliutech__mbased.md
updated: 2026-08-17
confidence: high
---

# Mixed Boolean-Arithmetic

**MBA** obfuscation replaces simple arithmetic with equivalent expressions mixing bitwise (`&`, `|`, `^`, `~`) and integer (`+`, `-`, `*`) operators. Common in VMProtect, Themida, custom LLVM passes, and AC compile-time obfuscators. Static decompilers often emit unreadable pseudocode until expressions are simplified. (source: wiki/sources/skills/reverse-engineering.md)

## Variants

- **Linear MBA:** e.g. `x + y = (x ^ y) + 2*(x & y)` — single-degree boolean/arithmetic mix.
- **Polynomial MBA:** higher-degree expressions over the same operator set — harder for pattern matchers.

## Recovery approaches

1. **Algebraic simplification** — coefficient reconstruction and term cancellation ([[cobra]]; SSPAM, MBA-Blast, SiMBA in the broader corpus); practical MBA expression reduction via [[mbased]] (source: wiki/sources/descriptions/bliutech__mbased.md).
2. **Program synthesis** — oracle-guided expression search with SMT equivalence checks in IDA via [[qsynthesis]] (Python; Hex-Rays integration) (source: wiki/sources/descriptions/gmh5225__qsynthesis.md); exact finite-domain Drill & Join synthesis plus Bitwuzla equivalence proofs for 64-bit opaque predicates and MBA-style expressions via [[drill-and-join]] (C++17 header-only; SMT-guided bit dependency reduction) (source: wiki/sources/descriptions/fvrmatteo__DrillAndJoin.md).
3. **Backward slicing + oracle lookup** — slice MBA regions, query msynth-style tables ([[obfuscation-analysis]]).
4. **SMT/bitvector solvers** — prove equivalence or find simplifying substitutions ([[stp]], Z3 backends).
5. **Sample generation for testing** — synthesize MBA expressions to validate simplifier pipelines ([[mutaben]], [[mba-obfuscator]]); source-level constant/arithmetic replacement with Z3-verified polynomial MBA via [[mixed-boolean-transform]] (C++; Eigen3 + GMP) (source: wiki/sources/descriptions/mizt0__mixed-boolean-transform.md). VM-based protectors such as [[covirt]] embed MBA transforms inside stack-VM obfuscation passes for protected regions (source: wiki/sources/descriptions/dmaivel__covirt.md).

## Detection context

MBA-heavy regions often co-occur with [[control-flow-flattening]] and opaque predicates. Binary Ninja heuristics in [[obfuscation-detection]] and analysis passes in [[obfuscation-analysis]] help locate MBA blocks before manual simplification.

## Related

[[cobra]] · [[mbased]] · [[qsynthesis]] · [[drill-and-join]] · [[mutaben]] · [[mba-obfuscator]] · [[mixed-boolean-transform]] · [[covirt]] · [[obfuscation-analysis]] · [[stp]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
