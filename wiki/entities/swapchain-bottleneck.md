---
title: swapchain-bottleneck
kind: entity
topics: [graphics-api, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/dantebuilds__swapchain-bottleneck.md
updated: 2026-08-16
confidence: medium
---

# swapchain-bottleneck

Architecture analysis document arguing that many PC gaming symptoms—stuttering, overlay crashes, TDR resets, and BSODs—share a root cause: Windows lacks an officially supported channel for overlays to draw alongside a game's DXGI swapchain. Traces how Steam, Discord, monitoring tools, and similar software resort to DLL injection and `Present` API hooking, colliding with the game, each other, and the driver outside DWM coordination. Covers cascades from overlay race conditions to kernel bugchecks (against Microsoft documentation), plus DXGI, WDDM, HAGS, Multiplane Overlays (MPO), and anti-cheat whitelist friction with legitimate injectors. Proposes directions such as parallel swapchains and an official overlay API for isolated, coordinated secondary presenters. (source: wiki/sources/descriptions/dantebuilds__swapchain-bottleneck.md)

## Links

- Repo: https://github.com/dantebuilds/swapchain-bottleneck

## Related

[[present-hook]] · [[winbo]] · [[steam-overlay-x64]] · [[discord-overlay-hook]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
