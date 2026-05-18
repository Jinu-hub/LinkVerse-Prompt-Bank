# daily-market-memory-data v1

## Agent metadata

| key | value |
|-----|-------|
| id | daily-market-memory-data |
| version | 1.0 |
| status | active |
| scope | pipelines/daily-market-memory |
| owner | daily-market-memory-pipeline |
| name | Daily Market Memory Data (i18n) |
| description | Daily Market Memory core 객체를 받아 대시보드용 ko/en/ja 다국어 표시 데이터(i18n_rows)를 생성하는 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | core_data |
| input_contract.optional_fields | top_tags, top_entities, risk_signals |
| output_contract.type | json |
| output_contract.required_fields | i18n_rows |
| model_hints.temperature | 0.3 |

### Tags
- daily-market-memory
- i18n
- dashboard
- localization
- pipeline

# INPUT_DATA

| key | value |
|-----|-------|
| core_data | {{$json.core_data}} |
| top_tags | {{$json.top_tags}} |
| top_entities | {{$json.top_entities}} |
| risk_signals | {{$json.risk_signals}} |

## 변경 이력

- **왜 수정했는지**: system.yaml 출력 계약(i18n_rows, ko/en/ja 고정 3행)에 맞춰 schema, developer, agent_meta, examples를 초기 운영 버전으로 정의.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 파이프라인 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
