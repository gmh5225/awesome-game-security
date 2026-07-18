---
title: WinDefCtl
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__WinDefCtl.md
updated: 2026-07-18
confidence: medium
---

# WinDefCtl

CLI utility to halt, disable, and neutralize Windows Defender real-time protection and Tamper Protection on Windows 11 (26H1). Uses a kernel driver for privilege escalation, bypasses forced UAC/GUI paths, and aims for invisible execution with automatic privilege handling plus stealth techniques to avoid detection. (source: wiki/sources/descriptions/wesmar__WinDefCtl.md)

Useful research reference for the AV/EDR-control and platform-trust lane when studying how signed/kernel helpers open paths past Defender Tamper Protection under modern Windows assumptions—adjacent to DSE/vulnerable-driver work such as [[kvc]] and process-kill BYOVD samples such as [[av-edr-killer]].

## Links

- Repo: https://github.com/wesmar/WinDefCtl

## Related

[[byovd]] · [[kvc]] · [[av-edr-killer]] · [[ven0m-ransomware]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
