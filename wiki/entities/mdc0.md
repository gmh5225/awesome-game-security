---
title: mdc0
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/34306__mdc0.md
updated: 2026-09-05
confidence: medium
---

# mdc0

**Swift iOS customization app** for **jailed devices** that applies system UI tweaks **without a traditional jailbreak**. Targets **iOS 15.0 through 18.3.2**, using an **exploit path** to modify normally read-only system files. Features include dock and blur adjustments, lockscreen UI tweaks, and other cosmetic or behavior-level modifications that often require a **respring helper app**. Primary use case is **iOS customization** and **exploit-oriented research** on modern non-jailbroken devices; README tags **[CVE-2025-24203]**. (source: wiki/sources/descriptions/34306__mdc0.md)

Sits in the **jailed sideload** lane beside perma-signed installers such as [[trollstore]] and non-jailbreak patch tooling such as [[ipapatch]], but goes further by **writing system UI state** rather than only repackaging third-party IPAs. The CVE tag aligns this consumer app with kernel primitives such as [[dirty-zero]] and DarkSword-family research such as [[darksword-kexploit-fun]] / [[lara]] on contemporary XNU surfaces. From the same maintainer ecosystem as emulator/jailbreak labs [[vphone-aio]] and [[usbliter8-fun]] (34306).

## Links

- Repo: https://github.com/34306/mdc0 (README: CVE-2025-24203; jailed-device system UI customization)

## Related

[[dirty-zero]] · [[trollstore]] · [[ipapatch]] · [[vphone-aio]] · [[usbliter8-fun]] · [[dopamine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
