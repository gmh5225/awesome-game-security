---
title: AntiCheat (SLAUC91)
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/SLAUC91__AntiCheat.md
updated: 2026-08-21
confidence: medium
---

# AntiCheat (SLAUC91)

Windows scanning suite for detecting malicious activity common in gaming environments. Written mainly in **C++** with a partial **C kernel driver**, built as a Visual Studio Win32/x64 console application. Uses documented and undocumented **Native WinAPI** routines to inspect processes under constrained checks. Feature set covers **USN** and **DNS** scanning, **PE** and **PEB** parsing, module and handle enumeration, thread inspection, driver and system-module scanning, pattern matching, and detection of user-mode **IAT hooks** plus kernel-oriented **MSR**, **IDT**, **SSDT**, and **IRP handler** hooks. Aimed at game security and anti-cheat research — prototyping client-side integrity and hook detection on Windows. (source: wiki/sources/descriptions/SLAUC91__AntiCheat.md)

README lane: **Windows rootkit and cheat scanner** (hooks, handles, drivers, modules). Complements GUI anti-rootkit toolkits such as [[openark]], live injection scanners such as [[xmalhunter]], and hidden-thread detectors such as [[unkover]].

## Links

- Repo: https://github.com/SLAUC91/AntiCheat

## Related

[[openark]] · [[xmalhunter]] · [[unkover]] · [[anticheat-poc]] · [[basic-anti-cheat]] · [[anti-cheat-testing-framework]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
