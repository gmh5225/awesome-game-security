---
title: MemJect
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/danielkrupinski__MemJect.md
updated: 2026-08-16
confidence: medium
---

# MemJect

Minimal Windows **DLL injector** (danielkrupinski) that embeds a compiled DLL as a **raw byte array** in the injector source, then **manually maps** it into a target process (`csgo.exe` in the demo) entirely from user mode via `VirtualAllocEx`, `WriteProcessMemory`, and `CreateRemoteThread`. The mapper parses PE headers, allocates sized memory in the target, copies sections, resolves imports through `LoadLibraryA`/`GetProcAddress`, applies relocations, and optionally **erases the PE header and entry point** after `DllMain` to reduce forensic artifacts. Useful for studying in-memory DLL injection and user-mode PE manual mapping—the same PEB-unlisted executable memory tradecraft anti-cheat scanners target. (source: wiki/sources/descriptions/danielkrupinski__MemJect.md)

README lane: Manual Map.

## Links

- Repo: https://github.com/danielkrupinski/MemJect

## Related

[[modexmap]] · [[shtreeba]] · [[wizard-loader]] · [[osiris]] · [[faultline]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
