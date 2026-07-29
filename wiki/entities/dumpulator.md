---
title: dumpulator
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/mrexodia__dumpulator.md
updated: 2026-07-29
confidence: medium
---

# dumpulator

Python framework for emulating x86/x64 code directly from Windows minidump (`.dmp`) files using Unicorn Engine. Reconstructs process memory layout, thread contexts, loaded modules, and handle tables from dump streams; provides NT syscall stubs, PEB/TEB emulation, and API hooking so researchers can call arbitrary functions in the dump's address space without a live process. (source: wiki/sources/descriptions/mrexodia__dumpulator.md)

Sits in the offline minidump parse → execute lane alongside [[minidump]] / [[minidumpreader]] parsers and Unicorn harness peers such as [[sogen]] / [[ripr]] / [[smallworld]]. Companion to [[lldbext-dump]], which captures Android LLDB sessions into Windows-compatible dumps for dumpulator-style replay.

## Links

- Repo: https://github.com/mrexodia/dumpulator

## Related

[[minidump]] · [[minidumpreader]] · [[lldbext-dump]] · [[sogen]] · [[ephemera]] · [[ripr]] · [[smallworld]] · [[kace]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
