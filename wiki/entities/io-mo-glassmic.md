---
title: GlassMic (io.mo.glassmic)
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/lm060719__io.mo.glassmic.md
updated: 2026-11-14
confidence: medium
---

# GlassMic (io.mo.glassmic)

**GlassMic** is an open-source **virtual microphone** and **Android audio-pipeline testing** module for **rooted** phones running **LSPosed**. Kotlin **Compose** UI plus Java and C++ **native hooks** (shadowhook inline hooking with libxposed) intercept **AudioRecord**, **AAudio**, **OpenSL ES**, and related capture paths so target apps receive PCM from imported files, **TTS** output, or experimental live playback capture. An experimental root **AudioPolicy** backend can inject audio system-wide; floating controls and diagnostics support on-device experiments. Optional cloud TTS providers use **encrypted API keys** in config. (source: wiki/sources/descriptions/lm060719__io.mo.glassmic.md)

## Audience

Aimed at developers and researchers who need **controlled**, on-device tests of microphone routing, capture API compatibility, and hook visibility—not production anti-cheat or voice-identity bypass tooling. (source: wiki/sources/descriptions/lm060719__io.mo.glassmic.md)

## Posture

Sits in the **Cheat / Xposed** and **LSPosed module** lane beside scaffolds such as [[xposed-module-kit]] and [[lsposed-universal-template]], and opposite mobile AC stacks that fingerprint microphone behavior—use for **pipeline RE**, not live-service evasion.

## Links

- Repo: https://github.com/lm060719/io.mo.glassmic

## Related

[[xposed-module-kit]] · [[lsposed-universal-template]] · [[lspfrida]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]