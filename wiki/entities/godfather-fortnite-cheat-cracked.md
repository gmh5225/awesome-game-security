---
title: GodFather-Fortnite-Cheat-Cracked
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/CheaterRehab__GodFather-Fortnite-Cheat-Cracked.md
updated: 2026-08-28
confidence: medium
---

# GodFather-Fortnite-Cheat-Cracked

**GodFather-Fortnite-Cheat-Cracked** (CheaterRehab/GodFather-Fortnite-Cheat-Cracked) is a **leaked and modified external Fortnite cheat codebase** spanning user-mode and kernel-mode components. The user-mode side is C++ with a **DirectX 9 Dear ImGui overlay**; the kernel side includes **driver logic and callback-based communication** for KM↔UM I/O. Accompanying notes cover **detection status**, **loader behavior**, and **mapping techniques** used to deploy the driver. Useful for game-security researchers studying pasted-cheat infrastructure, hybrid external cheat architecture, anti-cheat bypass patterns, and real-world driver deployment on EAC-protected UE clients. (source: wiki/sources/descriptions/CheaterRehab__GodFather-Fortnite-Cheat-Cracked.md)

Sits in the hybrid UM+KM Fortnite external lane beside [[subzero-fortnite-cheat]], [[interic-fortnite-external-cheat]], and [[fortnite-external-cheat-leak]] as a leaked reference for overlay rendering plus kernel-assisted memory access and loader/mapper workflows.

## Architecture

| Layer | Role |
|-------|------|
| User-mode | C++ client; DirectX 9 Dear ImGui overlay |
| Kernel-mode | Driver logic; callback-based KM↔UM communication |
| Loader / deploy | Notes on mapping techniques and loader behavior |
| Research notes | Detection-status commentary for AC bypass study |

## Links

- Repo: https://github.com/CheaterRehab/GodFather-Fortnite-Cheat-Cracked

## Related

[[subzero-fortnite-cheat]] · [[interic-fortnite-external-cheat]] · [[fortnite-external-cheat-leak]] · [[flirtnite]] · [[easy-anti-cheat]] · [[kernel-callbacks]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
