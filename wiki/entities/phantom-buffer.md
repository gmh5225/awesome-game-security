---
title: PhantomBuffer
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/TwoSevenOneT__PhantomBuffer.md
updated: 2026-10-18
confidence: medium
---

# PhantomBuffer

**Windows C++ research tool** that delivers shellcode into a **remote process** without calling `VirtualAllocEx` or `WriteProcessMemory` (TwoSevenOneT). Payload bytes are staged through **`SendMessage` with `WM_SETTEXT`** against a standard **Edit control** window handle so the target process receives the buffer in its own address space via normal GUI message handling. The injector then **pattern-scans remote memory** to locate the staged bytes, adjusts page protection with `VirtualProtectEx`, and redirects the **main thread instruction pointer** through the Windows debugger **`cdb.exe`**. The Visual Studio solution includes **FindTargetWindows**, which enumerates suitable Edit controls or launches hidden helper processes for lab targets. Aimed at offensive security and **EDR bypass** research—studying how endpoint products flag classic cross-process memory writes and how alternative injection paths behave. (source: wiki/sources/descriptions/TwoSevenOneT__PhantomBuffer.md)

README lane: **Injection Testing** — stealth shellcode delivery via SendMessage `WM_SETTEXT` and cdb RIP redirect; avoids `VirtualAllocEx`/`WriteProcessMemory`.

Sits in the **GUI-message / Edit-control** injection lane beside stdin-pipe samples such as [[injectsetconsole]] from the same author and Debug API orchestrators such as [[dbgnexum]], within broader corpora such as [[windows-process-injection]] and [[process-injection-techniques]].

## Technique summary

1. Resolve a remote **Edit** control HWND (FindTargetWindows or lab helper process).
2. Stage shellcode with **`SendMessage(..., WM_SETTEXT, ...)`** so text lands in the target VA space without WPM.
3. **Remote pattern scan** to locate the staged buffer.
4. **`VirtualProtectEx`** to make the region executable.
5. Use **`cdb.exe`** to redirect the main thread **RIP** to the payload.

## Links

- Repo: https://github.com/TwoSevenOneT/PhantomBuffer

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[injectsetconsole]] · [[dbgnexum]] · [[threadject]] · [[windows-process-injection]] · [[process-injection-techniques]] · [[injectors]]
