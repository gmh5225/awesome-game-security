---
title: Process-Injection-Techniques
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/MahmoudZohdy__Process-Injection-Techniques.md
updated: 2026-08-23
confidence: medium
---

# Process-Injection-Techniques

C/C++ **Windows process injection and persistence** technique collection (MahmoudZohdy). Implements multiple injection paths—CreateRemoteThread variants, APC and Early Bird, TLS callback injection, thread hijacking, reflective DLL loading, process hollowing, doppelganging, and ghosting—plus persistence-oriented mechanisms such as IFEO, AppInit_DLLs, and AppCertDlls. A single command-line entry point selects techniques with usage guidance. Primary use: security training, offensive technique research, and testing defensive detections in controlled lab environments. (source: wiki/sources/descriptions/MahmoudZohdy__Process-Injection-Techniques.md)

README lane: **Injection Testing** — broad inject + persistence lab corpus for AC/EDR evaluation.

Complements broader catalogs such as [[windows-process-injection]], unified C# CLI toolkit [[process-injection]] (3xpl01tc0d3r; vanilla/DLL/hollowing/APC queue/KernelCallbackTable; P/Invoke/D/Invoke/syscalls; shellcode formats, encryption, PPID spoof), focused PoCs such as [[thread-hijacking-injector]] and [[frankenstein-apc-injection]], harnesses such as [[injectors]], and defensive blockers such as [[pi-defender]] and [[ghost]].

## Links

- Repo: https://github.com/MahmoudZohdy/Process-Injection-Techniques

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[injectors]] · [[dirty-vanity]] · [[poolparty]] · [[dll-thread-injection-detector]]
