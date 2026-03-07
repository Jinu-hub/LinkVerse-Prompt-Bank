#!/usr/bin/env python3
"""Run evaluations for an agent version using evals/datasets and evals/rubrics."""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run prompt evals")
    parser.add_argument("--agent", type=str, default="normalizer")
    parser.add_argument("--version", type=str, default="v1")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    datasets = root / "evals" / "datasets" / args.agent
    if not datasets.exists():
        print(f"Dataset dir not found: {datasets}")
        return
    print(f"Eval placeholder for agent={args.agent} version={args.version}")


if __name__ == "__main__":
    main()
