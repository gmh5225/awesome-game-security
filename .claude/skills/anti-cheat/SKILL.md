---
name: anti-cheat-systems
description: Guide for modern game anti-cheat architecture, Windows kernel monitoring, and detection tradeoffs. Use this skill when analyzing EAC, BattlEye, Vanguard, FACEIT AC, kernel callbacks, handle protection, manual-map detection, boot-start drivers, BYOVD, DMA threats, or behavioral telemetry in game security research.
---

# Anti-Cheat Systems & Analysis

## Overview

This skill covers layered anti-cheat design across kernel drivers, privileged services, in-game components, and backend telemetry. It is most useful for mapping how modern anti-cheats monitor process handles, image loads, memory integrity, driver trust, virtualization abuse, DMA threats, and suspicious input behavior on Windows.

## README Coverage

- `Anti Cheat > Guide`
- `Anti Cheat > Stress Testing`
- `Anti Cheat > Driver Unit Test Framework`
- `Anti Cheat > Anti Debugging`
- `Anti Cheat > Page Protection`
- `Anti Cheat > Binary Packer`
- `Anti Cheat > CLR Protection`
- `Anti Cheat > Anti Disassembly`
- `Anti Cheat > Sample Unpacker`
- `Anti Cheat > Dump Fix`
- `Anti Cheat > Encrypt Variable`
- `Anti Cheat > Lazy Importer`
- `Anti Cheat > Anti-Cheat Programming`
- `Anti Cheat > Compile Time`
- `Anti Cheat > Shellcode Engine & Tricks`
- `Anti Cheat > Obfuscation Engine`
- `Anti Cheat > Screenshot`
- `Anti Cheat > Game Engine Protection:*`
- `Anti Cheat > Open Source Anti Cheat System`
- `Anti Cheat > Analysis Framework`
- `Anti Cheat > Detection:*`
- `Anti Cheat > Signature Scanning`
- `Anti Cheat > Information System & Forensics`
- `Anti Cheat > Dynamic Script`
- `Anti Cheat > Kernel Mode Winsock`
- `Anti Cheat > Fuzzer`
- `Anti Cheat > Windows Ring3 Callback`
- `Anti Cheat > Windows Ring0 Callback`
- `Anti Cheat > Winows User Dump Analysis`
- `Anti Cheat > Winows Kernel Dump Analysis`
- `Anti Cheat > Sign Tools`
- `Anti Cheat > Backup File / Backup Drivers`
- `Anti Cheat > Black Signature`
- `Windows Security Features`

## Major Anti-Cheat Systems

### Easy Anti-Cheat (EAC)
- Multi-component architecture with service, driver, and game-facing protections
- Process integrity verification and memory inspection
- Runtime driver loading with strong client-side enforcement
- Used by: Fortnite, Apex Legends, Rust

### BattlEye
- Kernel driver plus service and game module coordination
- Handle protection, process monitoring, and memory scanning
- Strong focus on injected code and runtime tampering visibility
- Used by: PUBG, Rainbow Six Siege, DayZ

### Vanguard (Riot Games)
- Boot-start kernel driver with early visibility into later-loaded drivers
- Boot-time initialization
- Driver allowlisting and aggressive system trust checks
- Used by: Valorant, League of Legends

### FACEIT AC
- Kernel-level competitive anti-cheat with strong process and driver monitoring
- Emphasis on platform integrity and low tolerance for hostile drivers
- Often discussed alongside Vanguard in kernel anti-cheat research

### Valve Anti-Cheat (VAC)
- User-mode detection
- Signature-based scanning
- Delayed ban waves
- Used by: CS2, Dota 2, TF2

### Other Systems
- **PunkBuster**: Legacy FPS anti-cheat
- **FairFight**: Server-side statistical analysis
- **nProtect GameGuard**: Korean anti-cheat solution
- **XIGNCODE3**: Mobile game protection
- **ACE (Tencent)**: Chinese market protection

## Detection Mechanisms

### Memory Detection
```
- Code section hashing and integrity verification
- Executable private memory and manual-map detection
- Injected module and anomalous image mapping detection
- Memory modification and stack provenance monitoring
```

### Process Detection
```
- Handle access stripping and protected-process enforcement
- Thread start address, APC, and context inspection
- Debug register and hidden-thread monitoring
- Stack trace and module-correlation analysis
```

