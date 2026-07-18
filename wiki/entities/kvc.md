---
title: kvc
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__kvc.md
updated: 2026-07-18
confidence: medium
---

# kvc

Windows kernel vulnerability controller for unsigned-driver research: disables Driver Signature Enforcement (DSE) by patching CI.dll options (`g_CiOptions`) through a signed Microsoft driver, with additional loader strategies (`skci.dll` hijack, `SeCiCallbacks` redirection) and certificate-based signing of payloads. Also covers PP/PPL manipulation aimed at LSASS memory dumping on [[hvci]]/VBS-enabled Windows. (source: wiki/sources/descriptions/wesmar__kvc.md)

Useful reference for the Cheat PatchGuard/DSE and vulnerable-driver lanes when studying how signed helpers open paths past Driver Signature Enforcement under modern VBS assumptions. Same-author [[kvcforensic]] covers LSA secret extraction from the resulting dumps / live LSASS memory.

## Links

- Repo: https://github.com/wesmar/kvc

## Related

[[kvcforensic]] · [[byovd]] · [[hvci]] · [[lsass-extend-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
