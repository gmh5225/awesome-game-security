---
title: scc
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Vector35__scc.md
updated: 2026-08-19
confidence: medium
---

# scc

Open-source **shellcode compiler** from Vector35, originally an internal CTF tool and later integrated into Binary Ninja. Implemented mainly in C/C++ with CMake, it focuses on producing compact shellcode-oriented output and ships dedicated usage and build documentation. Most useful for exploit development and reverse-engineering workflows that need controlled low-level code generation rather than hand-written assembly. (source: wiki/sources/descriptions/Vector35__scc.md)

Complements in-process asm prototyping such as [[quickasm]], cross-platform shellcode frameworks such as [[scfw]], and Binary Ninja analysis tooling such as [[binary-ninja-mcp]], [[bn]], and [[tanto]].

## Links

- Repo: https://github.com/Vector35/scc

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[quickasm]] · [[scfw]] · [[shellcode-factory]] · [[obj2shellcode]] · [[binary-ninja-mcp]] · [[bn]] · [[tanto]]
