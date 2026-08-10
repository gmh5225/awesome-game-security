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
  - wiki/sources/descriptions/gmh5225__vgk-illegal-pf-logger.md
  - wiki/sources/descriptions/kali11211__valorant-internal-cheat.md
  - wiki/sources/descriptions/gmh5225__valorant-internal.md
  - wiki/sources/descriptions/gmh5225__valorant-internal-base.md
  - wiki/sources/descriptions/gmh5225__Valorant-cheat-internal.md
  - wiki/sources/descriptions/gmh5225__Valorant-Cheat.md
  - wiki/sources/descriptions/gmh5225__Valorant-Aimbot-Bypass.md
  - wiki/sources/descriptions/gmh5225__Valorant-Esp-Aimbot-Hack.md
  - wiki/sources/descriptions/gmh5225__Valorant-Esp-Aimbot-Cheat-Hack.md
  - wiki/sources/descriptions/gmh5225__VALORANT-HACK-ESP-AIMBOT-SKINCHANGER.md
  - wiki/sources/descriptions/gmh5225__Valorant-Dumper-Tool.md
  - wiki/sources/descriptions/gmh5225__valorant-externals.md
  - wiki/sources/descriptions/gmh5225__valorant-esp-hack-with-driver.md
  - wiki/sources/descriptions/gmh5225__valo-driver.md
  - wiki/sources/descriptions/gmh5225__ValorantCheatExternal.md
  - wiki/sources/descriptions/gmh5225__Valorant-CheatExternal.md
  - wiki/sources/descriptions/gmh5225__Valorant.External.md
  - wiki/sources/descriptions/gmh5225__Valorant-External-Source.md
  - wiki/sources/descriptions/gmh5225__Valorant-External-P2C-Leaked.md
  - wiki/sources/descriptions/gmh5225__Valorant-External-1.md
  - wiki/sources/descriptions/gmh5225__lol_patcher.md
  - wiki/sources/descriptions/gmh5225__lol-offset-dumper.md
  - wiki/sources/descriptions/gmh5225__lol-unpackman.md
  - wiki/sources/descriptions/gmh5225__league-base.md
  - wiki/sources/descriptions/gmh5225__hh-lol-prophet.md
  - wiki/sources/descriptions/gmh5225__frank.md
  - wiki/sources/descriptions/gmh5225__ayaya-league-external.md
  - wiki/sources/descriptions/gmh5225__augur-riot.md
  - wiki/sources/descriptions/gmh5225__VanguardImportResolver.md
updated: 2026-08-10
confidence: medium
---

# Vanguard

Riot Games anti-cheat featuring a **boot-start** kernel driver for early visibility into later-loaded drivers, boot-time initialization, driver allowlisting, and aggressive system trust checks. Used by Valorant and League of Legends. (source: wiki/sources/skills/anti-cheat.md)

## Distinguishing trait

Early load timing changes the BYOVD/test-sign window relative to runtime-loaded ACs ([[easy-anti-cheat]], [[battleye]]). Research often pairs Vanguard with FACEIT AC discussions on kernel integrity.

EFI manual-map research such as [[xigmapper]] notes a practical consequence of that early load: USB-hosted driver images are discovered by Windows *after* Vanguard, so payloads intended for pre-OS map paths cannot rely on USB media. (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md)

Per-title Valorant UE dump tooling such as [[valorant-dumper]] (GObjects/GNames, player/weapon layouts from the live process) and [[valorant-dumper-tool]] (C++; README `[Dump]`; gmh5225) is useful when modeling what cheat SDK generators probe under a Vanguard-protected title. (source: wiki/sources/descriptions/xehn1337__valorant-dumper.md) (source: wiki/sources/descriptions/gmh5225__Valorant-Dumper-Tool.md) Narrower FNamePool walk/decrypt samples such as [[valorant-fnamepool]] (iterate and decrypt `FNamePool->Entries`) sit in the same Valorant UE name-pool research lane. (source: wiki/sources/descriptions/percpopper__VALORANT-FNamePool.md) External offset feeds such as [[valorant-externals]] (README `[Offset]` tag; incremental refresh; gmh5225) complement dump tooling for out-of-process memory-layout study under Vanguard. (source: wiki/sources/descriptions/gmh5225__valorant-externals.md)

