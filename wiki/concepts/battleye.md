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
  - wiki/sources/descriptions/gmh5225__R6S-internal-Cheat.md
  - wiki/sources/descriptions/gmh5225__R6S-External-V2.md
  - wiki/sources/descriptions/gmh5225__Rainbow-Six-Siege-Rs6-External-Esp-Aimbot-Hack-Cheat.md
  - wiki/sources/descriptions/gmh5225__Rainbow-6-Siege-Cheat.md
  - wiki/sources/descriptions/gmh5225__R6-Cheat-Dumper.md
  - wiki/sources/descriptions/mexploitui__FakeEye.md
  - wiki/sources/descriptions/Hypercall__FakeEye.md
  - wiki/sources/descriptions/masterpastaa__BattlEye-Handler-BYPASS.md
  - wiki/sources/descriptions/lguilhermee__Battleye-Shellcode-Dumper.md
  - wiki/sources/descriptions/huoji120__goodeye.md
  - wiki/sources/descriptions/gmh5225__bedaisy-bypass.md
  - wiki/sources/descriptions/gmh5225__be_shellcode_dump.md
  - wiki/sources/descriptions/haram__splendid_implanter.md
  - wiki/sources/descriptions/HadockKali__battleye-user-mode-bypass.md
  - wiki/sources/descriptions/gmh5225__StealthSytemThreadFinderBE.md
  - wiki/sources/descriptions/gmh5225__BadEye.md
  - wiki/sources/descriptions/gmh5225__BE-Forcer-Fortnite.md
  - wiki/sources/descriptions/gmh5225__BE-Emulator.md
  - wiki/sources/descriptions/gmh5225__BE-BattlEye_shellcode.md
  - wiki/sources/descriptions/experienceds__pubg-p2c-re.md
  - wiki/sources/descriptions/experienceds__battleye-re.md
  - wiki/sources/descriptions/dllcrt0__bedaisy-reversal.md
  - wiki/sources/descriptions/dllcrt0__battleye-shellcode.md
  - wiki/sources/descriptions/dllcrt0__battleye-decryption.md
  - wiki/sources/descriptions/es3n1n__be-shellcode-tester.md
  - wiki/sources/descriptions/Schnocker__NoEye.md
  - wiki/sources/descriptions/R4YVEN__beservice_intcallbacks.md
  - wiki/sources/descriptions/LilPidgey__BEClient.md
  - wiki/sources/descriptions/JonathanEke__DayZ-Server-Battleye-Remover.md
updated: 2026-08-25
confidence: medium
---

# BattlEye

Kernel driver plus service and game module coordination. Emphasizes handle protection, process monitoring, memory scanning, and visibility into injected code / runtime tampering. Used by PUBG, Rainbow Six Siege, DayZ, and others. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Object callbacks and handle stripping, injected-module detection, pool/driver forensics, and comparison with boot-start models like [[vanguard]].

[[blindeye]] shows an offensive research angle: hook BE’s imported pool allocators and drop allocations for the kernel “report” path. (source: wiki/sources/descriptions/zouxianyu__BlindEye.md)

Thread-start heuristics (system threads whose start address is outside any loaded driver image) are reconstructed in tools such as [[system-thread-finder]], derived from BE’s thread-detection logic. (source: wiki/sources/descriptions/weak1337__SystemThreadFinder.md)

[[stealth-sytem-thread-finder-be]] (gmh5225) enumerates stealth system threads BE misses via PspCidTable walks, scheduler queue scans, and thread-list cross-reference—beyond standard API calls—for manually mapped driver threads. (source: wiki/sources/descriptions/gmh5225__StealthSytemThreadFinderBE.md)

User-mode prologue hooks (JMP / INT3 on WinAPI and game functions) are a common BE-style control surface; [[skiphook]] studies trampolines that skip the first instruction so those hooks are never hit while return-address checks still look legitimate. (source: wiki/sources/descriptions/weak1337__SkipHook.md)

Graphics Present integrity is another BE-linked lane: [[present-hook-detection]] recreates dummy-D3D11 swap-chain Present pointer + `dxgi.dll` prologue comparison against inline/vtable hooks used by overlay ESP. (source: wiki/sources/descriptions/weak1337__PresentHookDetection.md)

