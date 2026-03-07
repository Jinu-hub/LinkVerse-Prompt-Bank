"""Tests for normalizer schema validity and example conformance."""

import json
from pathlib import Path


def test_schema_json_valid() -> None:
    root = Path(__file__).resolve().parent.parent
    schema_path = root / "prompts" / "agents" / "normalizer" / "v1" / "schema.json"
    with open(schema_path) as f:
        data = json.load(f)
    assert "properties" in data
    assert "required" in data


def test_expected_01_conforms_to_schema_structure() -> None:
    root = Path(__file__).resolve().parent.parent
    schema_path = root / "prompts" / "agents" / "normalizer" / "v1" / "schema.json"
    expected_path = root / "prompts" / "agents" / "normalizer" / "v1" / "examples" / "expected_01.json"
    with open(schema_path) as f:
        schema = json.load(f)
    with open(expected_path) as f:
        example = json.load(f)
    for key in schema.get("required", []):
        assert key in example, f"Missing required key: {key}"
