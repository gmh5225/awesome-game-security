---
title: kernel-codecave-poc
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/rogerxiii__kernel-codecave-poc.md
updated: 2026-07-24
confidence: medium
---

# kernel-codecave-poc

Windows kernel PoC that hides executable code in **code caves** (unused padding) inside loaded legitimate drivers’ `.text` sections. It scans for those gaps, copies shellcode into them, and runs from the trusted module’s address space—avoiding fresh executable kernel allocations that anti-cheat pool/integrity scans often flag. Aimed at researchers studying codecave abuse and stealthy Ring0 execution. (source: wiki/sources/descriptions/rogerxiii__kernel-codecave-poc.md)

README tag: `Find Codecave`.

## Links

- Repo: https://github.com/rogerxiii/kernel-codecave-poc

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[zero-thread-kernel]] · [[revert-mapper]] · [[system-thread-finder]]
