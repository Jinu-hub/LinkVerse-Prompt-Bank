# Digest Summary & Headline Agent v2

## Agent metadata

| key | value |
|-----|-------|
| id | report_headline |
| version | 2.0.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Digest Summary & Headline Agent |
| description | 확정된 요약(summary)을 output_lang으로 정리하고, 그 요약을 기반으로 핵심 문구를 최대한 보존한 하나의 간결한 헤드라인을 생성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | summary, output_lang |
| output_contract.type | json |
| output_contract.required_fields | summary, headline |
| model_hints.temperature | 0.3 |


### Tags
- headline
- summary
- digest
- compression
- translation
- language-preservation


# INPUT_DATA

| key | value |
|-----|-------|
| summary | {{$json.summary}} |
| output_lang | {{$json.output_lang}} |


## 변경 이력

- **왜 수정했는지**: v2에서 헤드라인 생성 전에 summary를 output_lang으로 정리하는 역할이 추가되어, 출력 스키마와 메타데이터를 system.yaml과 일치시킴
- **어떤 문제가 있었는지**: v1 스키마(`output` 단일 필드)가 v2 system.yaml(`summary` + `headline`)과 불일치
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