### Kernel-Level Detection
```
- Driver verification, signature policy, and blocklist checks
- Callback registration and object access monitoring
- System call, dispatch table, and hook integrity checks
- PatchGuard, test-signing, and kernel trust state checks
- Kernel pool scanning (Segment Heap aware) for hidden drivers and shellcode
```

### Kernel Pool Scanning (Segment Heap Era)
```
Why Segment Heap matters for anti-cheat:
Cheat drivers allocate memory in NonPagedPool for shellcode, hook tables,
hidden modules. The Segment Heap (19H1+) changed pool internals:
headers are HeapKey XOR encoded, allocation paths are split (kLFH, VS,
Segment, Large), metadata is isolated. Anti-cheat pool scanners must
understand these mechanisms to scan accurately without false positives.

Detection targets:

1. BigPool / Large Allocation scanning:
   - Walk nt!PoolBigPageTable (nt!PoolTrackTable)
   - Find allocations without corresponding DRIVER_OBJECT or loaded module
   - Detect manually mapped drivers that allocate large pool chunks
   - Large allocations have no inline header; metadata is external

2. VS Allocator chunk scanning:
   - Traverse _SEGMENT_HEAP → VsContext → SubsegmentList
   - Decode _HEAP_VS_CHUNK_HEADER using HeapKey:
     real_sizes = encoded_header ^ chunk_address ^ HeapKey
   - Check decoded chunk for suspicious PoolTag, executable content,
     or allocation without matching driver
   - VS chunks carry both _HEAP_VS_CHUNK_HEADER (encoded) and
     _POOL_HEADER (PoolTag still present)

3. kLFH bucket scanning:
   - _SEGMENT_HEAP → LfhContext → Buckets[] → AffinitySlots → Subsegments
   - kLFH randomizes block placement (harder to predict adjacency)
   - FreeHint encoded with LfhKey
   - Allocation pattern anomalies in specific size buckets can indicate
     pool grooming by cheat drivers

4. Suspicious PoolTag detection:
   - Cheat drivers use custom or rare tags; maintain blacklist
   - Cross-reference tags against known-good tag database (pooltag.txt)
   - Tags present in pool but absent from any loaded module = suspicious

5. Executable memory in NonPagedPool:
   - Find chunks with X permission but no corresponding module
   - Scan decoded chunk content for known cheat signatures, ROP gadgets,
     specific syscall stub patterns

6. Segment Heap integrity checks:
   - Validate _SEGMENT_HEAP.Signature == 0xDDEEDDEE
   - Verify VS chunk header encoding consistency
   - Detect tampered heap metadata (indicates heap exploitation attempt)

Required knowledge for scanner:
- nt!RtlpHpHeapGlobals (HeapKey, LfhKey) — obtained via pattern scan
- nt!ExpPoolQuotaCookie — for ProcessBilled decoding
- Per-pool-type _SEGMENT_HEAP instance addresses (nt!PoolVector)
- Allocation path determination (size → kLFH/VS/Segment/Large)

Anti-cheat KDP integration:
- Store detection rule tables in Secure Pool (ExAllocatePool3 + KDP)
- Rules become VTL0-immutable — cheat drivers cannot modify
  detection signatures even with kernel R/W primitives
```

### Behavioral Analysis
```
- Raw input timing and pattern analysis
- Movement and aim anomaly detection
- Statistical improbability and ML-assisted scoring
- Telemetry collection and server-side review
- AI visual aimbot detection (input pattern + gameplay behavior)
```

