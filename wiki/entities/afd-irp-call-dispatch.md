---
title: AfdIrpCallDispatch
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/muturikaranja__AfdIrpCallDispatch.md
updated: 2026-07-29
confidence: medium
---

# AfdIrpCallDispatch

C kernel research sample centered on a **`.data` pointer hook in `Afd.sys`** targeting **`AfdIrpCallDispatch`**—an AFD (Auxiliary Function Driver) IRP dispatch path used to study stealthy cheat / driver-communication channels rather than obvious IOCTL or named-device surfaces. (source: wiki/sources/descriptions/muturikaranja__AfdIrpCallDispatch.md)

Mainly useful for game-security and reverse-engineering researchers mapping offensive KM↔UM channels (adjacent to [[data-ptr-swap]], [[dataptrhookwin11]], [[read-write-driver]], [[evcommunication]], [[boom]]).

## Links

- Repo: https://github.com/muturikaranja/AfdIrpCallDispatch

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[dataptrhookwin11]] · [[read-write-driver]] · [[evcommunication]] · [[boom]] · [[poseidon]] · [[window-hijack]]
