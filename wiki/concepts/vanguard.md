---
title: Vanguard
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/xtremegamer1__xigmapper.md
  - wiki/sources/descriptions/xehn1337__valorant-dumper.md
  - wiki/sources/descriptions/weedeej__ValorantCC.md
updated: 2026-07-18
confidence: medium
---

# Vanguard

Riot Games anti-cheat featuring a **boot-start** kernel driver for early visibility into later-loaded drivers, boot-time initialization, driver allowlisting, and aggressive system trust checks. Used by Valorant and League of Legends. (source: wiki/sources/skills/anti-cheat.md)

## Distinguishing trait

Early load timing changes the BYOVD/test-sign window relative to runtime-loaded ACs ([[easy-anti-cheat]], [[battleye]]). Research often pairs Vanguard with FACEIT AC discussions on kernel integrity.

EFI manual-map research such as [[xigmapper]] notes a practical consequence of that early load: USB-hosted driver images are discovered by Windows *after* Vanguard, so payloads intended for pre-OS map paths cannot rely on USB media. (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md)

Per-title Valorant UE dump tooling such as [[valorant-dumper]] (GObjects/GNames, player/weapon layouts from the live process) is useful when modeling what cheat SDK generators probe under a Vanguard-protected title. (source: wiki/sources/descriptions/xehn1337__valorant-dumper.md)

Client-side Valorant crosshair config samples such as [[valorantcc]] sit in the adjacent cheat / game:valorant utility lane (Riot-owned assets/endpoints; not an AC product). (source: wiki/sources/descriptions/weedeej__ValorantCC.md)

## Related

[[easy-anti-cheat]] · [[battleye]] · [[hvci]] · [[byovd]] · [[xigmapper]] · [[valorant-dumper]] · [[valorantcc]] · [[overviews/anti-cheat]]
