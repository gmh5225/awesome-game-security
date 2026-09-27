---
title: InjectSetConsole
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/TwoSevenOneT__InjectSetConsole.md
updated: 2026-09-27
confidence: medium
---

# InjectSetConsole

**Windows C++ injection tool** that delivers shellcode to a **child console process** through **standard-input pipes** instead of `VirtualAllocEx` and `WriteProcessMemory` (TwoSevenOneT). It launches an interactive console program, writes embedded shellcode via stdin, scans remote memory for a marker pattern to locate the buffer, makes that region executable with `VirtualProtectEx`, and hijacks the main thread's instruction pointer through `NtSetContextThread`. Helpers cover remote pattern scanning, main-thread discovery, and pipe-based I/O, with customizable shellcode and search patterns for evasion. Aimed at security researchers studying process injection, EDR bypass techniques, and anti-cheat or offensive tooling on **Windows x64**. (source: wiki/sources/descriptions/TwoSevenOneT__InjectSetConsole.md)

README lane: **Injection Testing** — console stdin-pipe shellcode inject without cross-process WPM/alloc APIs.

Sits in the **stdin-pipe / console-child** injection lane beside Debug API injectors such as [[dbgnexum]] (file-mapping + HWBP orchestration without WPM/RPM/VirtualAllocEx) and thread-hijack PoCs such as [[threadject]], within broader corpora such as [[windows-process-injection]] and [[process-injection-techniques]].

## Technique summary

1. Spawn an interactive console child process with piped stdin.
2. Write marker-tagged shellcode into the child through stdin I/O.
3. Scan remote memory for the marker pattern to resolve the payload buffer.
4. Call `VirtualProtectEx` to make the located region executable.
5. Discover the main thread and redirect execution via `NtSetContextThread`.

## Links

- Repo: https://github.com/TwoSevenOneT/InjectSetConsole

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[dbgnexum]] · [[threadject]] · [[earlycascade-injection]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[injectors]]
