---
title: windows-process-injection
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/toneillcodes__windows-process-injection.md
  - wiki/sources/descriptions/RixedLabs__IDLE-Abuse.md
  - wiki/sources/descriptions/NullTerminatorr__ThreadHijackingInjector.md
  - wiki/sources/descriptions/MahmoudZohdy__Process-Injection-Techniques.md
updated: 2026-08-23
confidence: medium
---

# windows-process-injection

Collection of **Windows process injection** techniques with working C/C++ examples (plus asm helpers for syscalls) and Python utilities for module-stomping / process profiling. Covers local and remote shellcode injection, dynamic function resolution, PEB and export-address-table walking, direct and indirect syscalls, module stomping, thread-pool and fiber injection, PPID spoofing, and call-stack spoofing. Aimed at RE / offensive researchers studying injection tradecraft and EDR evasion—material that maps to game-security and anti-cheat injection detection. (source: wiki/sources/descriptions/toneillcodes__windows-process-injection.md)

Contrasts with focused samples such as [[process-injection-techniques]] (MahmoudZohdy; unified CLI over hollowing/doppelganging/ghosting, APC/Early Bird/TLS/thread hijack, reflective DLL, and IFEO/AppInit_DLLs/AppCertDlls persistence; Injection Testing), [[thread-hijacking-injector]] (NullTerminatorr; minimal C++ thread-hijack DLL inject PoC; compact context manipulation + execution redirection; Injection Testing), [[modexmap]] (UM PE manual-map), [[simple-manual-map-injector]] (compact C++ manual-map; x86/x64; optional header/section strip; TheCruZ), [[hintinject]] (import-table Hint/Name Table shellcode staging), [[injectors]] (injection-testing harness), [[jektor]] (shellcode execution vectors + dynamic resolve + XOR/NOP-sled payloads), [[the-perfect-injector]] (`NtCreateThreadEx` + runtime `LdrLoadDll`-resolving PIC shellcode; no fixed `LoadLibrary`), [[poolparty]] (thread-pool worker-factory overwrite + TP_* queue insertion; SafeBreach-Labs), [[frankenstein-apc-injection]] (leaked handles + natural RWX + `NtQueueApcThreadEx2`; S12cybersecurity), [[idle-abuse]] (`RegisterWaitForInputIdle` idle-state callback shellcode/process-manipulation PoC; RixedLabs), [[tartarus-tp-alloc-inject]] (TpAllocInject + Tartarus' Gate indirect syscalls), [[dbgnexum]] (Debug API + HWBP + file-mapping shellcode inject without WPM/RPM/VirtualAllocEx), [[dirty-vanity]] (`RtlCreateProcessReflection` fork inherit + start-address redirect; no WPM), [[kinject]] / [[injdrv]] (kernel APC paths), and stack-spoof illustrations such as [[return-address-spoofer]].

## Links

- Repo: https://github.com/toneillcodes/windows-process-injection

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injectors]] · [[modexmap]] · [[hintinject]] · [[dbgnexum]] · [[dirty-vanity]] · [[kinject]] · [[injdrv]] · [[return-address-spoofer]] · [[tietwagent]]
