---
title: bad-query
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/forcequitOS__bad_query.md
updated: 2026-08-15
confidence: medium
---

# bad-query

Experimental Xcode proof of concept for iOS application sandbox escape on iOS 26.0–26.6.1 and iOS 27.0 beta 4. Can reach selected application, internal-daemon, plug-in, shared App Group, and—on iOS 27—system-container paths; App Group access on iOS 26 requires sacrificing an App Group. Author positions it as a developer PoC rather than a practical jailbreak; iOS 18 compatibility is untested. Intended for research into iOS sandbox boundaries and container isolation. (source: wiki/sources/descriptions/forcequitOS__bad_query.md)

Useful for mobile game-security study of iOS container isolation and sandbox-boundary research—alongside kernel r/w playgrounds such as [[darksword-kexploit-fun]] and WIP DarkSword kexploit [[lara]], userland chains such as [[lightsaber]], and jailbreak trees like [[dopamine2-roothide]].

## Links

- Repo: https://github.com/forcequitOS/bad_query

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[darksword-kexploit-fun]] · [[lara]] · [[lightsaber]] · [[dopamine2-roothide]]
