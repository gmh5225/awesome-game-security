---
title: NO_ACCESS_Protection
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/weak1337__NO_ACCESS_Protection.md
updated: 2026-07-18
confidence: medium
---

# NO_ACCESS_Protection

C++ library that marks protected code pages `PAGE_NOACCESS` via `VirtualProtect`, then uses a Vectored Exception Handler to catch the resulting access violations, temporarily restore `PAGE_EXECUTE_READ` for the faulting page, and re-protect after execution via a single-step trap (`STATUS_SINGLE_STEP`). Legitimate execution continues through the VEH trampoline; external memory scanners or debuggers that read the protected pages hit AVs. (source: wiki/sources/descriptions/weak1337__NO_ACCESS_Protection.md)

Useful research reference for PAGE_NOACCESS-based anti-tamper and for AC developers evaluating memory-protection strategies against external scanners—pairs with VEH-chain dump tooling such as [[veh-dumper]].

## Links

- Repo: https://github.com/weak1337/NO_ACCESS_Protection

## Related

[[veh-dumper]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
