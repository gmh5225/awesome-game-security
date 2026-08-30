---
title: bemaniutils
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/DragonMinded__bemaniutils.md
updated: 2026-08-30
confidence: medium
---

# bemaniutils

**bemaniutils** is a Python toolkit for analyzing, modifying, and emulating Konami **BEMANI** arcade rhythm games and their **eAmusement** network services. It unpacks and repacks proprietary asset formats (IFS, 2DX, AFP/BSI animations, encrypted NVRAM) and implements the binary eAmusement wire protocol. Network RE tooling includes packet sniffers, MITM proxies, traffic replay, and psmap-based response generators for black-box protocol research. A hobby eAmusement server stack ships game backends for titles such as Beatmania IIDX, DDR, Pop'n Music, and Sound Voltex—aimed at preservationists and researchers studying legacy arcade game security and networking. (source: wiki/sources/descriptions/DragonMinded__bemaniutils.md)

README lane: RE toolkit for BEMANI arcade titles—network service emulation, packet sniff/redirect/reconstruct, and binary asset unpack/repack utilities.

## Links

- Repo: https://github.com/DragonMinded/bemaniutils

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[packet-sniffer]] · [[spirit-ptcgo]] · [[protobufs]] · [[ds3os]]
