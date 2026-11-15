---
title: RootAtlas (android-root-feed-bridge)
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/stupidgiraffe__android-root-feed-bridge.md
updated: 2026-11-15
confidence: medium
---

# RootAtlas (android-root-feed-bridge)

**RootAtlas** is a serverless **federated index** that merges Android root module catalogs into unified feeds consumable by **MMRL** and **KernelSU Next**. Python tooling discovers and validates upstream MMRL JSON, KernelSU manifests, curated federation sources, and GitHub repositories, then merges, deduplicates, and caches metadata while **preserving upstream download links** instead of rehosting flashable ZIPs. Daily **GitHub Actions** refresh discovery, run contract validation, inspect many module archives for `module.prop` structure, and publish generated JSON plus live coverage and provenance reports. (source: wiki/sources/descriptions/stupidgiraffe__android-root-feed-bridge.md)

Targets rooted-device researchers, module maintainers, and power users who want one maintained bridge to browse **Magisk**, **KernelSU**, **Zygisk**, and related root tooling without wiring dozens of separate repo manifests by hand. Listed under **Cheat → Magisk** alongside curated catalogs such as [[zamr]] and index hubs such as [[magisk-hub]].

## Links

- Repo: https://github.com/stupidgiraffe/android-root-feed-bridge (README tag: RootAtlas federated MMRL / KernelSU Next index)

## Related

[[zamr]] · [[magisk-hub]] · [[fox-magisk-module-manager]] · [[magisk]] · [[kernelsu]] · [[zygisk]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]