---
title: LaZagne
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AlessandroZ__LaZagne.md
updated: 2026-09-02
confidence: medium
---

# LaZagne

**LaZagne** (AlessandroZ) is an open-source **credential recovery framework** written primarily in **Python**. It extracts locally stored passwords from many applications through **modular collectors** targeting different software families and storage mechanisms. The tool runs on **multiple platforms** and is commonly used in **post-exploitation**, security **auditing**, and **forensic** workflows when assessing credential exposure on compromised or test systems. (source: wiki/sources/descriptions/AlessandroZ__LaZagne.md)

Compared with Windows-focused static-binary harvesters such as [[pillager]] or browser-only decrypt utilities such as [[browser-password-exportor]], LaZagne emphasizes **breadth across application categories** (browsers, mail clients, databases, chat apps, and more) rather than a single host snapshot or browser profile lane.

## Links

- Repo: https://github.com/AlessandroZ/LaZagne

## Related

[[pillager]] · [[browser-password-exportor]] · [[kvcforensic]] · [[custom-dpapi]] · [[dfirtriage]] · [[qvoid-token-grabber]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
