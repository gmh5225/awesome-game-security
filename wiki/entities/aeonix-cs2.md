---
title: Aeonix CS2
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Fr0go1__Aeonix-Cs2.md
updated: 2026-08-25
confidence: medium
---

# Aeonix CS2

**External Counter-Strike 2 cheat framework** from Fr0go1, built as a derivative of an earlier external base. Implemented in **C++** on Windows, it bundles overlay and tooling components with ESP, aimbot with recoil control (RCS), triggerbot, radar, and config management. The stack follows common external patterns—memory access modules, offset handling, and real-time rendering of visual aids—for offensive game security experimentation and cheat development learning. README **External** tag. (source: wiki/sources/descriptions/Fr0go1__Aeonix-Cs2.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Memory access modules | Out-of-process game state reads |
| Offset handling | Post-patch layout maintenance |
| Overlay + tooling | Real-time ESP and menu rendering |
| ESP / radar | Entity visualization and awareness |
| Aimbot + RCS | Targeting with recoil compensation |
| Triggerbot | Automated fire assist |
| Config management | Feature and layout persistence |

Sits beside similar C++ external frameworks such as [[tkazer-cs2-external]], [[cs2-external-cheat]], and [[aimstar]]. Pair with [[cs2-offsets]] and [[cs2-dumper]] for layout refresh and [[world-to-screen]] for projection math.

## Links

- Repo: https://github.com/Fr0go1/Aeonix-Cs2

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[tkazer-cs2-external]] · [[cs2-external-cheat]] · [[cs2-external-1]] · [[aimstar]] · [[cs2-offsets]] · [[cs2-dumper]] · [[world-to-screen]]
