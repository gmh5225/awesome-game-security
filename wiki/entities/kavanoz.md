---
title: kavanoz
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/eybisi__kavanoz.md
updated: 2026-08-15
confidence: medium
---

# kavanoz

Kavanoz is an automated Python Android DEX and resource unpacker. It detects packed or encrypted DEX in APKs protected by commercial packers (Bangcle, Ijiami, Qihoo 360, and others), identifies the packing scheme, locates the encrypted payload, and applies scheme-specific decryption or decompression. Aimed at Android malware analysts and reverse engineers who need static analysis of protected APKs—including common Android banker malware. (source: wiki/sources/descriptions/eybisi__kavanoz.md)

Complements runtime DEX recovery via [[zygisk-dump-dex]] and general Sample Unpacker tooling such as [[android-unpacker]]; pairs with packer fingerprinting via [[apkid]] and downstream decompile via [[jadx]].

## Links

- Repo: https://github.com/eybisi/kavanoz

## Related

[[android-unpacker]] · [[zygisk-dump-dex]] · [[apkid]] · [[jadx]] · [[dalivm]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
