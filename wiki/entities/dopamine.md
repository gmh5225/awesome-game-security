---
title: Dopamine
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/opa334__Dopamine.md
updated: 2026-07-26
confidence: medium
---

# Dopamine

Semi-untethered rootless jailbreak for iOS 15.0–15.4.1 (all devices; README also tags iOS 15/16). Chains multiple kernel vulnerabilities for arbitrary kernel read/write, bypasses PAC and PPL, patches AMFI for unsigned code execution, and installs Sileo plus a procursus bootstrap under a rootless `/var/jb` layout. Swift/Objective-C codebase with a GUI app to trigger the exploit. Aimed at iOS security researchers studying modern kernel exploitation and rootless jailbreak architecture. (source: wiki/sources/descriptions/opa334__Dopamine.md)

Upstream of RootHide fork [[dopamine2-roothide]]; complements checkm8 [[palera1n]] and historical [[oob-entry]] (`tfp0`). Same-author tooling [[trollstore]] / [[opainject]] covers jailed sideload and runtime dylib inject beside full jailbreak privilege.

## Links

- Repo: https://github.com/opa334/Dopamine

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[dopamine2-roothide]] · [[palera1n]] · [[oob-entry]] · [[trollstore]] · [[opainject]]
