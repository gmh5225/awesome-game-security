---
title: ntqueueapcthreadex-ntdll-gadget-injection
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/LloydLabs__ntqueueapcthreadex-ntdll-gadget-injection.md
updated: 2026-08-23
confidence: medium
---

# ntqueueapcthreadex-ntdll-gadget-injection

C **proof of concept** for stealth-oriented Windows code injection using **`NtQueueApcThreadEx`** and random **NTDLL gadgets**. Scans executable sections of `ntdll.dll` for suitable pop-and-return sequences and uses them so queued APC routine pointers appear module-backed while execution returns into shellcode—more legitimate-looking than classic direct APC injection. Documents likely detection vectors. Primary use: offensive tradecraft research and evaluation of anti-cheat or EDR telemetry around APC-based execution. (source: wiki/sources/descriptions/LloydLabs__ntqueueapcthreadex-ntdll-gadget-injection.md)

README lane: **NtQueueApcThreadEx + gadget** — APC injection with NTDLL ROP-style return gadgets.

Complements low-footprint APC injectors such as [[frankenstein-apc-injection]] and [[stealth-apc-dispatcher]], broader injection corpora such as [[process-injection-techniques]] and [[windows-process-injection]], and APC internals study such as [[apc-research]]. Same author lane as [[shellcode-plain-sight]] and [[wsb-detect]].

## Links

- Repo: https://github.com/LloydLabs/ntqueueapcthreadex-ntdll-gadget-injection (README: NtQueueApcThreadEx + gadget)

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[frankenstein-apc-injection]] · [[stealth-apc-dispatcher]] · [[process-injection-techniques]] · [[windows-process-injection]] · [[apc-research]] · [[shellcode-plain-sight]] · [[wsb-detect]]
