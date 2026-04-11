# Reinterpretation v1

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-reinterpretation |
| version | 1.0 |
| status | active |
| scope | pipelines/thesis |
| owner | marketmemory |
| name | Report Reinterpretation Analyzer |
| description | Extracts editorial backbone and reusable investment mappings from long-form thesis reports without rewriting the source. |

| contract | detail |
|----------|--------|
| input_contract.required_fields | doc_body |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- thesis
- reinterpretation
- editorial-structure
- investment-mapping


# Input_DATA

| key | value |
|-----|-------|
| doc_body | {{$json.doc_body}} |


## 변경 이력

- **왜 수정했는지**: 템플릿 상태 메타데이터를 시스템 프롬프트와 예시 출력 계약에 맞게 실제 운영용으로 정리.
- **어떤 문제가 있었는지**: 입력 필드/스코프/에이전트 식별자가 placeholder 상태여서 파이프라인 연결 및 자동 검증 신뢰성이 낮았음.
- **어떤 예시에서 실패했는지**: `examples/expected_01.json` 기준의 대형 구조화 출력(`core_message`, `company_mapping`, `compression_plan` 등)을 템플릿 메타만으로는 추적하기 어려웠음.
