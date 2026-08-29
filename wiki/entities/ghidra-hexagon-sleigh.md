---
title: ghidra-hexagon-sleigh
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/CUB3D__ghidra-hexagon-sleigh.md
updated: 2026-08-29
confidence: medium
---

# ghidra-hexagon-sleigh

**ghidra-hexagon-sleigh** (CUB3D) is a **Ghidra processor module and extension** that implements the **Qualcomm Hexagon QDSP6** architecture in **SLEIGH** for disassembly and decompilation. It supports **Hexagon v81** instructions with **p-code** for most operations, **hardware loops**, **predicate handling**, and **System/Monitor** and **System/Guest** modes. The extension includes **Java analyzers**, a **QDB log viewer**, and **Python scripts** for Qualcomm-specific tasks such as **QMI handler discovery**, **QuRT task identification**, **RTTI annotation**, and **Q6Zip** or **DLPager decompression via emulation**. Built with SLEIGH, Java, Python, and Gradle, it targets reverse engineers analyzing **Qualcomm firmware and binaries** in game security and mobile security research. (source: wiki/sources/descriptions/CUB3D__ghidra-hexagon-sleigh.md)

Complements general-purpose Ghidra workflows such as [[ghidra]] and architecture-specific Ghidra plugins such as [[ghidra-nativeaot]] and [[ghidradboy]] when targets run on Qualcomm DSP or modem firmware rather than conventional ARM/x86 application processors.

## Links

- Repo: https://github.com/CUB3D/ghidra-hexagon-sleigh

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[ghidra]] · [[qualcomm-avb-exploit-poc]] · [[rax]] · [[research-rigor]]
