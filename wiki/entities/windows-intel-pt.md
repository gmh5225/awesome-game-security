---
title: windows-intel-pt
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/intelpt__WindowsIntelPT.md
updated: 2026-08-04
confidence: medium
---

# windows-intel-pt

**WindowsIntelPT** is a Windows kernel driver and user-mode library for capturing **Intel Processor Trace (IPT)** data. The driver configures IPT MSRs and manages trace buffers; the user-mode API starts/stops traces and processes captured data. Supports per-process and system-wide tracing modes. Aimed at security researchers and tool developers using Intel PT for Windows binary tracing, coverage-guided fuzzing, and execution analysis. (source: wiki/sources/descriptions/intelpt__WindowsIntelPT.md)

Sits beside `ipt.sys` wrapper libraries such as [[winipt]], LBR/BTS branch-recording drivers such as [[branch-monitoring-project]], and Intel hardware-trace libraries such as [[libiht]] as a native Windows IPT capture stack with its own driver. Decode captured buffers with [[processor-trace]] (libipt).

## Links

- Repo: https://github.com/intelpt/WindowsIntelPT (README tag: Intel PT)

## Related

[[winipt]] · [[processor-trace]] · [[libiht]] · [[branch-monitoring-project]] · [[qemu-nyx]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
