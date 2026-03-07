"""Tests for prompt rendering (placeholder)."""

from pathlib import Path


def test_render_placeholder() -> None:
    root = Path(__file__).resolve().parent.parent
    assert (root / "scripts" / "render_prompt.py").exists()
