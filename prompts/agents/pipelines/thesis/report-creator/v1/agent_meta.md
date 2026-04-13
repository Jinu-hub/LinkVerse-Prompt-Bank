# thesis-report-creator v1

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-report-creator |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | thesis-pipeline |
| name | Thesis Report Creator |
| description | 구조화된 thesis 입력을 분석 리포트 JSON으로 생성하는 작성 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | topic, summary, structured_thesis, confidence, output_lang |
| output_contract.type | json |
| output_contract.required_fields | title, thesis, lead, report_body, key_points, risk_note, deck, confidence |
| model_hints.temperature | 0.3 |

### Tags
- thesis
- report-drafting
- structured-output
- pipeline

# INPUT_DATA

| key | value |
|-----|-------|
| topic | {{$json.topic}} |
| summary | {{$json.summary}} |
| structured_thesis | {{$json.structured_thesis}} |
| confidence | {{$json.confidence}} |
| output_lang | {{$json.output_lang}} |

## 변경 이력

- **왜 수정했는지**: 템플릿 상태를 실제 report-creator 계약에 맞는 운영 메타로 교체.
- **어떤 문제가 있었는지**: 입력/출력 필드가 placeholder여서 system prompt와 schema 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: `examples/input_01.md` 및 `examples/expected_01.json` 기준 필드 매핑 불일치.
