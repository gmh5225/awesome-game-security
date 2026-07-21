---
title: kptnhook
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/sum-catnip__kptnhook.md
updated: 2026-07-21
confidence: medium
---

# kptnhook

Windows kernel-mode driver that injects a DLL into **each process** and performs **system-wide function hooking**. Uses a Ring0 driver so targets are reachable from early boot processes (before the login screen), not only post-logon user sessions. Aimed at game-security researchers and reverse engineers studying offensive cheat / injection:windows techniques. (source: wiki/sources/descriptions/sum-catnip__kptnhook.md)

Related kernel APC injectors include [[injdrv]] (process-create notify → user APC → `LdrLoadDll`) and map + APC samples such as [[kinject]]. Contrasts with user-mode PE manual-map tools such as [[modexmap]] and injection-testing harnesses such as [[injectors]].

## Links

- Repo: https://github.com/sum-catnip/kptnhook

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[injdrv]] · [[kinject]] · [[modexmap]] · [[injectors]] · [[kernel-callbacks]]
