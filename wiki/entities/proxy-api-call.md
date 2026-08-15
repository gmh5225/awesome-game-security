---
title: ProxyAPICall
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/evilashz__ProxyAPICall.md
updated: 2026-08-15
confidence: medium
---

# ProxyAPICall

Windows **custom stack call** utility for **proxying API calls** through **fabricated call stacks**. Written in C/C++; aimed at game-security researchers and reverse engineers studying offensive cheat / spoof-stack tradecraft in the `Cheat > Spoof Stack` / `[Custom stack call]` lane. (source: wiki/sources/descriptions/evilashz__ProxyAPICall.md)

Sits beside return-address spoofing libraries such as [[spoof-stack-safecall]], assembly-trampoline PoCs such as [[callstackspoofer-2]], and HWBP stack forgers such as [[hw-call-stack]] by focusing on **API-call proxying** with a **custom-presented stack** rather than bare return-slot patching alone.

## Links

- Repo: https://github.com/evilashz/ProxyAPICall

## Related

[[stack-spoofing]] · [[spoof-stack-safecall]] · [[callstackspoofer-2]] · [[hw-call-stack]] · [[thread-stack-spoofer]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
