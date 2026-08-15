---
title: drvtrace
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/eversinc33__drvtrace.md
updated: 2026-08-15
confidence: medium
---

# drvtrace

**drvtrace** (eversinc33) is a Windows **kernel driver tracing** tool that logs **IRP (I/O Request Packet)** traffic to and from specific target drivers. It attaches as a **filter driver** to intercept IRP requests, logging IRP major/minor function codes, buffer contents, and completion status. The C driver provides runtime visibility into driver communication patterns for reverse engineers and security researchers analyzing **IOCTL interfaces** and device communication protocols. (source: wiki/sources/descriptions/eversinc33__drvtrace.md)

Complements static driver analysis via [[cognitor]] / [[driver-buddy-reloaded]] and live IRP monitoring frameworks such as [[cfb]] when mapping how target drivers expose IOCTL and device-control surfaces.

## Links

- Repo: https://github.com/eversinc33/drvtrace

## Related

[[cfb]] · [[cognitor]] · [[driver-buddy-reloaded]] · [[ida-kmdf]] · [[unkover]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
