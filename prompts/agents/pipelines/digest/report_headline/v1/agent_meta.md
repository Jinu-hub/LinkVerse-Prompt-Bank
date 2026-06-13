# Digest Headline Agent v1

## Agent metadata

| key | value |
|-----|-------|
| id | report_headline |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Digest Headline Agent |
| description | 요약(summary)을 기반으로 핵심 문구를 최대한 보존해 하나의 간결한 헤드라인을 생성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | summary, output_lang |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- headline
- digest
- compression
- language-preservation


# INPUT_DATA

| key | value |
|-----|-------|
| summary | {{$json.summary}} |
| output_lang | {{$json.output_lang}} |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
