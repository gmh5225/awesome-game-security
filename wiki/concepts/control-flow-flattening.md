---
title: Control Flow Flattening
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/guheng-re__unflat.md
  - wiki/sources/descriptions/es3n1n__obfuscator.md
  - wiki/sources/descriptions/dronavallipranav__rust-obfuscator.md
updated: 2026-08-16
confidence: high
---

# Control Flow Flattening

**CFF** (control-flow flattening) reroutes many basic blocks through a central **dispatcher loop** with a state variable, destroying natural if/else and loop structure in static decompilers. OLLVM-style CFF is common in game clients, AC modules, and LLVM pass-plugin protectors ([[kagura]], [[the-poor-mans-obfuscator]], [[obscura]]). Source-level Rust CFF via proc macros such as [[rust-obfuscator]] (`labyrinth_macros`; automatic project-wide insertion) complements IR and binary flattening. Post-compile PE obfuscators such as [[obfuscator]] and [[alcatraz]] apply CFF passes at the binary level without source. Variants include nested dispatchers and encrypted state variables. (source: wiki/sources/skills/reverse-engineering.md) (source: wiki/sources/descriptions/es3n1n__obfuscator.md) (source: wiki/sources/descriptions/dronavallipranav__rust-obfuscator.md)

## Recovery approaches

1. **Symbolic execution + pattern matching** — identify dispatcher, recover real edges ([[idadeflat]] with angr).
2. **Decompiler-time deflattening** — Hex-Rays passes at lift time ([[d810-ng]]).
3. **External OBPO backends** — closed-core simplification with open IDA client ([[obpo-plugin]]).
4. **Python unflattener plugins** — extensible Fix OLLVM unflatten hooks ([[unflat]]; plugin development focus). (source: wiki/sources/descriptions/guheng-re__unflat.md)
5. **Heuristic region detection** — loop/dominator analysis and BB complexity scoring ([[obfuscation-detection]]) before manual work.
6. **Trace-based recovery** — runtime traces from [[dynamic-binary-instrumentation]] resolve indirect branches under covered executions; completeness needs additional path exploration.

CFF often co-occurs with [[mixed-boolean-arithmetic]] and opaque predicates — simplify MBA blocks after CFG recovery for readable pseudocode.

## Related

[[idadeflat]] · [[d810-ng]] · [[obpo-plugin]] · [[unflat]] · [[obfuscator]] · [[rust-obfuscator]] · [[alcatraz]] · [[obfuscation-detection]] · [[obfuscation-analysis]] · [[mixed-boolean-arithmetic]] · [[dynamic-binary-instrumentation]] · [[overviews/reverse-engineering]]
