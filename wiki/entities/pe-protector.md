---
title: pe-protector
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ATsahikian__pe-protector.md
updated: 2026-09-04
confidence: medium
---

# pe-protector

Windows PE protection framework designed to make executables harder to crack and analyze. Implemented mainly in C++, it provides instruction mutation, a built-in x86 assembler pipeline, configurable stub logic, and binary compression support. The repository also includes compiler components, tests, and CMake-based build tooling for reproducible development. Listed under Anti Cheat → Binary Packer (`[X86]`); primary use case is software protection research, anti-tamper experimentation, and understanding packer-style defense techniques. (source: wiki/sources/descriptions/ATsahikian__pe-protector.md)

Useful as an x86 PE protection-framework reference alongside [[pe-packer]], [[hm-pe-packer]], and [[packer-tutorial]]—not a commercial AC product or unpacker.

## Links

- Repo: https://github.com/ATsahikian/pe-protector

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pe-packer]] · [[hm-pe-packer]] · [[packer-tutorial]] · [[exe-packer]] · [[atom-pe-packer]]
