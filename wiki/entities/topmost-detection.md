---
title: TOPMOST-Detection
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Oliver-1-1__TOPMOST-Detection.md
updated: 2026-08-22
confidence: medium
---

# TOPMOST-Detection

Small **Windows C++** utility (Oliver-1-1) that **detects topmost windows** on the desktop. It enumerates visible windows with Win32 APIs and checks extended styles such as **`WS_EX_TOPMOST`** to flag always-on-top overlays. The solution includes a companion console app that marks itself topmost via **`SetWindowPos`** for testing. Mainly useful for **anti-cheat prototyping** and game security experiments that need basic overlay-detection logic. README **Detect simple top most windows**. (source: wiki/sources/descriptions/Oliver-1-1__TOPMOST-Detection.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Visible-window enumeration | Win32 scan of desktop HWNDs |
| `WS_EX_TOPMOST` check | Flags always-on-top overlay candidates |
| Companion test console | Self-topmost via `SetWindowPos` for validation |

Complements overlay-evasion PoCs such as [[not-an-overlay]] and [[window-hijack-overlay]], and modular AC test harnesses such as [[anti-cheat-testing-framework]] that exercise overlay rendering as an attack primitive.

## Links

- Repo: https://github.com/Oliver-1-1/TOPMOST-Detection

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[not-an-overlay]] · [[window-hijack-overlay]] · [[anti-cheat-testing-framework]] · [[uefi-graphic]]
