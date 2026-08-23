---
title: IOCTLDump
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Kharos102__IOCTLDump.md
updated: 2026-08-23
confidence: medium
---

# IOCTLDump

**IOCTLDump** (Kharos102) is a Windows **kernel driver** for hooking and **dumping IOCTL traffic** from other device drivers. It records request metadata—IOCTL code, transport path type, buffer sizes—and can persist **input buffer contents** while deduplicating repeated combinations. The repository ships both driver and **client-side** components for selecting target devices and collecting logs in a defined output layout. Primary use cases are reverse engineering proprietary drivers, including **anti-cheat interfaces** and other security-sensitive kernel communication paths. (source: wiki/sources/descriptions/Kharos102__IOCTLDump.md)

README lane: **Monitor IRP**.

Complements passive IRP tracers such as [[cfb]] and [[drvtrace]] when capturing black-box IOCTL flows from kernel modules, and user-mode repeaters [[ioctlpus]] / [[ioctl-helper]] when replaying discovered control codes. Defensive dispatch-integrity scanners such as [[device-control-hooks-scanner]] audit hooked `IRP_MJ_DEVICE_CONTROL` handlers rather than logging IOCTL payloads.

## Links

- Repo: https://github.com/Kharos102/IOCTLDump (README tag: Monitor IRP)

## Related

[[cfb]] · [[drvtrace]] · [[ioctlpus]] · [[ioctl-helper]] · [[device-control-hooks-scanner]] · [[driver-buddy-reloaded]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
