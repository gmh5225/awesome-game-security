---
title: ida-settings
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/williballenthin__ida-settings.md
updated: 2026-08-30
confidence: medium
---

# ida-settings

Python library and companion **IDA Pro** plugin for reading and managing configuration values used by **IDAPython** plugins through Hex-Rays' shared settings infrastructure. Plugin authors declare typed settings in `ida-plugin.json` and fetch them at runtime with a simple API that integrates with **hcli** and **ida-config.json**; a Qt-based **Plugin Settings Manager** offers a dockable GUI to browse, edit, validate, and revert options across installed plugins. The repository also ships a legacy **IDASettings** module that provides scoped, dictionary-like configuration at system, user, directory, or IDB levels with import and export support. Built in Python with PyQt5 or PySide6 for **IDA Pro 9.0+**, aimed at reverse engineers and plugin developers who need centralized, validated settings for analysis workflows such as game binary research and anti-cheat investigation. (source: wiki/sources/descriptions/williballenthin__ida-settings.md)

Infrastructure helper—not decompilation, signature scanning, or analysis automation. Complements plugin discovery via [[list-of-ida-plugins]], workflow shortcuts via [[lazyida]], and plugin-development tooling such as [[ida-claude-code-plugins]].

## Links

- Repo: https://github.com/williballenthin/ida-settings

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[list-of-ida-plugins]] · [[lazyida]] · [[ida-claude-code-plugins]] · [[idacomments]] · [[ida-taskr]]
