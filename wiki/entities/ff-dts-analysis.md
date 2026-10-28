---
title: ff-dts-analysis
kind: entity
topics: [anti-cheat, reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/Shrawan-13__ff-dts-analysis.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# ff-dts-analysis

**Defensive Il2CPP static-analysis pipeline** for the **Free Fire MAX** Android client (Shrawan-13). Python automation turns a supplied **XAPK** into focused IL2CPP intelligence on client-side combat mechanics—aim assist, hitboxes, recoil, ballistics, and related systems—so anti-cheat and game-security researchers can study which native/managed surfaces could explain a specific aim-related cheat pattern without manual RE alone. (source: wiki/sources/descriptions/Shrawan-13__ff-dts-analysis.md)

## Pipeline

1. Extract `libil2cpp.so` and `global-metadata.dat` from the XAPK.
2. Decrypt obfuscated metadata with a **single-byte XOR** key.
3. Run **Il2CppDumper** on the decrypted pair → `dump.cs`, JSON, and companion artifacts.
4. Companion scan pass over dumped C# / JSON for methods, string literals, and class excerpts tied to combat/aim systems.

Framed as **analysis and detection research**, not a bypass or cheat kit. Listed under **Anti Cheat** / **Analysis Framework** beside mobile AC RE samples such as [[ff-ace-anticheat-analysis]] and [[g-presto-anti-cheat-reverse-engineered]].

Complements Tencent ACE client RE on classic Free Fire ([[ff-ace-anticheat-analysis]]) with Unity IL2CPP metadata workflow on **Free Fire MAX**.

## Links

- Repo: https://github.com/Shrawan-13/ff-dts-analysis

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[il2cpp]] · [[il2cppdumper]] · [[ff-ace-anticheat-analysis]] · [[g-presto-anti-cheat-reverse-engineered]] · [[research-rigor]]