### AI Visual Aimbot Detection
```
AI visual cheats (OBS capture + YOLO + hardware input) are the hardest
class to detect because they involve no memory access, no code injection,
no kernel driver on the gaming PC. Detection must move to behavioral
analysis and environmental signals.

Input Pattern Analysis:
- Mouse movement micro-signature: AI-generated trajectories have
  characteristic acceleration profiles distinct from human muscle control
  even with smoothing and jitter injection
- Engagement timing: AI reacts within a narrow, consistent latency band
  (capture → inference → output, typically 20-50 ms total) that lacks
  the variance of human reaction time distributions
- Sub-pixel precision: hardware input devices report integer deltas,
  but AI-calculated movements exhibit systematic rounding patterns
  that differ from natural hand movement
- Correction patterns: AI trajectories show characteristic overshoot-and-settle
  patterns at consistent magnitudes; human correction is more variable
- Target switching: AI switches between targets with machine-like
  priority ordering (closest-to-crosshair or highest-confidence);
  humans exhibit attention bias and tunnel vision

Gameplay Behavioral Signals:
- Anomalous K/D ratio combined with other statistical outliers
- "Snap" engagement pattern: rapid crosshair movement to target
  followed by immediate fire, repeated consistently
- FOV-limited engagement: AI only engages targets within a specific
  pixel radius (the configured FOV), creating an unnatural engagement
  boundary visible in replay analysis
- Consistent headshot angle distribution that doesn't match
  the player's ranked skill bracket
- Engagement rate: AI engages available targets at a higher percentage
  than human players who miss, ignore, or react slowly to some targets

Environmental Detection:
- OBS process detection: Game Capture mode injects a graphics hook DLL
  (obs-graphics-hook64.dll) into the game process; detectable via
  loaded module enumeration, though banning it risks false-positive
  on legitimate streamers
- Window Capture detection: DXGI Desktop Duplication creates detectable
  API state (IDXGIOutputDuplication usage patterns)
- Frame readback detection: unusual GPU-to-CPU copy patterns
  (ReadbackTexture / staging resource creation at frame rate)
- Known hardware input device USB VID/PID signatures
  (KMBox, certain Arduino/Teensy boards)
- USB device enumeration anomalies: input device appearing/changing
  mid-session
- Logitech driver version detection: known exploitable G HUB versions
- Interception driver (interception.sys) loaded = high-risk signal

Server-Side Statistical Analysis:
- Aim trajectory reconstruction from server-received input deltas
- Compare aim distribution against player population at same rank
- Detect systematic per-frame aim correction vectors
  (AI produces consistent delta sequences)
- Cross-session pattern analysis: AI users show unnaturally stable
  performance metrics across sessions (low variance in accuracy)
- Replay-based ML classifiers trained on confirmed AI aimbot cases

Anti-AI Countermeasures (Game Design):
- Visual disruption: flashbang/smoke effects that confuse CV models
- Character skin variety and camouflage that reduce YOLO confidence
- Dynamic UI elements overlapping character models
- Server-side aim validation: reject physically impossible aim transitions
- Randomized character proportions or outline disruption to break
  trained model assumptions
```

### Server-Side Replay Analysis for AI Aimbot Detection
```
Server-side detection operates on input telemetry data uploaded
from the client, independent of what runs on the gaming PC.
This is the strongest layer against zero-memory AI cheats.

Input Telemetry Collection:
- Record raw mouse delta (dx, dy) per tick at server tick rate
- Record timestamps of each input event (sub-millisecond precision)
- Record crosshair angle / view angle per tick
- Record fire events with corresponding view angle at fire time
- Record damage events with hit location (head/body/limb)
- Collect per-session: total engagement count, hit count,
  headshot count, K/D, average engagement distance

Replay-Based Trajectory Reconstruction:
- Reconstruct full crosshair trajectory from recorded input deltas
- Overlay trajectory onto 3D game state (player positions, obstacles)
- Identify "engagement windows": trajectory segments where crosshair
  moves toward and locks onto a target
- Measure per-engagement: time-to-target, overshoot magnitude,
  correction count, final hold time before fire

Statistical Features for AI Detection:
  (extracted from reconstructed trajectories)

Temporal features:
- Reaction time distribution: time from target visibility to
  first crosshair movement toward target
  → AI: narrow, consistent band (30-80 ms capture+inference+output)
  → Human: wide, right-skewed distribution (150-400 ms typical)
- Time-to-lock distribution: time from engagement start to
  crosshair on target
  → AI: consistent, speed-limited by smoothing algorithm
  → Human: highly variable, depends on initial angular distance

Spatial features:
- Trajectory curvature: AI Bézier curves have characteristic
  smooth, parametric curvature; human paths are more erratic
  with micro-corrections and random deviations
- Overshoot-correction ratio: AI smoothing algorithms produce
  predictable overshoot magnitudes; humans vary wildly
- End-point precision: AI consistently lands on bounding box
  center or specific offset; humans show scatter distribution
- Angular velocity profile: AI ramps up/down smoothly;
  humans have irregular acceleration spikes

Engagement pattern features:
- Target selection consistency: AI always picks closest-to-crosshair
  or highest-confidence target; humans show attention bias, tunnel
  vision, and suboptimal target priority
- FOV boundary effect: AI shows sharp engagement cutoff at
  configured pixel radius; humans have gradual falloff
- Engagement rate: percentage of visible targets engaged;
  AI engages more consistently than humans who miss, ignore,
  or react slowly to peripheral targets
- Multi-target switch pattern: AI switches with machine-like
  regularity; humans show grouping and hesitation
```

