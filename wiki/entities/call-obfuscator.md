---
title: call-obfuscator
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/d35ha__CallObfuscator.md
updated: 2026-08-16
confidence: medium
---

# call-obfuscator

PE binary **post-processing** tool that obfuscates API call targets by rewriting a binary's import table to point at decoy functions, then patching call sites at load time to redirect to the real targets through position-independent shellcode. The resolver walks `PEB→Ldr` module lists and parses export tables at runtime, so static analysis and signature-based scans see misleading API references. Configured via an INI file mapping real API calls to fake ones. Mainly useful for malware researchers, red teamers, and game security researchers studying import-table obfuscation to evade static analysis. (source: wiki/sources/descriptions/d35ha__CallObfuscator.md)

Useful as a focused **Call Obfuscation** / IAT-misdirection reference alongside post-compile IAT obfuscators such as [[alcatraz]] and lazy-import research tools such as [[blitz]].

## Links

- Repo: https://github.com/d35ha/CallObfuscator

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[alcatraz]] · [[blitz]] · [[obfuscation-detection]] · [[dumpepe]]
