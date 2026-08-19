---
title: ioctlpus
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/VoidSec__ioctlpus.md
updated: 2026-08-19
confidence: medium
---

# ioctlpus

**ioctlpus** (VoidSec) is a Windows **DeviceIoControl repeater** for crafting and replaying IOCTL requests against kernel drivers. Written in C# with both WinForms GUI and CLI modes, it lets researchers control arbitrary input and output buffers, save and edit payloads, rerun requests, and inspect responses during testing. Primary use cases are driver security research, IOCTL interface auditing, and fuzzing preparation. (source: wiki/sources/descriptions/VoidSec__ioctlpus.md)

Complements passive IRP tracers such as [[cfb]] and [[drvtrace]] when actively probing known device handles and IOCTL codes, and static driver analysis via [[cognitor]] / [[driver-buddy-reloaded]] when mapping dispatch surfaces.

## Links

- Repo: https://github.com/VoidSec/ioctlpus

## Related

[[cfb]] · [[drvtrace]] · [[cognitor]] · [[driver-buddy-reloaded]] · [[winafl]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
