---
title: SJCAM
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/keowu__sjcam.md
updated: 2026-08-02
confidence: medium
---

# SJCAM

Reverse-engineering and security research toolkit for SJCAM action cameras and their embedded firmware stacks. Includes a Python **AVIOCTRL** client over the camera TCP control protocol (login, capture, streaming, file transfer, configuration), C++ **Lelouch** native code built with an Android ARM toolchain for on-device UI, camera, Wi-Fi, and related services, IDA databases of camera binaries, firmware dumps, and Python parsers for AllWinner **EGON/IMAGEWTY** and Novatek **BCL1** images, plus vulnerability disclosure materials and proof-of-concept payloads (including **CVE-2026-52656**). Targets IoT and firmware security researchers studying camera protocol RE, embedded exploitation, and responsible disclosure on the SJ4000 Air (Allwinner V3). (source: wiki/sources/descriptions/keowu__sjcam.md)

## Links

- Repo: https://github.com/keowu/sjcam

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[embedded-hacking]] · [[fiano]] · [[sourceengineexplorer]]
