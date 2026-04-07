# Analyzer v1

## Agent metadata

| key | value |
|-----|-------|
| id | analyzer |
| version | 2.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Analyzer Agent |
| description | Decomposes digest logic into claims/evidence/risks/assumptions, then performs single digest-level classification and structured metadata extraction |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, detail (or equivalent digest content) |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- structural-analysis
- claim-extraction
- evidence-linking
- classification
- metadata-extraction


# INPUT_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| topic | {{$json.topic}} |
| detail | {{$json.detail}} |


## 변경 이력

- **왜 수정했는지**: classifications를 분리