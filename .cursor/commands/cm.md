---
description: Generate a conventional commit message from staged changes
---

You are a professional software engineer.

When this command is invoked, do the following:

1. Analyze ONLY the currently staged changes (git diff --staged).
2. Understand both:
   - what changed (implementation)
   - why it changed (intent or outcome)
3. Generate a concise but slightly descriptive commit message in English.
4. Follow the Conventional Commits specification (feat, fix, refactor, chore, docs, etc.).
5. Use imperative tone (e.g., "add", "fix", "refactor").
6. Keep the subject line under 72 characters.
7. The subject line must clearly describe the user-visible outcome or main purpose.
8. Add a short body (1–3 lines) when helpful to explain:
   - key implementation details OR
   - important context that is not obvious from the subject
9. Avoid overly generic messages like "update", "improve", or "fix stuff".

Output format:
- Return ONLY one code block.
- The code block must contain ONLY the commit message.
- Do NOT include explanations, labels, or extra text.

Style guidelines:
- Be slightly more descriptive than minimal commits.
- Balance clarity and brevity (do not be verbose).
- Prefer clarity of intent over listing all changes.

Example:
