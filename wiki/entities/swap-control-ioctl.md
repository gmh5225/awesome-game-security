---
title: Swap-control-ioctl
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Barracudach__Swap-control-ioctl.md
updated: 2026-08-31
confidence: medium
---

# Swap-control-ioctl

Windows **kernel proof-of-concept** that intercepts a target driver's **`IRP_MJ_DEVICE_CONTROL`** dispatch routine via **dispatch-pointer redirection** and a **trampoline**, forwarding ioctl traffic through custom handling logic. The sample implements process **memory copy**, **allocation**, and **protection** request handlers plus **module base lookup**. Primary use case is studying **driver communication hooks** and **anti-cheat detection** around ioctl interception. (source: wiki/sources/descriptions/Barracudach__Swap-control-ioctl.md)

README lane: **Hijack IRP SpeedFan.sys** — same legitimate-driver hijack pattern as [[driver-read-write]] on `Beep.sys`, but targeting **SpeedFan.sys** device-control dispatch.

Complements defensive `IRP_MJ_DEVICE_CONTROL` integrity scanners such as [[device-control-hooks-scanner]] and passive IOCTL tracers such as [[ioctldump]] / [[cfb]].

## Links

- Repo: https://github.com/Barracudach/Swap-control-ioctl (README tag: Hijack IRP SpeedFan.sys)

## Related

[[driver-read-write]] · [[device-control-hooks-scanner]] · [[ioctldump]] · [[cfb]] · [[driver-driver-no-image]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
