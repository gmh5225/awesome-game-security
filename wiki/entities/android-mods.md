---
title: Android Mods
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/PallabKumarS__android-mods.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: high
---

# Android Mods

**android-mods** (PallabKumarS/android-mods) is a suite of **systemless Magisk and KernelSU modules** combined with **LSPosed hook modules** for rooted Android phones on **HyperOS, MIUI, and custom AOSP-style ROMs**. It packages Play Integrity and Tricky Store workflows, enterprise compliance bypasses, and ROM tweaks researchers use when studying the same device-integrity signals many mobile games and anti-cheat stacks evaluate. (source: wiki/sources/descriptions/PallabKumarS__android-mods.md)

## Catalog lane

Cheat / Magisk — bundled attestation, root-hide, and hook stacks beside orchestration tools such as [[jerrymanager]] and catalogs such as [[magisk-hub]] and [[zamr]]. (source: wiki/sources/README-categories.md)

## Component families

| Area | Role |
|------|------|
| Play Integrity + Tricky Store | All-in-one module bundles; **Strong Keybox** Tricky Store variants; spoof **build properties** and **hardware keystore attestation** |
| Enterprise / MAM | **Intune and MAM compliance bypass** for Microsoft work apps via runtime **Java hooks** |
| ROM tweaks | Examples include AOD brightness stabilization and removal of the keyboard “chin” on AOSP-style builds |

## Delivery stack

Most hook and app logic is built with **Java and Gradle**. Module delivery uses **shell installers**, **Zygisk native injection**, and a small **Python** helper for packaging. (source: wiki/sources/descriptions/PallabKumarS__android-mods.md)

## Research framing

The collection groups scattered release threads into reproducible attestation and concealment stacks. Backend Play Integrity verdicts, game-specific checks, and enterprise policy enforcement remain independent—local module success does not establish universal bypass without server-side validation. Pair with [[mobile-trust-boundaries]] and [[mobile-anti-cheat]] when mapping platform vs server trust.

## Links

- Repo: https://github.com/PallabKumarS/android-mods

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk]] · [[kernelsu]] · [[zygisk]] · [[trickystore]] · [[magisk-hub]] · [[jerrymanager]] · [[mobile-anti-cheat]]
