---
title: OfflineCrashDumpUefi
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__OfflineCrashDumpUefi.md
updated: 2026-08-11
confidence: medium
---

# OfflineCrashDumpUefi

Microsoft **EDK2** package for **Offline Crash Dump** support on Windows-capable firmware: the platform writes a memory dump **before or instead of** the operating system handling crash collection. Ships shared headers for dump GUIDs/structures, `OfflineDumpLib` helpers (dump-partition discovery, Windows-defined UEFI variable reads), and `OfflineDumpWriterLib` (buffered dump generation with encryption and redaction). Includes redistributable/sample UEFI apps such as `OfflineDumpWrite.efi`, benchmarks, tests, and a full DXE package layout usable as a reference for other firmware stacks. Upstream README positions the code for **bring-up, debugging, and device stabilization** rather than retail deployment—most useful to firmware/platform engineers studying pre-OS crash collection. (source: wiki/sources/descriptions/gmh5225__OfflineCrashDumpUefi.md)

Complements live OS-side acquirers such as [[dumpit-mirror]] and [[tool-diy-system-memory-dump]] in the offline memory-forensics lane, but captures from **firmware DXE** rather than a running Windows kernel.

## Links

- Repo: https://github.com/gmh5225/OfflineCrashDumpUefi

## Related

[[dumpit-mirror]] · [[tool-diy-system-memory-dump]] · [[eficmake]] · [[minivisorpkg]] · [[volatility]] · [[volatility3]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
