---
title: Pillager
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/qwqdanchun__Pillager.md
updated: 2026-07-25
confidence: medium
---

# Pillager

Go-based Windows post-exploitation credential harvester: exports and decrypts saved browser passwords, cookies, bookmarks, and history (Chrome / Firefox / Edge), Wi-Fi profiles, chat-application data, and other locally stored credentials into a single static binary for red-team / authorized pentest collection. (source: wiki/sources/descriptions/qwqdanchun__Pillager.md)

README lane: exporting and decrypting useful data from a target host. Complements live DFIR triage such as [[dfirtriage]] (broader host snapshot) and LSA dump forensics such as [[kvcforensic]] (LSASS secrets) when studying what attackers collect after compromise.

## Links

- Repo: https://github.com/qwqdanchun/Pillager

## Related

[[dfirtriage]] · [[kvcforensic]] · [[minidump]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
