---
title: Foxo
kind: entity
topics: [game-hacking, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/miaoyu2233__Foxo.md
updated: 2026-11-26
confidence: high
---

# Foxo

**Foxo** (miaoyu2233/Foxo) is a Windows **zero-injection, external OCR overlay translator** for PC game UIs. It captures on-screen text, streams machine translation (Chinese by default), and draws translated text above the original interface in a separate transparent window **without modifying the game process**—keeping the stack in the localization / accessibility lane rather than in-guest cheat tooling. (source: wiki/sources/descriptions/miaoyu2233__Foxo.md)

## Architecture

- **Python** + **PySide6** UI; frame capture via **DXGI** or **mss**
- Hybrid **OCR**: DirectML-accelerated Japan **PP-OCRv4**, **WinRT**, or CPU **RapidOCR**
- **OpenAI-compatible** APIs for streaming machine translation
- Click-through transparent overlay; **`SetWindowDisplayAffinity`** so the translation HWND can be excluded from some screen-capture loops (see [[anti-screenshot-capture]])
- Configurable game terminology packs with fuzzy matching; **SQLite** translation cache (source: wiki/sources/descriptions/miaoyu2233__Foxo.md)

## Anti-cheat posture

Targets players and localizers of Japanese and other foreign-language titles who need low-latency UI translation while staying **non-invasive** relative to kernel anti-cheat stacks that flag injection, memory access, and render hooking—contrasted with in-process trainers, Present hooks, and RPM cheat stacks. (source: wiki/sources/descriptions/miaoyu2233__Foxo.md)

## Links

- Repo: https://github.com/miaoyu2233/Foxo

## Related

[[tft-ocr-bot]] · [[ferret]] · [[llm-game-automation-mcp]] · [[iris-overlay]] · [[anti-screenshot-capture]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]