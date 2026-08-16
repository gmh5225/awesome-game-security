---
title: SuperMega
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dobin__SuperMega.md
updated: 2026-08-16
confidence: medium
---

# SuperMega

**Shellcode loader** that **infects legitimate PE executables** (`.exe` and `.dll`) by injecting a **carrier shellcode tightly integrated into the host binary**, making static analysis difficult to distinguish from the original code. Implements the **Cordyceps parasitic injection** technique with a **web-based project management interface** for configuring payloads, anti-emulation strategies, and injection targets. Listed under Cheat → stealthy shellcode injection; aimed at security researchers studying advanced shellcode loading, PE infection techniques, and evasion of static analysis tools—not an AC product. (source: wiki/sources/descriptions/dobin__SuperMega.md)

Complements PE import-table staging via [[hintinject]], polymorphic shellcode encoding such as [[shoggoth]], and PE packers such as [[2pack]] and [[shellcode-factory]].

## Links

- Repo: https://github.com/dobin/SuperMega

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hintinject]] · [[shoggoth]] · [[2pack]] · [[shellcode-factory]] · [[windows-process-injection]]
