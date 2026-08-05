---
title: process-cloning
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/huntandhackett__process-cloning.md
updated: 2026-08-05
confidence: medium
---

# process-cloning

Windows **process cloning** proof of concept in C that creates a copy of a running process using `NtCreateProcessEx` with the parent process handle. The cloned process inherits a virtual address space snapshot of the original, enabling techniques such as process hollowing, memory analysis, or credential dumping from the clone without directly accessing the target. Aimed at security researchers studying process manipulation techniques and their detection opportunities. (source: wiki/sources/descriptions/huntandhackett__process-cloning.md)

Contrasts with broader injection catalogs such as [[windows-process-injection]] (remote shellcode / syscalls / module stomping) and process/file obfuscation such as [[herpaderping]] (write→map→modify→execute timing). Complements offline dump/replay lanes such as [[minidump]] and [[dumpulator]] when live attach to the target is undesirable.

## Links

- Repo: https://github.com/huntandhackett/process-cloning

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[herpaderping]] · [[minidump]] · [[dumpulator]] · [[kvcforensic]]
