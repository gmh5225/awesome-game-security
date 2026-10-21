---
title: SUSFS LKM Loader
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/linflame__SusfsLkmLoader.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: medium
---

# SUSFS LKM Loader

**Magisk-, KernelSU-, and APatch-compatible root module** that automatically loads the **SUSFS** guard kernel module at boot for filesystem and module hiding on rooted Android hosts. (source: wiki/sources/descriptions/linflame__SusfsLkmLoader.md)

Ships prebuilt kernel objects matched to many Android/Linux kernel version pairs at install time, uses a bundled `insmod` helper to expose SUSFS proc control nodes, and offers a next track (Action buttons, WebUI, daily upstream sync from susfs4ksu-lkm) plus a legacy minimal-install track. Shell and PowerShell packaging scripts assemble module zips, metadata, and changelogs for nightly distribution.

Targets mobile security researchers and rooted users who need SUSFS-based concealment when studying **Play Integrity**, banking apps, or **mobile anti-cheat** integrity probes—not a bypass guarantee. (source: wiki/sources/descriptions/linflame__SusfsLkmLoader.md)

Listed in the README under **Cheat → Magisk** beside other root-hide and integrity tooling.

## Links

- Repo: https://github.com/linflame/SusfsLkmLoader

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk-hub]] · [[jerrymanager]] · [[zygisk]] · [[mobile-anti-cheat]]
