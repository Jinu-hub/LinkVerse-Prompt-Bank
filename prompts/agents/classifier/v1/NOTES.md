# Classifier v1

## Agent metadata

| key | value |
|-----|-------|
| id | classifier |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Classifier Agent |
| description | Classifies multi-item digest (one category, subcategories), extracts regions/asset classes/entities and raw numeric/time expressions |

**tags:** classification, digest, metadata, extraction

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, summary, highlights, items, ending (or equivalent digest content) |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
