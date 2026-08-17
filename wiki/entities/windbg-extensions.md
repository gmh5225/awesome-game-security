---
title: WinDbg-Extensions
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/ch3rn0byl__WinDbg-Extensions.md
updated: 2026-08-17
confidence: medium
---

# WinDbg-Extensions

WinDbg extension that enumerates kernel callback registrations during live kernel-debug sessions. Walks `PspCreateProcessNotifyRoutine`, `PspCreateThreadNotifyRoutine`, and `PspLoadImageNotifyRoutine`, listing callback pointers with owning driver modules; optional filters for process, thread, image, or all types. (source: wiki/sources/descriptions/ch3rn0byl__WinDbg-Extensions.md)

Useful for anti-cheat researchers, rootkit hunting, and driver analysis when correlating notify routines with loaded `.sys` images — complements GUI enumerators such as [[openark]] and [[winobjex64]], static API catalogs such as [[kernel-callback-functions-list]], and other WinDbg automation such as [[windbg-scripts]] and [[windbg-decompile-ext]].

## Links

- Repo: https://github.com/ch3rn0byl/WinDbg-Extensions (README tag: Callback Extension)

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[kernel-callback-functions-list]] · [[openark]] · [[winobjex64]] · [[windbg-scripts]] · [[windbg-decompile-ext]]
