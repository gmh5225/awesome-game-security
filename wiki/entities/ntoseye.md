---
title: ntoseye
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/dmaivel__ntoseye.md
updated: 2026-08-16
confidence: medium
---

# ntoseye

Windows kernel debugger for **Linux hosts** that attaches to Windows 10/11 guests running under KVM/QEMU. Connects through a GDB stub to the hypervisor for guest memory access and register manipulation, exposing WinDbg-style commands plus PDB symbol fetch/parse and breakpoint support — essentially a WinDbg replacement when the analysis host is Linux rather than Windows. (source: wiki/sources/descriptions/dmaivel__ntoseye.md)

Useful for security researchers who need Windows kernel debugging and introspection from a Linux virtualization lab without a Windows host or native WinDbg install.

## Links

- Repo: https://github.com/dmaivel/ntoseye (README tag: Kernel Debugger)

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[windows-kernel-debugging-guide]] · [[ida-vmware-windows-gdb]] · [[memflow-kvm]] · [[nokd]] · [[windbg-scripts]] · [[mcp-windbg]]
