---
title: Polymorphic-Engine
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Nou4r__Polymorphic-Engine.md
updated: 2026-08-22
confidence: medium
---

# Polymorphic-Engine

**Nou4r** prototype **C++ runtime polymorphism and obfuscation framework** for protecting **in-memory variables**. Supports stack and heap transformations across multiple primitive and string types, with optional **SIMD** type support in extended builds. Targets **LLVM/Clang** most strongly; includes experimental **MSVC** compatibility and example code. Primary use case is software protection experimentation and anti-analysis research in low-level security contexts—not a commercial protector or turnkey AC product. (source: wiki/sources/descriptions/Nou4r__Polymorphic-Engine.md)

Contrasts with compile-time Encrypt Variable libraries such as [[obfuscxx]] / [[encrypted-value]] / [[xv]] by mutating variable representations at runtime. Sits in the Anti Cheat → Encrypt Variable / Obfuscation Engine lane beside Nou4r injection and external samples such as [[present-injector]] and [[pkernelinterface-eft]].

## Links

- Repo: https://github.com/Nou4r/Polymorphic-Engine (README tag: Prototype runtime C++ polymorphic type engine)

## Related

[[obfuscxx]] · [[encrypted-value]] · [[xv]] · [[kernelcloak]] · [[obfusheader-h]] · [[present-injector]] · [[pkernelinterface-eft]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
