---
title: external-warzone-cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/NMan1__external-warzone-cheat.md
updated: 2026-08-22
confidence: medium
---

# external-warzone-cheat

**external-warzone-cheat** (NMan1/external-warzone-cheat) is an **external cheat framework** for **Call of Duty: Warzone** built around a **manually mapped kernel driver**. A separate C++ usermode client combines driver-assisted cross-process memory access with an **overlay hijacking** approach to render **ESP** and related on-screen features. The codebase ships as distinct Visual Studio projects for client and driver, plus game SDK and offset scaffolding for Warzone reverse-engineering and feature prototyping. Intended for game hacking and anti-cheat research on driver-assisted external tooling. (source: wiki/sources/descriptions/NMan1__external-warzone-cheat.md)

Sits in the COD Warzone external lane beside [[call-of-duty-warzone-mw-hack-esp-aimbot]] and [[call-of-duty-warzone-hack-esp-slient-aimbot-internal-unlock-all]], and complements NMan1's in-process [[warzone-internal]] sample with an out-of-process kernel-driver + overlay-hijack path.

## Architecture

| Component | Role |
|-----------|------|
| Kernel driver | Manually mapped driver for cross-process memory access |
| Usermode client | C++ cheat logic, entity reads, feature modules |
| Overlay hijack | External on-screen ESP / visual rendering without in-process hooks |
| Game SDK / offsets | Warzone structure and offset scaffolding for RE iteration |

See [[world-to-screen]] for ESP projection and [[mwclap]] for COD overlay-hijack patterns in the same title lane.

## Links

- Repo: https://github.com/NMan1/external-warzone-cheat

## Related

[[warzone-internal]] · [[warzone-internal-cheat]] · [[modern-warfare-warzone-cheat]] · [[call-of-duty-warzone-mw-hack-esp-aimbot]] · [[mwclap]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
