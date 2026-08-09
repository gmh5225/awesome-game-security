---
title: BEDaisy.sys report bypass
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__bedaisy-bypass.md
updated: 2026-08-09
confidence: medium
---

# BEDaisy.sys report bypass

Offensive research sample (gmh5225) targeting BattlEye **`BEDaisy.sys`** kernel report delivery: suppresses outbound detection reports to the BE service while still allowing inbound response traffic. Useful for game-security researchers and reverse engineers studying BE's kernel-to-service report channel without triggering server-side ban telemetry. Cheat / explore anticheat system:be lane. (source: wiki/sources/descriptions/gmh5225__bedaisy-bypass.md)

Complements report-path disruption via hooked pool allocators in [[blindeye]] and APC instrumentation RE via [[goodeye]]—this sample focuses specifically on blocking BEDaisy report transmission rather than allocation drops or callback observation.

## Links

- Repo: https://github.com/gmh5225/bedaisy-bypass

## Related

[[battleye]] · [[blindeye]] · [[goodeye]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
