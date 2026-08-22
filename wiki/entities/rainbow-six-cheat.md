---
title: rainbow-six-cheat
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/NMan1__Rainbow-Six-Cheat.md
updated: 2026-08-22
confidence: medium
---

# rainbow-six-cheat

**rainbow-six-cheat** (NMan1/Rainbow-Six-Cheat) is a **full-source Windows cheat framework** for **Rainbow Six Siege** built around a **kernel driver**, an **external menu**, and **shared-memory communication**. Implemented mainly in **C and C++**, it includes loader logic, rendering components, and gameplay manipulation modules. Documented capabilities cover **ESP** and **chams** visuals, **silent-aim**, recoil and spread controls, unlock and movement modifications, and configurable settings. Intended for game hacking research and analysis of kernel-assisted cheat designs from an anti-cheat perspective under [[battleye]]. (source: wiki/sources/descriptions/NMan1__Rainbow-Six-Cheat.md)

Sits in the R6 kernel-assisted external lane beside [[external-r6s-cheat]], [[r6s-external-v2]], and the v2 successor [[overflow-r6-v2]], and complements NMan1's [[apex-legends-cheat]] and [[external-warzone-cheat]] samples with a shared-memory KM↔UM driver + external-menu path for the BattlEye-protected Siege client.

## Architecture

| Component | Role |
|-----------|------|
| Kernel driver | Cross-process memory and kernel-assisted cheat pipeline |
| External menu | Out-of-process UI and configuration surface |
| Shared memory | KM↔UM communication channel between driver and client |
| Loader | User-mode bring-up and driver loading logic |
| Feature modules | ESP/chams, silent-aim, recoil/spread, unlock/movement mods |

See [[world-to-screen]] for ESP projection and [[battleye]] for the protected-title context.

## Links

- Repo: https://github.com/NMan1/Rainbow-Six-Cheat

## Related

[[external-r6s-cheat]] · [[r6s-external-v2]] · [[overflow-r6-v2]] · [[rainbow-six-siege-rs6-external-esp-aimbot-hack-cheat]] · [[apex-legends-cheat]] · [[external-warzone-cheat]] · [[warzone-internal]] · [[battleye]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
