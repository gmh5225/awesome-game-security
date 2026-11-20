---
title: deltaforce-cleaner
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Siselea__deltaforce-cleaner.md
updated: 2026-11-20
confidence: medium
---

# deltaforce-cleaner

**Delta Force Cleaner** (Siselea) is a Windows **clean uninstaller** for Delta Force (三角洲行动) that removes the game and **leftover Tencent ACE (AntiCheatExpert)** stack artifacts after a normal uninstall. Implemented in **Python 3.9+** with only the standard library: Tk GUI, CLI, and a headless engine module with unit tests and **dry-run** support. (source: wiki/sources/descriptions/Siselea__deltaforce-cleaner.md)

## Scope

The scanner targets ACE **kernel drivers** and versioned services, Program Files and ProgramData install paths, game folders across drives, uninstall registry keys, **WeGame** remnants, and launcher shortcuts. It explicitly **excludes** Windows storage drivers that falsely match ACE naming and shared Tencent folders used by WeChat or QQ. Detection rules are documented so each removal target is provably ACE- or game-owned, with protected lists to avoid damaging the OS or other Tencent apps.

## Audience

Players, researchers, and security practitioners who need a **reviewable, repeatable** way to fully purge persistent kernel-level anti-cheat after uninstall—complementary to runtime mitigation tools such as [[fuck-ace]] and [[anticheattoggle]] rather than bypass or cheat development.

## Links

- Repo: https://github.com/Siselea/deltaforce-cleaner

## Related

[[fuck-ace]] · [[anticheattoggle]] · [[sguard-limit]] · [[ff-ace-anticheat-analysis]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]