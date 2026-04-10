# Summarizer v1

## Agent metadata

| key | value |
|-----|-------|
| id | analysis-summarizer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Summarizer Agent |
| description | Converts structured analysis into concise human-readable summary while preserving original meaning and uncertainty framing |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, original_text, structured_analysis, confidence_result (optional), output_language (optional) |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- summarization
- editorial-layer
- structure-preserving
- risk-aware


# INPUT_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| topic | {{$json.topic}} |
| original_text | {{$json.original_text}} |
| structured_analysis | {{$json.structured_analysis}} |
| confidence_result | {{$json.confidence_result}} |
| output_language | {{$json.output_language}} |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
