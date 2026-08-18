---
title: UniStory
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ppodds__UniStory.md
updated: 2026-08-18
confidence: medium
---

# UniStory

**UniStory** (ppodds) is a **Unity-based MapleStory client reimplementation** (WIP) targeting **TMS v245**. Written in C#, it loads official MapleStory **WZ asset archives** and renders maps, characters, and related game content in a modern engine. It relies on **WzComparerR2.WzLib** to parse KMS/TMS-format WZ data and implements MapleStory-style map layers, foothold physics, portals, sprite animations, and BGM playback from extracted assets. Unity 2D rendering, NAudio audio decoding, and LZ4-compressed WZ support feed a modular loader for Character, Map, Mob, Npc, Skill, and other standard WZ categories. No server component yet. (source: wiki/sources/descriptions/ppodds__UniStory.md)

Useful for developers building private servers, studying MapleStory client mechanics, or reverse engineering and analyzing game assets from WZ files—not live official-client anti-cheat bypass.

Complements WZ tooling such as [[wzcomparerr2]] (extractor/viewer), other C# client emulators such as [[maplenecrocer]] (GM client / WZ parsing), and private-server stacks such as [[mnwvs196]] and [[maplestory-v113-server-eimulator]].

## Links

- Repo: https://github.com/ppodds/UniStory (README tag: Unity MapleStory emulator (WIP))

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[wzcomparerr2]] · [[maplenecrocer]] · [[maplestory-packer-modpacker]] · [[mnwvs196]] · [[maplestory-heavenclient]]
