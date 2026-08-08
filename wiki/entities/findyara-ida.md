---
title: findyara-ida
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__findyara-ida.md
updated: 2026-08-08
confidence: medium
---

# findyara-ida

IDA Pro plugin that integrates YARA rule scanning into the disassembly workflow. Runs YARA rules against the loaded binary from within IDA, highlights matches in the disassembly view, and provides navigation to matched locations. Supports custom rule sets for malware signatures, crypto constants, or packer patterns—aimed at malware analysts and reverse engineers using YARA-based detection inside IDA Pro. (source: wiki/sources/descriptions/gmh5225__findyara-ida.md)

In-disassembly YARA scan with match highlighting—not a rule compiler or compiled-rule bytecode analyzer.

Complements other in-IDA YARA tooling such as [[findcrypt-yara]] (built-in crypto-constant signatures), [[yara4ida]] (Alt-Y scan integration), [[yarascan-ida]] (Python file scan), rule generation via [[hyara]], and compiled-rule analysis via [[yaravm]].

## Links

- Repo: https://github.com/gmh5225/findyara-ida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[findcrypt-yara]] · [[yara4ida]] · [[yarascan-ida]] · [[hyara]] · [[yaravm]] · [[idaplugins]]
