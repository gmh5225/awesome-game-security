---
title: palera1n
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/palera1n__palera1n.md
updated: 2026-07-26
confidence: medium
---

# palera1n

Developer jailbreak for iOS 15+ on checkm8-compatible devices (A8–A11). Exploits the hardware-level checkm8 bootrom vulnerability over USB to boot a patched kernel with AMFI and codesigning disabled, then installs Sileo and a bootstrap environment. Supports rootful and rootless modes (rootless keeps the root filesystem sealed). Aimed at iOS security researchers, jailbreak developers, and reverse engineers needing root on modern iOS. (source: wiki/sources/descriptions/palera1n__palera1n.md)

Complements software-chain jailbreaks such as [[dopamine2-roothide]] (iOS 15/16) and historical [[oob-entry]] (`tfp0`); useful when studying bootrom-backed privilege vs userland/kernel exploit chains like [[lightsaber]].

## Links

- Repo: https://github.com/palera1n/palera1n

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[dopamine2-roothide]] · [[oob-entry]] · [[lightsaber]]
