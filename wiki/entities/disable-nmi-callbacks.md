---
title: Disable NMI callbacks
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Disable-nmi-callbacks.md
updated: 2026-08-14
confidence: medium
---

# Disable NMI callbacks

Kernel driver that **disables NMI (Non-Maskable Interrupt) callbacks** in the Windows kernel. Uses pattern scanning to locate `KiNmiInterruptStart`-related variables in `ntoskrnl.exe` and patches processor affinity and NMI state to block anti-cheat **NMI-based stack-walking** detections. (source: wiki/sources/descriptions/gmh5225__Disable-nmi-callbacks.md)

Adjacent to other disable PoCs such as [[nmi-callback-blocker2]]; complements register/trigger research such as [[nmi-nmi-callback]], enumeration such as [[nmi-enum-nmi-callback]], and defensive NMI callback study such as [[nmi-callback]] within the [[kernel-callbacks]] lane. Defensive NMI stack-walk telemetry appears in experimental AC such as [[kernel-anti-cheat]].

## Links

- Repo: https://github.com/gmh5225/Disable-nmi-callbacks [Disable NMI]

## Related

[[nmi-callback-blocker2]] · [[nmi-nmi-callback]] · [[nmi-enum-nmi-callback]] · [[nmi-callback]] · [[kernel-callbacks]] · [[kernel-anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
