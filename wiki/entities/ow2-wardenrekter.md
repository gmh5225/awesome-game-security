---
title: OW2 Wardenrekter
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__OW2-wardenrekter.md
updated: 2026-08-11
confidence: medium
---

# OW2 Wardenrekter

Injected **Overwatch 2** research DLL (gmh5225) that disables **Warden** anti-cheat checks at `DLL_PROCESS_ATTACH` by patching multiple user-mode detection vectors. README tag: `[Emulate OW2 AC]`. (source: wiki/sources/descriptions/gmh5225__OW2-wardenrekter.md)

**Bypass surface:** overwrites `KiUserExceptionDispatcher` with a `RET` (`0xC3`) to neutralize Warden's **VEH-based INT3 hook monitoring**; NOPs `DbgBreakPoint` / `DbgUserBreakPoint` integrity checks; zeroes `PEB.BeingDebugged` and `NtGlobalFlag` to hide debugger presence; stubs `GetTickCount64` against timing checks; patches `NtQuerySystemInformation` to block system-information queries. Also sets hardware debug register **DR0** via `SetThreadContext` to demonstrate debug-register manipulation against Warden hardware-breakpoint detection. (source: wiki/sources/descriptions/gmh5225__OW2-wardenrekter.md)

Useful for game security researchers studying Warden bypass techniques—VEH hook removal, PEB spoofing, API patching, and hardware-breakpoint evasion—in Overwatch 2. Contrasts with feature cheats such as [[overwatch-2-cheat-aimbot-esp]] and stack-spoof samples such as [[overwatch-1-cheat-source]]; complements WoW-era Warden research such as [[x14-08-coverstory-blizzard]] and Overwatch client RE tooling such as [[overwatch-iat-fixer]].

## Links

- Repo: https://github.com/gmh5225/OW2-wardenrekter

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overwatch-2-cheat-aimbot-esp]] · [[overwatch-1-cheat-source]] · [[overwatch-iat-fixer]] · [[ow-outlines]] · [[meowsense]] · [[x14-08-coverstory-blizzard]] · [[custom-veh]]
