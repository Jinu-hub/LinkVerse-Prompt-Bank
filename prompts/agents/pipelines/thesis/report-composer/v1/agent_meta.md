# thesis-report-composer v1

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-report-composer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | prompt-bank |
| name | Thesis Report Composer |
| description | 구조화된 thesis 데이터를 완성형 에디토리얼 리포트로 구성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, headline, thesis, lead, deck, report_body, key_points, risk_note, confidence |
| output_contract.type | json |
| model_hints.temperature | 0.2 |

### Tags
- thesis
- composition
- editorial
- markdown
- multilingual

# Input_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| headline | {{$json.headline}} |
| thesis | {{$json.thesis}} |
| lead | {{$json.lead}} |
| deck | {{$json.deck}} |
| report_body | {{$json.report_body}} |
| key_points | {{$json.key_points}} |
| risk_note | {{$json.risk_note}} |
| confidence | {{$json.confidence}} |

## 변경 이력

- **2026-04-13**: report-composer v1 메타데이터를 실제 입출력 계약 기준으로 초기 작성
