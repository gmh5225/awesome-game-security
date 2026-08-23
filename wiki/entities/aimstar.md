---
title: AimStar
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/M3351AN__AimStar.md
updated: 2026-08-23
confidence: medium
---

# AimStar

**External Counter-Strike 2 cheat framework** from **M3351AN**, implemented in **C++**. It bundles bone-based aimbot logic, entity tracking, ESP rendering, triggerbot, offset management, and a menu configuration system, with multi-language documentation in English, Russian, and Chinese. Primary research value: studying **external cheat architecture** and **CS2 memory reading techniques** for game security researchers. README **External** tag. (source: wiki/sources/descriptions/M3351AN__AimStar.md)

Sits in the usermode external CS2 lane beside [[tkazer-cs2-external]], [[cs2-external-cheat]], and [[cs2external]], and beside same-author samples such as [[samidare]], [[ukia-rpm]], and [[echinoidea]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Offset management | Game structure / field bootstrap and maintenance for CS2 builds |
| Entity tracking | Player and world entity enumeration for aim and visualization |
| Bone-based aimbot | Skeleton-aware target selection and aim assistance |
| ESP rendering | External on-screen entity visualization |
| Triggerbot | Input-assisted fire on crosshair overlap |
| Menu / config | Runtime feature toggles and persisted settings |

## Links

- Repo: https://github.com/M3351AN/AimStar (README: External)

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[samidare]] · [[ukia-rpm]] · [[echinoidea]] · [[tkazer-cs2-external]] · [[cs2-external-cheat]] · [[cs2external]] · [[cs2-dumper]] · [[world-to-screen]]
