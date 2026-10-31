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
  - wiki/sources/descriptions/gamboozino__ngbrecomp.md
  - wiki/sources/descriptions/Coz-0__smo-recomp.md
  - wiki/sources/descriptions/raulzrrs__letsgo-recomp.md
  - wiki/sources/descriptions/MaryNCRT__Ultimate-Mortal-Kombat-3-iOS-Decompiled.md
  - wiki/sources/descriptions/nefariousjosiah__WWE-SVR2009-RECOMP.md
  - wiki/sources/descriptions/formix__sre-re.md
  - wiki/sources/descriptions/Manya3084__SF33RDSXBRecompo.md
  - wiki/sources/descriptions/everettjf__copyapp.md
  - wiki/sources/descriptions/Jstar269__nakagawa-recomp.md
  - wiki/sources/descriptions/danielalves96__gow-pc-port.md
  - wiki/sources/descriptions/KamiKitsune420__bgt-decomp-tools.md
updated: 2026-10-31
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

Static recompilation projects such as [[jsrf-recomp]] (OG Xbox XBE→native macOS ARM64 via xboxrecomp) pair translated C output with an extensive diagnostics harness that validates behavior against reference emulator traces—illustrating how static translation claims should be corroborated with runtime or trace-aligned evidence before treating recompiled builds as faithful. (source: wiki/sources/descriptions/andeecollard__jsrf-recomp.md) [[ngbrecomp]] (gamboozino; *Ninja Gaiden Black* XBE→native Linux/Windows/macOS; xboxrecomp lift plus custom kernel/audio/input/D3D→Vulkan runtime—not full-system emulation) shows the same lift-vs-HLE boundary when the goal is a playable native port with user-supplied disc assets rather than trace harnesses alone. (source: wiki/sources/descriptions/gamboozino__ngbrecomp.md) [[sf33rdsxbrecompo]] (Manya3084; *Street Fighter III: 3rd Strike*; **decompiled** OG Xbox game logic on x86-64 Linux/Windows via the 3s-decomp-ogxb pipeline—not an xboxrecomp XBE lift; C platform services, NV2A-style Vulkan/OpenGL draws, OpenAL XACT cues, SQLite saves, plus shader/stub generators and XBE/XDVDFS/disc readers; BYO disc) illustrates the decomp-to-native boundary: decompilation supplies structure, but fidelity claims still require labeling which draw, audio, and save paths match retail vs remain stubbed. (source: wiki/sources/descriptions/Manya3084__SF33RDSXBRecompo.md) [[saturnkit]] (vs-sr-dev; Python SH-2 analysis + static recomp to C++ with a C++20 Saturn hardware runtime for native PC ports) splits the same static/runtime boundary across analysis tooling and an embedded per-title port submodule model. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md) Xbox 360 XenonRecomp ports such as [[dead-rising-2-case-zero-xenon-recomp]] (wivi514; Case Zero XBLA; XenonRecomp + XenosRecomp; kernel high-level emulation with **honest-failure stubs**; jump-table recovery + recompilation-pitfall documentation) and [[mcla-pc]] (Midnight Club: LA; XenonRecomp + Xenos→DXIL replay) show how partially implemented kernel/GPU runtime services must be labeled explicitly when static PPC translation outruns host emulation coverage. (source: wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md) [[motorstorm-mv-recomp]] (robbe1912; PS3 *MotorStorm: Monument Valley* WIP; static PPU/SPU translation via ps3recomp instead of full Cell emulation; **source-coverage auditing** with retail binaries and lift output kept local) illustrates the same uncertainty labeling for incomplete native ports aimed at preservation RE rather than finished gameplay. (source: wiki/sources/descriptions/robbe1912__motorstorm-mv-recomp.md)

BBC Micro preservation rebuilds such as [[pipeline-disasm]] (mattgodbolt; annotated 6502 + BBC BASIC reassembly; baron toolchain; Python/Node disc compare; jsbeeb headless runs) treat **byte-identical disc and flux images** plus symbol dumps and execution traces as the baseline that every reassembly step must match—static disassembly claims are not accepted without that retail-aligned output check. (source: wiki/sources/descriptions/mattgodbolt__pipeline-disasm.md) [[frogman]] (same author; unreleased flip-screen platformer) adds **multi-stage VIA-timer XOR loaders** where static images stay opaque until decrypted stages are captured from jsbeeb memory dumps—another static-vs-runtime split for classic copy protection. (source: wiki/sources/descriptions/mattgodbolt__frogman.md)

