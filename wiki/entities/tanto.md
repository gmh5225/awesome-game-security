---
title: tanto
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/Vector35__tanto.md
updated: 2026-08-19
confidence: medium
---

# tanto

Binary Ninja plugin for **program slicing** to speed up code comprehension during reverse engineering (Vector35). Implemented mainly in Python, it integrates with Binary Ninja UI views and intermediate-language representations so analysts can inspect variable and block relationships through focused slices instead of navigating full-function complexity. Target audience: reverse engineers and vulnerability researchers who need faster navigation of complex binaries. (source: wiki/sources/descriptions/Vector35__tanto.md)

Complements other BN analysis plugins such as [[workflow-objc]] (ObjC dispatch cleanup), [[obfuscation-analysis]] (backward slicing for MBA/opaque predicates), and agent transports such as [[binary-ninja-mcp]] and [[bn]].

## Links

- Repo: https://github.com/Vector35/tanto

## Related

[[overviews/reverse-engineering]] · [[workflow-objc]] · [[obfuscation-analysis]] · [[binary-ninja-mcp]] · [[bn]] · [[triton-bn]] · [[seninja]]
