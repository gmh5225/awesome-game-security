---
title: windows-process-injection
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/toneillcodes__windows-process-injection.md
updated: 2026-08-16
confidence: medium
---

# windows-process-injection

Collection of **Windows process injection** techniques with working C/C++ examples (plus asm helpers for syscalls) and Python utilities for module-stomping / process profiling. Covers local and remote shellcode injection, dynamic function resolution, PEB and export-address-table walking, direct and indirect syscalls, module stomping, thread-pool and fiber injection, PPID spoofing, and call-stack spoofing. Aimed at RE / offensive researchers studying injection tradecraft and EDR evasion—material that maps to game-security and anti-cheat injection detection. (source: wiki/sources/descriptions/toneillcodes__windows-process-injection.md)

Contrasts with focused samples such as [[modexmap]] (UM PE manual-map), [[hintinject]] (import-table Hint/Name Table shellcode staging), [[injectors]] (injection-testing harness), [[jektor]] (shellcode execution vectors + dynamic resolve + XOR/NOP-sled payloads), [[dbgnexum]] (Debug API + HWBP + file-mapping shellcode inject without WPM/RPM/VirtualAllocEx), [[dirty-vanity]] (`RtlCreateProcessReflection` fork inherit + start-address redirect; no WPM), [[kinject]] / [[injdrv]] (kernel APC paths), and stack-spoof illustrations such as [[return-address-spoofer]].

## Links

- Repo: https://github.com/toneillcodes/windows-process-injection

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injectors]] · [[modexmap]] · [[hintinject]] · [[dbgnexum]] · [[dirty-vanity]] · [[kinject]] · [[injdrv]] · [[return-address-spoofer]] · [[tietwagent]]
