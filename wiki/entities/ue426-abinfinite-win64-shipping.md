---
title: UE426 ABInfinite Win64 Shipping
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/cra0__UE426_ABInfinite-Win64-Shipping.md
updated: 2026-08-16
confidence: medium
---

# UE426 ABInfinite Win64 Shipping

**Arena Breakout Infinite UE4.26 SDK** (cra0; C/C++) centered on **SDK generation** — pre-generated Unreal Engine 4.26 class layouts and offsets for the ABInfinite `Win64-Shipping` client. Useful for game security researchers and reverse engineers studying offensive techniques in the cheat / game:arena breakout infinite lane, especially when building internal tools or validating UObject/property paths against a title-specific header kit. (source: wiki/sources/descriptions/cra0__UE426_ABInfinite-Win64-Shipping.md)

Sits in the title-specific Unreal SDK lane beside generic generators such as [[ue4genny]] and pre-built header kits such as [[ue-unreal-engine-sdk]], feeding the same [[unreal-object-model]] research surface for UE4.26 tactical-shooter client RE.

## Links

- Repo: https://github.com/cra0/UE426_ABInfinite-Win64-Shipping

## Related

[[ue4genny]] · [[ue-unreal-engine-sdk]] · [[unrealdumper-4-25]] · [[unreal-object-model]] · [[patternsleuth]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
