---
title: DataPtrHookWin11
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/oakboat__DataPtrHookWin11.md
updated: 2026-07-27
confidence: medium
---

# DataPtrHookWin11

C/C++ Win11 kernel research sample centered on **`NtUserSetGestureConfig`**—a win32k gesture-config path used to study data-pointer hook / cheat driver-communication channels rather than obvious IOCTL or named-device surfaces. (source: wiki/sources/descriptions/oakboat__DataPtrHookWin11.md)

Mainly useful for game-security and reverse-engineering researchers mapping offensive KM↔UM channels (adjacent to [[data-ptr-swap]], [[read-write-driver]], [[evcommunication]], [[boom]]).

## Links

- Repo: https://github.com/oakboat/DataPtrHookWin11

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[read-write-driver]] · [[evcommunication]] · [[boom]] · [[poseidon]] · [[window-hijack]]
