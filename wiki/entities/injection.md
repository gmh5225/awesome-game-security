---
title: injection
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__injection.md
updated: 2026-08-10
confidence: medium
---

# injection

Windows **injection testing** collection (README: Injection Testing) from gmh5225. Implements a broad set of alternative injection vectors for anti-cheat engineers and defensive security researchers stress-testing detection coverage — not a single production cheat stack. (source: wiki/sources/descriptions/gmh5225__injection.md)

Representative technique families include Conhost ExtraBytes, PROPagate, service control handler abuse, Print Spooler / ALPC paths, KernelCallbackTable manipulation, named PoCs (WordWarping, Hyphentension, AutoCourgette, Streamception, Oleum, ListPlanting, Treepoline), Windows Notification Facility, Windows Sockets Helper Functions, MPR DLL and shell notifications, DNS Client API, Breaking BaDDEr, tooltip/common-controls abuse, and KnownDlls cache poisoning. (source: wiki/sources/descriptions/gmh5225__injection.md)

Complements broader catalogs such as [[windows-process-injection]] and [[awesome-injection]], harnesses such as [[injectors]], focused SetWindowsHookExW PoCs such as [[setwindowshookex-injector]], and focused Rust injectors such as [[rust-dll-crab]].

## Links

- Repo: https://github.com/gmh5225/injection

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[awesome-injection]] · [[injectors]] · [[setwindowshookex-injector]] · [[rust-dll-crab]]
