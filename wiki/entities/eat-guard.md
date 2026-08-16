---
title: EATGuard
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/connormcgarr__EATGuard.md
updated: 2026-08-16
confidence: medium
---

# EATGuard

Windows proof-of-concept that monitors and protects the **Export Address Table (EAT)** of loaded modules against runtime modification. Uses **VEH** (Vectored Exception Handling) to set **`PAGE_GUARD`** on EAT memory pages, detecting and logging attempts to overwrite exported function pointers. Demonstrates how defenders can detect **EAT hooking**—a technique used by rootkits and cheats—for security researchers studying EAT integrity monitoring and hook detection. (source: wiki/sources/descriptions/connormcgarr__EATGuard.md)

README tag: **VEH + PAGE_GUARD**. Complements defensive page-protection libraries such as [[memory-guard]], offensive Page Guard hook samples such as [[pghooker]], and export-walking injection corpora such as [[windows-process-injection]].

## Links

- Repo: https://github.com/connormcgarr/EATGuard

## Related

[[memory-guard]] · [[pghooker]] · [[veh-printf-hook]] · [[voidmaw]] · [[windows-process-injection]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
