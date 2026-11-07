---
title: VD-Backup
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/VD171__VD-Backup.md
updated: 2026-11-07
confidence: medium
---

# VD-Backup

**VD-Backup** (VD171/VD-Backup) is a rooted **Android Magisk module** that backs up and restores installed applications and their data through a **browser-based WebUI**, running on **KernelSU**, **APatch**, or **Magisk**. Implementation is mainly **POSIX shell scripts** with a vanilla JavaScript front end, optional Kotlin companion pieces, and a JSON-driven helper API for automation. (source: wiki/sources/descriptions/VD171__VD-Backup.md)

## Catalog lane

Cheat — KernelSU/APatch/Magisk WebUI module for full APK, app data, OBB, and incremental backup/restore as root, with Neo-Backup and Android-DataBackup import paths. (source: wiki/sources/descriptions/VD171__VD-Backup.md)

## Scope

Backups can include APK splits, private and external app data, **OBB**, permissions, **AppOps**, and optional **SSAID** when root allows. Supported formats include full **tar.zst** archives, encrypted **restic** snapshots, and **rclone** or **rsync** mirrors. Optional portable encryption, integrity checks, selective restore, scheduling, and import from Neo-Backup and Android-DataBackup support migration and offline copies of game installs and protected mobile app state on rooted devices. (source: wiki/sources/descriptions/VD171__VD-Backup.md)

## Audience

Researchers and power users who need reliable device migration and offline preservation of heavy game installs (APK + OBB + sandbox data) without relying on host-only `adb backup` or partial file explorers alone.

## Positioning

Complements [[app-manager]] and [[file-explorer]] interactive backup UIs with module-native scheduling, incremental backends, and cross-device restore. Pairs with [[magisk]] / [[kernelsu]] / [[apatch]] root stacks and sits in the same evidence-preservation lane as iOS acquisition tools such as [[copyapp]] and [[bagbak]] on the Android side.

## Links

- Repo: https://github.com/VD171/VD-Backup

## Related

[[overviews/mobile-security]] · [[magisk]] · [[kernelsu]] · [[apatch]] · [[app-manager]] · [[copyapp]]
