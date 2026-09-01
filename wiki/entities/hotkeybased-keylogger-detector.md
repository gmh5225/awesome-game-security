---
title: Hotkeybased Keylogger Detector
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/AsuNa-jp__HotkeybasedKeyloggerDetector.md
updated: 2026-09-01
confidence: medium
---

# Hotkeybased Keylogger Detector

**Defensive Windows kernel driver** (AsuNa-jp) that detects keyloggers abusing **global hotkey registration** via `RegisterHotKey`. The driver scans **win32kfull** internals to resolve the global hotkey table and inspects registered entries for suspicious usage patterns. Implemented in **C++** as a **KMDF** driver with installation and debugging guidance for test environments. Intended for **defensive endpoint research** and Windows security testing—not a production EDR product. (source: wiki/sources/descriptions/AsuNa-jp__HotkeybasedKeyloggerDetector.md)

## Detection surface

| Signal | Mechanism |
|--------|-----------|
| **Global hotkey abuse** | Walk win32kfull global hotkey table; flag suspicious `RegisterHotKey` registrations |
| **Kernel context** | KMDF driver; win32kfull structure resolution |

## Positioning

Complements offensive keylog research such as [[keyboardkit]] (keyboard IRP filter + exfil) by targeting an alternate capture path—**hotkey callbacks** rather than IRP interception. Sits in the same win32k GUI-subsystem defensive lane as export-trampoline scanners such as [[driver-detect-nullshit]] and win32k RE references such as [[win32khooker]].

## Links

- Repo: https://github.com/AsuNa-jp/HotkeybasedKeyloggerDetector

## Related

[[keyboardkit]] · [[driver-detect-nullshit]] · [[win32khooker]] · [[win32k-file-collection]] · [[autohotkey-l]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
