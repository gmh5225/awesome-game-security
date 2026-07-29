---
title: emulator
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/mojtabafalleh__emulator.md
updated: 2026-07-29
confidence: medium
---

# emulator

Debugger-emulator hybrid built on Unicorn Engine and Capstone that loads PE binaries, emulates x86/x64 execution with API hooking, and provides detailed instruction-level logging. Resolves imports via dbghelp, maps PE sections into the emulator address space, and intercepts Windows API calls to simulate OS behavior — useful for analyzing DRM-protected or obfuscated executables without live attach. (source: wiki/sources/descriptions/mojtabafalleh__emulator.md)

Sits in the `Windows User Space Emulator` lane alongside Unicorn peers such as [[sogen]] and [[dumpulator]], WHP-hosted [[winvisor]], and RING3 driver sandboxes such as [[kace]].

## Links

- Repo: https://github.com/mojtabafalleh/emulator (README tag: Windows User Space Emulator)

## Related

[[sogen]] · [[dumpulator]] · [[winvisor]] · [[kace]] · [[ripr]] · [[smallworld]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
