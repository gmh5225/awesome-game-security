---
title: Driver-SessionMapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-SessionMapper.md
updated: 2026-08-13
confidence: medium
---

# Driver-SessionMapper

Session-space driver mapper that manually loads a driver image into session memory instead of using the normal kernel module loading path. A kernel component pairs with a client that passes raw image data for import fixing, section copying, relocation, and entry-point execution. (source: wiki/sources/descriptions/gmh5225__Driver-SessionMapper.md)

The main hook replaces an internal `ntoskrnl` callback path, allocates session-space memory for the target image, resolves imports and relocations, then clears parts of the loader metadata on unload to reduce the mapped driver's visibility in ordinary loader structures. Primarily useful for Windows kernel researchers studying manual mapping into session space, alternative driver loading flows, and techniques for hiding mapped modules from PiDDBCache/MmUnloadedDrivers-style forensics.

## Links

- Repo: https://github.com/gmh5225/Driver-SessionMapper

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[callmewin32kdriver]] · [[nullmap]] · [[map-file-in-system-space]] · [[revert-mapper]] · [[known-driver-mappers]] · [[kernel-pool-scanning]]
