---
title: wpp
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/btbd__wpp.md
updated: 2026-08-17
confidence: medium
---

# wpp

**wpp** (btbd/wpp) is a kernel proof-of-concept that intercepts driver **DeviceControl** by hijacking **Windows Software Trace Preprocessor (WPP)** tracing infrastructure. It repoints WPP trace function pointers and control flags in system drivers such as `disk.sys` and `mountmgr.sys`, then detects DeviceControl invocations via return-address checks and IRP pointer extraction through stack walking or register capture. The sample shows how `.data` section WPP pointers in signed drivers can be repurposed for unconventional hooking — including HWID research via disk-serial interception. (source: wiki/sources/descriptions/btbd__wpp.md)

Sits in the Ring0 driver-hijack lane beside `.data` pointer swap research such as [[afd-irp-call-dispatch]], [[data-ptr-swap]], and [[driver-read-write]], and upstream to BTBD HWID research such as [[hwid]] and forks such as [[driver-hwid-btbd-modified]].

## Links

- Repo: https://github.com/btbd/wpp

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[hwid]] · [[driver-hwid-btbd-modified]] · [[afd-irp-call-dispatch]] · [[driver-read-write]] · [[easy-hwid-spoofer]] · [[hdd-serial-spoofer]]
