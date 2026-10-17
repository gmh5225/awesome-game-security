---
title: Static–Runtime Evidence
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md
  - wiki/sources/descriptions/vs-sr-dev__saturnkit.md
  - wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md
  - wiki/sources/descriptions/robbe1912__motorstorm-mv-recomp.md
  - wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md
  - wiki/sources/descriptions/mattgodbolt__frogman.md
  - wiki/sources/descriptions/xshxdex98__OpenMCM2.md
  - wiki/sources/descriptions/dybeky__custos.md
  - wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md
  - wiki/sources/descriptions/elkir0__sc2-android-recomp.md
updated: 2026-10-17
confidence: high
---

# Static–Runtime Evidence

Discipline for separating **static inference** (disassembly, decompilation, diffing, symbolic reachability) from **runtime evidence** (breakpoints, traces, hooks, observed calls) and labeling **protection-induced uncertainty** before drawing security conclusions. Pair with [[binary-evidence]] for question classification and [[research-rigor]] when README tool claims are generalized. (source: wiki/sources/skills/reverse-engineering.md)

## Baseline before interpretation

| Dimension | Why it matters |
|-----------|----------------|
| Artifact hash and provenance | Same filename ≠ same build; diff and offset claims require matched inputs |
| Format and architecture | PE/ELF/Mach-O, bitness, and ABI change calling conventions and layout |
| Tool and analysis configuration | Disassembler version, scripts, and decompiler settings alter recovered structure |
| Environment | OS build, integrity level, debugger presence, and VM/sandbox state affect anti-analysis paths |
| Observed addresses | File offset, RVA, and runtime VA must stay distinct—including relocation assumptions |

Record these fields on every report. A static graph or decompiled function is not proof the path executes under the tested environment. (source: wiki/sources/skills/reverse-engineering.md)

## Static vs runtime findings

| Evidence kind | Typical sources | Limit to state |
|---------------|-------------------|----------------|
| Static structure | Imports, strings, CFG, decompiler output, diff matches | Reachable or present in image ≠ invoked or security-relevant at runtime |
| Runtime observation | Breakpoint hit, trace, hook callback, memory snapshot | Coverage may be partial; instrumentation can alter timing and behavior |
| Protection interaction | Packer stub, VM handler, anti-debug branch | Recovered logic may be incomplete; label uncertainty explicitly |

Decompiler output is a **reconstruction**—validate types, names, prototypes, and boundaries against instructions and ABI constraints before treating pseudocode as ground truth. (source: wiki/sources/skills/reverse-engineering.md)

## Protection-induced uncertainty

Packing, virtualization, control-flow obfuscation, and anti-analysis checks change what static and dynamic tools can observe:

- Unpack/devirt stages may leave handler gaps or synthetic control flow.
- Anti-debug and environment checks can gate code behind conditions not met in the lab.
- Timing, integrity scans, and self-modifying regions can invalidate naive trace interpretation.

State which protections were identified, which recovery steps were applied, and which paths remain unexecuted or unrecovered. Obfuscation or anti-analysis behavior alone does not establish maliciousness or bypass feasibility—pair with [[binary-evidence]] question tables and corroboration rules.

## Reference-trace validation

Static recompilation projects such as [[jsrf-recomp]] (OG Xbox XBE→native macOS ARM64 via xboxrecomp) pair translated C output with an extensive diagnostics harness that validates behavior against reference emulator traces—illustrating how static translation claims should be corroborated with runtime or trace-aligned evidence before treating recompiled builds as faithful. (source: wiki/sources/descriptions/andeecollard__jsrf-recomp.md) [[saturnkit]] (vs-sr-dev; Python SH-2 analysis + static recomp to C++ with a C++20 Saturn hardware runtime for native PC ports) splits the same static/runtime boundary across analysis tooling and an embedded per-title port submodule model. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md) Xbox 360 XenonRecomp ports such as [[dead-rising-2-case-zero-xenon-recomp]] (wivi514; Case Zero XBLA; XenonRecomp + XenosRecomp; kernel high-level emulation with **honest-failure stubs**; jump-table recovery + recompilation-pitfall documentation) and [[mcla-pc]] (Midnight Club: LA; XenonRecomp + Xenos→DXIL replay) show how partially implemented kernel/GPU runtime services must be labeled explicitly when static PPC translation outruns host emulation coverage. (source: wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md) [[motorstorm-mv-recomp]] (robbe1912; PS3 *MotorStorm: Monument Valley* WIP; static PPU/SPU translation via ps3recomp instead of full Cell emulation; **source-coverage auditing** with retail binaries and lift output kept local) illustrates the same uncertainty labeling for incomplete native ports aimed at preservation RE rather than finished gameplay. (source: wiki/sources/descriptions/robbe1912__motorstorm-mv-recomp.md)

