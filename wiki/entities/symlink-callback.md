---
title: SymlinkCallback
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/yardenshafir__SymlinkCallback.md
updated: 2026-07-17
confidence: medium
---

# SymlinkCallback

Windows kernel research that modifies a symlink object and replaces the `LinkTarget` string with a callback invoked whenever the symlink is accessed—useful for anti-cheat / Ring0 callback defensive research. (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md)

## Links

- Repo: https://github.com/yardenshafir/SymlinkCallback

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
