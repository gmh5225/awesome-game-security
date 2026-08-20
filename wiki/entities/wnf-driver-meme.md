---
title: wnf-driver-meme
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/zensenzay__wnf-driver-meme.md
updated: 2026-08-20
confidence: medium
---

# wnf-driver-meme

Windows kernel driver with a C++ user-mode client that exchanges commands through **Windows Notification Facility (WNF)** state names instead of conventional device paths or IOCTL codes. The client discovers the channel via registry keys under `WnfNotify`, avoiding a visible driver device object. The driver supports kernel-level read and write access to arbitrary process memory by PID and can protect selected processes by registering **ObRegisterCallbacks** hooks that strip sensitive handle rights such as VM read/write, duplicate, and suspend/resume. Intended for game security research, anti-cheat analysis, and reverse engineering where stealthy cross-privilege communication and process hardening are explored. (source: wiki/sources/descriptions/zensenzay__wnf-driver-meme.md)

## Links

- Repo: https://github.com/zensenzay/wnf-driver-meme

## Related

[[kernel-callbacks]] · [[memfilter-fn-driver]] · [[evcommunication]] · [[boundcallback]] · [[van1338]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
