---
title: Titanium Macro
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/guvenada__Titanium-Macro.md
updated: 2026-09-27
confidence: medium
---

# Titanium Macro

**Titanium Macro Engine** (guvenada) is a Windows input automation framework for recording, editing, and replaying keyboard and mouse macros with kernel-level precision. Written primarily in Python with a PyQt6 GUI, it injects and captures events through an **Interception driver** wrapper, records raw HID trajectories and scan codes, and replays them with sub-millisecond timing via performance counters. Features include Bézier-curve mouse humanization, block-based conditional scripting, screen vision with OpenCV, OCR through Tesseract, coordinate mapping, profiles, and hotkey-driven recording and playback. The project targets game security researchers and anti-cheat engineers studying low-level input automation, macro tooling, and how kernel-mode input injection bypasses standard user-mode APIs. (source: wiki/sources/descriptions/guvenada__Titanium-Macro.md)

## Links

- Repo: https://github.com/guvenada/Titanium-Macro

## Related

[[ib-input-simulator]] · [[autohotkey-l]] · [[mouse-input-injection]] · [[windmouse]] · [[hardware-input-injection]] · [[input-provenance]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