16-bit DOS preservation RE such as [[sre-re]] (formix; *Solar Realms Elite* 0.994b Borland C++ 3.0 BBS door binary; Ghidra including headless export; **VROOMM overlay flattening** for static study; Python disassembly/string/call annotation; encrypted `.II` save decoders) transcribes turn-by-turn rules from decompiled logic but treats a **DOSBox workflow** that re-runs formulas against the retail executable as the gate before accepting recovered specs—static Ghidra output alone is not sufficient for game-rule claims. (source: wiki/sources/descriptions/formix__sre-re.md)

Windows PE32 relink harnesses such as xshxdex98/[[openmcm2]] (*Motocross Madness 2*; fixed-base MSVC 6.0 image; Ghidra export + assembly/link verification) keep **retail sections byte-for-byte** while selectively replacing routines with ported C that must match retail behavior; optional DirectDraw tracing compares renderer calls against the original path. (source: wiki/sources/descriptions/xshxdex98__OpenMCM2.md)

BGT/NVGT blind-audio-game toolkits such as [[bgt-decomp-tools]] (KamiKitsune420; Python) chain **PE overlay** extraction through **AES-256-CBC** and **LZ77** before AngelScript disassembly/lift—engine readers use **trial decryption** and **self-verifying format checks** so static pack recovery is not accepted until decrypted layouts parse cleanly; optional **UPX** runtime unpack and Ghidra headless extend opcode tables when shipped binaries add packers. (source: wiki/sources/descriptions/KamiKitsune420__bgt-decomp-tools.md)

Win32 PE32 static recompilation such as [[nfsu2recomp]] (TalhaMudo; *Need for Speed: Underground 2* x86→ARM64 macOS; ahead-of-time lift to C plus Win32/D3D9 runtime translation) separates **static discovery** (PE relocation recovery, recursive function discovery, indirect-call dispatch tables) from **runtime fidelity** claims about HLE shortcuts (e.g. D3DX effect framework)—label which API paths are fully lifted vs emulated before treating the native build as a reference port. (source: wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md)

Win32 PE32 x86-32 static recompilation to Android ARM64 such as [[sc2-android-recomp]] (elkir0; StarCraft II reference target; per-function differential testing against Unicorn as a lift oracle; offline D3D9 SM2/3→SPIR-V plus Bionic/Vulkan porting helpers; users supply lifted artifacts from legitimate installs) requires the same split—label which graphics, audio, and Win32 runtime paths are translated vs stubbed before treating the ARM64 build as a fidelity reference. (source: wiki/sources/descriptions/elkir0__sc2-android-recomp.md)

Switch AArch64 static recompilation to native Windows x64 such as [[smo-recomp]] (Coz-0; *Super Mario Odyssey* 1.4.1; Python AOT lifter→C with Clang build; Unicorn per-function difftest as lift oracle; custom host runtime for Switch system libraries, file I/O, audio, SDL3 input, and NVN-style graphics on Vulkan with Maxwell→SPIR-V shader translation; users supply decrypted dumps—no bundled assets) illustrates the same boundary between lifted guest code and reimplemented platform services when studying commercial porting without a CPU interpreter or JIT. (source: wiki/sources/descriptions/Coz-0__smo-recomp.md)

