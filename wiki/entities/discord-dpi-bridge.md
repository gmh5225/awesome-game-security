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

**User-space Discord connectivity setup** (egeorcun) that routes Discord through ISP DPI blocks without loading kernel packet-interception drivers such as **WinDivert**, which **Easy Anti-Cheat** and **Denuvo Anti-Cheat** commonly reject. Catalogued under **Some Tricks > Windows Ring3**. (source: wiki/sources/descriptions/egeorcun__discord-dpi-bridge.md)

## Components

Stack combines four layers so both Discord's chat client and updater can connect:

| Layer | Role |
|-------|------|
| **ByeDPI** | User-space SOCKS5 proxy for DPI desync / bypass |
| **PowerShell TCP→SOCKS5 relay** | Bridges Discord's updater traffic into the SOCKS5 path |
| **DNS over HTTPS (DoH)** | Bypasses ISP DNS hijacking |
| **Hosts + Chromium proxy flags** | Routes Discord client and updater endpoints through the proxy stack |

Ships as PowerShell **install**, **status**, **fix**, and **uninstall** scripts with JSON configuration. Requires only built-in Windows PowerShell — no Python or other runtime dependencies. (source: wiki/sources/descriptions/egeorcun__discord-dpi-bridge.md)

## Use case

Targets gamers in regions where Discord is blocked who need Discord and anti-cheat-protected titles such as **ARC Raiders** to run concurrently. Traditional **GoodbyeDPI**-style kernel bypass tools load WinDivert-class drivers that prevent those games from launching; this setup stays entirely in Ring3. (source: wiki/sources/descriptions/egeorcun__discord-dpi-bridge.md)

## Research relevance

Illustrates the **AC–utility tradeoff** for WFP/NDIS kernel drivers vs pure user-mode proxy stacks; complements [[divert]] (WinDivert) and [[gecit]] (cross-platform DPI bypass) in network-path research.

## Links

- Repo: https://github.com/egeorcun/discord-dpi-bridge

## Related

[[divert]] · [[gecit]] · [[easy-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
