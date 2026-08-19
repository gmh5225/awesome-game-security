---
title: iOS Packager
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/addrianyy__ios_packager.md
updated: 2026-08-19
confidence: medium
---

# iOS Packager

Python **command-line utility** for **repackaging and signing iOS application bundles**. Parses certificate metadata, updates **Info.plist** and **entitlements**, retrieves **provisioning profiles**, and invokes **codesign**. Helper modules cover provisioning requests, caching, and template-driven packaging steps—useful when mobile app and game security workflows need repeated resigning and deployment during testing. (source: wiki/sources/descriptions/addrianyy__ios_packager.md)

Complements sideload/injection tooling such as [[xkvm-ios-injector]] and non-jailbreak patch workflows such as [[ipapatch]] on the IPA repack/sign lane, and perma-signed jailed installers such as [[trollstore]] when the workflow is developer-certificate resign rather than CoreTrust bypass.

## Links

- Repo: https://github.com/addrianyy/ios_packager

## Related

[[ipapatch]] · [[xkvm-ios-injector]] · [[trollstore]] · [[opainject]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
