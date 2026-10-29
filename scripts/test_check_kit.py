"""공개 준비 키트에서 누락·유출·잘못된 참조를 막는 회귀 검사입니다."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

from check_kit import validate


class KitValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary: tempfile.TemporaryDirectory[str] = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root: Path = Path(self.temporary.name) / "kit"
        source: Path = Path(__file__).resolve().parents[1]
        shutil.copytree(source, self.root, ignore=shutil.ignore_patterns("local", ".git", "__pycache__"))

    def test_clean_public_copy_passes_without_private_sources(self) -> None:
        self.assertFalse((self.root / "local").exists())
        self.assertEqual(validate(self.root), [])

    def test_missing_required_template_is_rejected(self) -> None:
        (self.root / "templates/PRD.md").unlink()
        self.assertTrue(any("templates/PRD.md" in error for error in validate(self.root)))

    def test_broken_relative_document_link_is_rejected(self) -> None:
        with (self.root / "README.md").open("a") as stream:
            stream.write("\n[누락 문서](docs/missing.md)\n")
        self.assertTrue(any("docs/missing.md" in error for error in validate(self.root)))

    def test_pinned_upstream_tampering_is_rejected(self) -> None:
        with (self.root / ".agents/skills/ponytail/SKILL.md").open("a") as stream:
            stream.write("\nmodified\n")
        self.assertTrue(any("HASH" in error for error in validate(self.root)))

    def test_secret_filename_is_rejected_without_printing_contents(self) -> None:
        (self.root / ".env").write_text("PRIVATE_EXAMPLE=not-a-real-secret\n")
        errors: list[str] = validate(self.root)
        self.assertTrue(any(".env" in error for error in errors))
        self.assertNotIn("not-a-real-secret", "\n".join(errors))

    def test_symlink_to_outside_is_rejected(self) -> None:
        outside: Path = Path(self.temporary.name) / "outside.txt"
        outside.write_text("private fixture\n")
        (self.root / "docs/escape.md").symlink_to(outside)
        self.assertTrue(any("SYMLINK" in error for error in validate(self.root)))

    def test_public_pdf_is_rejected(self) -> None:
        (self.root / "guide.pdf").write_bytes(b"%PDF-fixture")
        self.assertTrue(any("guide.pdf" in error for error in validate(self.root)))

    def test_manifest_cannot_escape_public_root(self) -> None:
        manifest: Path = self.root / "third-party/sources.json"
        entries: list[dict[str, object]] = json.loads(manifest.read_text())
        entries.append({"repository": "example/fixture", "commit": "a" * 40,
                        "path": "README.md", "url": "https://github.com/example/fixture/blob/" + "a" * 40 + "/README.md",
                        "sha256": "0" * 64, "local_path": "../outside.txt", "redistributed": True})
        manifest.write_text(json.dumps(entries))
        self.assertTrue(any("PATH" in error for error in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
