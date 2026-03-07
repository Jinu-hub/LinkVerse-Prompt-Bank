#!/usr/bin/env python3
"""Render a prompt by loading system, developer, user_template and substituting variables (e.g. {{SOURCE_TEXT}})."""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    print("Render placeholder: extend to load YAML/MD and substitute {{placeholders}}.")


if __name__ == "__main__":
    main()