User-mode shellcode injected into game processes is studied via [[be-shellcode]]: dump/disasm of BE detection modules covering system-thread scan, VEH enumeration, module walking, and signature-based integrity checks. (source: wiki/sources/descriptions/weak1337__BE-Shellcode.md)

Runtime shellcode streamed from the BE server and executed in-process is intercepted pre-execution by [[battleye-shellcode-dumper]]: saves scanning-module payloads plus decryption keys for offline RE of BE’s dynamic module architecture. (source: wiki/sources/descriptions/lguilhermee__Battleye-Shellcode-Dumper.md)

[[be-shellcode-dump]] (gmh5225) dumps BE runtime shellcode scanning modules from protected game processes—intercepts streamed payloads before offline RE of detection signatures and scanning logic. (source: wiki/sources/descriptions/gmh5225__be_shellcode_dump.md)

[[be-battleye-shellcode]] (gmh5225) reimplements recent BE user-mode shellcode as a DLL study scaffold: worker-thread scan stages (hidden system threads, `KiUserExceptionDispatcher` hook detection, module/function integrity, signature scan, thread scan) plus VEH-guarded Win32/CRT targets for shellcode-style control-flow recovery. (source: wiki/sources/descriptions/gmh5225__BE-BattlEye_shellcode.md)

[[be-shellcode-tester]] (es3n1n) is a C++ sandbox that loads dumped BE scanning modules, emulates their expected runtime, and logs memory scans, hash checks, and detection routines—useful for measuring BE shellcode detection coverage without a live protected game. (source: wiki/sources/descriptions/es3n1n__be-shellcode-tester.md)

VAS region enumeration for injected/shellcode and manual-mapped modules is reconstructed in [[battleye-region-walking]]: VirtualQuery walk plus BE-style filters on protection, size, `MEM_PRIVATE`/`MEM_MAPPED`, and address heuristics. (source: wiki/sources/descriptions/tr1xxx__battleye-region-walking.md)

