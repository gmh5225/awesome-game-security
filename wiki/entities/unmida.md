---
title: Unmida
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/pkochubey__Unmida.md
updated: 2026-11-15
confidence: medium
---

# Unmida

Windows command-line Themida unpacker for 32-bit and 64-bit PE executables and DLLs. Written in Go, the tool launches the protected target under a debugger, waits for the packer to unpack the image in memory, locates the original entry point, and rebuilds the import address table into a dumped PE. It uses `golang.org/x/arch` for disassembly, optional ScyllaHide integration to bypass anti-debug checks, and extra modes for shrinking dumps, building section data, and attaching to a process by PID. Aimed at reverse engineers and malware analysts recovering analyzable binaries from Themida-protected software—including games and commercial applications under authorized study. (source: wiki/sources/descriptions/pkochubey__Unmida.md)

Companion surface to Cheat → Fix Themida work ([[magicmida-rs]] Rust Win32 Debug API unpack, [[unlicense]] Frida-driven dynamic unpack, [[unthemidator]] static emulation unpack): Go CLI debugger-driven in-memory dump with OEP/IAT reconstruction rather than Frida instrumentation or Unicorn static emulation.

## Links

- Repo: https://github.com/pkochubey/Unmida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[magicmida]] · [[magicmida-rs]] · [[unlicense]] · [[unthemidator]] · [[bobalkkagi]] · [[themida-research]] · [[tde]]