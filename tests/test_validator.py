#!/usr/bin/env python3
"""Testes de regressão para detecção de pacotes inválidos, sem serviços externos."""
from pathlib import Path
import shutil
import tempfile
import unittest
from validate import validate, BASE

SOURCE = Path(__file__).resolve().parents[1]

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
        self.skill = self.root / BASE / "SKILL.md"

    def test_valid_package(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_reference(self):
        (self.root / BASE / "references/audio-and-dialogue.md").unlink()
        self.assertTrue(any("audio-and-dialogue" in e for e in validate(self.root)))

    def test_invalid_yaml(self):
        self.skill.write_text("---\nname: [invalid\n---\n", encoding="utf-8")
        self.assertTrue(any("YAML inválido" in e for e in validate(self.root)))

    def test_duplicate_yaml_key(self):
        s = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(s.replace("name: veo3-cinematic-director", "name: veo3-cinematic-director\nname: other"), encoding="utf-8")
        self.assertTrue(any("duplicada" in e for e in validate(self.root)))

    def test_wrong_name(self):
        s = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(s.replace("name: veo3-cinematic-director", "name: wrong"), encoding="utf-8")
        self.assertTrue(any("Nome técnico" in e for e in validate(self.root)))

    def test_broken_internal_link(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as f:
            f.write("\n[Quebrado](missing.md)\n")
        self.assertTrue(any("Link interno" in e for e in validate(self.root)))

    def test_empty_description(self):
        s = self.skill.read_text(encoding="utf-8")
        start = s.index("description:")
        end = s.index("\n---", start)
        self.skill.write_text(s[:start] + 'description: ""' + s[end:], encoding="utf-8")
        self.assertTrue(any("Description" in e for e in validate(self.root)))

    def test_missing_test_cases(self):
        (self.root / "tests/acceptance-tests.md").write_text("# Casos\n", encoding="utf-8")
        self.assertTrue(any("20 casos" in e for e in validate(self.root)))

    def test_changed_dialogue(self):
        p = self.root / BASE / "examples/brazilian-dialogue.md"
        p.write_text(p.read_text().replace('"Moço, esse ônibus passa na Central?"', '"Does this bus go downtown?"'))
        self.assertTrue(any("exact speech" in e for e in validate(self.root)))

    def test_missing_machine_cases(self):
        (self.root / "tests/test-cases.json").write_text("[]")
        self.assertTrue(any("twenty" in e for e in validate(self.root)))

if __name__ == "__main__":
    unittest.main()
