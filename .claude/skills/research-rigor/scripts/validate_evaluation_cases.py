#!/usr/bin/env python3
"""Validate local evaluation metadata without running prompts or using a network."""

import argparse
import json
import re
import sys
from pathlib import Path


def validate(data, skills_root):
    errors = []
    if (not isinstance(data, dict)
            or type(data.get("schema_version")) is not int
            or data["schema_version"] != 1):
        return ["Expected an object with schema_version 1."]
    if not isinstance(data.get("suite_id"), str) or not data["suite_id"].strip():
        errors.append("suite_id must be a non-empty string.")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list."]

    known = {p.parent.name for p in skills_root.glob("*/SKILL.md")}
    if not known:
        errors.append("No skill entrypoints found under skills_root.")
    seen = set()
    positive_coverage = set()
    kinds = set()
    for index, case in enumerate(cases):
        label = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label}: expected an object.")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case_id):
            errors.append(f"{label}: invalid id.")
        elif case_id in seen:
            errors.append(f"{label}: duplicate id {case_id}.")
        else:
            seen.add(case_id)
            label = case_id

        kind = case.get("kind")
        if not isinstance(kind, str) or kind not in {"positive", "boundary", "negative"}:
            errors.append(f"{label}: invalid kind.")
        else:
            kinds.add(kind)
        prompt = case.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{label}: prompt must be a non-empty string.")
        for field in ("checks", "critical_errors"):
            values = case.get(field)
            if not isinstance(values, list) or not values or any(
                not isinstance(value, str) or not value.strip() for value in values
            ):
                errors.append(f"{label}: {field} must contain non-empty strings.")

        primary = case.get("primary_skills")
        if not isinstance(primary, list) or any(not isinstance(name, str) for name in primary):
            errors.append(f"{label}: primary_skills must be a list of folder names.")
            continue
        if len(primary) != len(set(primary)):
            errors.append(f"{label}: duplicate primary skill.")
        if kind == "negative" and primary:
            errors.append(f"{label}: negative cases must not select a security skill.")
        if kind in ("positive", "boundary") and not primary:
            errors.append(f"{label}: domain cases need an acceptable primary skill.")
        for name in primary:
            if name not in known:
                errors.append(f"{label}: unknown skill folder {name!r}.")
        if kind == "positive":
            positive_coverage.update(name for name in primary if name in known)

    missing = known - positive_coverage
    if missing:
        errors.append("Missing positive routing coverage: " + ", ".join(sorted(missing)))
    if kinds != {"positive", "boundary", "negative"}:
        errors.append("Include positive, boundary, and negative scenarios.")
    return errors


def main():
    script = Path(__file__).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-file", type=Path, default=script.parents[1] / "assets/evaluation-cases.json")
    parser.add_argument("--skills-root", type=Path, default=script.parents[2])
    args = parser.parse_args()
    try:
        data = json.loads(args.case_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Cannot read evaluation suite: {error}", file=sys.stderr)
        return 1
    errors = validate(data, args.skills_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    count = len(list(args.skills_root.glob("*/SKILL.md")))
    print(f"PASS: {len(data['cases'])} cases; positive routing coverage for {count} skill folders.")
    print("Metadata only: prompts were not executed and answer quality was not scored.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
