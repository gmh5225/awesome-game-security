---
title: antidbg
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/NotRequiem__antidbg.md
updated: 2026-08-22
confidence: medium
---

# antidbg

Comprehensive **Windows userland anti-debugging library** in C/C++ from NotRequiem, shipped as an integratable library and CLI. Implements multiple detection primitives: **API-based checks**, **timing attacks**, **process-environment queries**, **hardware breakpoint detection**, **exception-based tricks**, and **direct syscall evasion** for stealth-focused anti-RE protections. Uses fully syscalled paths to reduce hook visibility on common ntdll/kernel32 instrumentation surfaces. (source: wiki/sources/descriptions/NotRequiem__antidbg.md)

Complements broader technique catalogs such as [[makin]] and [[anti-debugging]], modular anti-analysis kits such as [[dynamizer]], integratable libraries such as [[antidbg-baka]], and anti-tamper frameworks such as [[anti-crack-system]].

## Links

- Repo: https://github.com/NotRequiem/antidbg

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[antidbg-baka]] · [[anti-debugging]] · [[makin]] · [[dynamizer]] · [[anti-crack-system]] · [[scyllahidedetector2]] · [[titanhide]]
