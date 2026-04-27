# Report Surface v1

## Agent metadata

| key | value |
|-----|-------|
| id | report-surface |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Report Surface |
| description | Turns a completed report into a sharp, audience-facing distribution layer with headline angle, summaries, hooks, and a clear one-line takeaway. |

| contract | detail |
|----------|--------|
| input_contract.required_fields | report_text, output_lang |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- editorial
- distribution
- report-surface
- social-format


# Input_DATA

| key | value |
|-----|-------|
| report_text | {{$json.report_text}} |
| output_lang | {{$json.output_lang}} |
| topic | {{$json.topic}} |
| audience | {{$json.audience}} |
| tone_hint | {{$json.tone_hint}} |


## 변경 이력

- **왜 수정했는지**: 템플릿 상태의 메타데이터를 `report-surface` 에이전트의 실제 입력 계약과 출력 목적에 맞게 구체화하기 위해 수정.
- **어떤 문제가 있었는지**: placeholder 값이 남아 있어 운영 시 입력 필드, 설명, 태그, 소유자 정보가 실제 시스템 프롬프트 및 예시와 맞지 않았음.
- **어떤 예시에서 실패했는지**: `examples/expected_01.json` 기준으로는 7개 고정 출력 필드를 반환해야 하나, 기존 메타데이터는 계약 정보가 비어 있어 검증 및 문서 참조 시 혼선을 만들 수 있었음.
