---
title: dll-hot-reload
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ergrelet__dll-hot-reload.md
updated: 2026-08-15
confidence: medium
---

# dll-hot-reload

Small utility DLL that **loads and hot-reloads a target DLL when it is updated on disk**, avoiding a full unload/reinject cycle during development. Useful when developing and debugging injectable cheat or mod payloads in the Windows injection lane. Aimed at game security researchers and reverse engineers studying offensive techniques in cheat / injection:windows workflows. (source: wiki/sources/descriptions/ergrelet__dll-hot-reload.md)

Complements broader injection tradecraft catalogs such as [[windows-process-injection]] and injection-testing harnesses such as [[injectors]]; pairs with scripted in-process modding toolkits such as [[positron]] when iterating on injected DLL behavior.

## Links

- Repo: https://github.com/ergrelet/dll-hot-reload (README tag: [Hot Reload])

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[windows-process-injection]] · [[injectors]] · [[positron]] · [[awesome-injection]]
