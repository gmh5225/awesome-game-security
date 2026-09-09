---
title: Binary Evidence
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
updated: 2026-09-09
confidence: high
---

# Binary Evidence

Discipline for framing **what a binary artifact can prove** before converting static views, debugger observations, or diff output into security conclusions. Pair with [[research-rigor]] and [[overviews/reverse-engineering]] when reporting interface abuse, integrity findings, obfuscation, anti-analysis behavior, or build-to-build changes. (source: wiki/sources/skills/reverse-engineering.md)

## Provenance to preserve

Record sample hash, provenance, architecture, image layout, tool version, analysis configuration, and symbol identity. Keep **file offsets**, **RVAs**, and **runtime addresses** distinct, including relocation assumptions in disk/memory comparisons. Match symbols to the actual binary—public and private symbol sets expose different information.

Decompiler output is a **reconstruction**. Validate inferred types, names, prototypes, and function boundaries against instructions, ABI constraints, and available observations. Ghidra instruction semantics and p-code explain why displayed C is not recovered source.

## Question classification

Classify the investigative question before selecting tools or stating limits:

| Question | Evidence to develop | Limit to state |
|----------|---------------------|----------------|
| Interface abuse | Input origin, callers, required privilege, validation and protected resource | Reachable code is not proof of invocation or abuse |
| Integrity tampering | Independently acquired comparison data and collector trust | A compromised or incomplete collector can distort results |
| Packing/obfuscation | Representation changes and uncertainty in recovered structure | Obfuscation alone does not establish maliciousness |
| Anti-analysis behavior | Conditions associated with differing execution | Observation coverage may be limited by the environment |
| Security-relevant binary change | Semantic differences and affected trust boundary | Compiler, library, and layout changes can dominate a diff |

## Finding granularity

Report supporting addresses/artifacts and explain each inference. Treat these as **distinct findings**:

- **Imported API** — symbol/import table or loader resolution evidence
- **Reachable path** — static or symbolic reachability under stated assumptions
- **Observed call** — dynamic trace, breakpoint hit, or hook confirmation under recorded conditions

Preserve missing symbols, incomplete dumps, generated code, and unexecuted paths as explicit limitations.

## Related

[[research-rigor]] · [[binary-diffing]] · [[dynamic-binary-instrumentation]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
