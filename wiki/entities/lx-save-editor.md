---
title: LX Save Editor
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Null993__LX-SaveEditor.md
updated: 2026-11-21
confidence: medium
---

# LX Save Editor

Standalone Android application (Java root-privileged APK, with Python build/catalog/test utilities) for reading and modifying offline role save data for package `local.lx.offline.game`. Validates saves via JSON schema and format rules rather than pinning a single game version.

Edits currency, growth, inventory, equipment enhancement stars, cultivation systems, and related progress files while preserving unknown fields and server-compatible structure. Save and restore stop the game process, verify hashes, maintain SHA-256 backup manifests, and use transactional file replacement with rollback plus ZIP-based backup import/export.

Targets modders, rooted players, and researchers studying client-side save formats and integrity boundaries outside the official client. Complements [[lx-save-manager]] multi-slot library workflows with direct in-place field editing. (source: wiki/sources/descriptions/Null993__LX-SaveEditor.md)

## Links

- Repo: https://github.com/Null993/LX-SaveEditor

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[lx-save-manager]]