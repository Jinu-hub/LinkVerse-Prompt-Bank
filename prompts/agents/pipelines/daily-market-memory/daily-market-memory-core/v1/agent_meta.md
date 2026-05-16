# daily-market-memory-core v1

## Agent metadata

| key | value |
|-----|-------|
| id | daily-market-memory-core |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | daily-market-memory-pipeline |
| name | Daily Market Memory Core Generator |
| description | 일일 시장 리포트·스냅샷 입력을 영어 대시보드용 core JSON으로 압축 생성하는 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | source_report_count, core_lang_code, input_context.reports |
| input_contract.optional_fields | market_snapshot, input_context (partial), top-level reports fallback |
| output_contract.type | json |
| output_contract.required_fields | core_data, top_tags, top_entities, risk_signals |
| model_hints.temperature | 0.3 |

### Tags
- daily-market-memory
- market-dashboard
- core-generation
- english-source
- structured-output
- pipeline

# INPUT_DATA

| key | value |
|-----|-------|
| source_report_count | {{$json.source_report_count}} |
| core_lang_code | {{$json.core_lang_code}} |
| market_snapshot | {{$json.market_snapshot}} |
| input_context | {{$json.input_context}} |

## 변경 이력

- **왜 수정했는지**: system.yaml 출력 계약에 맞춰 schema, developer, agent_meta, examples를 초기 운영 버전으로 정의.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 파이프라인 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
