---
title: dirty-zero
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/jailbreakdotparty__dirtyZero.md
updated: 2026-09-05
confidence: medium
---

# dirty-zero

iOS XNU kernel exploit ([CVE-2025-24203](https://github.com/jailbreakdotparty/dirtyZero)) that targets a zero-day or recently patched XNU vulnerability to obtain arbitrary kernel read/write on modern iOS releases. Builds a reliable KRW primitive chainable with other jailbreak or post-exploit components for security research. (source: wiki/sources/descriptions/jailbreakdotparty__dirtyZero.md)

Useful for mobile game-security and reverse-engineering study of contemporary XNU kernel exploitation surfaces—complementary to DarkSword-family work such as [[lara]] (DirtyZero2 experiments) and lab-oriented [[xnu-1day-practice]], and to userland chains like [[lightsaber]]. Consumer jailed-device apps such as [[mdc0]] (34306; system UI customization via CVE-2025-24203-tagged exploit path) illustrate downstream application of the same kernel surface.

## Links

- Repo: https://github.com/jailbreakdotparty/dirtyZero

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[lara]] · [[xnu-1day-practice]] · [[lightsaber]] · [[mdc0]] · [[dopamine2-roothide]] · [[oob-entry]]
