---
title: sgame-ace-analysis
kind: entity
topics: [anti-cheat, mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/SuKERY918__sgame-ace-analysis.md
updated: 2026-11-27
confidence: medium
---

# sgame-ace-analysis

Full reverse-engineering study of Tencent **ACE (Anti-Cheat Expert)** as shipped in a specific **Honor of Kings** (王者荣耀) Android build, centered on native libraries `libtersafe.so` and `libtprt.so`. (source: wiki/sources/descriptions/SuKERY918__sgame-ace-analysis.md)

## Architecture and behavior

Documented surfaces include:

- **Static architecture** — ELF layout and interaction between `libtersafe` and `libtprt`
- **Cloud-controlled rules** — remote operators and rule delivery
- **Reporting** — non-TLS TCP telemetry to `anticheatexpert` endpoints
- **Hot-loaded detection** — RSA-verified detection blob fetch and load
- **Fingerprinting** — `libqimei` and related identity/telemetry libraries
- **Cloud modules** — OBJ_VM–style remote rule modules (per README lane)

On-device arm64 tests record detection timing, local intercept dialogs, and debugger or hook-framework triggers.

## Tooling

- **Python** — ELF inspection, encrypted string-table recovery, call-graph and blob analysis
- **Frida** — on-device tracing of device identity and telemetry flows

Aimed at game-security researchers, anti-cheat analysts, and mobile reverse engineers who need an evidence-based map of a production mobile ACE stack—not cheat or bypass tooling.

Listed in the README under **Explore AntiCheat System:ACE** for Honor of Kings `libtersafe`/`libtprt` RE (cloud rules, naked-TCP reporting, OBJ_VM cloud modules, arm64 Frida validation).

Complements [[honor-of-kings-re-research]], [[ff-ace-anticheat-analysis]], [[dfm-android-unicorn]], [[pubgm1.6-deadgame]], and Windows suite notes in [[anticheatexpert]] on [[mobile-anti-cheat]].

## Links

- Repo: https://github.com/SuKERY918/sgame-ace-analysis

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[mobile-anti-cheat]] · [[frida]] · [[network-environment-evidence]] · [[honor-of-kings-re-research]] · [[research-rigor]]