Title-specific client tooling such as [[arma3beclient]] (C# / PowerShell; Arma 3 / `game:arma3`) sits in the BattlEye Tool lane for modding and BE-protected client debugging. (source: wiki/sources/descriptions/tym32167__arma3beclient.md)

Server-side RCON is covered by [[battleye-rust]]: Rust packet encode/checksum + UDP socket I/O for BattlEye remote-console listen/read/write (admin / protocol research). (source: wiki/sources/descriptions/steffalon__battleye-rust.md)

Title-specific R6 external samples such as [[r6-external]] (C/C++; driver development; External tag) illustrate out-of-process / driver-backed research against BattlEye-protected Siege clients. (source: wiki/sources/descriptions/rushzzz-max__r6-external.md) [[r6s-external-v2]] (gmh5225; C++; kernel driver or handle elevation; ESP + aimbot without in-process injection; BattlEye UE4 external pattern study) adds a v2 external sample in the same Siege lane. (source: wiki/sources/descriptions/gmh5225__R6S-External-V2.md) Leaked R6 external ESP/aimbot source such as [[rainbow-six-siege-rs6-external-esp-aimbot-hack-cheat]] (gmh5225; WndProc-only input hooking to limit detectable hook surfaces) complements that lane with minimal user-mode input-path evasion study. (source: wiki/sources/descriptions/gmh5225__Rainbow-Six-Siege-Rs6-External-Esp-Aimbot-Hack-Cheat.md) R6 cheat source such as [[rainbow-6-siege-cheat]] (gmh5225; C/C++; rendering + hooking; cheat / game:r6) adds another user-mode hook/overlay sample in the BattlEye-protected Siege lane. (source: wiki/sources/descriptions/gmh5225__Rainbow-6-Siege-Cheat.md) R6 internal cheat source such as [[r6s-internal-cheat]] (gmh5225; C++; modding + overlays + memory analysis; cheat / game:r6) adds an in-process mod/overlay sample in the same lane. (source: wiki/sources/descriptions/gmh5225__R6S-internal-Cheat.md) R6 external cheat dumper tooling such as [[r6-cheat-dumper]] (gmh5225; C/C++; driver development + rendering + animation; out-of-process cheat-structure extraction; cheat / game:r6 [External]) adds dump-focused external research beside runnable Siege externals. (source: wiki/sources/descriptions/gmh5225__R6-Cheat-Dumper.md) [[external-r6s-cheat]] (gmh5225; kernel driver + shared mapped memory section for external entity/position/render reads; ESP + aimbot without in-process injection) adds a shared-memory external communication pattern study in the Siege lane. (source: wiki/sources/descriptions/gmh5225__External-R6S-Cheat.md)

Service/install/launch emulation is studied via [[fakeeye]] (Hypercall): lightweight C++ BattlEye-style launcher emulator that reproduces launcher-side behavior for isolated lab anti-cheat research and compatibility testing; earlier mexploitui fork documents SCM-managed `BEService`, external config, and BE-style game process creation without the real AC stack. (source: wiki/sources/descriptions/Hypercall__FakeEye.md; wiki/sources/descriptions/mexploitui__FakeEye.md)

Historical service-layer bypass tradecraft is preserved in [[noeye]] (Schnocker): C++ runtime modules plus a dedicated Windows service and C# setup app for service installation, process interaction, and runtime control against older BE protection behavior. (source: wiki/sources/descriptions/Schnocker__NoEye.md)

Client-side protocol emulation is studied via [[be-emulator]] (gmh5225): simulates BE communication protocol, heartbeat responses, and module-loading interface so games run without active BE protection—useful for analyzing game↔BE integration and protocol RE. (source: wiki/sources/descriptions/gmh5225__BE-Emulator.md)

Minimal in-process client-interface scaffolding is provided by [[beclient]] (LilPidgey; C++ Visual Studio PoC): initializes the BattlEye client DLL, defines game/AC data structures, registers callbacks, and calls exported run/command/exit handlers—useful for RE of how titles wire the BEClient DLL contract without a full emulator stack. (source: wiki/sources/descriptions/LilPidgey__BEClient.md)

Handle-stripping bypass via periodic handle re-creation is implemented in [[battleye-handler-bypass]]: a KMDF driver that re-opens process handles before BE’s ~5-second cleanup cycle strips them, with IOCTL paths for usermode control. (source: wiki/sources/descriptions/masterpastaa__BattlEye-Handler-BYPASS.md)

[[badeye]] (gmh5225) studies a complementary handle lane: BE assumes surviving handles already grant needed access and uses them only to resolve **EPROCESS** before **`MmCopyVirtualMemory`** cross-process reads—C++ memory-analysis research on that trust gap. (source: wiki/sources/descriptions/gmh5225__BadEye.md)

BEDaisy APC instrumentation is studied via [[goodeye]]: a kernel callback runs in each thread where the BE driver registers an APC, exposing BE’s kernel APC inspection surface for RE. (source: wiki/sources/descriptions/huoji120__goodeye.md)

[[bedaisy-bypass]] targets **BEDaisy.sys** report delivery: suppress outbound detection reports to the BE service while preserving inbound response traffic—useful for studying the kernel-to-service report channel without server-side ban telemetry. (source: wiki/sources/descriptions/gmh5225__bedaisy-bypass.md)

[[battleye-re]] (experienceds) is a defensive RE reference for **BEDaisy.sys**: PE layout, dynamic kernel API resolution, BattlEye device IOCTL dispatch, HAL table verification, anti-DMA behavior, custom VM obfuscation, and security-cookie derivation—JSON findings, address lists, disassembly, and section hex dumps for titles such as Enlisted. (source: wiki/sources/descriptions/experienceds__battleye-re.md)

[[bedaisy-reversal]] (dllcrt0) documents the full scope of BEDaisy kernel checks and reporting: integrity validation, callback enumeration, HAL table verification, manual-mapped driver detection, object handle protection, filesystem minifilter checks, physical memory scanning, CSRSS integrity validation, graphics component verification, and thread/image notification callbacks. (source: wiki/sources/descriptions/dllcrt0__bedaisy-reversal.md)

[[battleye-shellcode]] (dllcrt0) publishes decompiled BE user-mode shellcode modules for runtime integrity checks: AutoHotKey detection, swap-chain [[present-hook]] scanning, and stack-walking return-address validation—complementing dump/reimplement samples such as [[be-battleye-shellcode]] with readable scan-stage source. (source: wiki/sources/descriptions/dllcrt0__battleye-shellcode.md)

[[battleye-decryption]] (dllcrt0) decrypts BattlEye's multi-layered encrypted communication packets between **BEService** and **BEDaisy** over named pipes—XOR-based generic packet decryption, hardware-information crypto, and second-stage key-derived routines for client↔driver protocol RE. (source: wiki/sources/descriptions/dllcrt0__battleye-decryption.md)

[[be-forcer-fortnite]] (gmh5225) targets Fortnite's BattlEye integration: forces or manipulates BE initialization to disable title-specific detection checks, enabling cheat injection or memory access normally blocked—offensive research on Fortnite-specific BE protection and bypass techniques. (source: wiki/sources/descriptions/gmh5225__BE-Forcer-Fortnite.md)

User-mode-only injection against BE-protected processes is demonstrated by [[splendid-implanter]] (secret.club): a Ring-3 injector that abuses a flaw in BattlEye's user-mode component to achieve BE-compatible DLL injection without a kernel driver. (source: wiki/sources/descriptions/haram__splendid_implanter.md)

[[battleye-user-mode-bypass]] (HadockKali) is a C++ Visual Studio PoC for a historical user-mode BE bypass: an implanter plus sample DLL hooks **CreateFileW** and manipulates file checks so a payload masquerades as a trusted module, with example injection and exported hook callbacks—useful for studying previously vulnerable UM loading-path trust validation. (source: wiki/sources/descriptions/HadockKali__battleye-user-mode-bypass.md)

Instrumentation Callback–based BattlEye bypass research such as [[beservice-intcallbacks]] (R4YVEN; C++/assembly Visual Studio PoC; callback and symbol-handling techniques; exploratory BE service bypass experiment—not a polished end-user tool; anti-cheat bypass + Windows internals study) extends the user-mode BE evasion lane beside Ring3 hook samples such as [[hooking-via-instrumentation-callback]]. (source: wiki/sources/descriptions/R4YVEN__beservice_intcallbacks.md)

PUBG commercial P2C loader RE such as [[pubg-p2c-re]] (experienceds) documents injecting ESP into `dwm.exe` instead of `TslGame.exe` to avoid BattlEye process-targeted scans, and how Krafton's Zakynthos anti-cheat detects DWM vtable and code hooks—architecture diagrams, detection templates, and an anti-cheat comparison matrix for BE/kernel AC evasion study. (source: wiki/sources/descriptions/experienceds__pubg-p2c-re.md)

Server-side executable patching against BE-integrated titles is studied via [[dayz-server-battleye-remover]] (JonathanEke): C++ utility that pattern-scans and patches the DayZ **server** binary to disable specific BE checks, automating re-patch after executable updates for controlled anti-cheat bypass experimentation. (source: wiki/sources/descriptions/JonathanEke__DayZ-Server-Battleye-Remover.md)

## Related

[[easy-anti-cheat]] · [[vanguard]] · [[pubg-p2c-re]] · [[dayz-server-battleye-remover]] · [[battleye-re]] · [[bedaisy-reversal]] · [[battleye-decryption]] · [[battleye-shellcode]] · [[blindeye]] · [[be-shellcode]] · [[be-battleye-shellcode]] · [[be-shellcode-dump]] · [[be-shellcode-tester]] · [[battleye-shellcode-dumper]] · [[battleye-region-walking]] · [[battleye-rust]] · [[battleye-handler-bypass]] · [[badeye]] · [[bedaisy-bypass]] · [[be-forcer-fortnite]] · [[be-emulator]] · [[beclient]] · [[beservice-intcallbacks]] · [[arma3beclient]] · [[r6-external]] · [[r6s-external-v2]] · [[external-r6s-cheat]] · [[r6-cheat-dumper]] · [[rainbow-6-siege-cheat]] · [[rainbow-six-siege-rs6-external-esp-aimbot-hack-cheat]] · [[r6s-internal-cheat]] · [[r6-internal-v3]] · [[fakeeye]] · [[noeye]] · [[goodeye]] · [[splendid-implanter]] · [[battleye-user-mode-bypass]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[skiphook]] · [[present-hook-detection]] · [[present-hook]] · [[libelevate]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