Client-side Valorant crosshair config samples such as [[valorantcc]] sit in the adjacent cheat / game:valorant utility lane (Riot-owned assets/endpoints; not an AC product). (source: wiki/sources/descriptions/weedeej__ValorantCC.md) In-process internal cheat bases such as [[valorant-internal-cheat]] (C/C++; UE SDK generation + hooking), [[valorant-internal]] (C/C++; SDK generation + hooking; gmh5225), and [[valorant-internal-base]] (C/C++; internal base scaffold; gmh5225) illustrate the offensive in-process lane under Vanguard rather than dump-only or utility tooling. (source: wiki/sources/descriptions/kali11211__valorant-internal-cheat.md) (source: wiki/sources/descriptions/gmh5225__valorant-internal.md) (source: wiki/sources/descriptions/gmh5225__valorant-internal-base.md) Menu-driven internal samples such as [[valorant-cheat-internal]] (Insert-key menu toggle; rebindable; README `[Internal]`; gmh5225) complement SDK/hook bases for in-process UX study. (source: wiki/sources/descriptions/gmh5225__Valorant-cheat-internal.md) StuzziKLL-lineage internal samples such as [[valorant-cheat]] (C/C++; StuzziKLL source fork with minor adjustments; anti-cheat research + driver development; gmh5225) complement menu-driven internals for studying in-process + kernel-driver offensive stacks under Vanguard. (source: wiki/sources/descriptions/gmh5225__Valorant-Cheat.md) Fully featured internal ESP/aimbot samples such as [[valorant-esp-aimbot-hack]] (Eduty; C++; gmh5225) illustrate the in-process offensive feature stack under Vanguard rather than dump-only or external tooling. (source: wiki/sources/descriptions/gmh5225__Valorant-Esp-Aimbot-Hack.md) Human-aim aimbot samples such as [[valorant-aimbot-bypass]] (author-coded Valorant aimbot with human-like aim smoothing; gmh5225) complement that lane for studying behavioral-evasion-oriented aim assist under Vanguard. (source: wiki/sources/descriptions/gmh5225__Valorant-Aimbot-Bypass.md)

Update-monitoring tooling such as [[vanguard-update-notifier]] (Discord bot; polls Riot clientconfig, SHA-256 hashes Vanguard setup archive contents, alerts on version/hash drift) helps researchers track installer changes without manual diffing. (source: wiki/sources/descriptions/luavmload__vanguard-update-notifier.md)

