---
title: Unicorn PE
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hzqst__unicorn_pe.md
updated: 2026-08-05
confidence: medium
---

# Unicorn PE

Unicorn-based instrumentation framework for emulating Windows PE code execution, with emphasis on packed binaries. Logs disassembly for every executed instruction—useful when unpacking or tracing obfuscated control flow without live attach. Targets game-security researchers and reverse engineers studying cheat / dynamic binary instrumentation workflows. (source: wiki/sources/descriptions/hzqst__unicorn_pe.md)

Sits in the Windows User Space Emulator lane alongside Unicorn peers such as [[emulator]], [[sogen]], and [[dumpulator]], and function-level harness tools such as [[ripr]].

## Links

- Repo: https://github.com/hzqst/unicorn_pe

## Related

[[emulator]] · [[sogen]] · [[dumpulator]] · [[ripr]] · [[vmpimportfixer]] · [[smallworld]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
