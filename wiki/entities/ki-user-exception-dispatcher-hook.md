---
title: KiUserExceptionDispatcher Hook (brew02)
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/brew02__KiUserExceptionDispatcherHook.md
updated: 2026-08-17
confidence: medium
---

# KiUserExceptionDispatcher Hook (brew02)

**KiUserExceptionDispatcherHook** (brew02/KiUserExceptionDispatcherHook) demonstrates hooking **`KiUserExceptionDispatcher`** — the initial user-mode exception dispatcher invoked from the kernel — by modifying the **`Wow64PrepareForException`** function pointer stored in ntdll's protected **`.mrdata`** section. The C++ sample uses **`LdrProtectMrdata`** to unlock MRDATA and **Zydis** to dynamically locate target function pointers within ntdll, offering an alternative exception-handler hooking technique that avoids traditional **VEH chain manipulation**. Aimed at Windows kernel and anti-cheat researchers studying user-mode exception-dispatch internals and stealthy hook installation. (source: wiki/sources/descriptions/brew02__KiUserExceptionDispatcherHook.md)

Complements VEH registration research such as [[custom-veh]] (`RtlpCallVectoredHandlers` hook), direct `LdrpVectorHandlerList` manipulation such as [[ghostveh]] (shared `LdrProtectMrdata` MRDATA unlock pattern), BattlEye `KiUserExceptionDispatcher` hook **detection** in [[be-battleye-shellcode]], and offensive patches such as [[ow2-wardenrekter]] (RET overwrite neutralization).

## Links

- Repo: https://github.com/brew02/KiUserExceptionDispatcherHook

## Related

[[custom-veh]] · [[ghostveh]] · [[be-battleye-shellcode]] · [[ow2-wardenrekter]] · [[veh-dumper]] · [[dump-val-exception-handler]] · [[mount-system-partition]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
