---
title: al-khaser
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/LordNoteworthy__al-khaser.md
updated: 2026-08-23
confidence: medium
---

# al-khaser

Windows **proof-of-concept anti-analysis test suite** that simulates many malware evasion behaviors. C++ codebase with a command-line interface exercising anti-debugging, anti-VM, anti-dumping, anti-disassembly, and timing-based checks. Broad environment-detection coverage for VirtualBox, VMware, QEMU, Wine, and common analysis workflows. Primary use case: validating sandbox, EDR, and anti-malware visibility against real-world evasion techniques. (source: wiki/sources/descriptions/LordNoteworthy__al-khaser.md)

Complements modular anti-analysis testers such as [[pafish]], embeddable VM fingerprinting such as [[compact-vm-detector]], sandbox demos such as [[anticuckoo]] and [[anti-sandbox]], and anti-debug bypass/hide tooling studied in RE workflows ([[scyllahide]], [[titanhide]], [[makin]]).

## Links

- Repo: https://github.com/LordNoteworthy/al-khaser

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pafish]] · [[compact-vm-detector]] · [[anti-sandbox]] · [[anticuckoo]] · [[vmaware]] · [[hypervisor-detection]]
