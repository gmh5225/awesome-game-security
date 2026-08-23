---
title: Unwinder
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Kudaes__Unwinder.md
updated: 2026-08-23
confidence: medium
---

# Unwinder

**Unwinder** is a **Rust** crate implementing **call stack spoofing** techniques inspired by [[silent-moonwalk]]. It provides macros for invoking regular functions and **indirect syscalls** while maintaining **stable spoofed stack traces**, with support for argument passing, return-value capture, and **repeated chained spoofing without linear stack growth**. Rust code is combined with **assembly helpers** to control low-level execution flow on Windows. Primary use case: low-level offensive security research focused on **call-stack evasion** in the `Cheat > Spoof Stack` / thread stack spoofing lane. (source: wiki/sources/descriptions/Kudaes__Unwinder.md)

Sits beside SilentMoonWalk-lineage PoCs such as [[silent-moonwalk]] and [[loudsunrun]], assembly-trampoline implementations such as [[callstackspoofer-2]], and macro helpers such as [[stack-spoofer-macro]]. Same-author companion crate: [[shelter]] (ROP-based sleep obfuscation with integrated stack spoofing and indirect syscalls).

## Links

- Repo: https://github.com/Kudaes/Unwinder

## Related

[[stack-spoofing]] · [[silent-moonwalk]] · [[callstackspoofer-2]] · [[thread-stack-spoofer]] · [[stack-spoofer-macro]] · [[windows-process-injection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
