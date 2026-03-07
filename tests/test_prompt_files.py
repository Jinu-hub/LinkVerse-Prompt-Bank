"""Tests for prompt file structure and presence."""

from pathlib import Path


def test_prompts_dir_exists() -> None:
    root = Path(__file__).resolve().parent.parent
    assert (root / "prompts").is_dir()


def test_normalizer_v1_has_required_files() -> None:
    root = Path(__file__).resolve().parent.parent
    v1 = root / "prompts" / "agents" / "normalizer" / "v1"
    assert (v1 / "system.yaml").exists()
    assert (v1 / "developer.yaml").exists()
    assert (v1 / "user_template.md").exists()
    assert (v1 / "schema.json").exists()
