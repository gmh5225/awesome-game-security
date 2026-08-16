---
title: Dirty-Vanity
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/deepinstinct__Dirty-Vanity.md
updated: 2026-08-16
confidence: medium
---

# Dirty-Vanity

**Proof-of-concept process injection** that abuses the Windows **process forking API** (`RtlCreateProcessReflection`) to clone a target process and redirect the forked copy's **start address** to injected shellcode. Shellcode is written into the original process and **inherited by the fork**, avoiding traditional `WriteProcessMemory`-based remote injection and evading common EDR detection heuristics that monitor cross-process memory writes. Listed for security researchers studying novel injection tradecraft and anti-cheat engineers evaluating **fork-based evasion** methods. (source: wiki/sources/descriptions/deepinstinct__Dirty-Vanity.md)

Complements broader injection catalogs such as [[windows-process-injection]], process-snapshot cloning PoCs such as [[process-cloning]] (`NtCreateProcessEx`), and Debug API injectors such as [[dbgnexum]] that also avoid conventional WPM/RPM paths.

## Links

- Repo: https://github.com/deepinstinct/Dirty-Vanity

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[windows-process-injection]] · [[process-cloning]] · [[dbgnexum]] · [[jektor]] · [[injectors]]
