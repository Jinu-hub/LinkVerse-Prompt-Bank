# Digest Writer v1

---
id: digest-writer
version: 0.1.0
status: active
scope: shared
owner: marketmemory
name: Digest Writer Agent
description: Writes digest output from pre-selected highlights and items
tags:
  - digest
  - editorial
  - multi-item
input_contract:
  required_fields:
    - input_date
    - topic
    - highlights
    - items
output_contract:
  type: json
model_hints:
  temperature: 0.3
---
