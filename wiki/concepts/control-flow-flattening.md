---
title: Control Flow Flattening
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/guheng-re__unflat.md
  - wiki/sources/descriptions/es3n1n__obfuscator.md
  - wiki/sources/descriptions/dronavallipranav__rust-obfuscator.md
  - wiki/sources/descriptions/cdong1012__ollvm-unflattener.md
  - wiki/sources/descriptions/JbvrgtonYT__ollvm-unflattener.md
  - wiki/sources/descriptions/R7flex__dll-ollvm.md
  - wiki/sources/descriptions/RolfRolles__HexRaysDeob.md
  - wiki/sources/descriptions/PAGalaxyLab__ghidra_scripts.md
  - wiki/sources/descriptions/tomhamidi97-arch__frida-vmp-bypass.md
  - wiki/sources/descriptions/IIIImmmyyy__AntiOllvm.md
  - wiki/sources/descriptions/ElvisBlue__emotet-deobfuscator.md
  - wiki/sources/descriptions/seifreed__xrefgen.md
updated: 2026-08-25
confidence: high
---

# Control Flow Flattening

**CFF** (control-flow flattening) reroutes many basic blocks through a central **dispatcher loop** with a state variable, destroying natural if/else and loop structure in static decompilers. OLLVM-style CFF is common in game clients, AC modules, and LLVM pass-plugin protectors ([[kagura]], [[the-poor-mans-obfuscator]], [[dll-ollvm]] — LLVM 18 IR plugin with insn sub / bogus CFG / CFF / ctor-trim for manual-map DLL injection hardening; R7flex; source: wiki/sources/descriptions/R7flex__dll-ollvm.md), [[obscura]]). Source-level Rust CFF via proc macros such as [[rust-obfuscator]] (`labyrinth_macros`; automatic project-wide insertion) complements IR and binary flattening. Post-compile PE obfuscators such as [[obfuscator]] and [[alcatraz]] apply CFF passes at the binary level without source. Variants include nested dispatchers and encrypted state variables. (source: wiki/sources/skills/reverse-engineering.md) (source: wiki/sources/descriptions/es3n1n__obfuscator.md) (source: wiki/sources/descriptions/dronavallipranav__rust-obfuscator.md)

## Recovery approaches

1. **Symbolic / simulated execution** — identify dispatcher, recover real edges ([[idadeflat]] with angr; [[ollvm-unflattener]] with Miasm — BFS call following, deobfuscated binary output for Win/Linux x86/x64; JbvrgtonYT fork adds graph visualization and bundled sample binaries for CFF experiments). **Arm64 fake-runtime simulation** via [[anti-ollvm]] (C# core; dispatcher pattern ID + if-else CFG rebuild; Python IDA CFG extract + Keystone codegen; IIIImmmyyy). (source: wiki/sources/descriptions/cdong1012__ollvm-unflattener.md) (source: wiki/sources/descriptions/JbvrgtonYT__ollvm-unflattener.md) (source: wiki/sources/descriptions/IIIImmmyyy__AntiOllvm.md)
2. **Decompiler-time deflattening** — Hex-Rays microcode passes at lift time ([[d810-ng]]; [[hex-rays-deob]] — pattern-based expression simplify + dispatcher-driven CFF unflatten; RolfRolles; source: wiki/sources/descriptions/RolfRolles__HexRaysDeob.md); Emotet-specific CFF recovery via [[emotet-deobfuscator]] (Python IDA plugin; dispatcher register/status identification; flattened branch rewrite; ElvisBlue; source: wiki/sources/descriptions/ElvisBlue__emotet-deobfuscator.md).
3. **External OBPO backends** — closed-core simplification with open IDA client ([[obpo-plugin]]).
4. **Python unflattener plugins** — extensible Fix OLLVM unflatten hooks ([[unflat]]; plugin development focus). (source: wiki/sources/descriptions/guheng-re__unflat.md) Ghidra in-process OLLVM CFF deobfuscation via [[pagalaxylab-ghidra-scripts]] (Python Ghidra scripts; PAGalaxyLab; source: wiki/sources/descriptions/PAGalaxyLab__ghidra_scripts.md).
5. **Heuristic region detection** — loop/dominator analysis and BB complexity scoring ([[obfuscation-detection]]) before manual work; [[xrefgen]] (Python IDA; data-flow taint + call-graph analysis; flags CFF and opaque predicates while recovering indirect control-flow xrefs; XRefer-compatible export; seifreed; source: wiki/sources/descriptions/seifreed__xrefgen.md).
6. **Trace-based recovery** — runtime traces from [[dynamic-binary-instrumentation]] resolve indirect branches under covered executions; completeness needs additional path exploration.
7. **Boundary-hook monitoring** — when stacked VMP+OLLVM on Android resists static deflattening, [[frida-vmp-bypass]] hooks libc/JNI/Java API exits and logs caller addresses inside the protected library to reconstruct security-sensitive call chains without lifting flattened bytecode. (source: wiki/sources/descriptions/tomhamidi97-arch__frida-vmp-bypass.md)

CFF often co-occurs with [[mixed-boolean-arithmetic]] and opaque predicates — simplify MBA blocks after CFG recovery for readable pseudocode.

## Related

[[anti-ollvm]] · [[frida-vmp-bypass]] · [[idadeflat]] · [[ollvm-unflattener]] · [[pagalaxylab-ghidra-scripts]] · [[d810-ng]] · [[hex-rays-deob]] · [[emotet-deobfuscator]] · [[obpo-plugin]] · [[unflat]] · [[obfuscator]] · [[rust-obfuscator]] · [[alcatraz]] · [[obfuscation-detection]] · [[xrefgen]] · [[obfuscation-analysis]] · [[mixed-boolean-arithmetic]] · [[dynamic-binary-instrumentation]] · [[overviews/reverse-engineering]]
