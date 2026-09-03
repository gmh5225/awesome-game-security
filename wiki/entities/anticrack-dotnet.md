---
title: AntiCrack-DotNet
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/AdvDebug__AntiCrack-DotNet.md
updated: 2026-09-03
confidence: medium
---

# AntiCrack-DotNet

**AntiCrack-DotNet** (AdvDebug) is a **.NET protection toolkit** written in C# that bundles anti-debugging, anti-virtualization, anti-injection, and hook-detection techniques for managed applications. Checks span PEB and thread flags, sandbox heuristics, syscall-based probes, and integrity hardening. The repository also detects common anti-anti-debug user-mode hooks and several runtime tamper scenarios. Primary use case is hardening software and building defensive components for anti-cheat or anti-cracking workflows. (source: wiki/sources/descriptions/AdvDebug__AntiCrack-DotNet.md)

Complements native anti-debug libraries such as [[godefender]], [[avanguard]], and [[antidbg-baka]]; managed obfuscation/protection tooling such as [[confuserex]]; and broader anti-tamper frameworks such as [[anti-crack-system]]. Same maintainer lane as [[brovan]] (.NET RE/emulation).

README category: CSharp (Anti Debugging / managed protection).

## Links

- Repo: https://github.com/AdvDebug/AntiCrack-DotNet

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[brovan]] · [[godefender]] · [[avanguard]] · [[antidbg-baka]] · [[anti-crack-system]] · [[confuserex]] · [[scyllahidedetector2]] · [[wubbaboomark]]
