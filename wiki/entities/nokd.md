---
title: nokd
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/irql__nokd.md
updated: 2026-08-04
confidence: medium
---

# nokd

**Kernel debugger (KD) protocol** implementation that avoids setting the standard ntoskrnl KD globals. It copies `KdDebuggerDataBlock` into local memory, decodes it inline, and supplies that block to WinDbg — making attach harder to flag via `KdDebuggerEnabled` and related kernel anti-debug heuristics. Aimed at game-security researchers and reverse engineers studying offensive kernel inspection in the cheat / Windows kernel explorer lane. (source: wiki/sources/descriptions/irql__nokd.md)

Complements remote KD setup guides such as [[windows-kernel-debugging-guide]], LiveKD-style tooling such as [[kn-live-dbg]], and WinDbg automation such as [[windbg-scripts]] / [[mcp-windbg]] — but targets stealthy KD block provisioning rather than driver-backed memory primitives or scripting.

## Links

- Repo: https://github.com/irql/nokd

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[windows-kernel-debugging-guide]] · [[kn-live-dbg]] · [[windbg-scripts]] · [[mcp-windbg]] · [[titanhide]]
