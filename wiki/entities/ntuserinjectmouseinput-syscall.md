---
title: NtUserInjectMouseInput-syscall
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__NtUserInjectMouseInput-syscall.md
updated: 2026-08-11
confidence: medium
---

# NtUserInjectMouseInput-syscall

Reference documentation for the **NtUserInjectMouseInput** syscall path: injecting mouse input from user mode through **win32k** rather than higher-level APIs such as `SendInput`. The README frames the repo as preserved reference material rather than an original research write-up. (source: wiki/sources/descriptions/gmh5225__NtUserInjectMouseInput-syscall.md)

Mainly useful for game security researchers studying **input injection**, **triggerbot/aimbot** execution primitives, and related **detection surfaces**—how aim logic reaches the input stack and what telemetry AC can observe on win32k syscall paths. Complements MouClass kernel-driver research such as [[kernel-mouse]] and user-mode alternatives catalogued under [[hardware-input-injection]]; win32k binary corpora such as [[win32k-file-collection]] help diff syscall internals across builds.

## Links

- Repo: https://github.com/gmh5225/NtUserInjectMouseInput-syscall

## Related

[[kernel-mouse]] · [[hardware-input-injection]] · [[win32k-file-collection]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
