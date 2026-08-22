---
title: Exception-Ret-Spoofing
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Peribunt__Exception-Ret-Spoofing.md
updated: 2026-08-22
confidence: medium
---

# Exception-Ret-Spoofing

Minimal **x64 return-address spoofing** proof of concept implemented through an **exception-handler flow**. The C++ example demonstrates how a spoofed call path can be built and chained with gadgets while documenting practical tradeoffs around convenience, **calling-convention constraints**, reliability, and performance. Primarily useful for low-level control-flow research in anti-cheat evasion and offensive tooling experiments. (source: wiki/sources/descriptions/Peribunt__Exception-Ret-Spoofing.md)

Complements [[ret-spoofing]] from the same author, which avoids exception handlers for lower overhead in simple call-redirection scenarios.

## Links

- Repo: https://github.com/Peribunt/Exception-Ret-Spoofing

## Related

[[stack-spoofing]] · [[ret-spoofing]] · [[callstackspoofer-2]] · [[x86-ret-spoof]] · [[vpgather]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
