---
title: Double Data Pointer
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Astronaut00__DoubleDataPointer.md
updated: 2026-09-01
confidence: medium
---

# Double Data Pointer

**DoubleDataPointer** (Astronaut00/DoubleDataPointer) is a Windows kernel communication proof of concept that uses a **double-pointer channel** between user mode and a **manually mapped driver**. The C++ implementation provides primitives for reading and writing **virtual and physical memory** from kernel context. It also demonstrates stealth-oriented techniques such as **page frame number (PFN) cleanup** and **pool-related artifact reduction** while documenting detection risks. Intended for **anti-cheat bypass experimentation** and **low-level game security research**. Listed under cheat / driver communication as README `[Double Data Pointer]`. (source: wiki/sources/descriptions/Astronaut00__DoubleDataPointer.md)

Sits in the **double-pointer / covert KM↔UM comms** lane beside [[data-ptr-swap]], [[data-communication]], and [[comm-data-pointer-swap]], and near manual-map trace hygiene samples such as [[trace-cleaner]] and [[driver-read-write]].

## Capabilities

- Double-pointer user-mode ↔ manually mapped kernel driver channel
- Virtual and physical memory read/write from kernel context
- PFN cleanup and pool artifact reduction (with documented detection risks)

## Links

- Repo: https://github.com/Astronaut00/DoubleDataPointer

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[data-communication]] · [[trace-cleaner]] · [[driver-read-write]] · [[astronaut00-apex-external]]
