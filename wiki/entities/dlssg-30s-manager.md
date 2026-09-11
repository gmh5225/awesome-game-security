---
title: DLSSG 30s Manager
kind: entity
topics: [graphics-api, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/BUNNY-19C__DLSSG-30s-manager.md
updated: 2026-09-11
confidence: medium
---

# DLSSG 30s Manager

**Windows desktop deploy manager** (BUNNY-19C) for the **dlssg_for_sm86** DLL proxy mod that enables **DLSS frame generation** on **RTX 30-series (SM86 / Ampere)** GPUs in titles shipping `nvngx_dlssg.dll`. Built with **C# and WPF on .NET 8**; scans Steam libraries and custom folders; supports per-game INI configuration, one-click deploy/restore, and on-demand mod downloads verified by **Authenticode** signatures and **SHA-256** hashes. Catalogued under **DirectX Compatibility**. (source: wiki/sources/descriptions/BUNNY-19C__DLSSG-30s-manager.md)

## Anti-cheat interaction

Implements **kernel anti-cheat detection** through filename and directory fingerprinting for **Easy Anti-Cheat**, **BattlEye**, **Riot Vanguard**, **Tencent ACE**, **NetEase NEAC**, **HoYoKProtect**, and similar systems—blocking deployment to protected titles and identifying **quarantined proxy DLLs** left after anti-cheat interception. Safe file handling uses digital-signature ownership checks, hash verification on restore, and backups of displaced non-mod files.

## Audience

Targets PC gamers enabling DLSS frame generation on Ampere hardware and **game security researchers** studying how kernel anti-cheat detects and quarantines DLL proxy injection.

## Links

- Repo: https://github.com/BUNNY-19C/DLSSG-30s-manager

## Related

[[dlss-unlocked]] · [[dxwrapper]] · [[ghost-recon-wildlands-first-person-no-eac]] · [[easy-anti-cheat]] · [[battleye]] · [[vanguard]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
