---
title: LX Save Manager
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Null993__LX-SaveManager.md
updated: 2026-11-21
confidence: medium
---

# LX Save Manager

Standalone Android application (Java, with Python build/test/release scripts) for backing up, restoring, and managing offline game progress files under the Unity title package `local.lx.offline.game` private data directory. Requires root and integrates with common root managers.

Users can inspect live character stats, maintain a labeled multi-slot save library, start fresh characters after automatic backups, and import or export saves as ZIP archives—imports never overwrite the active in-game slot. Backups record full file manifests, schema checks, and SHA-256 hashes; restore uses transactional file replacement with rollback when writes fail.

Aimed at players and researchers who need controlled, root-level access to local save data rather than modifying the game binary or anti-cheat systems. (source: wiki/sources/descriptions/Null993__LX-SaveManager.md)

## Links

- Repo: https://github.com/Null993/LX-SaveManager

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]]