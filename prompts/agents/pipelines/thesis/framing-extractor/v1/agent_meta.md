# Framing Extractor v1

## Agent metadata

| key | value |
|-----|-------|
| id | framing-extractor |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Framing Extractor Agent |
| description | Extracts and sharpens the core thesis framing from a high-quality introduction into a report-ready English opening block with structured framing signals |

| contract | detail |
|----------|--------|
| input_contract.required_fields | detail_text |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- thesis
- framing
- editorial-layer
- investment-writing


# INPUT_DATA

| key | value |
|-----|-------|
| detail_text | {{$json.detail_text}} |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
