# Graphics Resource Selection

Load this guide when choosing a resource for a rendering or capture claim. The
locations below match the local [README](../../../../README.md), checked on
2026-09-09. Use [repository navigation](../../overview/references/repository-navigation.md)
for local summaries, snapshots, casing, and current upstream verification.

## Select by Observation

| README location and representative | Select when | Contract and common confusion | Expected review output |
|---|---|---|---|
| `OpenGL > Guide`: [LearnOpenGL](https://github.com/JoeyDeVries/LearnOpenGL) | Choosing an owned teaching sample to isolate an API concept | Chapter samples explain rendering features; they do not specify every driver, compositor, or production application's behavior. Record sample revision, context/profile, dependencies, and driver. | Small baseline description, expected output, API assumptions, and observed divergence |
| `Game Testing`: [PresentMon](https://github.com/GameTechDev/PresentMon) | Reviewing frame pacing or CPU/GPU/display-duration and latency evidence on Windows | Upstream uses ETW event analysis and, in the service, additional hardware telemetry. Its per-frame metrics are not framebuffer images or proof of everything visible on a display. Bind metric definitions to the chosen component and version. | Metric and event-source inventory, tool/OS/driver versions, missing-data limits, and timing interpretation |
| `Game Testing`: [Tracy](https://github.com/wolfpld/tracy) | Correlating CPU/GPU work, allocations, or locks in an owned instrumented application | Profiling coverage depends on integration, enabled features, API, and build. A recorded zone or high timestamp resolution does not establish complete execution coverage or cross-machine clock accuracy. | Instrumentation and coverage map, capture/tool versions, CPU/GPU clock domains, and supported performance finding |
| `DirectX > Compatibility`: [D3D9On12](https://github.com/microsoft/D3D9On12) | Explaining a D3D9 application observed through a D3D12 backend | Microsoft's mapping layer translates D3D9 DDI work through the D3D12 translation layer. Record the active OS component/build; upstream source and privately built copies need not match the OS-shipped implementation. Do not collapse compatibility translation, emulation, and capture into one category. | Application API to active backend map, module provenance, component version, and observation-layer limits |

Role and capability sources are the linked upstream documents, reviewed on
2026-09-09. PresentMon and Tracy are listed under `Game Testing`; do not invent
their placement under `DirectX > Tools`. Hook or overlay examples elsewhere in
the README are a different resource family from diagnostic tooling.

## Apply the Boundary

State the required observation before selecting a tool: API contract, instrumented
work, presentation timing, compositor output, or captured pixels. Preserve the
metric definition and acquisition layer; do not convert an event timestamp into
an image observation or a profiler result into a protection verdict.

For inappropriate frame access or unauthorized rendering changes, first identify
the process/module, resource ownership, and access or load boundary required.
Review provenance, permissions, and trusted graphics configuration. Driver
changes, compatibility translation, legitimate overlays, disabled instrumentation,
or dropped events are alternative explanations to assess from existing evidence.

Return a path diagram, version/coverage matrix, measured result, benign controls,
and unresolved visibility. Consult the parent skill's platform/validation sources
for API misuse, and [time and replay evidence](../../game-server-security/references/time-ordering-and-replay.md)
when timing is compared across simulation, rendering, or machines.
