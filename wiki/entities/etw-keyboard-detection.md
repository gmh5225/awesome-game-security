---
title: EtwKeyboardDetection
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Oliver-1-1__EtwKeyboardDetection.md
updated: 2026-08-22
confidence: medium
---

# EtwKeyboardDetection

**Windows proof-of-concept** (Oliver-1-1) for detecting **emulated keyboard input** using **ETW traces**. Native C++ code monitors USB-related telemetry paths and compares observed events to distinguish **physical key presses** from **software-generated input**. Requires manual setup and keyboard-specific tuning — useful as a starting point for **input integrity** research in anti-cheat and endpoint security. README **[ETW]**. (source: wiki/sources/descriptions/Oliver-1-1__EtwKeyboardDetection.md)

Complements sibling mouse-validation PoC [[mousedetection]] and sits opposite offensive keyboard injection samples such as [[karlann]] and [[directinput]], with ETW telemetry context in [[concepts/etw-threat-intelligence]].

## Links

- Repo: https://github.com/Oliver-1-1/EtwKeyboardDetection

## Related

[[mousedetection]] · [[karlann]] · [[directinput]] · [[delbot-mouse]] · [[concepts/etw-threat-intelligence]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
