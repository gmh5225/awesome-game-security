---
title: GhostVEH
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/EvilBytecode__GhostVEH.md
updated: 2026-08-25
confidence: medium
---

# GhostVEH

**GhostVEH** (EvilBytecode) is a **C++ proof-of-concept** demonstrating stealthy manipulation of the Windows **Vectored Exception Handler (VEH)** chain. Instead of registering handlers through `RtlAddVectoredExceptionHandler`, it locates ntdll's internal **`LdrpVectorHandlerList`**, uses **`RtlEncodePointer`** / **`RtlDecodePointer`** for handler pointer obfuscation, and calls **`LdrProtectMrdata`** to unlock the protected **MRDATA** section for in-place list modification. Primary audience is security researchers studying VEH internals, anti-debug techniques, and exception-handler manipulation on Windows. (source: wiki/sources/descriptions/EvilBytecode__GhostVEH.md)

Complements VEH registration research such as [[custom-veh]] (`RtlpCallVectoredHandlers` hook), direct **`LdrpVectorHandlerList`** manipulation in the same stealth lane, and alternative dispatch hooks such as [[ki-user-exception-dispatcher-hook]] (`.mrdata` pointer patch via `LdrProtectMrdata`; avoids VEH chain). VEH-chain dumpers such as [[veh-dumper]] and defensive VEH inspection in [[godefender]] sit in the same exception-dispatch research lane.

README category: Register VEH by directly manipulating LdrpVectorHandlerList instead of RtlAddVectoredExceptionHandler.

## Links

- Repo: https://github.com/EvilBytecode/GhostVEH

## Related

[[custom-veh]] · [[ki-user-exception-dispatcher-hook]] · [[veh-dumper]] · [[veh]] · [[dump-val-exception-handler]] · [[godefender]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
