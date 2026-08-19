---
title: Bugcheck Suppressor
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/XaFF-XaFF__BugcheckSuppressor.md
updated: 2026-08-19
confidence: medium
---

# Bugcheck Suppressor

Windows **kernel driver** proof-of-concept that suppresses blue-screen crashes (BSODs) by hooking **bugcheck callbacks** and recovering from kernel exceptions with **SEH**-based **`RtlUnwindEx`** unwinding. Targets **HVCI** and **kCET** (kernel Control-flow Enforcement Technology) constraints: uses a **data-only HAL dispatch hook** (no `.text` patches) and **CET-compatible assembly stubs** so recovery paths survive shadow-stack and Memory Integrity enforcement. (source: wiki/sources/descriptions/XaFF-XaFF__BugcheckSuppressor.md)

Research lane: kernel exception handling, bugcheck pipeline interception, and VBS/HVCI/CET interaction under the README `Windows Security Features` category—not a production stability tool.

## Links

- Repo: https://github.com/XaFF-XaFF/BugcheckSuppressor

## Related

[[hvci]] · [[cet-research]] · [[windows-kernel-shadow-stack]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
