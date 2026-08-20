---
title: nt_unhooker
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Teach2Breach__nt_unhooker.md
updated: 2026-08-20
confidence: medium
---

# nt_unhooker

Rust-based Windows tool and library for detecting and removing hooks in **NTDLL**. Analyzes inline and IAT hook states, compares in-memory code against a clean reference image, and restores modified regions while handling critical safety checks. Implementation includes PE parsing, symbol-based clean DLL retrieval, and both programmatic and CLI usage paths. Used by malware analysts, red team researchers, and defenders investigating user-mode hook tampering. (source: wiki/sources/descriptions/Teach2Breach__nt_unhooker.md)

## Links

- Repo: https://github.com/Teach2Breach/nt_unhooker

## Related

[[edrsandblast]] · [[detoursnt]] · [[ntminhook]] · [[syscall-detect]] · [[antihook]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
