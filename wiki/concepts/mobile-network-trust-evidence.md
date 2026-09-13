---
title: Mobile Network Trust Evidence
kind: concept
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/skills/mobile-security.md
updated: 2026-09-13
confidence: high
---

# Mobile Network Trust Evidence

Discipline for interpreting mobile game traffic, TLS, and certificate-pinning evidence: record the **networking stack, build variant, and observation point** before treating a proxy capture or Frida hook as proof of release-build trust behavior. Pair with [[mobile-trust-boundaries]] for server-authorization questions and [[research-rigor]] when README bypass scripts are generalized. (source: wiki/sources/skills/mobile-security.md)

## Baseline before interpretation

| Dimension | Why it matters |
|-----------|----------------|
| Networking stack | OkHttp, Conscrypt, Cronet, Flutter, React Native, or custom/native TLS change hook targets |
| Target SDK and build variant | Android Network Security Configuration defaults and debuggable flags differ by variant |
| Manifest-linked NSC | Domain policies, debug overrides, and cleartext rules are packaged artifacts |
| Observation point | mitmproxy, Charles, Frida Java hook, or native intercept each cover different paths |
| iOS trust contract | ATS, pinning in native code, and NSPinnedDomains need separate evidence from Android |

A proxy record or decrypted capture only covers traffic **visible at that observation point**—it does not establish that all libraries or the release build share the same trust configuration. (source: wiki/sources/skills/mobile-security.md)

## Pinning and trust-manager evidence

For Android owned-app tests, inspect the actual stack rather than assuming a universal Java `TrustManager` hook:

- Documented default CA trust changes with target SDK; debug-only trust anchors apply when the application is debuggable.
- A successful **debug** capture cannot establish **release** pinning behavior or production trust anchors.
- Replacement trust managers are not a universal TLS analysis method—custom/native stacks and independent certificate checks require their own contracts and evidence.

Preserve the test configuration, validation result, and unobserved paths. Review authorized debug configuration and release checks without weakening production trust or publishing bypass recipes. (source: wiki/sources/skills/mobile-security.md)

## Capture vs backend decision

**Observed traffic** (HTTP log, WebSocket frame, decrypted body) is collection evidence. **Server authorization** (purchase validation, session binding, rate limits) requires backend policy and corroboration—do not infer entitlement or anti-cheat scope from a single mitm session alone. Route purchase and entitlement questions to game-server-security; route client-side billing hooks such as [[freedom]] under [[mobile-anti-cheat]] IAP lanes.

## Related

[[mobile-trust-boundaries]] · [[mobile-anti-cheat]] · [[frida]] · [[ssl-bypass]] · [[frida-mobile-kit]] · [[android-proxy-mcp]] · [[research-rigor]] · [[overviews/mobile-security]]
