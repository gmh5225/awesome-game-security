---
title: PipeViewer
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/cyberark__PipeViewer.md
updated: 2026-08-16
confidence: medium
---

# PipeViewer

**PipeViewer** is a Windows GUI tool for enumerating and inspecting **named pipes** on the system. It lists active pipe instances with **security descriptors**, **connected clients**, **access modes**, and **owning process** information. The C# application supports filtering, searching, and **real-time monitoring** of pipe creation and deletion — aimed at security researchers, malware analysts, and penetration testers studying Windows IPC and named-pipe attack surfaces. (source: wiki/sources/descriptions/cyberark__PipeViewer.md)

Complements live pipe I/O interceptors such as [[thats-no-pipe]] for endpoint discovery before protocol capture, and AC client↔driver pipe research such as [[battleye-decryption]].

## Links

- Repo: https://github.com/cyberark/PipeViewer (README: Shows detailed information about named pipes in Windows)

## Related

[[thats-no-pipe]] · [[battleye-decryption]] · [[winobjex64]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
