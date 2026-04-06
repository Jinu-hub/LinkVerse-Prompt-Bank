# Analysis Finalizer v1

## Agent metadata

| key | value |
|-----|-------|
| id | analysis-finalizer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Report Finalizer Agent |
| description | Turns structured report fields into one polished editorial Markdown article wrapped in JSON (report string) |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, headline, deck, report_body, key_points, risk_note |
| output_contract.type | json (single field: report) |
| model_hints.temperature | 0.3 |

### Tags

- editorial
- report
- markdown
- market-intelligence

# Input_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| headline | {{$json.headline}} |
| deck | {{$json.deck}} |
| report_body | {{$json.report_body}} |
| key_points | {{$json.key_points}} |
| risk_note | {{$json.risk_note}} |

`key_points` may be a JSON string array or equivalent; align with your workflow (n8n / API).

## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
