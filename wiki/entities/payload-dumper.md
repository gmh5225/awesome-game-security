---
title: payload_dumper
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/vm03__payload_dumper.md
updated: 2026-07-19
confidence: medium
---

# payload_dumper

Python tool that dumps partitions from Android OTA `payload.bin` images. Useful for ROM/root and mobile RE workflows that need system/vendor/product images extracted from full or incremental OTA packages before boot-image or filesystem analysis. (source: wiki/sources/descriptions/vm03__payload_dumper.md)

Sits in the Cheat Magisk / Android ROM–root / RE-tools lane alongside boot-image tooling such as [[magiskboot-ndk-on-linux]] and recovery device trees such as [[ofrp-device-xiaomi-mondrian]].

## Links

- Repo: https://github.com/vm03/payload_dumper

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[magiskboot-ndk-on-linux]] · [[ofrp-device-xiaomi-mondrian]]
