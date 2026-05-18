# copy-polisher v1

## Agent metadata

| key | value |
|-----|-------|
| id | copy-polisher |
| version | 1.0 |
| status | active |
| scope | pipelines/daily-market-memory |
| owner | daily-market-memory-pipeline |
| name | Copy Polisher |
| description | daily-market-memory-data의 i18n 행 배열을 받아 동일 항목 구조로 대시보드 표시 문구만 자연스럽게 다듬는 에이전트 (의미·구조·잠금 필드 불변) |

| contract | detail |
|----------|--------|
| input_contract.required_fields | i18n row array (from `i18n_rows` or bare array) |
| output_contract.type | json |
| output_contract.required_fields | i18n row array (top-level, no wrapper) |
| output_contract.schema_ref | daily-market-memory-data v1 i18n row items (array root) |
| model_hints.temperature | 0.2 |

### Tags
- daily-market-memory
- copy-polish
- dashboard
- i18n
- pipeline

# INPUT_DATA

| key | value |
|-----|-------|
| (input) | `{{$json.i18n_rows}}` — data 에이전트 `i18n_rows` 배열 (n8n에서 배열로 전달) |

## 변경 이력

- **왜 수정했는지**: system.yaml 역할(문구 보정 전용)과 daily-market-memory-data 출력 계약에 맞춰 schema, developer, agent_meta, examples를 초기 운영 버전으로 정의.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 파이프라인 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
