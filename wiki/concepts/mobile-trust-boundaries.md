---
title: Mobile Trust Boundaries
kind: concept
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/skills/mobile-security.md
updated: 2026-09-09
confidence: high
---

# Mobile Trust Boundaries

Android and iOS game security spans **independent trust surfaces** that fail separately. Repackaging, privileged instrumentation, local-data exposure, request replay, and client assertions affect different boundaries—state whether the scenario requires ordinary app access, a developer build, privileged runtime access, kernel control, or server access before drawing conclusions. (source: wiki/sources/skills/mobile-security.md)

## Baseline before analysis

Record before generalizing root, hook, emulator, or integrity signals:

| Dimension | Why it matters |
|-----------|----------------|
| Device / build / ABI | OEM, GKI kernel, signing, and policy vary by release |
| Package signer & entitlements | Debug vs release, sideload, enterprise profiles |
| Required privilege | App sandbox vs root/jailbreak vs kernel module vs server |
| Observation source & limits | Who collected the signal and what they could not see |

Apply [[research-rigor]]—mobile behavior is strongly version-, OEM-, entitlement-, signing-, kernel-, and policy-dependent. A root indicator is not proof of cheating; a valid integrity response does not validate arbitrary game logic.

## Boundary map

| Surface | Typical failure mode | Route elsewhere |
|---------|---------------------|-----------------|
| Package / signing | Repackaged APK/IPA, tampered assets accepted locally | [[overviews/mobile-security]] static lane; supply-chain review |
| Runtime / process | Hook/injection, memory tamper, local-data leak | [[frida]], [[zygisk]], [[mobile-anti-cheat]] |
| Platform / device | Root/jailbreak, emulator, SELinux state, attestation | Play Integrity / Key Attestation; [[keyattestation]] |
| Server authorization | Purchase spoof, entitlement bypass, replayed requests | game-server-security (authority, verified purchases) |
| Build / update provenance | Tampered update channel or third-party content | game-supply-chain-security |

Keep **local indicators**, **verified attestation**, **backend decisions**, and **sanctions** separate in written findings.

## Platform integrity specifics

- **SELinux** — mandatory access control applies to root processes too. Record enforcement state, domain, build, and relevant policy denials instead of assigning universal trust or stealth ratings to framework names. (source: wiki/sources/skills/mobile-security.md)
- **Play Integrity** — validate request details, identity, binding, and freshness on the backend before interpreting app/device/account verdicts. Research modules such as [[pif-config-generator]] and [[zamr]] catalog attestation-spoof configs for controlled testing—not proof that production backends accept them.
- **App Attest (iOS)** — requires server verification of attestations/assertions, including challenge and counter handling; keep development and production context separate.
- **Network trust configuration** — for owned-app transport tests, distinguish debug-only trust anchors from release configuration. Android Network Security Configuration defaults change with target SDK; a successful debug capture does not establish release-build trust or pinning behavior. Custom/native TLS stacks need their own contracts and evidence.

Include supported emulators, stock devices, developer builds, OS updates, and service/attestation errors as **controls**. Record unavailable evidence separately from a verified negative result.

## Privilege and instrumentation limits

KernelSU and APatch grant root through kernel components, but a root-enabled app does not execute all code in kernel mode—distinguish user-space credentials, privileged services, kernel components, and their interfaces. Do not infer universal stock-kernel compatibility, interchangeable module APIs, or detectability from a framework name alone.

For dynamic instrumentation, Frida injected/embedded/preloaded modes are **integration modes**, not universal stealth tiers. Bind reports to exact tool revision, target build, entry point, required privilege, and actual evidence source. See [[frida]] observation-limit table and [[mobile-anti-cheat]] detection-finding review.

## Evidence report fields

When documenting mobile security findings, include:

1. **Boundary crossed** — package, runtime, platform, or server
2. **Prerequisite** — device/build, privilege level, signing identity
3. **Artifact** — APK hash, attestation payload, trace, or local indicator
4. **Backend interpretation** — how server policy used (or ignored) the signal
5. **False-positive alternatives** — developer build, custom ROM, stale artifact, unavailable visibility
6. **Unresolved limits** — collection gaps and counterevidence retained

## Related

[[research-rigor]] · [[mobile-anti-cheat]] · [[frida]] · [[keyattestation]] · [[android-hardware-attestation-demo]] · [[detector-operations]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
