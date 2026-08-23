---
title: Usugumo
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/M3351AN__Usugumo.md
updated: 2026-08-23
confidence: medium
---

# Usugumo

Windows **kernel-mode proof-of-concept driver** from **M3351AN** that proxies **memory and input operations** for user-mode clients. Written in C/C++ with some MASM, it handles **DIRECT_IO IRP** requests for cross-process **RPM/WPM**, process lookup, module information, and **mouse/keyboard injection**. The repository also ships anti-capture and driver↔usermode communication examples while explicitly stating the project is **not production-ready**. Primary use case: kernel communication and low-level game-security experimentation on x64 Windows. README tag: **Kernel-mode W/RPM/mouse_event for Windows**. (source: wiki/sources/descriptions/M3351AN__Usugumo.md)

Sits in the combined KM memory + input proxy lane beside [[driver-physical-rw]], [[norsefire]], and [[readwrite-kernel-stable]], and complements same-author usermode tooling such as [[shirakumo]], [[mouse-input-injection]], BYOVD injection research such as [[zhangbing-injector]], and kernel-assisted CS2 externals such as [[ukia-rpm]].

## Architecture highlights

| Component | Role |
|-----------|------|
| DIRECT_IO IRP dispatch | User–kernel proxy via structured IRP buffers |
| Memory ops | Cross-process RPM/WPM |
| Process helpers | Process lookup and module information |
| Input injection | Kernel mouse and keyboard injection paths |
| Examples | Anti-capture and KM↔UM communication samples |

## Links

- Repo: https://github.com/M3351AN/Usugumo (README: Kernel-mode W/RPM/mouse_event for Windows)

## Related

[[driver-physical-rw]] · [[norsefire]] · [[readwrite-kernel-stable]] · [[km-um-communication]] · [[kernel-mouse]] · [[mouse-input-injection]] · [[shirakumo]] · [[zhangbing-injector]] · [[ukia-rpm]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
