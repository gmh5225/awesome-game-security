---
title: hide-file
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/sina85__hide-file.md
updated: 2026-07-22
confidence: medium
---

# hide-file

C kernel/driver sample focused on file hiding for offensive cheat / hide research—useful when studying how Ring0 components conceal files from usermode enumeration and how that surface relates to anti-cheat Detection:Hide. (source: wiki/sources/descriptions/sina85__hide-file.md)

Contrasts with defensive FSFilter minifilter file-protection tools such as [[vaultguard]] (hide/lock/RO/block-exec) on the same kernel file-visibility surface.

## Links

- Repo: https://github.com/sina85/hide-file

## Related

[[vaultguard]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