[[letsgo-recomp]] (raulzrrs; *Pokémon Let's Go* Switch 1.0.0 on LAS Recomp; AArch64→x86-64 lift with Horizon system HLE, NVN→Vulkan, Python/Zig one-time per-dump codegen; FSR upscaling, mod hooks, memory watch, profiling, and RenderDoc integration) extends that Switch static-recomp cluster—label which NVN/audio paths are fully reimplemented vs developer-instrumented before treating the Windows build as a renderer reference. (source: wiki/sources/descriptions/raulzrrs__letsgo-recomp.md)

PSP MIPS static recompilation to native Windows such as [[nakagawa-recomp]] (Jstar269; sal063 fork lineage; EBOOT→C lift with MIPS guest runtime and VFPU support tables; Vulkan + SDL3 launcher/player; Python codegen, pipeline tests, cosimulation against a reference interpreter, decomp.me export, optional real-PSP verification; BYO disc) applies the same static/runtime split on a handheld MIPS+VFPU target—separate lifted guest code from reimplemented PSP services and GPU paths before citing gameplay or preservation claims. (source: wiki/sources/descriptions/Jstar269__nakagawa-recomp.md)

PS2 R5900 static recompilation such as [[gow-pc-port]] (danielalves96; *God of War* SCUS-97399; Rust MIPS recompiler + ELF/R5900 tooling with **parity checks** against reference output; C++ IOP/runtime and VU1/texture hooks; OpenGL host; ISO installer helpers—label which EE/IOP/GS paths are fully reimplemented vs developer-instrumented before treating the native build as a fidelity reference beside verified decomp ports like [[ps2-port-engine]]; BYO disc) extends the same lift-vs-HLE boundary on Emotion Engine hardware. (source: wiki/sources/descriptions/danielalves96__gow-pc-port.md)

[[ultimate-mortal-kombat-3-ios-decompiled]] (MaryNCRT; iOS armv7 Mach-O clean-room Ghidra lift to verified C with armrecomp/differential oracle tests and Win32/SDL2 desktop hosts on OpenGL/Vulkan/D3D12) illustrates mobile fighting-game preservation where lift fidelity is argued via per-function differential checks rather than Switch-style NVN HLE—separate LIME engine/format recovery from GPU backend choice before citing gameplay logic. (source: wiki/sources/descriptions/MaryNCRT__Ultimate-Mortal-Kombat-3-iOS-Decompiled.md)

[[copyapp]] (everettjf; Python CLI + agent workflow on USB-attached **iOS/macOS** targets) chains device collection (UI/accessibility trees, sandbox, optional Frida traces; FairPlay-related decrypt on jailbroken paths) with optional Ghidra/Hopper/ARM64 static follow-on through **verifiable evidence cases** and playbooks—label which observations came from standard capture vs jailbroken/runtime lanes before treating rebuilt flows as behaviorally equivalent to the original app. (source: wiki/sources/descriptions/everettjf__copyapp.md)

ReXGlue-based Xbox 360 static ports such as [[wwe-svr2009-recomp]] (nefariousjosiah; *WWE SmackDown vs. Raw 2009*; ReXGlue PPC→x86-64 + XenosRecomp ahead-of-time shader conversion + native re:Blue/plume renderer on D3D12 or Vulkan; optional D3D call census and shader dumping for GPU translation RE; BYO disc image) pair lifted guest binaries with explicitly reimplemented graphics/runtime services—label which shader and API paths are translated vs instrumented before treating the native build as a renderer reference beside [[nhl-legacy-remaster]]. (source: wiki/sources/descriptions/nefariousjosiah__WWE-SVR2009-RECOMP.md)

## Behavioral capability from TTD traces

Full-process **Time Travel Debugging (TTD)** recordings capture executed API calls and unpacked/runtime-generated code paths that static PE analysis may miss. [[ttd-capa-cpp]] replays `.run` traces through the TTD SDK, decodes Win32/native call arguments, and matches observed behavior against capa rules—including optional code-region scanning and capability timelines—so analysts can label **observed calls** vs static import/reachability claims. (source: wiki/sources/descriptions/HullaBrian__ttd-capa-cpp.md)

## Host execution traces vs live process observation

Game-server PC checks often combine **offline host artifacts** (Prefetch, Amcache, BAM, registry/browser traces, DNS cache, file hashes, anti-forensics tampering indicators) with optional **live** module/hook/thread/memory signature probes against a running title. [[custos]] (dybeky; read-only Electron desktop scanner; twenty-one offline artifact lanes plus optional admin Live Scan; integrity-hashed reports) illustrates separating persisted execution-trace evidence from in-session runtime observation—label which lane produced each finding before moderation or appeal decisions. (source: wiki/sources/descriptions/dybeky__custos.md)

## Related

[[binary-evidence]] · [[binary-diffing]] · [[dynamic-binary-instrumentation]] · [[jsrf-recomp]] · [[ngbrecomp]] · [[sf33rdsxbrecompo]] · [[nfsu2recomp]] · [[sc2-android-recomp]] · [[smo-recomp]] · [[letsgo-recomp]] · [[nakagawa-recomp]] · [[gow-pc-port]] · [[ultimate-mortal-kombat-3-ios-decompiled]] · [[copyapp]] · [[wwe-svr2009-recomp]] · [[nhl-legacy-remaster]] · [[saturnkit]] · [[motorstorm-mv-recomp]] · [[dead-rising-2-case-zero-xenon-recomp]] · [[mcla-pc]] · [[pipeline-disasm]] · [[frogman]] · [[sre-re]] · [[openmcm2]] · [[ttd-capa-cpp]] · [[custos]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[overviews/game-engine]]
