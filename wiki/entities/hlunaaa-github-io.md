---
title: hLunaaa.github.io
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/hLunaaa__hLunaaa.github.io.md
updated: 2026-08-06
confidence: medium
---

# hLunaaa.github.io

Research blog and **Driver Trace Cleaner** material focused on kernel driver development, asset pipelines, and offensive hide techniques for game-security researchers and reverse engineers. Covers clearing or evading kernel load and pool artifacts that anti-cheat and EDR stack on top of manual-map / BYOVD driver paths. (source: wiki/sources/descriptions/hLunaaa__hLunaaa.github.io.md)

## Notable write-ups

- **Exploring CI.dll and Bigpool Cache** — studies **CI.dll** validation surfaces and **BigPool** cache bookkeeping in the context of **CR3 abuse with physical R/W**; sits in the cheat / hide lane opposite [[kernel-pool-scanning]] BigPool walks and PiDDBCache / MmUnloadedDrivers forensics.

## Links

- Repo: https://github.com/hLunaaa/hLunaaa.github.io
- Post: [Exploring CI.dll and Bigpool Cache](https://github.com/hLunaaa/hLunaaa.github.io/blob/4eb5450cb245217543733b475ce1198b812551a6/_posts/2025-04-25-Bypassing-CR3-Abuse-with-Physical-RW%20copy.markdown)

## Related

[[kernel-pool-scanning]] · [[eac-cr3-bypass]] · [[ntmemory]] · [[revert-mapper]] · [[bootbypass]] · [[upgdsed]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
