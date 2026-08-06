---
title: GH AntiDebug Bypass Practice Tool
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/guidedhacking__GH_AntiDebug_Bypass_Practice_Tool.md
updated: 2026-08-06
confidence: medium
---

# GH AntiDebug Bypass Practice Tool

Win32 **anti-debug bypass practice** application from Guided Hacking for the `Anti Cheat → Anti Debugging` lane. Implements common Windows debugger-detection checks so reverse engineers and game-security learners can attach a debugger, toggle each method on, and practice bypassing until the overlay stops reporting **DETECTED**. (source: wiki/sources/descriptions/guidedhacking__GH_AntiDebug_Bypass_Practice_Tool.md)

Built as a C++ Visual Studio solution with an **ImGui** overlay on **DirectX 11**. Covered checks include `IsDebuggerPresent`, PEB `BeingDebugged` and `NtGlobalFlag`, `CheckRemoteDebuggerPresent`, heap and LFH flags, `ThreadHideFromDebugger`, trap-flag and SEH tricks, parent-process inspection, and timing via `QueryPerformanceCounter`, `GetTickCount`, and `GetLocalTime`. New methods can be registered as header callbacks in the main loop.

Complements passive technique catalogs such as [[makin]] and [[anti-debugging]], TTD stress samples such as [[ttd-anti-debugging]], and hide/bypass tooling (ScyllaHide-class plugins, [[steam-anti-anti-debug]]) for live attach practice with immediate per-check feedback.

## Links

- Repo: https://github.com/guidedhacking/GH_AntiDebug_Bypass_Practice_Tool

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[makin]] · [[anti-debugging]] · [[ttd-anti-debugging]] · [[scyllahidedetector2]] · [[x64dbg]] · [[intro-to-gamehacking]]
