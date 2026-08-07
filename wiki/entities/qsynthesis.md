---
title: QSynthesis
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__qsynthesis.md
updated: 2026-08-07
confidence: medium
---

# QSynthesis

IDA Pro Python plugin that synthesizes simplified expressions from complex obfuscated code using **program synthesis**. Applies oracle-guided synthesis and SMT solving to find simpler equivalent forms for MBA (Mixed Boolean-Arithmetic) computations in protected binaries; integrates with Hex-Rays decompiler output for VM-protected or MBA-heavy targets. (source: wiki/sources/descriptions/gmh5225__qsynthesis.md)

Greybox synthesizer lane for assembly-instruction deobfuscation—complements algebraic MBA simplifiers such as [[cobra]] and Binary Ninja oracle/msynth workflows in [[obfuscation-analysis]].

## Links

- Repo: https://github.com/gmh5225/qsynthesis

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[mixed-boolean-arithmetic]] · [[cobra]] · [[obfuscation-analysis]] · [[ida-easy-life]] · [[stp]]
