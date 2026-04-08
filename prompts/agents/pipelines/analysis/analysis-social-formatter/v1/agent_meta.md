# Analysis Social Formatter v1

## Agent metadata

| key | value |
|-----|-------|
| id | analysis-social-formatter |
| version | 1.0 |
| status | active |
| scope | pipelines/analysis |
| owner | marketmemory |
| name | Analysis Social Formatter |
| description | Converts a full analysis report into a mobile-readable SNS text while preserving facts, logic, and market interpretation. |

| contract | detail |
|----------|--------|
| input_contract.required_fields | report, output_lang |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- analysis
- social-format
- editorial


# Input_DATA

| key | value |
|-----|-------|
| report | {{$json.report}} |
| output_lang | {{$json.output_lang}} |


## 변경 이력

- **왜 수정했는지**: 템플릿 상태의 메타데이터를 실제 입력/출력 계약과 시스템 규칙에 맞게 정리하기 위해 수정.
- **어떤 문제가 있었는지**: placeholder 값이 남아 있어 운영 시 입력 필드, 스코프, 설명의 일관성이 깨질 수 있었음.
- **어떤 예시에서 실패했는지**: `examples/expected_01.json` 기준으로는 출력 키가 `sns_report`여야 하나, 기존 템플릿에서는 계약 필드가 비어 있어 검증 자동화에서 실패 가능.