BBC Micro preservation rebuilds such as [[pipeline-disasm]] (mattgodbolt; annotated 6502 + BBC BASIC reassembly; baron toolchain; Python/Node disc compare; jsbeeb headless runs) treat **byte-identical disc and flux images** plus symbol dumps and execution traces as the baseline that every reassembly step must match—static disassembly claims are not accepted without that retail-aligned output check. (source: wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md) [[frogman]] (same author; unreleased flip-screen platformer) adds **multi-stage VIA-timer XOR loaders** where static images stay opaque until decrypted stages are captured from jsbeeb memory dumps—another static-vs-runtime split for classic copy protection. (source: wiki/sources/descriptions/mattgodbolt__frogman.md)

Windows PE32 relink harnesses such as xshxdex98/[[openmcm2]] (*Motocross Madness 2*; fixed-base MSVC 6.0 image; Ghidra export + assembly/link verification) keep **retail sections byte-for-byte** while selectively replacing routines with ported C that must match retail behavior; optional DirectDraw tracing compares renderer calls against the original path. (source: wiki/sources/descriptions/xshxdex98__OpenMCM2.md)

Win32 PE32 static recompilation such as [[nfsu2recomp]] (TalhaMudo; *Need for Speed: Underground 2* x86→ARM64 macOS; ahead-of-time lift to C plus Win32/D3D9 runtime translation) separates **static discovery** (PE relocation recovery, recursive function discovery, indirect-call dispatch tables) from **runtime fidelity** claims about HLE shortcuts (e.g. D3DX effect framework)—label which API paths are fully lifted vs emulated before treating the native build as a reference port. (source: wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md)

Win32 PE32 x86-32 static recompilation to Android ARM64 such as [[sc2-android-recomp]] (elkir0; StarCraft II reference target; per-function differential testing against Unicorn as a lift oracle; offline D3D9 SM2/3→SPIR-V plus Bionic/Vulkan porting helpers; users supply lifted artifacts from legitimate installs) requires the same split—label which graphics, audio, and Win32 runtime paths are translated vs stubbed before treating the ARM64 build as a fidelity reference. (source: wiki/sources/descriptions/elkir0__sc2-android-recomp.md)

## Behavioral capability from TTD traces

Full-process **Time Travel Debugging (TTD)** recordings capture executed API calls and unpacked/runtime-generated code paths that static PE analysis may miss. [[ttd-capa-cpp]] replays `.run` traces through the TTD SDK, decodes Win32/native call arguments, and matches observed behavior against capa rules—including optional code-region scanning and capability timelines—so analysts can label **observed calls** vs static import/reachability claims. (source: wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md)

## Host execution traces vs live process observation

Game-server PC checks often combine **offline host artifacts** (Prefetch, Amcache, BAM, registry/browser traces, DNS cache, file hashes, anti-forensics tampering indicators) with optional **live** module/hook/thread/memory signature probes against a running title. [[custos]] (dybeky; read-only Electron desktop scanner; twenty-one offline artifact lanes plus optional admin Live Scan; integrity-hashed reports) illustrates separating persisted execution-trace evidence from in-session runtime observation—label which lane produced each finding before moderation or appeal decisions. (source: wiki/sources/descriptions/dybeky__custos.md)

## Related

[[binary-evidence]] · [[binary-diffing]] · [[dynamic-binary-instrumentation]] · [[jsrf-recomp]] · [[nfsu2recomp]] · [[sc2-android-recomp]] · [[saturnkit]] · [[motorstorm-mv-recomp]] · [[dead-rising-2-case-zero-xenon-recomp]] · [[mcla-pc]] · [[pipeline-disasm]] · [[frogman]] · [[openmcm2]] · [[ttd-capa-cpp]] · [[custos]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[overviews/game-engine]]
