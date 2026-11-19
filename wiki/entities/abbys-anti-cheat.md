---
title: ABBYS Anti-Cheat
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Vanshu160__ABBYS-Anti-Cheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-19
confidence: medium
---

# ABBYS Anti-Cheat

**ABBYS Anti-Cheat** (Vanshu160/ABBYS-Anti-Cheat) is an open-source, **consent-based** mobile integrity workflow: an administrator issues a short-lived PIN from a web dashboard, the player enters it in an Android client, and graded scan results return to staff for human review—not automatic bans. (source: wiki/sources/descriptions/Vanshu160__ABBYS-Anti-Cheat.md)

## Architecture

| Component | Role |
|-----------|------|
| **Android client** | Kotlin + Jetpack Compose; user-consented device scan and report upload |
| **Reporting server** | Node.js; deployable on Render; session tokens so PIN guessing alone does not expose report data |
| **Admin dashboard** | Issues one-time PINs; reviews submitted findings |

## Detection surface

| Layer | Checks |
|-------|--------|
| **Native C++** | Root and Magisk binaries, suspicious mount entries, Frida or LSPosed strings in process memory maps, attached debuggers |
| **Kotlin scanners** | Installed packages, storage paths, SAF-accessible folders, Minecraft-oriented cheat indicators |

Findings use **HIGH**, **WARN**, and **INFO** tiers so operators can weight strong signals separately from name-only matches or benign conditions such as sideloaded apps or ADB. (source: wiki/sources/descriptions/Vanshu160__ABBYS-Anti-Cheat.md)

## Positioning

Lightweight **indicator-based mobile screening** for game operators and community moderators—not kernel-level enforcement. Workflow lane beside consent-gated PC checks such as [[hapiscanner]] and static APK triage such as [[mobsentry]]; complementary to RASP SDKs like [[free-rasp-android]] when admins want operator-controlled PIN sessions instead of always-on client RASP.

## Links

- Repo: https://github.com/Vanshu160/ABBYS-Anti-Cheat

## Related

[[hapiscanner]] · [[mobsentry]] · [[free-rasp-android]] · [[mobile-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]]