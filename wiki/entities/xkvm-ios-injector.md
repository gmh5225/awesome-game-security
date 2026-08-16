---
title: xKVM iOS Injector
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/xscope0__xkvm-ios-injector.md
updated: 2026-08-16
confidence: medium
---

# xKVM iOS Injector

Pure-Go **command-line and TUI toolbox** for **sideloading iOS apps** by injecting tweaks into **IPA**, **TIPA**, or **`.app` bundles** and repacking them with correct code signatures. A from-scratch rewrite of the cyan/pyzule-rw injector with restored Azule capabilities. (source: wiki/sources/descriptions/xscope0__xkvm-ios-injector.md)

Core workflows include **dylib and `.deb` injection**, **tweak extraction**, **jailbreak package conversion** between rootful, rootless, and roothide formats, and **App Store IPA decryption**. The toolchain embeds hooking runtimes such as **ElleKit**, **CydiaSubstrate**, and **Orion**, applies sideload repair patches, fetches packages from Cydia repos via **Canister** or **MobileAPT**, and validates bundle completeness before install. Mach-O manipulation and Apple-format ad-hoc signing are implemented in pure Go for deterministic, reproducible builds. Targets iOS tweak developers, reverse engineers, and security researchers who modify sideloaded apps or study how injected code loads at runtime.

Complements non-jailbreak IPA patch tooling such as [[ipapatch]] and perma-signed jailed installers such as [[trollstore]] on the sideload/repack lane, and runtime patching libraries such as [[kittymemory-ios]] when the workflow is bundle-time injection rather than in-process memory edit.

## Links

- Repo: https://github.com/xscope0/xkvm-ios-injector

## Related

[[ipapatch]] · [[trollstore]] · [[kittymemory-ios]] · [[opainject]] · [[ios-mod-menu-template-for-theos]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
