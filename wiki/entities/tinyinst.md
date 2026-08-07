---
title: TinyInst
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/googleprojectzero__TinyInst.md
updated: 2026-08-07
confidence: medium
---

# TinyInst

**TinyInst** is a Google Project Zero **lightweight dynamic binary instrumentation** library in the Cheat / DBI lane. Written in **C/C++**, it centers on **hooking and debugging** for instrumenting selected modules while leaving the rest of a process to run natively — a lighter alternative to full frameworks such as Pin or DynamoRIO. Aimed at game-security researchers and reverse engineers studying offensive DBI techniques. (source: wiki/sources/descriptions/googleprojectzero__TinyInst.md)

Sits beside full DBI frameworks ([[dynamic-binary-instrumentation]], [[frida]], [[cpp-veh-dbi]]) and coverage-guided fuzzing peers such as [[winafl]] in the Windows RE / instrumentation lane.

## Links

- Repo: https://github.com/googleprojectzero/TinyInst

## Related

[[dynamic-binary-instrumentation]] · [[frida]] · [[cpp-veh-dbi]] · [[winafl]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
