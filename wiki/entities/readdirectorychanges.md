---
title: ReadDirectoryChanges
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/jimbeveridge__readdirectorychanges.md
updated: 2026-08-03
confidence: medium
---

# ReadDirectoryChanges

C++ wrapper around the Windows `ReadDirectoryChangesW` API for real-time filesystem monitoring. Provides a clean interface for watching directory trees and receiving notifications on file create, modify, delete, and rename events. Handles asynchronous I/O, buffer management, and recursive directory monitoring—aimed at Windows developers building file watchers, sync tools, or security monitoring applications. (source: wiki/sources/descriptions/jimbeveridge__readdirectorychanges.md)

Complements kernel/minifilter telemetry tools such as [[openprocmon]] and ETW-based monitors such as [[fibratus]] with a lightweight user-mode directory-watch building block for AC integrity or sync research.

## Links

- Repo: https://github.com/jimbeveridge/readdirectorychanges

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[openprocmon]] · [[fibratus]] · [[usn]]
