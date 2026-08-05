---
title: CFB
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/hugsy__CFB.md
updated: 2026-08-05
confidence: medium
---

# CFB

**CFB** (Canadian Furious Beaver) is a Windows kernel-mode **IRP (I/O Request Packet) monitoring framework**. A filter driver hooks the IRP dispatch table of target drivers and logs IRP requests with parameters, buffers, and return values. The C kernel driver plus Python client enable real-time monitoring of driver communication for reverse engineering IOCTL interfaces. Aimed at Windows kernel researchers and reverse engineers studying driver communication protocols and IOCTL fuzzing. (source: wiki/sources/descriptions/hugsy__CFB.md)

Complements static driver analysis via [[cognitor]] / [[ida-kmdf]] and offensive IRP-hijack research such as [[afd-irp-call-dispatch]] / [[gina-public]] when mapping how legitimate drivers expose IOCTL surfaces.

## Links

- Repo: https://github.com/hugsy/CFB

## Related

[[cognitor]] · [[ida-kmdf]] · [[afd-irp-call-dispatch]] · [[gina-public]] · [[keyboardkit]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
