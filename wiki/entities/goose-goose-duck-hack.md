---
title: goose-goose-duck-hack
kind: entity
topics: [game-hacking, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Goose_Goose_Duck_Hack.md
updated: 2026-08-12
confidence: medium
---

# goose-goose-duck-hack

**Internal** cheat for **Goose Goose Duck** built on **Unity IL2CPP** runtime manipulation with an **ImGui** overlay. Ships dumped Unity **Assembly-CSharp** DLLs and **Anti-Cheat Toolkit (ACTk)** bypasses to implement ESP, role reveal, and other gameplay modifications. (source: wiki/sources/descriptions/gmh5225__Goose_Goose_Duck_Hack.md)

Useful for studying social-deduction Unity titles where hidden role state is client-side and client-side integrity plugins (ACTk) are the primary defense layer—not kernel anti-cheat. Complements [[rust-rustinternal]] and [[taskbarhero-bot]] for comparing in-process IL2CPP hooking vs external ACTk bypass patterns on Unity builds.

## Links

- Repo: https://github.com/gmh5225/Goose_Goose_Duck_Hack

## Related

[[il2cpp]] · [[rust-rustinternal]] · [[taskbarhero-bot]] · [[imgui]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
