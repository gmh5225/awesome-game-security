---
title: Battleye-VAC-EAC-Kernel-Bypass
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/daswareinfach__Battleye-VAC-EAC-Kernel-Bypass.md
updated: 2026-08-16
confidence: medium
---

# Battleye-VAC-EAC-Kernel-Bypass

Windows **kernel driver** that targets [[battleye]], Valve Anti-Cheat (VAC), and [[easy-anti-cheat]] by **hiding processes** and exposing **kernel-level read/write memory** to a usermode client over **IOCTL** dispatch. Concealment combines **filesystem minifilter** (`FltRegisterFilter`), **registry filtering**, and **process monitoring callbacks** so the driver and protected cheat processes are less visible to AC enumeration. README category: **FsFilter Testing** — primarily for researchers studying kernel AC bypass, driver-based process hiding, and FSFilter/registry-callback evasion surfaces. (source: wiki/sources/descriptions/daswareinfach__Battleye-VAC-EAC-Kernel-Bypass.md)

Complements process-hide samples such as [[blanket]] (ActiveProcessLinks / PspCidTable / `NtQuerySystemInformation` hook) and rootkit frameworks such as [[fenrir]]; differs by bundling cross-process kernel R/W with FSFilter + registry + notify-based concealment aimed at the three major PC AC stacks.

## Links

- Repo: https://github.com/daswareinfach/Battleye-VAC-EAC-Kernel-Bypass (README: FsFilter Testing)

## Related

[[battleye]] · [[easy-anti-cheat]] · [[kernel-callbacks]] · [[blanket]] · [[fenrir]] · [[vaultguard]] · [[battleye-handler-bypass]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
