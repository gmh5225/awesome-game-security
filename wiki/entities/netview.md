---
title: Netview
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/mubix__netview.md
updated: 2026-07-29
confidence: medium
---

# Netview

Windows Active Directory enumeration tool by mubix. With `-d` it uses the current domain or a specified domain to enumerate hosts — useful for mapping domain-attached endpoints during incident response or lab triage. Listed in the Anti Cheat → Information System & Forensics lane for anti-cheat engineers and defensive security researchers who need domain-wide host visibility. (source: wiki/sources/descriptions/mubix__netview.md)

## Usage notes

- `-d` — enumerate against the current domain or pass an explicit domain name.
- Complements live host triage collectors such as [[dfirtriage]] and offline NTFS forensics tooling ([[ntfstool]], [[usn]]) when building an enterprise cheat-investigation or IR picture.

## Links

- Repo: https://github.com/mubix/netview

## Related

[[dfirtriage]] · [[ntfstool]] · [[usn]] · [[searchex]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
