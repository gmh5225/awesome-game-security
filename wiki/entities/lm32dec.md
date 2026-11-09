---
title: lm32dec
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/ProximaV__lm32dec.md
updated: 2026-11-09
confidence: medium
---

# lm32dec

Python decompiler and lifter that recovers readable C from firmware and binaries targeting the 32-bit **LatticeMico32 (LM32)** RISC soft processor. Ships as a Hex-Rays-style interactive plugin for IDA Pro 8.x and 9.x and as a standalone headless tool that emits C without IDA. The pipeline covers big- and little-endian instruction decoding, custom IR lifting, control-flow structuring, LM32 EABI stack-frame and calling-convention recovery, SSA-style def-use analysis, and C generation with virtual locals, hardware CSR intrinsics, and switch jump-table recovery. Targets FPGA softcores, embedded firmware, QEMU LM32 images, and proprietary little-endian security coprocessors—including PlayStation Vita security-coprocessor firmware where LM32 must be understood at source level. (source: wiki/sources/descriptions/ProximaV__lm32dec.md)

Complements other embedded ISA decompilers in IDA such as [[mcore-decompiler]] (Motorola M·CORE) and IoT/firmware audit tooling such as [[firmeye]] when lifting obscure soft-core firmware to structured C beside [[embedded-hacking]] workflows.

## Links

- Repo: https://github.com/ProximaV/lm32dec (README: IDA Pro plugin and standalone LM32 decompiler/lifter)

## Related

[[overviews/reverse-engineering]] · [[mcore-decompiler]] · [[firmeye]] · [[embedded-hacking]] · [[list-of-ida-plugins]]
