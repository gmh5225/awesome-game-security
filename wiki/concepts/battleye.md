---
title: BattlEye
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zouxianyu__BlindEye.md
  - wiki/sources/descriptions/weak1337__SystemThreadFinder.md
  - wiki/sources/descriptions/weak1337__SkipHook.md
  - wiki/sources/descriptions/weak1337__PresentHookDetection.md
  - wiki/sources/descriptions/weak1337__BE-Shellcode.md
  - wiki/sources/descriptions/tym32167__arma3beclient.md
updated: 2026-07-19
confidence: medium
---

# BattlEye

Kernel driver plus service and game module coordination. Emphasizes handle protection, process monitoring, memory scanning, and visibility into injected code / runtime tampering. Used by PUBG, Rainbow Six Siege, DayZ, and others. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Object callbacks and handle stripping, injected-module detection, pool/driver forensics, and comparison with boot-start models like [[vanguard]].

[[blindeye]] shows an offensive research angle: hook BE’s imported pool allocators and drop allocations for the kernel “report” path. (source: wiki/sources/descriptions/zouxianyu__BlindEye.md)

Thread-start heuristics (system threads whose start address is outside any loaded driver image) are reconstructed in tools such as [[system-thread-finder]], derived from BE’s thread-detection logic. (source: wiki/sources/descriptions/weak1337__SystemThreadFinder.md)

User-mode prologue hooks (JMP / INT3 on WinAPI and game functions) are a common BE-style control surface; [[skiphook]] studies trampolines that skip the first instruction so those hooks are never hit while return-address checks still look legitimate. (source: wiki/sources/descriptions/weak1337__SkipHook.md)

Graphics Present integrity is another BE-linked lane: [[present-hook-detection]] recreates dummy-D3D11 swap-chain Present pointer + `dxgi.dll` prologue comparison against inline/vtable hooks used by overlay ESP. (source: wiki/sources/descriptions/weak1337__PresentHookDetection.md)

User-mode shellcode injected into game processes is studied via [[be-shellcode]]: dump/disasm of BE detection modules covering system-thread scan, VEH enumeration, module walking, and signature-based integrity checks. (source: wiki/sources/descriptions/weak1337__BE-Shellcode.md)

Title-specific client tooling such as [[arma3beclient]] (C# / PowerShell; Arma 3 / `game:arma3`) sits in the BattlEye Tool lane for modding and BE-protected client debugging. (source: wiki/sources/descriptions/tym32167__arma3beclient.md)

## Related

[[easy-anti-cheat]] · [[vanguard]] · [[blindeye]] · [[be-shellcode]] · [[arma3beclient]] · [[system-thread-finder]] · [[skiphook]] · [[present-hook-detection]] · [[present-hook]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
