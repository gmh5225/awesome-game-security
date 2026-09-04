---
title: Zodiak
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/3a1__Zodiak.md
updated: 2026-09-04
confidence: medium
---

# Zodiak

**Zodiak** (3a1/Zodiak) is a **full kernel driver cheat** for **Counter-Strike 1.6** (Fastcup) designed to **minimize user-visible traces** on the system. Implemented in **C and assembly**, it combines **kernel GDI-based ESP rendering** with **MouHID callback abuse** for aimbot input control. The project documents **automatic offset detection**, **thread context spoofing**, and a **compact single-thread execution model**. Primary audience is advanced game security researchers studying kernel-level cheat engineering and anti-cheat evasion strategies. (source: wiki/sources/descriptions/3a1__Zodiak.md)

Sits in the ring-0 CS 1.6 lane beside user-mode samples such as [[oxware]], [[hpp-hack]], [[ezfrags]], and external ESP samples from the same author such as [[evelion]], and full-kernel CS:GO frameworks such as [[csgo-full-kernel]] and [[raybot-zero]]. Technique-wise it bridges [[kernel-gdi-draw]] / [[kernel-drawing]] GDI render paths and [[mouhid-input-hook]] MouHid ClassService interception for combined ESP + aimbot from one driver.

## Techniques

| Area | Approach |
|------|----------|
| Visuals | Kernel GDI ESP rendering |
| Aimbot | MouHID callback abuse for input injection |
| Offsets | Automatic offset detection |
| Stealth | Thread context spoofing; single-thread execution model |
| Footprint | Minimize user-visible system traces |

## Links

- Repo: https://github.com/3a1/Zodiak (CS 1.6 Fastcup Full Kernel Driver Cheat)

## Related

[[evelion]] · [[oxware]] · [[hpp-hack]] · [[ezfrags]] · [[csgo-full-kernel]] · [[kernel-gdi-draw]] · [[kernel-drawing]] · [[mouhid-input-hook]] · [[kernel-mouse]] · [[zero-thread-kernel]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
