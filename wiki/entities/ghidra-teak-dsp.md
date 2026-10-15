---
title: ghidra-teak-dsp
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/PSI-Rockin__ghidra-teak-dsp.md
updated: 2026-10-15
confidence: medium
---

# ghidra-teak-dsp

**ghidra-teak-dsp** (PSI-Rockin) is a work-in-progress **Ghidra extension** for the **CEVA XpertTeak DSP** in **Nintendo 3DS** and **DSi** systems. It defines the Teak architecture with **SLEIGH** language modules and **Java loader** code so Ghidra can **disassemble, analyze, and decompile** Teak firmware. Coverage is broad enough to fully disassemble images such as **3DS Home Menu** and **Sound App** firmware, and it ships a **CDC/DSP1 binary loader** for importing those binaries. Unimplemented context registers are surfaced with **p-code** operations where possible. The project targets reverse engineers studying **handheld console audio DSP firmware** and related embedded code. (source: wiki/sources/descriptions/PSI-Rockin__ghidra-teak-dsp.md)

Complements general [[ghidra]] workflows and architecture-specific Ghidra processor modules such as [[ghidra-hexagon-sleigh]] (Qualcomm Hexagon) when the target is Nintendo **Teak DSP** firmware rather than the ARM9/ARM11 application processors. Pairs with LLE 3DS emulation research via [[3beans]], which implements Teak DSP interpreters for full-system 3DS RE.

## Links

- Repo: https://github.com/PSI-Rockin/ghidra-teak-dsp

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[ghidra-hexagon-sleigh]] · [[3beans]] · [[ghidradboy]] · [[research-rigor]]
