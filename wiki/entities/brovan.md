---
title: Brovan
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/AdvDebug__Brovan.md
updated: 2026-09-03
confidence: medium
---

# Brovan

.NET-based binary analysis and emulation framework built on Unicorn Engine. Loads and emulates x86/x64/ARM Windows and Linux binaries—including PE, ELF, raw memory dumps, and unrecognized formats—with syscall emulation, API hooking, and configurable analysis workflows. Ships an interactive debugger shell for step-through RE without live attach. (source: wiki/sources/descriptions/AdvDebug__Brovan.md)

Sits in the Unicorn user-mode emulator lane alongside [[emulator]], [[unicorn-pe]], [[sogen]], and [[dumpulator]], and complements in-IDA Unicorn plugins such as [[sk3wldbg]] and [[ews]].

## Links

- Repo: https://github.com/AdvDebug/Brovan

## Related

[[emulator]] · [[unicorn-pe]] · [[sogen]] · [[dumpulator]] · [[sk3wldbg]] · [[ews]] · [[ripr]] · [[hikarisystem-hexcore]] · [[overviews/reverse-engineering]]
