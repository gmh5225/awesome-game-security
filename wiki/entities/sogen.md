---
title: sogen
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/momo5502__sogen.md
updated: 2026-07-29
confidence: medium
---

# sogen

Windows userspace emulator built on Unicorn Engine and Capstone that executes x86/x64 PE binaries with full syscall emulation, minidump loading, and Zstd-compressed state serialization. Includes a React/TypeScript web UI for interactive emulation sessions, cross-compilation support via Emscripten/Android NDK, and FlatBuffers-based IPC for structured execution traces. (source: wiki/sources/descriptions/momo5502__sogen.md)

Sits in the `Windows User Space Emulator` lane alongside Unicorn harnesses such as [[dumpulator]] and [[kace]], WHP-hosted emulators such as [[winvisor]], and WHP trap libraries such as [[vmtrace]] from the same author.

## Links

- Repo: https://github.com/momo5502/sogen (README tag: Windows User Space Emulator)

## Related

[[dumpulator]] · [[winvisor]] · [[vmtrace]] · [[kace]] · [[minidump]] · [[ripr]] · [[smallworld]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
