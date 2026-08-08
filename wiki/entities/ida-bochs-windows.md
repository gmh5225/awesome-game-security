---
title: IDA Bochs Windows
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__ida_bochs_windows.md
updated: 2026-08-08
confidence: medium
---

# IDA Bochs Windows

Configuration guide or plugin for using **IDA Pro's Bochs debugger backend on Windows**. Wires IDA to debug binaries through **Bochs software CPU emulation**, enabling full-system debugging including **kernel-mode code analysis** without a live target or traditional KD attach. Aimed at IDA Pro users who need Bochs-based emulation debugging on Windows hosts. (source: wiki/sources/descriptions/gmh5225__ida_bochs_windows.md)

Complements live attach paths such as [[ida-vmware-windows-gdb]] (VMware GDB stub) and WinDbg-centric material like [[windows-kernel-debugging-guide]]. Offline emulation sits beside Unicorn-based replay tooling such as [[emulator]] and [[sogen]] when studying protected or kernel code without hardware.

## Links

- Repo: https://github.com/gmh5225/ida_bochs_windows

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ida-vmware-windows-gdb]] · [[windows-kernel-debugging-guide]] · [[emulator]] · [[sogen]] · [[idacode]]
