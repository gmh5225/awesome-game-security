---
title: intraceptor
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/crvvdev__intraceptor.md
updated: 2026-08-16
confidence: medium
---

# intraceptor

**Intraceptor** (crvvdev) intercepts **Windows NT API calls** and redirects them to a **kernel driver**, bypassing **process and thread handle protections** that anti-cheat systems enforce via object callbacks and stripped usermode handles. The project is C/C++-centric and combines kernel driver development with usermode hooking for the access / RPM research lane. (source: wiki/sources/descriptions/crvvdev__intraceptor.md)

Listed under cheat / access for game-security researchers and reverse engineers studying offensive handle-bypass and cross-process memory access paths opposite AC handle stripping.

Contrasts with pure usermode elevation such as [[libelevate]] and kernel-side handle maintenance such as [[battleye-handler-bypass]]. Same author’s [[vac-bypass-kernel]] targets VAC external scanner memory reads rather than NT-call redirection for handle access.

## Links

- Repo: https://github.com/crvvdev/intraceptor

## Related

[[libelevate]] · [[battleye-handler-bypass]] · [[vac-bypass-kernel]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