### ML Classifier for AI Aimbot Detection
```
Feature engineering and model architecture for detecting
AI-generated mouse input at scale.

Feature Vector (per engagement window):
  f1:  reaction_time_ms
  f2:  time_to_lock_ms
  f3:  initial_angular_distance_deg
  f4:  trajectory_curvature_mean
  f5:  trajectory_curvature_std
  f6:  overshoot_magnitude_px
  f7:  correction_count
  f8:  final_hold_time_ms
  f9:  angular_velocity_max_deg_per_sec
  f10: angular_velocity_std
  f11: micro_correction_frequency (small deltas < 2px per tick)
  f12: trajectory_straightness_ratio (distance / path_length)
  f13: dx_dy_correlation (Pearson correlation of delta components)
  f14: delta_magnitude_entropy (Shannon entropy of |delta| sequence)
  f15: fire_timing_relative_to_lock_ms

Session-level aggregate features:
  s1:  headshot_ratio
  s2:  hit_ratio
  s3:  reaction_time_cv (coefficient of variation across engagements)
  s4:  engagement_rate (targets engaged / targets visible)
  s5:  k/d_ratio
  s6:  fov_engagement_boundary_sharpness
  s7:  target_selection_optimality_score
  s8:  trajectory_curvature_consistency (inter-engagement variance)

Model architecture options:
- Gradient Boosted Trees (XGBoost/LightGBM):
  Best for tabular feature vectors, interpretable feature importance,
  fast inference on server. Preferred for production deployment.
- Random Forest: simpler, less prone to overfitting on small datasets
- 1D-CNN / LSTM on raw delta sequences:
  Operates on raw (dx, dy, dt) sequences instead of engineered features.
  Can capture patterns human engineers might miss.
  Higher compute cost; suitable for batch/offline analysis.
- Ensemble: combine tree-based (tabular features) + sequence model
  (raw deltas) for highest accuracy

Training data:
- Positive samples: confirmed AI aimbot users (manual review, honeypot,
  or controlled testing with known cheat software)
- Negative samples: legitimate high-skill players (important: include
  top-percentile players to avoid false-positives on skilled play)
- Hard negatives: players with aim-assist controllers (console),
  players using legitimate accessibility tools

Evaluation metrics:
- False Positive Rate (FPR): must be extremely low (< 0.01%)
  for production deployment — banning legitimate players is catastrophic
- True Positive Rate (TPR): secondary to FPR; 70-85% TPR is acceptable
  if FPR is near-zero
- Use session-level aggregation: flag a player only if multiple
  sessions show consistent AI patterns (reduces both FP and FN)

Deployment pipeline:
  Client → input telemetry upload (per tick) → server telemetry DB
  → batch feature extraction (per engagement window)
  → ML inference (per session)
  → risk score aggregation (per player, across sessions)
  → threshold → manual review queue or automated action

Adversarial robustness:
- Cheat developers tune smoothing parameters to evade specific features
- Defense: retrain model periodically on newly confirmed samples
- Use feature combinations rather than single-feature thresholds
- Ensemble across multiple sessions reduces evasion success
- Raw sequence models (CNN/LSTM) are harder to evade than
  hand-crafted feature thresholds because the evasion space
  is higher-dimensional
```

