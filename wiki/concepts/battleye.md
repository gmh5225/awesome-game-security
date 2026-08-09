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
  - wiki/sources/descriptions/tr1xxx__battleye-region-walking.md
  - wiki/sources/descriptions/steffalon__battleye-rust.md
  - wiki/sources/descriptions/rushzzz-max__r6-external.md
  - wiki/sources/descriptions/mexploitui__FakeEye.md
  - wiki/sources/descriptions/masterpastaa__BattlEye-Handler-BYPASS.md
  - wiki/sources/descriptions/lguilhermee__Battleye-Shellcode-Dumper.md
  - wiki/sources/descriptions/huoji120__goodeye.md
  - wiki/sources/descriptions/gmh5225__bedaisy-bypass.md
  - wiki/sources/descriptions/haram__splendid_implanter.md
updated: 2026-08-09
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

Runtime shellcode streamed from the BE server and executed in-process is intercepted pre-execution by [[battleye-shellcode-dumper]]: saves scanning-module payloads plus decryption keys for offline RE of BE’s dynamic module architecture. (source: wiki/sources/descriptions/lguilhermee__Battleye-Shellcode-Dumper.md)

VAS region enumeration for injected/shellcode and manual-mapped modules is reconstructed in [[battleye-region-walking]]: VirtualQuery walk plus BE-style filters on protection, size, `MEM_PRIVATE`/`MEM_MAPPED`, and address heuristics. (source: wiki/sources/descriptions/tr1xxx__battleye-region-walking.md)

Title-specific client tooling such as [[arma3beclient]] (C# / PowerShell; Arma 3 / `game:arma3`) sits in the BattlEye Tool lane for modding and BE-protected client debugging. (source: wiki/sources/descriptions/tym32167__arma3beclient.md)

Server-side RCON is covered by [[battleye-rust]]: Rust packet encode/checksum + UDP socket I/O for BattlEye remote-console listen/read/write (admin / protocol research). (source: wiki/sources/descriptions/steffalon__battleye-rust.md)

Title-specific R6 external samples such as [[r6-external]] (C/C++; driver development; External tag) illustrate out-of-process / driver-backed research against BattlEye-protected Siege clients. (source: wiki/sources/descriptions/rushzzz-max__r6-external.md)

Service/install/launch emulation is studied via [[fakeeye]]: SCM-managed `BEService`, external config, and BE-style game process creation without the real AC stack. (source: wiki/sources/descriptions/mexploitui__FakeEye.md)

Handle-stripping bypass via periodic handle re-creation is implemented in [[battleye-handler-bypass]]: a KMDF driver that re-opens process handles before BE’s ~5-second cleanup cycle strips them, with IOCTL paths for usermode control. (source: wiki/sources/descriptions/masterpastaa__BattlEye-Handler-BYPASS.md)

BEDaisy APC instrumentation is studied via [[goodeye]]: a kernel callback runs in each thread where the BE driver registers an APC, exposing BE’s kernel APC inspection surface for RE. (source: wiki/sources/descriptions/huoji120__goodeye.md)

[[bedaisy-bypass]] targets **BEDaisy.sys** report delivery: suppress outbound detection reports to the BE service while preserving inbound response traffic—useful for studying the kernel-to-service report channel without server-side ban telemetry. (source: wiki/sources/descriptions/gmh5225__bedaisy-bypass.md)

User-mode-only injection against BE-protected processes is demonstrated by [[splendid-implanter]] (secret.club): a Ring-3 injector that abuses a flaw in BattlEye's user-mode component to achieve BE-compatible DLL injection without a kernel driver. (source: wiki/sources/descriptions/haram__splendid_implanter.md)

## Related

[[easy-anti-cheat]] · [[vanguard]] · [[blindeye]] · [[be-shellcode]] · [[battleye-shellcode-dumper]] · [[battleye-region-walking]] · [[battleye-rust]] · [[battleye-handler-bypass]] · [[bedaisy-bypass]] · [[arma3beclient]] · [[r6-external]] · [[r6-internal-v3]] · [[fakeeye]] · [[goodeye]] · [[splendid-implanter]] · [[system-thread-finder]] · [[skiphook]] · [[present-hook-detection]] · [[present-hook]] · [[libelevate]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
