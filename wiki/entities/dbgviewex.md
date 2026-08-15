---
title: DbgViewEx
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/emlinhax__DbgViewEx.md
updated: 2026-08-15
confidence: medium
---

# DbgViewEx

Windows tool for logging **ETW events** and **system debug output** in one place — aimed at game-security researchers and reverse engineers studying offensive cheat / RE tooling behavior. The project is in very early development and updated intermittently. (source: wiki/sources/descriptions/emlinhax__DbgViewEx.md)

Complements schema-oriented ETW browsers such as [[etw-explorer]] and cross-build manifest diff tools such as [[etw-watcher]] by focusing on live event and kernel/user debug-string capture rather than provider metadata alone. Useful when correlating cheat-driver IOCTL traces, syscall hooks, or AC telemetry with `DbgPrint`/`OutputDebugString` streams during Windows kernel exploration.

## Links

- Repo: https://github.com/emlinhax/DbgViewEx

## Related

[[etw-explorer]] · [[etw-watcher]] · [[fibratus]] · [[openprocmon]] · [[blitz]] · [[tableflipper]] · [[xv]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[etw-threat-intelligence]]
