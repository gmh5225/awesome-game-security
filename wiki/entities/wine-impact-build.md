---
title: Wine Impact Build
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/AlexPfaltz__wine-impact-build.md
updated: 2026-11-28
confidence: medium
---

# Wine Impact Build

**wine-impact-build** (AlexPfaltz) — patches and build automation for a modified Wine **ntoskrnl.exe** shim so **Impact** and **MRAC** kernel-style anti-cheat used by titles such as **Allods Online** can run under Wine or Proton on GNU/Linux. Extends Wine’s NT kernel implementation with behaviors proprietary AC drivers expect: MDL and locked-page mapping, virtual memory copy, process-creation notify routines, process image names and timestamps, security impersonation helpers, and x86_64 **KPCR** current-thread handling via gs-relative TEB state. An expanded patch set also improves IRP dispatch by resolving user-mode handles from the client process when device-manager context would otherwise break driver I/O. Primary changes are C against Wine’s ntoskrnl sources, plus shell deployment helpers and optional GitHub Actions workflows that publish downloadable build artifacts. Targets players and researchers who need Linux compatibility with proprietary kernel AC stacks—not a standalone cheat or bypass product. (source: wiki/sources/descriptions/AlexPfaltz__wine-impact-build.md)

Sits in the Wine/Proton **kernel-shim compatibility** lane beside [[proton]], user-mode prefix tooling such as [[pointblank-linux]], and GNU/Linux AC compatibility trackers such as [[are-we-anti-cheat-yet]] and [[ac-compat-research]].

## Stack

- **Target AC:** Impact, MRAC (e.g. Allods Online).
- **Runtime:** Patched Wine `ntoskrnl.exe` under Wine/Proton.
- **Kernel exports stubbed/emulated:** MDL/map, `MmCopyVirtualMemory`, process notify, image name/time, impersonation, KPCR/TEB on x86_64; optional IRP user-handle resolution.
- **Delivery:** C patches, deploy scripts, CI build artifacts.

## Links

- Repo: https://github.com/AlexPfaltz/wine-impact-build [CI-built Wine ntoskrnl.exe patches and deploy scripts to run Impact/MRAC (Allods Online) anti-cheat under Proton/Wine with stubbed kernel exports]

## Related

[[proton]] · [[pointblank-linux]] · [[are-we-anti-cheat-yet]] · [[ac-compat-research]] · [[winehooks]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]