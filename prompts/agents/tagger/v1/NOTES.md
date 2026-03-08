# Tagger v1

## Agent metadata

| key | value |
|-----|-------|
| id | tagger |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Tagger Agent |
| description | Generates search and discovery tags (hard_tags, soft_tags, core_tags) from a structured digest and optional classifications |

**tags:** tagging, search, discovery, indexing

| contract | detail |
|----------|--------|
| input_contract.required_fields | topic, summary, highlights, items, ending; classifications recommended when available |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
