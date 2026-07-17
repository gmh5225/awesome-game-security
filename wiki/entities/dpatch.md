---
title: dpatch
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/xmmword__dpatch.md
updated: 2026-07-17
confidence: medium
---

# dpatch

Syscall Dispatcher Patching PoC: makes a mutable copy of the system call table, overwrites table pointers with hook functions, then patches the first bytes of the dispatcher to jump to a custom syscall handler. (source: wiki/sources/descriptions/xmmword__dpatch.md)

Useful for game-security researchers studying offensive Android/kernel syscall-hook techniques in the cheat / Android kernel explorer lane (alongside DIY explorers such as [[op7t]]).

## Links

- Repo: https://github.com/xmmword/dpatch

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[op7t]]
