# Digest Finalizer v1

## Agent metadata

| key | value |
|-----|-------|
| id | digest_finalizer |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Digest Finalizer Agent |
| description | Finalizes a structured digest into a polished, publish-ready Markdown document and document-level metadata |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, summary, highlights, items, ending |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

### Tags
- digest
- markdown
- editing
- finalization


# INPUT_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| topic | {{$json.topic}} |
| headline | {{$json.headline}} |
| summary | {{$json.summary}} |
| highlights | {{$json.highlights}} |
| items | {{$json.items}} |
| ending | {{$json.ending}} |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
