---
title: lldbext-dump
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/mrexodia__lldbext-dump.md
updated: 2026-07-29
confidence: medium
---

# lldbext-dump

LLDB Python extension that snapshots a live Android debug target into a Windows-compatible minidump (`.dmp`): all mapped memory regions, thread contexts, and loaded modules. Intended for mobile game/native RE when you need an offline process image without Windows-only dump APIs. A companion emulation script replays the capture with dumpulator-style Unicorn Engine execution on the frozen memory layout. (source: wiki/sources/descriptions/mrexodia__lldbext-dump.md)

Bridges Android LLDB attach workflows to the same offline minidump parse/emulation lane as [[minidump]] / [[minidumpreader]] and Unicorn harness peers such as [[ripr]] / [[smallworld]]. Companion replay targets [[dumpulator]] (Windows minidump → Unicorn; NT syscall stubs / PEB·TEB / API hooks).

## Links

- Repo: https://github.com/mrexodia/lldbext-dump

## Related

[[dumpulator]] · [[minidump]] · [[minidumpreader]] · [[ephemera]] · [[pwatch]] · [[btrace]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
