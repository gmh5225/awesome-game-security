---
title: ETW Threat Intelligence
kind: concept
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md
  - wiki/sources/descriptions/preludeorg__ThreatIntelligenceConsumer.md
  - wiki/sources/descriptions/paranoidninja__EtwTi-Syscall-Hook.md
  - wiki/sources/descriptions/muturikaranja__disable-threat-tracing.md
  - wiki/sources/descriptions/zodiacon__EtwExplorer.md
  - wiki/sources/descriptions/jdu2600__EtwTi-FluctuationMonitor.md
  - wiki/sources/descriptions/jdu2600__Etw-SyscallMonitor.md
updated: 2026-08-03
confidence: high
---

# ETW Threat Intelligence

Event Tracing for Windows (ETW) provider/consumer architecture used by EDR and anti-cheat for kernel and user-mode telemetry. The **Microsoft-Windows-Threat-Intelligence** provider is the PPL-gated lane for detecting cross-process memory access to protected games and security software. (source: wiki/sources/skills/windows-kernel.md)

## Architecture

- **Providers** emit events (manifest-based, TraceLogging self-describing, or legacy MOF/WMI).
- **Consumers** subscribe in real time (ETW sessions) or from `.etl` log files.
- **Controllers** manage sessions (`xperf`, `tracelog`, `logman`).

Key kernel providers include process/thread lifecycle, file I/O, and audit-API call streams. Schema exploration tools such as [[etw-explorer]] help map manifest fields before writing detectors. (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md)

## Threat Intelligence provider

- Provider name: `Microsoft-Windows-Threat-Intelligence`
- Availability: Protected Process Light (PPL) and above
- Typical events: `NtReadVirtualMemory`, `NtWriteVirtualMemory`, `NtMapViewOfSection` targeting protected processes
- Defensive consumers: [[tietwagent]] (krabsetw/Yara; ELAM/PPL agent lane) (source: wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md)
- Research consumers without driver/PPL: [[threat-intelligence-consumer]] (Win11 24H2/25H2) (source: wiki/sources/descriptions/preludeorg__ThreatIntelligenceConsumer.md)
- Syscall-return instrumentation samples such as [[etwti-syscall-hook]] extend the same TI / Instrumentation Callback research surface. (source: wiki/sources/descriptions/paranoidninja__EtwTi-Syscall-Hook.md)
- User-mode EtwTi syscall monitors such as [[etw-syscall-monitor]] log SSNs, parameters, process/thread context, and stack traces in real time without kernel hooks or drivers — a syscall-behavioral detection reference for AC/EDR research. (source: wiki/sources/descriptions/jdu2600__Etw-SyscallMonitor.md)

## Common bypass patterns

Attackers with sufficient privilege may attempt to blind TI telemetry: (source: wiki/sources/skills/windows-kernel.md)

| Target | Effect |
|--------|--------|
| `EtwEventWrite` in `ntdll.dll` | User-mode ETW silencing |
| `nt!EtwpEventWriteFull` | Kernel-mode ETW silencing |
| `EtwThreatIntProvRegHandle` / registration list walks | Remove or redirect provider registration |
| `NtSetInformationThread(ThreadHideFromDebugger)` | Hide thread from some ETW consumers |

Stress-testing samples such as [[disable-threat-tracing]] sit on the disable/blind side of this lane. (source: wiki/sources/descriptions/muturikaranja__disable-threat-tracing.md)

## Defensive countermeasures

- **EPT-based protection:** hypervisor second-stage permissions can trap unauthorized writes to ETW globals and registration structures — guest kernel R/W alone cannot silently patch them when policy remains trustworthy. See [[hvci]] / hypervisor defense in [[overviews/windows-kernel]].
- **Registration tamper monitors:** real-time EtwTi callback registration fluctuation detectors such as [[etwti-fluctuation-monitor]] alert when provider registrations are removed or patched — the defensive counterpart to registration-walk bypasses. (source: wiki/sources/descriptions/jdu2600__EtwTi-FluctuationMonitor.md)
- **Cross-checks:** combine TI ETW with [[kernel-callbacks]], handle stripping, and [[kernel-pool-scanning]] for layered detection.

## Related

[[kernel-callbacks]] · [[hvci]] · [[etw-explorer]] · [[etw-watcher]] · [[etwti-fluctuation-monitor]] · [[etw-syscall-monitor]] · [[tietwagent]] · [[threat-intelligence-consumer]] · [[etwti-syscall-hook]] · [[disable-threat-tracing]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
