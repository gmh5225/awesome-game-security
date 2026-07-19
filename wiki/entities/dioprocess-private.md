---
title: DioProcess
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md
updated: 2026-07-19
confidence: medium
---

# DioProcess

Advanced Windows internals research framework (evasion, rootkits, hypervisors, SMM, bootkits). Ships as a Rust 2021 + Dioxus desktop app for real-time process, handle, module, and network monitoring, with a companion kernel driver and UEFI bootkit path aimed at DSE / [[patchguard]] (KPP) bypass research. (source: wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md)

Core research surface: live kernel event capture with SQLite persistence, plus security-research IOCTLs for process-protection and privilege-escalation experiments on Windows 10 22H2—useful in the Cheat / debugging lane for game-security and RE study. (source: wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md)

Adjacent host explorers such as [[systeminformer]] and [[openark]] focus on inspection GUIs; here the emphasis is a fuller UM+KM+UEFI research stack.

## Links

- Repo: https://github.com/un4ckn0wl3z/dioprocess-private

## Related

[[systeminformer]] · [[openark]] · [[patchguard]] · [[bootbypass]] · [[efitool]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
