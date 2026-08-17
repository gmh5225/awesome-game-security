---
title: Force Page Protection
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/changeofpace__Force-Page-Protection.md
updated: 2026-08-17
confidence: medium
---

# Force Page Protection

**x64dbg** plugin that forcefully sets **page protection** for **memory-mapped views** when **`NtProtectVirtualMemory`** fails. Handles views mapped with **`SEC_NO_CHANGE`**, views with incompatible initial protection settings, and **anti-patching** mechanisms that exploit these API limitations by **remapping views** with the desired protection. Adds **ForcePageProtection (`fpp`)** commands to x64dbg for overriding memory-protection restrictions during dynamic analysis. README lane: **Bypass Remap Memory**; aimed at reverse engineers and anti-cheat analysts who need to patch regions protected by anti-tamper techniques that abuse mapped-view restrictions. (source: wiki/sources/descriptions/changeofpace__Force-Page-Protection.md)

Complements changeofpace **self-remapping code** anti-tamper research [[self-remapping-code]] (aliased execute vs integrity-check views) and defensive page-protection samples such as [[no-access-protection]] and [[memory-guard]] when studying offensive vs defensive mapped-memory protection.

## Links

- Repo: https://github.com/changeofpace/Force-Page-Protection

## Related

[[x64dbg]] · [[self-remapping-code]] · [[no-access-protection]] · [[memory-guard]] · [[count-hook]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
