---
title: winipt
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/intelpt__winipt.md
updated: 2026-08-04
confidence: medium
---

# winipt

**WinIPT** is a C library and companion tools for controlling **Intel Processor Trace (IPT)** on Windows. It wraps the Windows IPT driver interfaces (`ipt.sys`) to configure trace buffers and collect IPT data from user-mode and kernel-mode code, supporting per-process and per-CPU tracing modes. Aimed at security researchers and performance analysts using Intel PT for code coverage, fuzzing, and execution tracing on Windows. (source: wiki/sources/descriptions/intelpt__winipt.md)

Sits beside LBR/BTS branch-recording drivers such as [[branch-monitoring-project]], Intel hardware-trace libraries such as [[libiht]], and Intel-PT hypervisor fuzzing stacks such as [[qemu-nyx]] as a native Windows IPT capture option. Decode captured buffers with [[processor-trace]] (libipt).

## Links

- Repo: https://github.com/intelpt/winipt (README tag: `ipt.sys`)

## Related

[[processor-trace]] · [[libiht]] · [[branch-monitoring-project]] · [[qemu-nyx]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
