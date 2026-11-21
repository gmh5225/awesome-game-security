---
title: outlast-trials-cheat
kind: entity
topics: [anti-cheat, game-hacking, game-engine, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/AIN-sch__outlast-trials-cheat.md
updated: 2026-11-21
confidence: medium
---

# outlast-trials-cheat

**outlast-trials-cheat** (AIN-sch) documents static and dynamic analysis of *The Outlast Trials* on UE **4.27**: a generated Unreal **C++ SDK** with offset and UObject metadata dumps (JSON mappings, GObject listings, PE-level notes for the shipping Windows client). It reverse engineers the **Easy Anti-Cheat EOS** stack—the kernel **minifilter** driver and the game’s **eight delayed-import anti-cheat entry points**—and records a tested **injection workflow** that hooks those APIs before resuming the suspended game process. Artifacts are automated dumper output (headers, function stubs) aimed at game security researchers, anti-cheat analysts, and reverse engineers who need reproducible UE4 internals and EAC client behavior on this title. (source: wiki/sources/descriptions/AIN-sch__outlast-trials-cheat.md)

## Links

- Repo: https://github.com/AIN-sch/outlast-trials-cheat

## Related

[[easy-anti-cheat]] · [[unreal-object-model]] · [[dumper-7]] · [[fortnite-ac-reversal]] · [[all-about-eac]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]