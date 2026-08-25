---
title: TF2BD Database
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Garou3299__tf2bd-database.md
updated: 2026-08-25
confidence: medium
---

# TF2BD Database

Community-curated **Team Fortress 2** player-intelligence database distributed as JSON lists and custom detection rules for the **TF2 Bot Detector (TF2BD)** client (surepy/tf2_bot_detector). Data follows PazerOP's **TF2BD v3 playerlist and rules schemas**, tagging Steam accounts with attributes such as **cheater**, **racist**, or **scammer** while recording last-seen metadata and supporting proof where available. (source: wiki/sources/descriptions/Garou3299__tf2bd-database.md)

## Data sets

- Main **player list** of cheaters and suspicious accounts
- Separate **scammer list**
- Custom **chat word-filter rules** that automatically mark racist behavior

## Usage

Import the JSON files into TF2BD or compatible forks to alert on known bad actors during gameplay. Contributors can submit new entries with video evidence via project discussions.

## Position in the TF2 security lane

Lightweight **client-side anti-cheat and moderation support** for TF2 players and server communities—complementary to server-side SourceMod plugins such as [[little-anti-cheat]] and [[nocheatz-3]], and orthogonal to offensive internal cheat research such as [[teamfortress2-internal]] and [[cunthook]].

## Links

- Repo: https://github.com/Garou3299/tf2bd-database
- Client: https://github.com/surepy/tf2_bot_detector

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[little-anti-cheat]] · [[nocheatz-3]] · [[teamfortress2-internal]] · [[cunthook]] · [[fedoraware]]
