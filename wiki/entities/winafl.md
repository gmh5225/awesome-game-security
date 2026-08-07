---
title: WinAFL
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/googleprojectzero__winafl.md
updated: 2026-08-07
confidence: medium
---

# WinAFL

**WinAFL** is Google Project Zero’s Windows port of **AFL** (American Fuzzy Lop), a coverage-guided fuzzer. It instruments binaries with **DynamoRIO** or **Intel PT** to track edge coverage, supports **persistent mode** for fast in-process fuzzing, and ships corpus minimization and crash triage utilities. The C tool can fuzz closed-source Windows binaries without source by hooking target functions and mutating input — aimed at vulnerability researchers fuzzing Windows applications, drivers, and parsers. (source: wiki/sources/descriptions/googleprojectzero__winafl.md)

Sits beside native IPT capture ([[winipt]], [[windows-intel-pt]]), Intel-PT hypervisor fuzzing ([[qemu-nyx]]), and DBI harness frameworks ([[dynamic-binary-instrumentation]]) in the Windows fuzzing / coverage lane.

## Links

- Repo: https://github.com/googleprojectzero/winafl (README tag: Intel PT Fuzzer)

## Related

[[winipt]] · [[windows-intel-pt]] · [[qemu-nyx]] · [[processor-trace]] · [[dynamic-binary-instrumentation]] · [[cfb]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
