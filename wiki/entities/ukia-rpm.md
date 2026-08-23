---
title: UkiaRPM
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/M3351AN__UkiaRPM.md
updated: 2026-08-23
confidence: medium
---

# UkiaRPM

**External Counter-Strike 2 cheat** from **M3351AN** that reads game state through **kernel driver–assisted remote process memory (RPM)** from a separate usermode process. Implemented in **C++**, it bundles aimbot, ESP, radar, recoil control, config persistence, and miscellaneous gameplay modifications behind an **ImGui DirectX 9** menu and visual overlay. Primary research value: studying **RPM-based external cheat architecture** and **kernel driver ↔ usermode communication** for protected-process game memory access. README **External** tag. (source: wiki/sources/descriptions/M3351AN__UkiaRPM.md)

Sits in the kernel-assisted CS2 external lane beside [[cs2-ext]], [[valthrun]], and [[tkazer-cs2-external]], and beside same-author kernel PoCs such as [[usugumo]], [[shirakumo]], and [[zhangbing-injector]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Kernel driver RPM | Cross-process memory reads/writes bypassing usermode handle restrictions |
| Feature modules | Aimbot, ESP, radar, recoil control, misc mods |
| DirectX 9 + ImGui | External menu and on-screen overlay rendering |
| Config system | Saved settings persistence |

## Links

- Repo: https://github.com/M3351AN/UkiaRPM (README: External)

## Related

[[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[usugumo]] · [[shirakumo]] · [[cs2-ext]] · [[tkazer-cs2-external]] · [[cs2-external-cheat]] · [[driver-physical-rw]] · [[norsefire]] · [[km-um-communication]] · [[world-to-screen]]
