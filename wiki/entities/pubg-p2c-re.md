---
title: pubg-p2c-re
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/experienceds__pubg-p2c-re.md
updated: 2026-08-15
confidence: medium
---

# pubg-p2c-re

Reverse-engineering report on a commercial **pay-to-cheat (P2C)** loader for PlayerUnknown's Battlegrounds (experienceds). Documents a **VMProtect**-packed loader that uses **Microsoft Edge WebView2** for licensing UI, **libcurl** over HTTPS to fetch an encrypted payload, and injects an **ESP renderer into `dwm.exe`** instead of `TslGame.exe` to avoid [[battleye]] process scans. Covers DWM injection mechanics, **Direct2D** overlay rendering, decoy stub executables, payload PE structure, and network protocol, plus how Krafton's **Zakynthos** anti-cheat identifies DWM vtable and code hooks. Includes architecture diagrams, detection templates, and an anti-cheat comparison matrix for game security researchers studying cheat evasion against BattlEye and kernel-level anti-cheat systems. (source: wiki/sources/descriptions/experienceds__pubg-p2c-re.md)

Sits beside runnable PUBG offensive samples such as [[pubg-external-cheat]], [[pubg-dx]], and [[pubg-internal]], DWM overlay research such as [[dwm-dwmdraw]] and [[dwmhook]], and VMProtect study surfaces such as [[vmprotect]].

## Links

- Repo: https://github.com/experienceds/pubg-p2c-re

## Related

[[battleye]] · [[pubg-external-cheat]] · [[pubg-dx]] · [[pubg-internal]] · [[pubg-lite-esp]] · [[dwm-dwmdraw]] · [[dwmhook]] · [[dwm-hook]] · [[vmprotect]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
