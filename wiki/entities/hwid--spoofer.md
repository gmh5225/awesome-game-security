---
title: Hwid--Spoofer (Theordernarkoz)
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Theordernarkoz__Hwid--Spoofer.md
updated: 2026-08-20
confidence: medium
---

# Hwid--Spoofer (Theordernarkoz)

**Hwid--Spoofer** is a Windows **kernel-mode HWID spoofer driver** built primarily in C with **KMDF**. It hooks disk, mount, and network control paths to alter hardware-identifying values, including disk identifiers, NIC data, SMBIOS information, and GPU-related strings. Primary use case: anti-cheat evasion and low-level hardware identity research in game security contexts. (source: wiki/sources/descriptions/Theordernarkoz__Hwid--Spoofer.md)

Distinct from the sibling [[theordernarkoz-hwid-spoofer]] repo (`Hwid-Spoofer`), which is a usermode ImGui+DirectX 9 launcher that downloads external driver/helper binaries rather than embedding kernel spoof logic in-tree.

Sits in the `Cheat > HWID` lane beside KMDF/kernel-hook samples such as [[easy-hwid-spoofer]], [[hwid-kernel-spoofer]], [[hwid-spoofer-eac-be]], and [[driver-hwid-btbd-modified]], and Detection:HWID counterparts such as [[hwid-checker-mg]].

## Links

- Repo: https://github.com/Theordernarkoz/Hwid--Spoofer

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[theordernarkoz-hwid-spoofer]] · [[easy-hwid-spoofer]] · [[hwid-kernel-spoofer]] · [[hwid-spoofer-eac-be]] · [[driver-hwid-btbd-modified]] · [[hwid-checker-mg]]
