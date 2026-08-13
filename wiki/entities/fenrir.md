---
title: Fenrir
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Fenrir.md
updated: 2026-08-13
confidence: medium
---

# Fenrir

**Fenrir** is a kernel-mode **rootkit / driver framework** for low-level Windows system manipulation — process hiding, cross-process memory access, and [[kernel-callbacks]] management — aimed at kernel security researchers studying offensive rootkit tradecraft. README also tags **stack spoofing via `jmp rdi`** in the `Cheat > Spoof Stack` lane. (source: wiki/sources/descriptions/gmh5225__Fenrir.md)

Sits beside gmh5225 rootkit-style utilities such as [[rtoolz]] (driver-backed process/callback hide and enum) and defensive hidden-process PoCs such as [[rootkit-2]]. Stack-spoof research complements [[stack-spoofer-macro]], [[spoof-stack-safecall]], and [[return-address-spoofer]] samples in the same cheat corpus.

## Links

- Repo: https://github.com/gmh5225/Fenrir [Stack spoofing using jmp rdi]

## Related

[[stack-spoofing]] · [[kernel-callbacks]] · [[rtoolz]] · [[rootkit-2]] · [[blanket]] · [[openark]] · [[stack-spoofer-macro]] · [[spoof-stack-safecall]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
