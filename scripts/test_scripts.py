"""Unit tests for maintenance scripts under scripts/."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import description_paths  # noqa: E402


def _load_script(name: str):
    path = SCRIPTS_DIR / f"{name}.py"
    mod_name = name.replace("-", "_")
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


check_and_fix_links = _load_script("check-and-fix-links")
check_missing_archives = _load_script("check-missing-archives")
archive_repos = _load_script("archive-repos")
generate_descriptions = _load_script("generate-descriptions")


class MaintenanceScriptTests(unittest.TestCase):
    def test_apply_replacements_respects_slug_boundaries(self):
        text = "\n".join(
            [
                "- https://github.com/owner/foo [Dead]",
                "- https://github.com/owner/foo/tree/main [Deep]",
                "- https://github.com/owner/foo.",
                "- https://github.com/owner/foobar [Different repo]",
                "- https://github.com/owner/foo-bar [Hyphenated repo]",
                "- https://github.com/owner/foo.js [Dotted repo]",
            ]
        )
        updated = check_and_fix_links.apply_replacements(
            text,
            {"https://github.com/owner/foo": "https://github.com/gmh5225/foo"},
        )
        lines = updated.splitlines()
        self.assertEqual(lines[0], "- https://github.com/gmh5225/foo [Dead]")
        self.assertEqual(lines[1], "- https://github.com/gmh5225/foo/tree/main [Deep]")
        self.assertEqual(lines[2], "- https://github.com/gmh5225/foo.")
        self.assertEqual(lines[3], "- https://github.com/owner/foobar [Different repo]")
        self.assertEqual(lines[4], "- https://github.com/owner/foo-bar [Hyphenated repo]")
        self.assertEqual(lines[5], "- https://github.com/owner/foo.js [Dotted repo]")

    def test_extractors_skip_non_repo_routes(self):
        readme = "\n".join(
            [
                "## Game Engine",
                "- https://github.com/stars/gmh5225",
                "- https://github.com/topics/game-hacking",
                "- https://github.com/gmh5225/awesome-game-security",
                "- https://github.com/RealOwner/RealRepo",
            ]
        )
        self.assertEqual(
            archive_repos.extract_github_repos(readme),
            [("RealOwner", "RealRepo")],
        )
        self.assertEqual(
            check_missing_archives.extract_repos_with_categories(readme),
            [("RealOwner", "RealRepo", "Game Engine")],
        )
        self.assertEqual(
            check_and_fix_links.extract_github_urls(readme),
            [
                "https://github.com/gmh5225/awesome-game-security",
                "https://github.com/RealOwner/RealRepo",
            ],
        )

    def test_archive_path_and_is_archived_resolve_canonical_case(self):
        with tempfile.TemporaryDirectory() as tmp:
            arc_dir = Path(tmp) / "archive"
            owner_dir = arc_dir / "lowerowner"
            owner_dir.mkdir(parents=True)
            existing = owner_dir / "MyRepo.txt"
            existing.write_text("snapshot", encoding="utf-8")

            resolved = description_paths.archive_path(
                "LowerOwner", "myrepo", archive_dir=arc_dir
            )
            self.assertEqual(resolved.parent.name, "lowerowner")
            self.assertEqual(resolved.name, "MyRepo.txt")
            self.assertTrue(resolved.is_file())

            with mock.patch.object(check_missing_archives, "ARCHIVE_DIR", arc_dir):
                self.assertTrue(check_missing_archives.is_archived("LowerOwner", "myrepo"))
                self.assertFalse(check_missing_archives.is_archived("LowerOwner", "other"))

    def test_needs_description_checks_empty_and_canonical_case(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            desc_dir = root / "description"
            arc_dir = root / "archive"
            empty_dir = desc_dir / "OwnerA" / "EmptyRepo"
            empty_dir.mkdir(parents=True)
            (empty_dir / "description_en.txt").write_text("", encoding="utf-8")

            filled_dir = desc_dir / "OwnerB" / "FilledRepo"
            filled_dir.mkdir(parents=True)
            (filled_dir / "description_en.txt").write_text(
                "Valid summary.", encoding="utf-8"
            )

            with (
                mock.patch.object(description_paths, "DESC_DIR", desc_dir),
                mock.patch.object(description_paths, "ARCHIVE_DIR", arc_dir),
            ):
                self.assertTrue(generate_descriptions.needs_description("ownera", "emptyrepo"))
                self.assertFalse(generate_descriptions.needs_description("ownerb", "filledrepo"))
                self.assertTrue(generate_descriptions.needs_description("OwnerC", "MissingRepo"))

    def test_git_commit_and_push_handles_non_utf8_stderr(self):
        with tempfile.TemporaryDirectory() as tmp:
            arc_dir = Path(tmp) / "archive"
            arc_dir.mkdir()
            calls = [
                subprocess.CompletedProcess(["git", "add"], 0),
                subprocess.CompletedProcess(["git", "diff"], 1),
                subprocess.CalledProcessError(
                    1, ["git", "commit"], stderr=b"fatal: \xff\xfe invalid utf8"
                ),
            ]
            with mock.patch.object(archive_repos.subprocess, "run", side_effect=calls):
                archive_repos.git_commit_and_push(arc_dir, 1)


if __name__ == "__main__":
    unittest.main()
