#!/usr/bin/env python3
"""
Shared Cursor SDK agent runner for repo automation scripts.
"""

from __future__ import annotations

import os
import random
import sys
import time
from pathlib import Path
from typing import Any

try:
    from cursor_sdk import Agent, LocalAgentOptions, ModelParameterValue, ModelSelection
except ImportError:
    sys.exit(
        "ERROR: cursor-sdk is not installed.\n"
        "Install with: python3 -m pip install 'cursor-sdk>=1.0.26'"
    )

DEFAULT_MODEL = "composer-2.5-fast"

# Transient Cursor / upstream capacity errors — retry with backoff.
# CI logs show bare ``([resource_exhausted] Error)`` with no wiki edits.
_TRANSIENT_ERROR_MARKERS: tuple[str, ...] = (
    "resource_exhausted",
    "resource exhausted",
    "rate_limit",
    "rate limit",
    "ratelimit",
    "too many requests",
    "quota exceeded",
    "quota_exceeded",
    "429",
    "503",
    "502",
    "504",
    "unavailable",
    "temporarily unavailable",
    "deadline exceeded",
    "timed out",
    "timeout",
    "connection reset",
    "connection aborted",
    "connection refused",
    "econnreset",
    "econnrefused",
    "broken pipe",
    "server disconnected",
)


def get_api_key() -> str:
    """Return CURSOR_API_KEY or exit with a helpful message."""
    key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not key:
        sys.exit(
            "ERROR: CURSOR_API_KEY environment variable is not set.\n"
            "Obtain a key from https://cursor.com/settings"
        )
    return key


def resolve_model(model: str | None) -> ModelSelection | str:
    """Map model flag values to SDK ``ModelSelection``."""
    raw = (model or DEFAULT_MODEL).strip()
    if not raw:
        raw = DEFAULT_MODEL

    lowered = raw.lower()
    if lowered in {"auto", "default"}:
        return "auto"

    if lowered in {"composer-2.5-fast", "composer-2.5"}:
        return ModelSelection(
            id="composer-2.5",
            params=[ModelParameterValue(id="fast", value="true")],
        )

    # ``name-fast`` → base id + fast=true when the base exists in SDK catalog.
    if lowered.endswith("-fast"):
        base = raw[: -len("-fast")]
        return ModelSelection(
            id=base,
            params=[ModelParameterValue(id="fast", value="true")],
        )

    return raw


def _format_model(model: str | ModelSelection | None) -> str:
    if isinstance(model, ModelSelection):
        parts = [model.id]
        for param in model.params or ():
            parts.append(f"{param.id}={param.value}")
        return "+".join(parts)
    return str(model or DEFAULT_MODEL)


def is_transient_agent_error(message: str | None) -> bool:
    """True when the SDK/API error is likely capacity / rate-limit related."""
    text = (message or "").lower()
    if not text:
        return False
    return any(marker in text for marker in _TRANSIENT_ERROR_MARKERS)


def _max_attempts() -> int:
    raw = os.environ.get("CURSOR_SDK_MAX_ATTEMPTS", "4").strip()
    try:
        return max(1, int(raw))
    except ValueError:
        return 4


def _retry_backoff_seconds(attempt: int) -> float:
    """Exponential backoff with jitter. attempt is 1-based (first retry → 1)."""
    base_raw = os.environ.get("CURSOR_SDK_RETRY_BASE_SECONDS", "15").strip()
    try:
        base = max(1.0, float(base_raw))
    except ValueError:
        base = 15.0
    # 15, 30, 60, ... capped at 120s, plus small jitter.
    delay = min(120.0, base * (2 ** (attempt - 1)))
    return delay + random.uniform(0.0, min(5.0, delay * 0.1))


