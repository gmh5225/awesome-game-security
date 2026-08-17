---
title: Known-Driver-Mappers
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/stuxnet147__Known-Driver-Mappers.md
updated: 2026-07-21
confidence: medium
---

# Known-Driver-Mappers

Catalog focused on **known Driver Mappers**, centered on driver development. Aimed at anti-cheat engineers and defensive researchers in the anti-cheat / stress-testing lane—mapping public mapper families and load paths for detection and lab stress rather than shipping a single mapper. (source: wiki/sources/descriptions/stuxnet147__Known-Driver-Mappers.md)

Companion research lane to concrete mapper samples such as [[lsass-extend-mapper]], minimalist BYOVD mappers such as [[umap]] (btbd; C; physmem primitive → full PE map from user mode; no registry / standard load-path traces), BTBD shellcode mappers such as [[smap]] (raw PIC shellcode → kernel pool via BYOVD exec primitive; no PE image), post-map cleanup such as [[revert-mapper]], and EFI early-load mappers such as [[xigmapper]].

## Links

- Repo: https://github.com/stuxnet147/Known-Driver-Mappers

## Related

[[lsass-extend-mapper]] · [[umap]] · [[smap]] · [[revert-mapper]] · [[xigmapper]] · [[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
