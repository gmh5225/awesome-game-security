---
title: bootlicker
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__bootlicker.md
updated: 2026-08-09
confidence: medium
---

# bootlicker

Generic UEFI bootkit proof of concept that loads malicious code during the Windows boot process before the OS kernel initializes. Patches the Windows Boot Manager or OS loader to inject kernel-mode code that runs with full system privileges, bypassing DSE, [[patchguard]], and other OS-level security measures. README positions it for initial usermode execution; aimed at boot-security researchers studying UEFI bootkit techniques and Secure Boot bypass. (source: wiki/sources/descriptions/gmh5225__bootlicker.md)

## Links

- Repo: https://github.com/gmh5225/bootlicker

## Related

[[uefi-bootloader]] · [[xigmapper]] · [[bootbypass]] · [[efixplorer]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
