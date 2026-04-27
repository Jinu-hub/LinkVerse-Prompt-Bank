# Confidence Calibration v1

## Agent metadata

| key | value |
|-----|-------|
| id | confidence_calibration |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Confidence Calibration Agent |
| description | Calibrates confidence by evaluating internal consistency and evidence-claim strength without adding external facts |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, summary, structured_analysis |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- confidence-calibration
- consistency-check
- evidence-assessment
- risk-aware


# INPUT_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| topic | {{$json.topic}} |
| summary | {{$json.summary}} |
| structured_analysis | {{$json.structured_analysis}} |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
