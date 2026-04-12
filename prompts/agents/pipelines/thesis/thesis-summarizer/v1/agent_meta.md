# Thesis Summarizer v1

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-summarizer |
| version | 1.0 |
| status | active |
| scope | pipelines/thesis |
| owner | marketmemory |
| name | Report Summary Generation Agent |
| description | Converts structured thesis core data into multi-layer summaries for report headers, UI blocks, and SNS distribution. |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, core_data |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- thesis
- summarization
- multi-layer-output
- investor-content


# Input_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| core_data | {{$json.core_data}} |


## 변경 이력

- **왜 수정했는지**: 템플릿 상태 메타를 실제 시스템/예시 계약에 맞는 운영 문서로 전환하기 위해 수정.
- **어떤 문제가 있었는지**: 입력 필드 및 에이전트 식별자가 placeholder로 남아 파이프라인 연동 시 해석 불일치 위험이 있었음.
- **어떤 예시에서 실패했는지**: `examples/expected_01.json`의 6개 출력 레이어(`headline_angle`~`summary_sns_post`)를 템플릿 메타데이터로는 명시적으로 보장하기 어려웠음.
