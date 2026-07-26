---
title: Poseidon
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/paradoxwastaken__Poseidon.md
updated: 2026-07-26
confidence: medium
---

# Poseidon

Kernel research sample centered on **`NtConvertBetweenAuxiliaryCounterAndPerformanceCounter`** as a cheat / driver-communication path—studying Ring0↔usermode I/O via an auxiliary-counter API rather than obvious IOCTL or named-device surfaces. (source: wiki/sources/descriptions/paradoxwastaken__Poseidon.md)

A 2023 note flags detection vectors identifiable by [[battleye]] and [[easy-anti-cheat]] (some discussed in closed issues). Mainly useful for game-security and reverse-engineering researchers mapping offensive KM↔UM channels (adjacent to [[data-ptr-swap]], [[evcommunication]], [[read-write-driver]], [[boom]]).

## Links

- Repo: https://github.com/paradoxwastaken/Poseidon

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[evcommunication]] · [[read-write-driver]] · [[boom]] · [[window-hijack]]