def _collect_run_output(run: Any) -> tuple[int, str, str | None]:
    """Drain run events, print assistant text live, return (code, text, error)."""
    chunks: list[str] = []
    err_msg: str | None = None

    for event in run.events():
        sdk_message = getattr(event, "sdk_message", None)
        if sdk_message is None:
            continue
        if getattr(sdk_message, "type", "") == "status":
            status = getattr(sdk_message, "status", "")
            message = getattr(sdk_message, "message", "") or ""
            if status == "ERROR" and message:
                err_msg = message
            continue
        if getattr(sdk_message, "type", "") != "assistant":
            continue
        content = getattr(getattr(sdk_message, "message", None), "content", ())
        for block in content:
            text = getattr(block, "text", "")
            if not text:
                continue
            print(text, end="", flush=True)
            chunks.append(text)

    result = run.wait()
    status = getattr(result, "status", "error")
    text = "".join(chunks) or (run.text() or "")
    if status != "finished":
        code = 1
        if not err_msg:
            err_msg = f"run status={status!r}"
    else:
        code = 0
    if text and not text.endswith("\n"):
        print()
    return code, text, err_msg


def run_agent(
    prompt: str,
    *,
    model: str | None = None,
    dry_run: bool = False,
    cwd: Path | str | None = None,
) -> int:
    """Run one local SDK agent prompt; return 0 on success."""
    code, _output = run_agent_with_output(
        prompt,
        model=model,
        dry_run=dry_run,
        cwd=cwd,
    )
    return code


def run_agent_with_output(
    prompt: str,
    *,
    model: str | None = None,
    dry_run: bool = False,
    cwd: Path | str | None = None,
) -> tuple[int, str]:
    """Run one local SDK agent prompt; return (exit_code, combined assistant text).

    Retries on transient ``resource_exhausted`` / rate-limit / timeout errors.
    Override attempts via ``CURSOR_SDK_MAX_ATTEMPTS`` (default 4) and base delay
    via ``CURSOR_SDK_RETRY_BASE_SECONDS`` (default 15).
    """
    workdir = Path(cwd or os.getcwd()).resolve()
    model_label = model or DEFAULT_MODEL
    model_sel = resolve_model(model_label)

    if dry_run:
        print("[DRY-RUN] would run cursor-sdk Agent (local):")
        print(f"  model={_format_model(model_sel)} cwd={workdir}")
        print("--- prompt preview ---")
        preview = prompt[:1200]
        print(preview)
        if len(prompt) > 1200:
            print(f"... ({len(prompt)} chars total)")
        print("---")
        return 0, ""

    api_key = get_api_key()
    attempts = _max_attempts()
    print(
        f"  $ cursor-sdk Agent local model={_format_model(model_sel)} cwd={workdir} ..."
    )
    started = time.time()
    last_err: str | None = None

    for attempt in range(1, attempts + 1):
        attempt_started = time.time()
        try:
            with Agent.create(
                model=model_sel,
                api_key=api_key,
                local=LocalAgentOptions(cwd=str(workdir)),
            ) as agent:
                run = agent.send(prompt)
                code, output, err_msg = _collect_run_output(run)
        except Exception as exc:
            elapsed = time.time() - attempt_started
            last_err = str(exc)
            print(f"  exit=1  elapsed={elapsed:.1f}s  error={exc}")
            if attempt < attempts and is_transient_agent_error(last_err):
                wait = _retry_backoff_seconds(attempt)
                print(
                    f"  transient SDK error — retry {attempt}/{attempts} "
                    f"in {wait:.1f}s ..."
                )
                time.sleep(wait)
                continue
            return 1, ""

        elapsed = time.time() - attempt_started
        if code != 0:
            detail = f"  ({err_msg})" if err_msg else ""
            print(f"  exit={code}  elapsed={elapsed:.1f}s{detail}")
            last_err = err_msg or f"exit={code}"
            if attempt < attempts and is_transient_agent_error(err_msg):
                wait = _retry_backoff_seconds(attempt)
                print(
                    f"  transient SDK error — retry {attempt}/{attempts} "
                    f"in {wait:.1f}s ..."
                )
                time.sleep(wait)
                continue
            return code, output

        total = time.time() - started
        if attempt > 1:
            print(f"  exit=0  elapsed={elapsed:.1f}s  (succeeded after {attempt} attempts, total={total:.1f}s)")
        else:
            print(f"  exit=0  elapsed={elapsed:.1f}s")
        return 0, output

    print(f"  exit=1  giving up after {attempts} attempts ({last_err})")
    return 1, ""
