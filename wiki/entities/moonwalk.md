---
title: moonwalk
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Teach2Breach__moonwalk.md
updated: 2026-08-20
confidence: medium
---

# moonwalk

Rust library and CLI for finding loaded **DLL base addresses without walking the PEB module list**. Uses a stack-walking approach from **TEB** and stack bounds data, with branch variants that either use **VirtualQuery** or avoid Windows API calls for stealth. Structured as both reusable library code and a command-line demonstration binary. Intended for offensive security research and low-level tooling where traditional module enumeration paths may be monitored. (source: wiki/sources/descriptions/Teach2Breach__moonwalk.md)

Complements PEB-based resolution such as [[rs-ldr]] and [[tabby]], module-list evasion injectors such as [[modmap]], and sibling Teach2Breach tooling such as [[nt-unhooker]]. Not to be confused with call-stack spoofing PoCs such as [[silent-moonwalk]].

## Links

- Repo: https://github.com/Teach2Breach/moonwalk

## Related

[[nt-unhooker]] · [[rs-ldr]] · [[tabby]] · [[modmap]] · [[vm]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
