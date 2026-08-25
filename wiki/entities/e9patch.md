---
title: e9patch
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/GJDuck__e9patch.md
updated: 2026-08-25
confidence: medium
---

# e9patch

**E9Patch** is a static binary rewriting tool for **x86-64 Linux ELF** binaries. It can insert jumps, trampolines, and instrumentation at any instruction **without reassembly**, using instruction punning and eviction techniques to make room for patches in-place. Useful for reverse engineers and security researchers who need offline ELF instrumentation, hook injection, or trace/probe insertion when runtime DBI is impractical or blocked. (source: wiki/sources/descriptions/GJDuck__e9patch.md)

Complements x86 bin2bin rewrite frameworks such as [[stitch]] and PE-focused virtualizers such as [[nocturne]] on the Linux/native ELF lane, and contrasts with runtime DBI stacks covered under [[dynamic-binary-instrumentation]].

## Links

- Repo: https://github.com/GJDuck/e9patch

## Related

[[stitch]] · [[neverd]] · [[dynamic-binary-instrumentation]] · [[mambo]] · [[frida]] · [[overviews/reverse-engineering]]
