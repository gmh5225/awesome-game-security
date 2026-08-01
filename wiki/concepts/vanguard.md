---
title: Vanguard
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/xtremegamer1__xigmapper.md
  - wiki/sources/descriptions/xehn1337__valorant-dumper.md
  - wiki/sources/descriptions/percpopper__VALORANT-FNamePool.md
  - wiki/sources/descriptions/weedeej__ValorantCC.md
  - wiki/sources/descriptions/luavmload__vanguard-update-notifier.md
  - wiki/sources/descriptions/lil-skies__val-exception-handler.md
updated: 2026-08-01
confidence: medium
---

# Vanguard

Riot Games anti-cheat featuring a **boot-start** kernel driver for early visibility into later-loaded drivers, boot-time initialization, driver allowlisting, and aggressive system trust checks. Used by Valorant and League of Legends. (source: wiki/sources/skills/anti-cheat.md)

## Distinguishing trait

Early load timing changes the BYOVD/test-sign window relative to runtime-loaded ACs ([[easy-anti-cheat]], [[battleye]]). Research often pairs Vanguard with FACEIT AC discussions on kernel integrity.

EFI manual-map research such as [[xigmapper]] notes a practical consequence of that early load: USB-hosted driver images are discovered by Windows *after* Vanguard, so payloads intended for pre-OS map paths cannot rely on USB media. (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md)

Per-title Valorant UE dump tooling such as [[valorant-dumper]] (GObjects/GNames, player/weapon layouts from the live process) is useful when modeling what cheat SDK generators probe under a Vanguard-protected title. (source: wiki/sources/descriptions/xehn1337__valorant-dumper.md) Narrower FNamePool walk/decrypt samples such as [[valorant-fnamepool]] (iterate and decrypt `FNamePool->Entries`) sit in the same Valorant UE name-pool research lane. (source: wiki/sources/descriptions/percpopper__VALORANT-FNamePool.md)

Client-side Valorant crosshair config samples such as [[valorantcc]] sit in the adjacent cheat / game:valorant utility lane (Riot-owned assets/endpoints; not an AC product). (source: wiki/sources/descriptions/weedeej__ValorantCC.md)

Update-monitoring tooling such as [[vanguard-update-notifier]] (Discord bot; polls Riot clientconfig, SHA-256 hashes Vanguard setup archive contents, alerts on version/hash drift) helps researchers track installer changes without manual diffing. (source: wiki/sources/descriptions/luavmload__vanguard-update-notifier.md)

Exception-dispatch research such as [[val-exception-handler]] (PoC; hardware exceptions / VEH; `ZwRaiseException` dump; potential code-exec or evasion angles in Vanguard's kernel exception flow) complements generic VEH tooling like [[veh-dumper]]. (source: wiki/sources/descriptions/lil-skies__val-exception-handler.md)

## Related

[[easy-anti-cheat]] · [[battleye]] · [[hvci]] · [[byovd]] · [[xigmapper]] · [[valorant-dumper]] · [[valorant-fnamepool]] · [[valorantcc]] · [[vanguard-update-notifier]] · [[val-exception-handler]] · [[overviews/anti-cheat]]
