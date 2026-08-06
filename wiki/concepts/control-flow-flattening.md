---
title: Control Flow Flattening
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/guheng-re__unflat.md
updated: 2026-08-06
confidence: high
---

# Control Flow Flattening

**CFF** (control-flow flattening) reroutes many basic blocks through a central **dispatcher loop** with a state variable, destroying natural if/else and loop structure in static decompilers. OLLVM-style CFF is common in game clients, AC modules, and LLVM pass-plugin protectors ([[kagura]], [[the-poor-mans-obfuscator]], [[obscura]]). Variants include nested dispatchers and encrypted state variables. (source: wiki/sources/skills/reverse-engineering.md)

## Recovery approaches

1. **Symbolic execution + pattern matching** — identify dispatcher, recover real edges ([[idadeflat]] with angr).
2. **Decompiler-time deflattening** — Hex-Rays passes at lift time ([[d810-ng]]).
3. **External OBPO backends** — closed-core simplification with open IDA client ([[obpo-plugin]]).
4. **Python unflattener plugins** — extensible Fix OLLVM unflatten hooks ([[unflat]]; plugin development focus). (source: wiki/sources/descriptions/guheng-re__unflat.md)
5. **Heuristic region detection** — loop/dominator analysis and BB complexity scoring ([[obfuscation-detection]]) before manual work.
6. **Trace-based recovery** — runtime traces from [[dynamic-binary-instrumentation]] resolve indirect branches under covered executions; completeness needs additional path exploration.

CFF often co-occurs with [[mixed-boolean-arithmetic]] and opaque predicates — simplify MBA blocks after CFG recovery for readable pseudocode.

## Related

[[idadeflat]] · [[d810-ng]] · [[obpo-plugin]] · [[unflat]] · [[obfuscation-detection]] · [[obfuscation-analysis]] · [[mixed-boolean-arithmetic]] · [[dynamic-binary-instrumentation]] · [[overviews/reverse-engineering]]
