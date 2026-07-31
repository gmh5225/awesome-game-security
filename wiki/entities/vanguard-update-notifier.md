---
title: vanguard-update-notifier
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/luavmload__vanguard-update-notifier.md
updated: 2026-07-31
confidence: medium
---

# vanguard-update-notifier

Python Discord bot that watches [[vanguard]] anti-cheat releases and alerts a configured channel when the version or bundled file hashes change. Polls Riot's public clientconfig API for the current Vanguard version and setup URL, downloads the installer archive, and hashes extracted contents with py7zr and SHA-256—falling back to a raw `setup.exe` hash when extraction fails. Periodic checks run every two hours via discord.py and aiohttp; slash commands register or remove notification channels; state persists in a local JSON config. Aimed at game security researchers and communities who want timely Discord alerts about Vanguard updates rather than manual installer diffing. (source: wiki/sources/descriptions/luavmload__vanguard-update-notifier.md)

## Links

- Repo: https://github.com/luavmload/vanguard-update-notifier

## Related

[[vanguard]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
