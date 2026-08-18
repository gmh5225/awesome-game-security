---
title: Magisk
kind: entity
topics: [mobile-security, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/descriptions/topjohnwu__Magisk.md
  - wiki/sources/descriptions/ri-char__zygisk-dump-dex.md
  - wiki/sources/descriptions/jiayuxuan123__RescueX.md
  - wiki/sources/descriptions/gmh5225__MagiskOnWSALocal.md
  - wiki/sources/descriptions/gmh5225__MagiskHide.md
  - wiki/sources/descriptions/xgl34222220-ops__BaiZe.md
  - wiki/sources/descriptions/anasfanani__Magisk-Tailscaled.md
updated: 2026-08-18
confidence: medium
---

# Magisk

Widely used Android root solution and **systemless** modification framework. Provides root via a `su` daemon, module-based changes without altering the system partition, **DenyList / Shamiko** root-hide (successor to MagiskHide), Zygisk module loading, and an app for modules / superuser grants. Operates at user/init level with medium stealth vs kernel roots ([[kernelsu]], APatch). Canonical Cheat Magisk / Android-root reference for mobile security and anti-cheat research on root frameworks, systemless mods, and root-hide tradeoffs. (source: wiki/sources/descriptions/topjohnwu__Magisk.md) (source: wiki/sources/skills/mobile-security.md)

Adjacent tooling: kernel-level root peers [[kernelsu]] and APatch (KernelPatch boot.img; stock GKI); boot-image tools [[magiskboot]] and [[magiskboot-ndk-on-linux]]; Magisk modules such as [[move-certificate]], Pixel-prop disguise [[easypixel]] (source: wiki/sources/descriptions/the-dise__EasyPixel.md), boot-loop recovery [[rescuex]] (source: wiki/sources/descriptions/jiayuxuan123__RescueX.md), graded storage cleanup [[baize]] (source: wiki/sources/descriptions/xgl34222220-ops__BaiZe.md), Tailscale daemon [[magisk-tailscaled]] (source: wiki/sources/descriptions/anasfanani__Magisk-Tailscaled.md), and Zygisk DEX dump [[zygisk-dump-dex]] (`libdexfile.so` hook; Android 14/15) (source: wiki/sources/descriptions/ri-char__zygisk-dump-dex.md); portable ptrace MagiskHide successor [[magiskhide]] (DenyList hidelist without Zygisk; Android 11+) (source: wiki/sources/descriptions/gmh5225__MagiskHide.md); [[zygisk]] injection lifecycle; install paths such as [[cheese]]; WSA local Magisk+GApps integration via [[magiskonwsalocal]] (source: wiki/sources/descriptions/gmh5225__MagiskOnWSALocal.md); detection samples such as [[magiskdetector]].

## Links

- Repo: https://github.com/topjohnwu/Magisk

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[kernelsu]] · [[rescuex]] · [[baize]] · [[magisk-tailscaled]] · [[zygisk]] · [[mobile-anti-cheat]] · [[magiskdetector]] · [[magiskboot]] · [[magiskboot-ndk-on-linux]] · [[move-certificate]] · [[easypixel]] · [[zygisk-dump-dex]] · [[cheese]] · [[magiskhide]] · [[magiskonwsalocal]] · [[keyattestation]] · [[frida]]
