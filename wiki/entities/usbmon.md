---
title: UsbMon (KelvinMsft)
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/KelvinMsft__UsbMon.md
updated: 2026-08-23
confidence: medium
---

# UsbMon (KelvinMsft)

**UsbMon** is a **kernel-mode USB and HID monitoring framework** for tracing device data flows into consumer processes on Windows. Driver components hook **IRP** paths and internal **IOCTL** or **URB** handling, **parse HID reports**, and coordinate capture or mapping control through custom **device control codes**. Implementation is mostly **C** with some **C++** project scaffolding, focused on Windows driver development and low-level input-stack analysis. Useful for reverse engineering USB input behavior in game-security contexts, including studies of **HID-based attack or detection surfaces**. (source: wiki/sources/descriptions/KelvinMsft__UsbMon.md)

Complements MouHid callback-hook samples such as [[mouhid-input-hook]] and MouClass injection PoCs such as [[kernel-mouse]] when studying upstream USB/HID telemetry rather than class-driver callback interception. Pairs with IRP/IOCTL tracers such as [[ioctldump]], [[cfb]], and [[drvtrace]] for driver-interface RE.

## Links

- Repo: https://github.com/KelvinMsft/UsbMon

## Related

[[mouhid-input-hook]] · [[kernel-mouse]] · [[ioctldump]] · [[cfb]] · [[drvtrace]] · [[hardware-input-injection]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
