---
title: WinVisor
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/x86matthew__WinVisor.md
updated: 2026-07-18
confidence: medium
---

# WinVisor

Hypervisor-based emulator for Windows x64 user-mode executables via the Windows Hypervisor Platform (WHP) API: runs guest PE code in a virtualized environment hosted from user mode. Aimed at emulator developers and Windows platform researchers in the `Windows Emulator` lane—not a production anti-cheat component. (source: wiki/sources/descriptions/x86matthew__WinVisor.md)

Complements WHP trap-driven / hypervisor-aware RE workflows next to Type-2 learning stacks such as [[hv]] (kernel VT-x) — WinVisor stays on the WHP user-mode path rather than a custom VMX driver.

## Links

- Repo: https://github.com/x86matthew/WinVisor (README tag: Windows Emulator)

## Related

[[hv]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
