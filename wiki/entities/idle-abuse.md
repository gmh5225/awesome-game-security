---
title: IDLE-Abuse
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/RixedLabs__IDLE-Abuse.md
updated: 2026-08-21
confidence: medium
---

# IDLE-Abuse

Proof-of-concept for **injecting code when a Windows process becomes idle** (RixedLabs; C++). Abuses the undocumented **`RegisterWaitForInputIdle`** callback path: after spawning a target process, a wait callback fires once the child reaches an input-idle state, enabling payload delivery without conventional remote-thread or `VirtualAllocEx` patterns. Sample flows cover **shellcode execution** and **process manipulation** tradecraft. Aimed at offensive security experimentation and at studying **process-lifecycle abuse** detections relevant to game anti-cheat and EDR visibility. (source: wiki/sources/descriptions/RixedLabs__IDLE-Abuse.md)

## Links

- Repo: https://github.com/RixedLabs/IDLE-Abuse

## Related

[[windows-process-injection]] · [[frankenstein-apc-injection]] · [[poolparty]] · [[dirty-vanity]] · [[kernel-dll-injector]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
