---
title: rep-mov-ept-detecc
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/JustasMasiulis__rep_mov_ept_detecc.md
updated: 2026-08-24
confidence: medium
---

# rep-mov-ept-detecc

Windows C++ proof-of-concept for detecting **EPT (Extended Page Table)**-based hooking or access monitoring. Exercises **REP MOVS** under page faults versus uninterrupted execution and treats overwrite patterns as a guest-visible signal that hypervisor EPT policy is intercepting memory-backed code. Ships as a compact single-file implementation with executable memory setup and structured exception handling. Targets the README `REP MOV based EPT detection` lane for anti-cheat and hypervisor detection research. (source: wiki/sources/descriptions/JustasMasiulis__rep_mov_ept_detecc.md)

Complements other REP MOV / ERMSB side-channel EPT probes such as [[ermsb-meme]], timing / write-and-compare detectors such as [[ept-hook-detection]], and VPGATHER / vectored-exception probes such as [[bloodhound]]; sits opposite stealth Type-2 stacks such as [[ophion]] and [[hypervisor]] that rely on EPT for hooking without guest-kernel patches. Same author lane as compile-time string obfuscation [[xorstr]].

## Links

- Repo: https://github.com/JustasMasiulis/rep_mov_ept_detecc

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[ermsb-meme]] · [[ept-hook-detection]] · [[bloodhound]] · [[hypervisor-detection]] · [[ophion]] · [[hypervisor]] · [[xorstr]]
