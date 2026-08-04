---
title: usb-monitor-bof
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/jakobfriedl__usb-monitor-bof.md
updated: 2026-08-04
confidence: medium
---

# usb-monitor-bof

Cobalt Strike **Beacon Object File (BOF)** that asynchronously monitors USB device insertion and removal on Windows via `WM_DEVICECHANGE`, reporting connected device info back to the operator. Can act on USB storage volumes (Conquest integration) and optionally coerce NetNTLM via `.url` files on removable media. (source: wiki/sources/descriptions/jakobfriedl__usb-monitor-bof.md)

Illustrates the same mid-session USB hotplug surface that AC **hardware enumeration** rules target (known cheat-device VID/PID, sudden device attach during gameplay). Complements user-mode file watchers such as [[readdirectorychanges]] with device-level telemetry in the Some Tricks / Windows Ring3 lane.

## Links

- Repo: https://github.com/jakobfriedl/usb-monitor-bof

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[readdirectorychanges]] · [[sigflip]]