Exception-dispatch research such as [[val-exception-handler]] (PoC; hardware exceptions / VEH; `ZwRaiseException` dump; potential code-exec or evasion angles in Vanguard's kernel exception flow) complements generic VEH tooling like [[veh-dumper]]. (source: wiki/sources/descriptions/lil-skies__val-exception-handler.md)

Page-fault telemetry such as [[vgk-illegal-pf-logger]] (logs intentional illegal PFs from `vgk.sys`; integrity-check detection mechanism RE) complements exception-dispatch PoCs and usermode working-set monitors like [[faultline]]. (source: wiki/sources/descriptions/gmh5225__vgk-illegal-pf-logger.md)

RITO streamed-module reconstruction such as [[augur-riot]] (hashed import resolve, section rebuild, valid PE/DLL output from Vanguard driver payloads; gmh5225) supports offline static RE of Vanguard kernel modules without live driver telemetry. (source: wiki/sources/descriptions/gmh5225__augur-riot.md) Protected `vgk.sys` import resolution such as [[vanguard-import-resolver]] (resolve Vanguard kernel import addresses; document import-protection mechanism; gmh5225) complements that lane for analyzing which kernel APIs the driver calls. (source: wiki/sources/descriptions/gmh5225__VanguardImportResolver.md)

Early-load offensive samples such as [[valorant-esp-hack-with-driver]] (ESP; exploits a Vanguard driver vulnerability to load a companion driver before Vanguard; kernel-injector workflow; gmh5225) illustrate the boot-order race against Vanguard's early visibility rather than in-process SDK or dump-only tooling. (source: wiki/sources/descriptions/gmh5225__valorant-esp-hack-with-driver.md)

Kernel external memory-read drivers such as [[valo-driver]] (C; physical translate / CR3 / MDL paths; avoids monitored standard APIs; gmh5225) demonstrate Vanguard-specific cross-process R/W bypass research beside generic CR3/MDL tooling. (source: wiki/sources/descriptions/gmh5225__valo-driver.md) Kernel-driver ESP/aimbot/skin-changer samples such as [[valorant-hack-esp-aimbot-skinchanger]] (UE4 entity overlays; aim smoothing; client-side skin modification; bypasses user-mode protections; gmh5225) complement that lane for studying multi-feature cheat stacks under Vanguard. (source: wiki/sources/descriptions/gmh5225__VALORANT-HACK-ESP-AIMBOT-SKINCHANGER.md)

Full external cheat stacks such as [[valorant-cheat-external]] (kernel driver RPM; no process injection; UE4 entity ESP/aimbot; bypasses injection detection; gmh5225) illustrate the out-of-process offensive architecture researchers study under Vanguard-protected Valorant. (source: wiki/sources/descriptions/gmh5225__ValorantCheatExternal.md) A related driver/shader/rendering external sample under the same name (`Valorant-CheatExternal`; gmh5225) complements that lane for studying external overlay and kernel-driver scaffolding. (source: wiki/sources/descriptions/gmh5225__Valorant-CheatExternal.md) Successor-style external samples such as [[valorant-external]] (latest iteration; enhanced security emphasis; gmh5225) sit in the same lane for studying hardened out-of-process cheat design. (source: wiki/sources/descriptions/gmh5225__Valorant.External.md) External cheat source samples such as [[valorant-external-source]] (ESP/aimbot/player info; kernel driver RPM; separate-window or hijacked overlay; README `[External]`; gmh5225) complement that lane for studying Vanguard kernel protection against out-of-process reads and overlay rendering. (source: wiki/sources/descriptions/gmh5225__Valorant-External-Source.md) Leaked commercial P2C external samples such as [[valorant-external-p2c-leaked]] (ESP/aimbot/triggerbot; kernel driver RPM; UE state reads under Vanguard; README `[External]`; gmh5225) illustrate typical pay-to-cheat external architecture for researchers studying bypass patterns. (source: wiki/sources/descriptions/gmh5225__Valorant-External-P2C-Leaked.md) OpenGL-overlay external samples such as [[valorant-external-1]] (C/C++; OpenGL rendering; out-of-process cheat / game:valorant; gmh5225) complement that lane for studying non-DX overlay paths under Vanguard. (source: wiki/sources/descriptions/gmh5225__Valorant-External-1.md) Dual-mode ESP/aimbot samples such as [[valorant-esp-aimbot-cheat-hack]] (external or internal memory access; UE4 entity outlines/health/distance ESP plus aimbot; README `[External]`; gmh5225) illustrate flexible memory-access cheat patterns researchers study under Vanguard. (source: wiki/sources/descriptions/gmh5225__Valorant-Esp-Aimbot-Cheat-Hack.md)

Historical League of Legends client mod/patcher samples such as [[lol-patcher]] (gmh5225; experimental; frozen Feb 2020) illustrate LoL-side offensive research under the same Vanguard-protected Riot title family as Valorant. (source: wiki/sources/descriptions/gmh5225__lol_patcher.md) LoL client unpacker samples such as [[lol-unpackman]] (C++; gmh5225) complement that lane for client-binary unpacking study. (source: wiki/sources/descriptions/gmh5225__lol-unpackman.md) LoL offset dump tooling such as [[lol-offset-dumper]] (C/C++; memory analysis; gmh5225) complements that lane for live client layout dumps. (source: wiki/sources/descriptions/gmh5225__lol-offset-dumper.md) LoL cheat base frameworks such as [[league-base]] (C++; memory read, object enumeration, champion data, overlay rendering; Packman/Vanguard considerations; gmh5225) illustrate full cheat scaffold research in that same LoL lane. (source: wiki/sources/descriptions/gmh5225__league-base.md) LoL modding samples such as [[hh-lol-prophet]] (Go; hh lol prophet; gmh5225) complement that lane for client modding study. (source: wiki/sources/descriptions/gmh5225__hh-lol-prophet.md) LoL assistant client samples such as [[frank]] (JavaScript; WeGame replacement; rendering/animation/asset pipelines; gmh5225) complement that lane for launcher/client-side study. (source: wiki/sources/descriptions/gmh5225__frank.md) LoL external script platforms such as [[ayaya-league-external]] (Node.js; AyayaLeague; custom user scripts; gmh5225) complement that lane for out-of-process scripting automation. (source: wiki/sources/descriptions/gmh5225__ayaya-league-external.md)

## Related

[[easy-anti-cheat]] · [[battleye]] · [[hvci]] · [[byovd]] · [[xigmapper]] · [[augur-riot]] · [[vanguard-import-resolver]] · [[lol-patcher]] · [[lol-offset-dumper]] · [[lol-unpackman]] · [[league-base]] · [[hh-lol-prophet]] · [[frank]] · [[ayaya-league-external]] · [[valorant-dumper]] · [[valorant-dumper-tool]] · [[valorant-fnamepool]] · [[valorant-externals]] · [[valorant-esp-hack-with-driver]] · [[valo-driver]] · [[valorant-cheat-external]] · [[valorant-external]] · [[valorant-external-1]] · [[valorant-external-p2c-leaked]] · [[valorant-external-source]] · [[valorant-internal]] · [[valorant-internal-base]] · [[valorant-internal-cheat]] · [[valorant-cheat]] · [[valorant-cheat-internal]] · [[valorant-aimbot-bypass]] · [[valorant-esp-aimbot-hack]] · [[valorant-esp-aimbot-cheat-hack]] · [[valorant-hack-esp-aimbot-skinchanger]] · [[valorantcc]] · [[vanguard-update-notifier]] · [[val-exception-handler]] · [[vgk-illegal-pf-logger]] · [[overviews/anti-cheat]]
