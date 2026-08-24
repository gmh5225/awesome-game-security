---
title: Butler
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/d4rken-org__butler.md
updated: 2026-08-24
confidence: medium
---

# Butler

Open-source Android file explorer and app manager (Kotlin, Jetpack Compose, Hilt, Room) combining multi-pane browsing, archive handling, trash recovery, a built-in text editor, and regex search. The installed-apps workspace exposes APK metadata, component details, running-process queries, and APK export. Escalates access through root, Shizuku, ADB, and shell backends to reach protected paths such as `Android/data` and to run package and file operations normal storage APIs cannot perform. Targets Android security researchers, reverse engineers, and game security analysts inspecting app data, manipulating game files, and auditing installed applications on rooted or debuggable devices. (source: wiki/sources/descriptions/d4rken-org__butler.md)

Listed in the README under **Cheat → Android File Explorer**.

## Links

- Repo: https://github.com/d4rken-org/butler

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[file-explorer]] · [[raival-file-explorer]] · [[app-manager]] · [[xfiles]] · [[adb-file-manager]] · [[apktool]] · [[jadx]]
