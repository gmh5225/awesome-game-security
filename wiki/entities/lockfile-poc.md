---
title: LockFile-Poc
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/rbmm__LockFile-Poc.md
updated: 2026-07-25
confidence: medium
---

# LockFile-Poc

C++ proof-of-concept focused on Windows **file locking** (`Lock File`). Aimed at anti-cheat engineers and defensive researchers in the Anti Cheat → Stress Testing lane, and also listed under Some Tricks → Windows Ring3. (source: wiki/sources/descriptions/rbmm__LockFile-Poc.md)

Useful when studying how exclusive/shared file locks interact with AC tooling, dumps, or host forensics—adjacent to same-author filesystem tooling such as [[usn]] / [[searchex]], and to process/file-protection stacks that include lock semantics such as [[vaultguard]].

## Links

- Repo: https://github.com/rbmm/LockFile-Poc

## Related

[[usn]] · [[searchex]] · [[vaultguard]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
