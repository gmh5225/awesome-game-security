---
title: Binary Evidence
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/mytechnotalent__rea.md
  - wiki/sources/descriptions/formix__sre-re.md
  - wiki/sources/descriptions/Battelle__cantordust.md
  - wiki/sources/descriptions/t1zzo__classrevive.md
updated: 2026-11-01
confidence: high
---

# Binary Evidence

Discipline for framing **what a binary artifact can prove** before converting static views, debugger observations, or diff output into security conclusions. Pair with [[static-runtime-evidence]] for artifact baseline and static/runtime separation, [[research-rigor]], and [[overviews/reverse-engineering]] when reporting interface abuse, integrity findings, obfuscation, anti-analysis behavior, or build-to-build changes. (source: wiki/sources/skills/reverse-engineering.md)

## Provenance to preserve

Record sample hash, provenance, architecture, image layout, tool version, analysis configuration, and symbol identity. Keep **file offsets**, **RVAs**, and **runtime addresses** distinct, including relocation assumptions in disk/memory comparisons. Match symbols to the actual binary—public and private symbol sets expose different information.

Decompiler output is a **reconstruction**. Validate inferred types, names, prototypes, and function boundaries against instructions, ABI constraints, and available observations. Ghidra instruction semantics and p-code explain why displayed C is not recovered source. For JVM bytecode, [[classrevive]] ranks CFR/Vineflower/Procyon/JADX candidates by recompiling with `javac` and checking signature/round-trip fit against original classfiles—structurally verifiable recovery is stronger evidence than a single-engine decompile alone. (source: wiki/sources/descriptions/t1zzo__classrevive.md) Legacy game-rule recovery such as [[sre-re]] (DOS BBS door binary; turn-by-turn mechanics transcribed from decompilation) pairs static Ghidra work with **DOSBox re-execution** to verify formulas before treating recovered specs as findings rather than hypotheses. (source: wiki/sources/descriptions/formix__sre-re.md)

Byte-level **visualization** (trigram clouds, metric maps, linear bitmaps—e.g. [[cantordust]] in Ghidra or standalone) accelerates **hypothesis generation** about where code, data, or embedded artifacts live; treat highlighted regions as pointers for disassembly or runtime checks, not standalone proof of behavior. (source: wiki/sources/descriptions/Battelle__cantordust.md)

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

Agent-assisted **first-pass triage** tools such as [[rea-mytechnotalent]] (offline PE/ELF/Mach-O + JS/Electron inventory, local RAG, propose–review–gate multi-agent workflow) still owe the same granularity: each automated claim should cite static artifacts (imports, strings, section layout) rather than collapsing imported API, reachable path, and observed call. (source: wiki/sources/descriptions/mytechnotalent__rea.md)

## Related

[[static-runtime-evidence]] · [[research-rigor]] · [[binary-diffing]] · [[dynamic-binary-instrumentation]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[rea-mytechnotalent]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