### Hardware Input Device Detection
```
Detecting KMBox and similar hardware input injectors at the
platform/driver level.

USB Enumeration Signals:
- Known VID/PID combinations for KMBox, Arduino Leonardo (2341:8036),
  Teensy (16C0:0486), generic CH340/CP2102 serial adapters
- USB device appearing/disappearing during game session
- Multiple HID mouse devices where only one physical mouse is expected
- USB device with HID mouse capability but no manufacturer string
  or generic "Arduino LLC" / "Teensyduino" manufacturer

USB HID Report Analysis:
- Hardware input devices generate genuine HID reports, but:
  - Report rate: KMBox/Arduino typically report at exactly the
    programmed rate (e.g., every 1ms or 8ms); real mice have
    polling rate jitter tied to USB microframe scheduling
  - Report timing: AI-injected movements arrive in bursts
    (idle → sudden burst of calculated deltas → idle),
    while human movement is continuous with natural pauses
  - Delta distribution: AI deltas cluster around computed values
    with optional noise; human deltas follow characteristic
    distributions per movement speed

Network Traffic Indicators (KMBox Net):
- KMBox Net uses UDP communication on the local network
- Packet pattern: consistent-size UDP packets at high frequency
  from a secondary device to the KMBox's IP
- If cheat PC is on the same network: detectable via
  network monitoring (firewall/router logs)

Driver-Level Detection:
- interception.sys: known driver signature, detectable via
  module enumeration and PiDDBCacheTable
- Logitech G HUB DLL injection: detect unexpected DLL loads
  into GHUB process, or specific exploitable GHUB versions
  via file version checking

Limitations:
- Pure hardware HID injection (KMBox, Arduino) is fundamentally
  indistinguishable from real mouse input at the HID protocol level
- Detection must rely on statistical input analysis rather than
  driver/device-level signatures
- Dual-machine setups with capture cards leave zero footprint
  on the gaming PC beyond the hardware input device
```

## Anti-Cheat Architecture

### User-Mode Components
- Process scanner
- Module verifier
- Overlay detector
- Screenshot capture

### Kernel-Mode Components
- Driver loader
- Memory protection
- System callback registration
- Hypervisor and driver trust detection
- VAD and executable memory inspection

### Hypervisor-Level Components
```
- EPT-based memory access monitoring
- Callback list write protection via EPT hooks
- ETW structure integrity enforcement
- AC driver code page protection (prevent patching)
- VMCALL interface for policy configuration from kernel driver
- VM exit handlers for EPT violations on protected regions
```

### Server-Side Components
- Statistical analysis
- Replay verification
- Report processing
- Ban management

## Research Techniques

### Static Analysis
1. Dump and analyze AC drivers
2. Reverse engineer detection routines
3. Identify signature patterns
4. Map callback registrations and trust boundaries

### Dynamic Analysis
1. Monitor system calls
2. Track driver communications
3. Inspect memory layout and module provenance
4. Debug with kernel or hypervisor tools

## Bypass Categories

### Memory Access
- Physical memory read/write
- DMA-based access
- Hypervisor memory virtualization
- Driver-based access

## DMA Cheat Detection Methodology

### PCIe-Layer Detection Pipeline
```
Detection targets inconsistencies between what a device claims to be
and how it actually behaves. Each technique targets a specific
firmware emulation tier or class of gap.

Configuration Integrity:
- VID/DID/SVID/SDID against known-real-silicon allowlist
- Capability-chain walk: DWord-aligned Next pointers, no overlaps, no cycles
- Signature-residue scanning: Xilinx 7-series default byte patterns,
  Device Capabilities field bits, reserved-field defaults
- Capability presence consistency: donor model must expose expected caps
- BAR mask verification: write 0xFFFFFFFF, compare size mask vs donor

BAR Memory Probing:
- Send Memory Read TLPs to BAR ranges, validate responses by donor class
- NIC BAR0: register layout (ring descriptors, interrupt mask, link status)
- NVMe BAR0: controller registers (CAP, VS, CC, CSTS, AQA, ASQ/ACQ)
- XHCI BAR0: capability registers (CAPLENGTH, HCSPARAMS, HCCPARAMS)
- stock pcileech zerowrite4k returns all-zeros; loopaddr echoes address

R/W Consistency:
- Toggle writable bits (Command BME, Device Control MPS/MRRS, MSI Enable)
- Walk W1C bits (Status, AER Status): write 1s, confirm clear semantics
- Walk reserved bits: write 1s, confirm read-back as 0
- Per-register writable masks must match donor model exactly

Link-State Validation:
- Negotiated Width/Speed vs claimed capabilities (Gen4 x8 claim
  but Gen2 x1 reality = one-read contradiction)
- DLL Active, Slot Clock Config consistency
- ASPM behavioral validation: L0 ↔ L1 transition patterns must
  match donor class; never leaving L0 when ASPM is claimed = anomalous

AER Baselining:
- Compare correctable-error rates against per-silicon baseline
- Implausibly clean logs (zero correctables when donor normally
  produces Bad TLP / Replay Timer Timeout) = anomalous
- UR/CA response distribution to probes of unimplemented offsets
```

