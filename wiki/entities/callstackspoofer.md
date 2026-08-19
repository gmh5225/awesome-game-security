---
title: CallStackSpoofer
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/WithSecureLabs__CallStackSpoofer.md
updated: 2026-08-19
confidence: medium
---

# CallStackSpoofer

**CallStackSpoofer** is a **WithSecure Labs** proof-of-concept for **spoofing arbitrary call stacks** when issuing **Windows system calls**. Implemented in **C++** with **selectable sample stack profiles** that imitate common process behaviors; documents practical **debugging and validation** workflows using telemetry and debugger tooling. Aimed at security researchers studying **EDR evasion** and **stack-based detection** logic. (source: wiki/sources/descriptions/WithSecureLabs__CallStackSpoofer.md)

Canonical WithSecure Labs PoC in the `Cheat > Spoof Stack` lane; downstream reimplementations include [[nimic-stack]] (Nim) and community forks such as [[callstackspoofer-2]].

## Links

- Repo: https://github.com/WithSecureLabs/CallStackSpoofer

## Related

[[stack-spoofing]] · [[nimic-stack]] · [[callstackspoofer-2]] · [[silent-moonwalk]] · [[spoof-stack-safecall]] · [[return-address-spoofer]] · [[thread-stack-spoofer]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
