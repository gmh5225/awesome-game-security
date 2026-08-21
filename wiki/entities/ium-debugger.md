---
title: IUM-Debugger
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/ReverseWarrior__IUM-Debugger.md
updated: 2026-08-21
confidence: medium
---

# IUM-Debugger

**IUM-Debugger** (ReverseWarrior/IUM-Debugger) is a **.NET-based debugger** for Windows **Isolated User Mode (IUM / trustlet)** processes. It uses **Hyper-V hypercalls** to read and write trustlet memory and to **disassemble protected code** running in **Virtualization-Based Security (VBS) / VSM secure enclaves** (VTL1). The workflow is a **Hyper-V host-side tool** via LiveCloudKd `hvmm.sys`: patch the guest **securekernel debug check in live RAM** so **WinDbg in the guest** can attach to **VTL1 IUM trustlets**. Aimed at kernel and RE researchers studying VBS isolation boundaries—not a general-purpose usermode debugger. (source: wiki/sources/descriptions/ReverseWarrior__IUM-Debugger.md)

Sits beside Hyper-V introspection and hypercall research such as [[hyper-rev]] and [[hyperdeceit]], and VBS memory-protection concepts under [[hvci]].

## Links

- Repo: https://github.com/ReverseWarrior/IUM-Debugger

## Related

[[hvci]] · [[hyper-rev]] · [[hyperdeceit]] · [[windbg-scripts]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