### Completion Latency Fingerprinting
```
Real silicon: DRAM contention + internal arbiters → heavy-tailed
latency distributions. BRAM-backed emulators: fixed clock cycles
→ much lower variance.

Statistical methods:
- Kolmogorov–Smirnov test: compare empirical CDFs vs reference
- Hill estimator: tail index (real silicon has non-trivial tail)
- Anderson-Darling test: sensitive to tail differences

Tier-5 firmwares add LFSR-based jitter, but matching real
distribution shape (mean, variance, tail index, mode count)
requires modeling donor DRAM access patterns.
```

### MSI/MSI-X Behavioral Validation
```
- Device with MSI Enable + programmed Address/Data + attached driver
  should produce interrupts
- Zero interrupts when driver should exercise device = anomalous
- Implausibly uniform arrival times (60 Hz heartbeat) = timer-driven
- MSI-X probe: mask vector → induce condition → observe PBA bit →
  unmask → observe interrupt firing. Real silicon passes; spoofed rarely does.
```

### Cheat-Phase Access Pattern Recognition
```
Development phase: slow, broad scanning (MemProcFS signature search)
Execution phase: narrow, periodic reads (60–240 Hz) of small offset set

Execution phase statistical signature:
- High temporal periodicity
- Low address-space breadth
- Alignment to game-frame intervals
- Distinguishing features: Fano factor, autocorrelation at frame intervals,
  address-space coverage entropy

Honeypot regions effective when combined with IOMMU denial/fault logging,
hypervisor EPT traps, decoy IOVA mappings, or server-side behavioral traps.
```

### IOMMU-Layer Detection
```
Fault-Rate Monitoring:
- Per-device fault rate from IOMMU fault-recording / WHEA
- Legitimate devices with correct drivers rarely fault
- Sustained nonzero rate = direct evidence of out-of-domain access

Domain Assignment Audit:
- Flag devices on passthrough/identity domains under strict mode
- Flag unexpectedly large IOMMU groups (poor ACS topology)
- Verify multi-function devices sharing Domain ID legitimately

ACS Topology Verification:
- Walk bridge topology, verify Source Validation, Translation Blocking,
  P2P Request/Completion Redirect on every relevant bridge
- Bridges without ACS = isolation holes
```

### IOMMU Containment Primitives
```
Before ban verdict, containment protects the live match:

1. IOMMU domain sandbox: reprogram device domain to sandbox memory;
   cheat reads garbage data

2. Bus Master Enable clearance: toggle Command[2] to 0;
   effective for tier-0 through tier-3

3. Downstream Port Containment (DPC): if upstream port supports
   DPC Extended Capability (0x001D), trigger Contained state —
   all TLPs dropped, no firmware-side BME race

4. Anti-cheat-owned device domain: map only sandbox IOVAs
```

### External Trust Anchors
```
When local kernel/hypervisor trust fails, external anchors close the gap:

TPM Remote Attestation:
- Server sends nonce → client requests TPM2_Quote(AIK, PCR_selection, nonce)
- Verifier checks: AIK signature, certificate chain, EK binding,
  nonce freshness, PCR composite matches known-good policy
- Compromised kernel cannot retroactively alter extend-only PCRs

Measured Boot PCR Relevance:
- PCR[0]: UEFI firmware code
- PCR[7]: Secure Boot policy + DMA Protection Disabled event
- PCR[17]: DRTM/Secure Launch measurement

UEFI Pre-Boot DMA Integrity:
- Verify DMAR/IVRS protection indicators
- Cross-check BIOS version against known vulnerable CVE lists
- Verify PCR[7] DMA Protection Disabled event state
```

