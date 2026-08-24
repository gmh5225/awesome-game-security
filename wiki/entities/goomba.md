---
title: goomba
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/HexRaysSA__goomba.md
updated: 2026-08-24
confidence: medium
---

# goomba

**goomba** (HexRaysSA) is a **Hex-Rays decompiler plugin** for simplifying **mixed Boolean-arithmetic (MBA)** obfuscation in decompiled pseudocode. Written in C++, it integrates directly into **IDA Pro** and Hex-Rays workflows. The plugin combines algebraic heuristics, linear and non-linear MBA simplification, and optional fingerprint-oracle support, and uses the **Z3 SMT solver** to verify simplification soundness—making it useful for reliable deobfuscation during reverse engineering of protected game and malware binaries. (source: wiki/sources/descriptions/HexRaysSA__goomba.md)

Complements other Hex-Rays deobfuscation plugins such as [[hex-rays-deob]] and [[hrtng]], synthesis-oriented MBA tools such as [[promba]] and [[qsynthesis]], and algebraic simplifiers such as [[cobra]] and [[mbased]].

## Links

- Repo: https://github.com/HexRaysSA/goomba

## Related

[[mixed-boolean-arithmetic]] · [[hex-rays-deob]] · [[hrtng]] · [[promba]] · [[qsynthesis]] · [[cobra]] · [[mbased]] · [[genmc]] · [[obfuscation-analysis]] · [[overviews/reverse-engineering]]
