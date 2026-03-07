# linkverse_prompt_bank

Reusable prompt assets for LinkVerse agents and workflows.

## Goals

- Manage prompts by role and version
- Reuse prompts across products and workflows
- Track prompt changes with examples and evaluations
- Enable structured testing and iterative improvement

## Structure

- `prompts/agents`: role-specific prompts
- `prompts/workflows`: multi-step workflow prompts
- `evals/`: evaluation datasets and results
- `scripts/`: validation and rendering tools
- `examples/`: integration examples

## Design Principles

1. Separate system / developer / user layers
2. Version prompts explicitly
3. Store examples next to prompts
4. Keep prompts human-readable
5. Make evaluations repeatable

## First Agents

- normalizer
- classifier
- summarizer
- report_writer