### Layered Detection Synthesis
```
No single signature is durable. Production pipeline layers:

1. Pre-game: IOMMU active, IR enabled, Secure Boot, VBS/HVCI,
   TPM provisioned, attestation validates, BIOS not vulnerable,
   ACS topology verified

2. Inventory: full 4 KB config dump per device, problem codes,
   SMBIOS slot cross-reference

3. Config integrity: per-donor reference database comparison

4. Behavioral sampling: Link Status, AER counters, interrupt rates,
   IOMMU fault rates, BAR content

5. Statistical analysis: latency distributions, interrupt distributions,
   ASPM transition rates

6. Cheat-phase: honeypot access, access pattern classifiers

Verdict requires multi-signal correlation — single signals can
false-positive; combinations rarely do. Three independent signals
push false-positive rates below practical threshold.
```

### Firmware Sophistication Tiers (Detection Mapping)
```
Tier 0 (Stock):        VID/DID blacklist catches immediately
Tier 1 (Bridge):       Signature residue, driverless device detection
Tier 2 (Shadow):       R/W consistency probing catches write drops
Tier 3 (Overlay RAM):  BAR probing + class-functional A/B testing
Tier 4 (BAR+MSI):      Interrupt distribution + BAR content baselining
Tier 5 (Behavioral):   Multi-session latency/ASPM/AER statistical analysis
Tier 6 (Private):      Requires external trust anchors (TPM + attestation)
```

### Forensic Evidence for DMA Cases
```
Capture on detection:
- Full 4 KB config dump + capability chain walk
- PCIe link state history (LTSSM, ASPM transitions)
- MSI/MSI-X arrival timeline
- AER correctable counts
- IOMMU fault log entries + domain assignments
- ACS bridge state
- Honeypot access records (EPT trap log)
- TPM PCR snapshot
- MCFG / DMAR / IVRS ACPI tables
- SMBIOS slot inventory + BIOS version
- Completion latency distribution histograms

Strongest evidence: hardware signal + behavioral signal + temporal correlation.
Three independent signals make false-positive appeals manageable.
```

### Code Execution
- Manual mapping
- Thread hijacking
- APC injection
- Kernel callbacks

### Detection Evasion
- Signature mutation
- Timing attack mitigation
- Stack spoofing
- Module hiding

## Security Features Interaction

### Windows Security
- Driver Signature Enforcement (DSE)
- PatchGuard/Kernel Patch Protection
- Hypervisor Code Integrity (HVCI)
- Secure Boot
- TPM-backed attestation considerations

### Virtualization Detection
- VT-x/AMD-V detection
- Hypervisor presence checks
- VM escape detection
- Timing-based detection

### Hypervisor-Based Defense for Anti-Cheat
```
Concept:
- Use hypervisor (EPT/SLAT) to enforce anti-cheat protections
  from a privilege level above the kernel
- Even if attacker achieves kernel R/W (BYOVD, exploit),
  hypervisor-level enforcement remains intact
- EPT hooks replace traditional kernel hooks:
  operate outside the guest OS, invisible to kernel-level rootkits

EPT Hook Protection Targets:
- Anti-cheat driver executable pages
  → Prevents attackers from patching AC driver code in memory
- Kernel callback lists (PsSetCreateProcessNotifyRoutine, ObRegisterCallbacks)
  → Write authorization moved to hypervisor; kernel-level callback removal denied
- ETW-related structures
  → Unauthorized writes trigger EPT violations, caught by hypervisor
- EPP/AC process memory
  → Protects security software from silent tampering

Hypervisor vs Kernel-Level Threats:
- Common kernel-level attack chain:
  1. Attacker uses BYOVD or kernel exploit for R/W primitives
  2. Patches callbacks to remove AC notifications
  3. Tampers with ETW to disable telemetry
  4. Modifies AC driver code to blind detection
- With hypervisor defense:
  1. Same kernel R/W primitives obtained
  2. Write to protected callback list → EPT violation → VM exit
  3. Hypervisor evaluates context and denies unauthorized modification
  4. AC callbacks and telemetry remain intact

Advantages:
- Higher privilege than kernel — cannot be disabled by kernel rootkits
- Transparent to guest: no kernel patches needed
- Effective even after full kernel compromise
- Complements existing kernel-mode detection (callbacks, signatures, scans)

Limitations:
- Requires hardware virtualization support (VT-x/AMD-V)
- Performance overhead from VM exits on protected region access
- Complexity: must handle nested virtualization (VMware, Hyper-V)
- DMA attacks bypass hypervisor memory protections (separate threat)
```

