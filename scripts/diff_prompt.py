#!/usr/bin/env python3
"""Diff two prompt versions or two rendered prompts."""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    print("Diff placeholder: extend to compare two prompt dirs or rendered outputs.")


if __name__ == "__main__":
    main()
