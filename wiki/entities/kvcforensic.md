---
title: KvcForensic
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/wesmar__KvcForensic.md
updated: 2026-07-18
confidence: medium
---

# KvcForensic

Cross-platform LSASS credential forensics tool: extracts Windows authentication secrets (MSV, WDigest, Kerberos, CredMan, DPAPI keys) from live memory or `lsass.dmp` minidumps via signature scanning and BCrypt decryption (AES-CFB128, 3DES-CBC). Pure Win32 (no DbgHelp); runs on Windows and Linux; targets Win11 24H2/25H2/26H1 and Server 2025. (source: wiki/sources/descriptions/wesmar__KvcForensic.md)

Companion to same-author [[kvc]] (PP/PPL → LSASS dump path): here the focus is post-dump / live LSA secret recovery rather than DSE bypass.

## Links

- Repo: https://github.com/wesmar/KvcForensic

## Related

[[kvc]] · [[lsass-extend-mapper]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