## Code Protection Techniques

### Page Protection
```
- Executable page guard pages and trap-based integrity monitoring
- NX bit enforcement and DEP policy
- PAGE_GUARD + single-step trap for code coverage without patching
- VirtualProtect monitoring to detect runtime permission changes
```

### Binary Packing & Encryption
```
- PE packers: UPX, Themida, VMProtect, Enigma, MPRESS
- CLR protection: .NET obfuscation (ConfuserEx, Dotfuscator, .NET Reactor)
- Encrypt Variable: runtime value encryption to frustrate memory scanners
- Lazy Importer: compile-time import hiding to avoid IAT-based detection
- Compile-time techniques: string encryption, constexpr obfuscation, COFF obfuscation
```

### Shellcode & Obfuscation
```
- Shellcode engines: position-independent code generation, syscall stubs
- Obfuscation engines: OLLVM-based, custom LLVM passes, MBA (Mixed Boolean-Arithmetic)
- Anti-disassembly: opaque predicates, junk code insertion, control flow flattening
```

## Heartbeat & Screenshot

### Heartbeat Mechanisms
```
- Periodic client-to-server health check packets
- Encrypted challenge-response with server nonce
- Timing-based integrity: detect suspended or debugged processes
- Failure modes: silent disconnect, delayed ban, immediate kick
```

### Screenshot Capture
```
- AC-initiated screen capture for manual or automated review
- BitBlt / PrintWindow / DXGI desktop duplication
- Anti-screenshot evasion: overlay hiding, DWM composition bypass
- Server-side ML classifiers for ESP/overlay detection in captured frames
```

## Telemetry Pipeline

### Client-Side Collection
```
- Module list enumeration and hash reporting
- Handle table snapshots for suspicious access patterns
- Stack trace sampling at periodic intervals
- Driver load events and callback registration state
- Hardware fingerprint (disk serial, NIC MAC, SMBIOS, GPU)
```

### Transport & Server-Side
```
- Encrypted telemetry channel (TLS + custom encryption layer)
- Server-side aggregation and anomaly scoring
- ML-based behavioral clustering for ban waves
- Replay system integration for suspicious session review
```

## Ethical Considerations

### Research Guidelines
- Focus on understanding, not exploitation
- Report vulnerabilities responsibly
- Respect Terms of Service implications
- Consider impact on gaming communities

### Legal Aspects
- DMCA considerations
- CFAA implications
- Regional regulations
- ToS enforcement

## Resources Organization

### Detection Research
```markdown
- Anti-cheat driver analysis
- Detection routine documentation
- Callback enumeration tools
```

### Bypass Research
```markdown
- Memory access techniques
- Injection methods
- Evasion strategies
```

### Tools
```markdown
- Custom debuggers
- Driver loaders
- Analysis frameworks
```

---

## Data Source

**Important**: This skill provides conceptual guidance and overview information. For detailed information use the following sources:

### 1. Project Overview & Resource Index

Fetch the main README for the full curated list of repositories, tools, and descriptions:

```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md
```

The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.

### 2. Repository Code Details (Archive)

For detailed repository information (file structure, source code, implementation details), the project maintains a local archive. If a repository has been archived, **always prefer fetching from the archive** over cloning or browsing GitHub directly.

**Archive URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/ufrisk/pcileech.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/000-aki-000/GameDebugMenu.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the archive URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name (no `.git` suffix).
3. Fetch the archive file — it contains a full code snapshot with file trees and source code generated by `code2prompt`.
4. If the fetch returns a 404, the repository has not been archived yet; fall back to the README or direct GitHub browsing.

### 3. Repository Descriptions

For a concise English summary of what a repository does, the project maintains auto-generated description files.

**Description URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/00christian00/UnityDecompiled/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/ufrisk/pcileech/description_en.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the description URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name.
3. Fetch the description file — it contains a short, human-readable summary of the repository's purpose and contents.
4. If the fetch returns a 404, the description has not been generated yet; fall back to the README entry or the archive.

**Priority order when answering questions about a specific repository:**
1. Description (quick summary) — fetch first for concise context
2. Archive (full code snapshot) — fetch when deeper implementation details are needed
3. README entry — fallback when neither description nor archive is available
