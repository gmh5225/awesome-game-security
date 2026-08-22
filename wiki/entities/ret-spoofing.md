---
title: Ret-Spoofing
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Peribunt__Ret-Spoofing.md
updated: 2026-08-22
confidence: medium
---

# Ret-Spoofing

Minimal **x64 return-address spoofing** implementation that **avoids exception-handler usage**. Combines C++ and assembly stubs to set and use fake return targets with very low overhead in simple call-redirection scenarios. Documents assumptions around preserved nonvolatile registers in the **Windows x64 calling convention**. Primarily used for stealth call-flow manipulation research in reverse engineering and cheat-development contexts. (source: wiki/sources/descriptions/Peribunt__Ret-Spoofing.md)

Sits in the `Cheat > Spoof Stack` lane beside x64 trampoline implementations such as [[callstackspoofer-2]], reusable libraries such as [[spoof-stack-safecall]], and x86 header-only samples such as [[x86-ret-spoof]].

## Links

- Repo: https://github.com/Peribunt/Ret-Spoofing

## Related

[[stack-spoofing]] · [[callstackspoofer-2]] · [[x86-ret-spoof]] · [[return-address-spoofer]] · [[vpgather]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
