---
title: BaiZe
kind: entity
topics: [mobile-security]
sources:
  - wiki/sources/descriptions/xgl34222220-ops__BaiZe.md
updated: 2026-08-16
confidence: medium
---

# BaiZe

Rooted Android **storage cleanup** system shipped as a **Magisk**, **KernelSU**, or **APatch** module with a companion app. Kotlin and C implementation: shell module scripts plus a libsu `RootService` drive a native scanning engine against thousands of curated deep-clean rules. Capabilities include app-cache and uninstall-residue cleanup, APK retention scanning, file organization, scheduled tasks with thermal and idle constraints, and quarantine with audit history. Safety is central—four-tier risk classification, path whitelists, scan-before-delete snapshots, symlink-safe deletion, and hard limits that keep high-risk targets scan-only during automated runs. Targets rooted Android users and security-minded operators who need accurate, policy-controlled cleanup without risking downloads, databases, or other protected user data. (source: wiki/sources/descriptions/xgl34222220-ops__BaiZe.md)

## Links

- Repo: https://github.com/xgl34222220-ops/BaiZe

## Related

[[overviews/mobile-security]] · [[magisk]] · [[kernelsu]] · [[rescuex]] · [[xfiles]]
