# Tagger v1

## Agent metadata

| key | value |
|-----|-------|
| id | core-tagger |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Tagger Agent |
| description | Generates search and discovery tags (hard_tags, soft_tags, core_tags) from a structured digest and optional classifications |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, summary, classifications |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

### tags
- tagging
- search
- discovery
- indexing


# INPUT_DATA
| key | value | required |
|-----|-------|----------|
| input_date | {{$json.input_date}} | required |
| topic | {{$json.topic}} | required |
| summary | {{$json.summary}} | required |
| highlights | {{$json.highlights}} | optional |
| ending | {{$json.ending}} | optional |
| classifications | {{$json.classifications}} | required |

## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
