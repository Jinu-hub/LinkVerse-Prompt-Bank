# Reinterpretation v2

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-reinterpretation |
| version | 2.0 |
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

- **2026-05-08**: report-reinterpretation v2 기존 프롬프트의 핵심 역할과 출력 방향은 유지하되, catalyst_map, scenario_framework, stakeholder_map, key_metrics가 원문에 있을 때만 강하게 작동하도록 다시 구성