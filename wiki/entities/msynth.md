---
title: msynth
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/mrphrazer__msynth.md
updated: 2026-09-11
confidence: medium
---

# msynth

**msynth** (mrphrazer) is a Python **Mixed Boolean-Arithmetic (MBA)** deobfuscation framework that reduces complex bitwise and arithmetic formulas to shorter equivalent forms. It walks expression abstract syntax trees and applies **oracle-backed algebraic and semantic rewrites** using large pre-computed lookup tables, or alternatively learns equivalent expressions through **stochastic program synthesis** augmented with Search Modulo Inference Rules (**Smir**). Built on **Miasm** with optional symbolic-execution integration, it incorporates techniques such as **SiMBA** and **GAMBA**, supports parallel processing, and can verify simplifications with an **SMT solver**. It targets reverse engineers and binary analysts recovering readable semantics from MBA-heavy obfuscation in protected software. (source: wiki/sources/descriptions/mrphrazer__msynth.md)

The same author's Binary Ninja plugin [[obfuscation-analysis]] uses backward slicing plus msynth-style oracle lookup for in-IL MBA simplification workflows.

## Links

- Repo: https://github.com/mrphrazer/msynth (README: MBA deobfuscation framework using pre-computed oracles, algebraic simplification, and stochastic program synthesis; integrates with Miasm symbolic execution)

## Related

[[mixed-boolean-arithmetic]] · [[gamba]] · [[goomba]] · [[obfuscation-analysis]] · [[qsynthesis]] · [[promba]] · [[overviews/reverse-engineering]]
