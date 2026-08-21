---
title: anti-crack-system
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ReFo0__anti-crack-system.md
updated: 2026-08-21
confidence: medium
---

# anti-crack-system

Windows **anti-tamper and anti-crack framework prototype** in C++ from ReFo0 for the software-protection / game-security hardening lane. Bundles **anti-debugging**, **anti-dump**, and **anti-attach** protections with **integrity checks**, **process-kill routines**, and **self-remapping code paths**, plus **string obfuscation** and lightweight **encryption helpers** for sensitive constants. Targets protection experiments whose defensive patterns can be adapted into game-security tooling. (source: wiki/sources/descriptions/ReFo0__anti-crack-system.md)

Complements anti-debug samples such as [[anti-debugger-protector-loader]] and [[anti-debugging]], self-remapping hardening via [[self-remapping-code]], and compile-time string hiding such as [[static-string-obfuscation]].

## Links

- Repo: https://github.com/ReFo0/anti-crack-system

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[anti-debugger-protector-loader]] · [[anti-debugging]] · [[self-remapping-code]] · [[static-string-obfuscation]] · [[makin]] · [[gh-anti-debug-bypass-practice-tool]]
