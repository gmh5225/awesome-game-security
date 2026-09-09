# Mobile Repository Resource Selection

Read this when choosing resources for an Android/iOS package, device-build question, or authorized mobile-network observation. Locate the exact category labels below in the local [README](../../../../README.md); retain the README spelling `IOS` when searching.

Local index and linked primary documentation reviewed: **2026-09-09**. Select against the actual app build, platform, ABI, signing context and device policy; a category placement does not establish tool compatibility or trust.

| Review question | Exact README location and representative source | Selection boundary and useful evidence |
|---|---|---|
| What does an Android package declare or contain? | `Cheat` → `Android File Explorer`: [Apktool](https://github.com/iBotPeaches/Apktool) and [JADX](https://github.com/skylot/jadx) | Select resource/manifest inspection and DEX reconstruction as different views. [Apktool documentation](https://apktool.org/) describes resource decoding; JADX explicitly warns that decompilation can be incomplete. Preserve original package/hash, split/build context, manifest findings and reconstruction errors. Java-like output is not original source or coverage of native code. |
| Which kernel source is relevant to this device? | `Cheat` → `Android Kernel Source`: [AOSP kernel build documentation](https://source.android.com/docs/setup/build/building-kernels), with Android kernel manifest/common repositories in the same category | Select the branch and vendor context that correspond to the observed image. AOSP documents GKI separately from vendor modules and version-dependent build tooling. Deliver device/OEM, Android and kernel build identity, branch/configuration and unresolved vendor differences; a generic common-kernel checkout does not prove the deployed binary. |
| Which app connections are observable on an owned test device? | `Cheat` → `Android Network Explorer`: [PCAPdroid](https://github.com/emanuele-f/PCAPdroid) | Its non-root capture uses a local VPN mechanism. Select connection metadata and retained packet evidence appropriate to the question; record capture mode, time window, app association and gaps. Successful capture does not by itself establish visibility into encrypted application contents or server-side authorization. |
| What packaging/signing assumptions does an iOS artifact make? | `Cheat` → `IOS App Packaging`: [ios_packager](https://github.com/addrianyy/ios_packager) | Use as a packaging/signing reference, not proof of App Store review or present OS compatibility; its brief README provides no comprehensive current-platform support matrix. Compare the artifact's team/bundle identity and signing context with [Apple's code-signing model](https://support.apple.com/guide/security/app-code-signing-process-sec7c917bf14/web). Preserve entitlements/provisioning evidence and distinguish development from distribution artifacts. |

## Avoid Misrouting

- `Android Key Attestation` is not a substitute for the official integrity/attestation contracts in the parent skill. Keep local root/emulator signals, cryptographic verification and server authorization separate; demonstration projects cannot establish current platform-wide behavior.
- `Frida`, kernel-explorer and jailbreak-related categories contain tools with different privileges and observation effects. For defensive analysis, record the prerequisites and instrumentation footprint; do not turn a listing into a stealth ranking or an unmodified-device finding.
- Route native/IL2CPP semantic reconstruction to [reverse-engineering](../../reverse-engineering/SKILL.md) or [game-engine](../../game-engine/SKILL.md), purchases/account rules to [game-server-security](../../game-server-security/SKILL.md), and release/plugin trust to [game-supply-chain-security](../../game-supply-chain-security/SKILL.md).

## Deliver a Review Record

Include the exact README locator, upstream revision/date and why the resource fits the artifact. Deliver package and signer provenance, device/build/ABI context, each trust boundary's required privilege, the observed evidence and its collection limits. Separate source-derived expectations from runtime observations and server-verified results; retain benign/debug-build comparisons and unanswered questions.

Use the shared [repository navigation](../../overview/references/repository-navigation.md) for local discovery layers, filename case, missing snapshots and currentness. Generated wiki or description text cannot independently verify a tool's capabilities or a device's integrity.
