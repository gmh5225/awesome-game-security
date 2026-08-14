---
title: BE BattlEye Shellcode
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__BE-BattlEye_shellcode.md
updated: 2026-08-14
confidence: medium
---

# BE BattlEye Shellcode

Study scaffold (gmh5225) that reimplements recent [[battleye]] **user-mode shellcode** behavior as a DLL mimicking the anti-cheat's in-process scan stages. A worker thread runs hidden system-thread checks, `KiUserExceptionDispatcher` hook detection, module and function integrity checks, signature scanning, and thread scanning in the same sequence shown by sample BE shellcode wrappers. Vectored exception handler setup registers Win32 and CRT targets (`GetAsyncKeyState`, `NtUserPeekMessage`, `NtSetEvent`, `sqrtf`) so shellcode-style control flow can recover after guarded calls. (source: wiki/sources/descriptions/gmh5225__BE-BattlEye_shellcode.md)

Complements [[be-shellcode]] (weak1337; offline dump/disasm of known BE detection lanes) and live capture tools [[be-shellcode-dump]] / [[battleye-shellcode-dumper]] by focusing on faithful reproduction of recent BE scanning logic rather than generic shellcode placeholders.

## Links

- Repo: https://github.com/gmh5225/BE-BattlEye_shellcode

## Related

[[battleye]] · [[be-shellcode]] · [[be-shellcode-dump]] · [[battleye-shellcode-dumper]] · [[system-thread-finder]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
