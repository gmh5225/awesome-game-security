---
title: meowna_detector
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Rem01Gaming__meowna_detector.md
updated: 2026-08-21
confidence: medium
---

# meowna_detector

Proof-of-concept Android detector for **meowna**-class root-hiding modules that disrupt logging services. A small C program built with Android NDK makefiles checks environment-tampering indicators such as missing **logd** sockets and package traces to flag suspicious root-hide behavior—useful for mobile security testing and for studying how fragile logging-disruption hide techniques can become detectable. (source: wiki/sources/descriptions/Rem01Gaming__meowna_detector.md)

Sits in the Anti Cheat `Detection:Android root` lane beside broader root probes such as [[android-native-root-detector]], [[magisk-killer]], and [[detection]]—opposite root-hide modules such as [[riru-momo-hider]] and [[hideroot]] that conceal Magisk artifacts from conventional checks.

## Links

- Repo: https://github.com/Rem01Gaming/meowna_detector

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[android-native-root-detector]] · [[magisk-killer]] · [[detection]] · [[riru-momo-hider]] · [[hideroot]] · [[magiskhide]]
