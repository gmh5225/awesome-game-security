---
title: KDBG
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/allogic__KDBG.md
updated: 2026-08-18
confidence: medium
---

# KDBG

**Windows kernel debugging toolkit** pairing a kernel driver backend with a command-line client. Exposes low-level **memory read/write** for user processes and kernel modules, **module/thread enumeration**, and **trace-oriented** features, with additional debugger capabilities in progress. Targets **x64** workflows and requires driver-loading steps that may temporarily alter **driver-signing** policy. Aimed at advanced researchers doing low-level game debugging, anti-cheat analysis, and kernel security experimentation. (source: wiki/sources/descriptions/allogic__KDBG.md)

README lane: Tool.

Complements LiveKD-style tooling such as [[kn-live-dbg]], stealth KD attach via [[nokd]], and WinDbg automation such as [[windbg-scripts]] / [[mcp-windbg]] — but focuses on driver-backed CLI memory primitives and enumeration rather than TUI disassembly or WinDbg protocol tricks. Pair with [[windows-kernel-debugging-guide]] for remote KD setup and [[wkpe]] for educational kernel memory-manager experiments.

## Links

- Repo: https://github.com/allogic/KDBG

## Related

[[kn-live-dbg]] · [[nokd]] · [[windbg-scripts]] · [[wkpe]] · [[windows-kernel-debugging-guide]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
