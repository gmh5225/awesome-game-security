---
title: Discord DPI Bridge
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/egeorcun__discord-dpi-bridge.md
  - wiki/sources/README-categories.md
updated: 2026-09-08
confidence: medium
---

# Discord DPI Bridge

**User-space Discord connectivity setup** (egeorcun) that routes Discord through ISP DPI blocks using **ByeDPI** as a SOCKS5 proxy, a PowerShell TCP-to-SOCKS5 relay for Discord's updater, **DNS over HTTPS**, and hosts/Chromium proxy flags — without loading kernel packet-interception drivers such as **WinDivert** that **Easy Anti-Cheat** and **Denuvo Anti-Cheat** commonly reject. Catalogued under **Some Tricks > Windows Ring3**. (source: wiki/sources/descriptions/egeorcun__discord-dpi-bridge.md)

## Mechanism

PowerShell install/status/fix/uninstall scripts with JSON configuration; requires only built-in Windows PowerShell (no Python runtime). Targets gamers in regions where Discord is blocked who need Discord and anti-cheat-protected titles such as ARC Raiders to run concurrently — when GoodbyeDPI-style kernel bypass tools would prevent the game from launching.

## Research relevance

Illustrates the **AC–utility tradeoff** for WFP/NDIS kernel drivers vs pure user-mode proxy stacks; complements [[divert]] (WinDivert) and [[gecit]] (cross-platform DPI bypass) in network-path research.

## Links

- Repo: https://github.com/egeorcun/discord-dpi-bridge

## Related

[[divert]] · [[gecit]] · [[easy-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
