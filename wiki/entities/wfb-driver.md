---
title: WFB-Driver
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/BotovodWF__wfb_driver.md
updated: 2026-11-11
confidence: medium
---

# WFB-Driver

Minimal Windows **kernel driver** (`kmemread.sys`) for cross-process virtual memory access when usermode anti-cheat blocks normal `ReadProcessMemory` / `WriteProcessMemory` on protected game clients. IOCTL handlers built on **`MmCopyVirtualMemory`** and **`KeStackAttachProcess`** expose kernel-mode RPM/WPM; companion C utilities run self-tests, magic-byte scans, and dumps of committed private regions. Built in C with MinGW-w64 against the Windows DDK for **test-signed** x64 Windows 10/11 deployment. Aimed at game-security researchers and reverse engineers studying Warface-style clients, **`impactdrv`** **ObCallback** handle filtering, and live in-process anti-cheat blobs—not production bypass or cheat authoring. (source: wiki/sources/descriptions/BotovodWF__wfb_driver.md)

Complements generic `MmCopyVirtualMemory` stress samples such as [[cheat-driver]] and BE handle-path analysis such as [[badeye]] by tying the IOCTL driver pattern to ObCallback-blocked target processes.

## Links

- Repo: https://github.com/BotovodWF/wfb_driver

## Related

[[cheat-driver]] · [[badeye]] · [[concepts/kernel-callbacks]] · [[ntmemory]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
