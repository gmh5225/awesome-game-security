---
title: Orbis Web Manager
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/kromossomom-debug__orbis-web-manager.md
  - wiki/sources/README-categories.md
updated: 2026-11-16
confidence: medium
---

# Orbis Web Manager

**Browser-based command center** for managing a **jailbroken PlayStation 4** running **GoldHEN** over the local network. The Windows PC side is a lightweight **C#** host using **`HttpListener`** with a responsive HTML, CSS, and JavaScript UI—**no Node.js** or other external runtime on the desktop. (source: wiki/sources/descriptions/kromossomom-debug__orbis-web-manager.md)

**Capabilities** include a live dashboard and port checks; game-library views backed by **`app.db`**; **FTP** file browsing with drag-and-drop uploads; **GoldHEN** cheat JSON viewing and regional **Title ID** (CUSA) conversion; **PKG** listing and remote installation; on-screen notifications; and **BinLoader** payload injection on ports **9090** and **12800**. Targets the PS4 homebrew/modding community who want **Prospero Manager**–style remote console administration without relying on USB drives for everyday file and cheat workflows.

README lists it under **PlayStation** (projected category map).

## Links

- Repo: https://github.com/kromossomom-debug/orbis-web-manager

## Related

[[remote-package-installer-ng]] · [[psfree-enhanced]] · [[cheatrunner-patches]] · [[reaperpy]] · [[slopstation]] · [[ghidra-orbis]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]