---
title: NMI nmi_callback
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__NMI-nmi_callback.md
updated: 2026-08-11
confidence: medium
---

# NMI nmi_callback

Windows kernel proof of concept for **registering and using Non-Maskable Interrupt (NMI) callbacks** — handlers that run on all CPUs simultaneously and are used by anti-cheat systems such as BattlEye to inspect thread contexts and detect hidden threads or injected code. Demonstrates NMI callback registration and cross-processor context inspection for kernel researchers studying NMI-based detection. (source: wiki/sources/descriptions/gmh5225__NMI-nmi_callback.md)

Complements defensive NMI callback research such as [[nmi-callback]], enumeration PoCs such as [[nmi-enum-nmi-callback]], and offensive disable PoCs such as [[nmi-callback-blocker2]] within the broader [[kernel-callbacks]] lane.

## Links

- Repo: https://github.com/gmh5225/NMI-nmi_callback [Triggering NMI]

## Related

[[nmi-callback]] · [[nmi-enum-nmi-callback]] · [[nmi-callback-blocker2]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
