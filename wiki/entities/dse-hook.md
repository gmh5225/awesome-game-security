---
title: dse_hook
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__dse_hook.md
updated: 2026-08-09
confidence: medium
---

# dse_hook

Windows Driver Signature Enforcement (DSE) bypass research PoC that hooks CI.dll code integrity checks to allow loading unsigned kernel drivers. Patches either CI.dll's signature verification routine or the `g_CiEnabled` global to disable enforcement — aimed at kernel researchers studying direct CI/DSE bypass without certificate or [[byovd]] primitives. (source: wiki/sources/descriptions/gmh5225__dse_hook.md)

Adjacent to CI/`g_CiOptions` controllers such as [[kvc]], boot-time `SeCiCallbacks` kits such as [[kernel-research-kit]], and multi-method runtime disable tooling such as [[upgdsed]] — here the focus is hooking CI.dll verification paths rather than signed-helper IOCTL writes or clock/cert abuse such as [[pastdse]].

## Links

- Repo: https://github.com/gmh5225/dse_hook

## Related

[[kvc]] · [[kernel-research-kit]] · [[bootbypass]] · [[upgdsed]] · [[pastdse]] · [[byovd]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
