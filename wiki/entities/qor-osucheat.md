---
title: qor-osucheat
kind: entity
topics: [game-hacking]
sources:
  - wiki/sources/descriptions/SymphonyPrime__qor-osucheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-11
confidence: medium
---

# qor-osucheat

Windows **external** osu! aim-assist (SymphonyPrime; Python; cheat / game:osu `[External]`). Runs **alongside** the proprietary client **without process injection**, driving cursor and taps through OS-level input only. (source: wiki/sources/descriptions/SymphonyPrime__qor-osucheat.md)

## Architecture

- **Input** — `ctypes` Windows API: relative/absolute cursor movement, `SendInput` keyboard/mouse; optional low-level mouse hook for high-frequency tablet pens.
- **Live state** — song position, beatmap path, and active mods from **tosu** or **gosumemory** over a local **WebSocket**.
- **Targeting** — hit-object timing and screen coordinates parsed from standard **`.osu` beatmap** files on disk (public format data, not in-process memory reads).
- **Features** — configurable aim correction, optional Relax-style automatic tap timing, **CustomTkinter** control panel, HTTPS manifest updates with **SHA-256** verification.

Useful for researchers studying rhythm-game cheating, external input automation, and how clients can be assisted using only OS events plus public beatmap metadata—alongside memory-oriented samples such as [[maniac]] and AC-analysis work such as [[osu-aac]].

## Links

- Repo: https://github.com/symphonyprime/qor-osucheat

## Related

[[osu]] · [[maniac]] · [[osu-aac]] · [[autohotkey-l]] · [[overviews/game-hacking]] · [[research-rigor]]
