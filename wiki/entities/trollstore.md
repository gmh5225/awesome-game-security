---
title: TrollStore
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/opa334__TrollStore.md
updated: 2026-07-26
confidence: medium
---

# TrollStore

Perma-signed jailed app installer for iOS (Objective-C). Exploits CoreTrust and AMFI bugs to install IPA files with arbitrary entitlements without a jailbreak; installed apps persist across reboots and do not require re-signing. Relies on a kernel vulnerability chain on certain iOS versions to bypass code-signing enforcement while remaining in the jailed sandbox. Aimed at iOS security researchers studying code-signing bypass and sideload workflows without developer certificates. (source: wiki/sources/descriptions/opa334__TrollStore.md)

Complements non-jailbreak IPA patching ([[ipapatch]]) and same-author runtime inject ([[opainject]]); sits beside full jailbreak trees such as [[palera1n]] / [[dopamine2-roothide]] when contrasting perma-sign sideload vs rootful/rootless privilege.

## Links

- Repo: https://github.com/opa334/TrollStore

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[ipapatch]] · [[opainject]] · [[palera1n]] · [[dopamine2-roothide]] · [[imgui-ios-mod-menu]]
