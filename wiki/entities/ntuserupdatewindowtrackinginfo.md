---
title: NtUserUpdateWindowTrackingInfo
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/D3DXVECTOR2__NtUserUpdateWindowTrackingInfo.md
updated: 2026-08-26
confidence: medium
---

# NtUserUpdateWindowTrackingInfo

**Windows kernel communication framework** (D3DXVECTOR2) that repurposes the **NtUserUpdateWindowTrackingInfo** syscall path as a covert command channel. A kernel component hooks **win32k** function pointers and exposes process memory read/write, pattern scanning, allocation, and pointer swapping through custom request codes. A user-mode client initializes the syscall stub and issues structured commands to interact with target processes. Geared toward game cheat development and anti-cheat evasion research at the kernel boundary. (source: wiki/sources/descriptions/D3DXVECTOR2__NtUserUpdateWindowTrackingInfo.md)

## Links

- Repo: https://github.com/D3DXVECTOR2/NtUserUpdateWindowTrackingInfo

## Related

[[kernel-eac-be-comm]] · [[interep-driver-leak]] · [[comm-data-ptr-driver]] · [[win32khooker]] · [[km-um-communication]] · [[driver-communication-list]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
