---
title: launcher-abuser
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Ricardonacif__launcher-abuser.md
updated: 2026-08-21
confidence: medium
---

# launcher-abuser

Stealth **external memory access** technique that reuses the **game process handle already held by platform launchers** such as Steam and Battle.net (Ricardonacif). A controller process communicates over **named shared memory**; a **minimal shellcode payload** is injected into the launcher and **hijacks an existing launcher thread** rather than opening new cross-process handles, loading modules, creating threads, or allocating executable pages. Uses **x86-to-x64 transition** logic and **direct-syscall** `NtReadVirtualMemory` / `NtWriteVirtualMemory` to read and write target game memory. Aimed at game-security research into **low-footprint process interaction** and anti-cheat evasion tradeoffs. (source: wiki/sources/descriptions/Ricardonacif__launcher-abuser.md)

Sits in the Cheat → **Launcher Abuser** lane beside platform-bypass launchers such as [[mini-launcher]], but focused on **covert RPM** through trusted launcher context rather than out-of-client game start.

## Links

- Repo: https://github.com/Ricardonacif/launcher-abuser

## Related

[[mini-launcher]] · [[rce-shield]] · [[windows-process-injection]] · [[frankenstein-apc-injection]] · [[libmem]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
