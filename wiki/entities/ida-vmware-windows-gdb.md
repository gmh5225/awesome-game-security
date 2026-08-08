---
title: IDA VMware Windows GDB
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__ida_vmware_windows_gdb.md
updated: 2026-08-08
confidence: medium
---

# IDA VMware Windows GDB

IDA Pro configuration and guide for **live Windows kernel debugging** of VMware guests over the **GDB protocol**. Wires IDA's GDB debugger to VMware's built-in GDB stub so researchers can set breakpoints, inspect memory, and single-step kernel code from IDA while the guest runs in a VM. Aimed at kernel researchers who prefer IDA's disassembly and annotation workflow over WinDbg-only setups. (source: wiki/sources/descriptions/gmh5225__ida_vmware_windows_gdb.md)

Configuration/guide rather than a standalone debugger — complements WinDbg-centric material such as [[windows-kernel-debugging-guide]], agent MCP tooling like [[mcp-windbg]], and IDA-side static KMDF annotation via [[ida-kmdf]]. VMware guest hardening loaders such as [[vmware-hardened-loader]] sit in the adjacent VM anti-analysis lane.

## Links

- Repo: https://github.com/gmh5225/ida_vmware_windows_gdb

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[windows-kernel-debugging-guide]] · [[windbg-scripts]] · [[mcp-windbg]] · [[iida-mcp]] · [[ida-kmdf]] · [[vmware-hardened-loader]]
