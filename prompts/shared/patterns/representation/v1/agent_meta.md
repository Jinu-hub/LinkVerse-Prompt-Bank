# today-in-30-seconds-representation v1

## Agent metadata

| key | value |
|-----|-------|
| id | today-in-30-seconds-representation |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Today in 30 Seconds Representation Generator |
| description | upstream에서 이미 선별·순위가 확정된 `core_data`를 30초 안에 파악 가능한 구조화 표현(pulse, highlights, market_reaction, takeaway)으로 압축·재구성하는 에이전트. 이슈 발견·재순위 없이 표현·압축·구성만 수행 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | core_data, output_lang |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

### Tags
- today-in-30-seconds
- market-representation
- dashboard
- compression
- shared-pattern

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| core_data | ✓ | `{{$json.core_data}}` |
| output_lang | ✓ | `{{$json.output_lang}}` |

## Top-level 입력 구조

```json
{
  "core_data": { },
  "output_lang": "ko"
}
```

| key | required | type |
|-----|:--------:|------|
| core_data | ✓ | object — upstream editorial pipeline이 생성한 당일 시장 이슈 데이터 |
| output_lang | ✓ | `ko` \| `ja` \| `en` 등 — 사용자-facing 출력 언어 코드 |

## `core_data` 구조

| key | required | type |
|-----|:--------:|------|
| input_date | ✓ | string — `YYYY-MM-DD` |
| topic | ✓ | string — 당일 이슈/브리핑 주제 |
| summary | ✓ | string — 당일 전체 시장 환경 요약 (→ `pulse` 주 소스) |
| highlights | ✓ | object[] — 최대 3개 핵심 이슈 (2–3개일 수 있음) |
| items | ✓ | object[] — 차순위 이슈 (→ `market_reaction` 주 소스) |
| more_items | ○ | object[] — 저우선 보조 자료 (fallback context only) |
| ending | ✓ | string — 당일 전체 함의 (→ `takeaway` 주 소스) |

### `highlights[]` 항목

| key | required | type |
|-----|:--------:|------|
| title | ✓ | string |
| summary | ✓ | string |
| why_it_matters | ✓ | string — 표현 맥락용; 출력 필드로는 생성하지 않음 |

### `items[]` / `more_items[]` 항목

| key | required | type |
|-----|:--------:|------|
| title | ✓ | string |
| summary | ✓ | string |

upstream digest/editorial pipeline(`digest_writer`, `digest_finalizer` 등)이 생성한 `core_data`를 전달하는 것을 권장.

## 출력 개요

`system.yaml`의 Output Schema 및 `schema.json` 기준:

```json
{
  "pulse": "string",
  "highlights": [{ "title": "string", "summary": "string" }],
  "market_reaction": [{ "label": "string", "value": "string|null", "direction": "up|down|mixed|unchanged|null" }],
  "takeaway": "string"
}
```

| 필드 | 역할 | 제약 |
|------|------|------|
| pulse | 당일 전체 시장 환경 | 1–2문장; `summary` 기반 |
| highlights | 핵심 2–3개 이슈 | `core_data.highlights` 개수·순서 유지; summary 1문장 |
| market_reaction | 관측 가능한 시장 반응 | 최대 3개; 없으면 빈 배열 |
| takeaway | 기억할 핵심 함의 | 1문장; `ending` 기반 |

## 섹션 매핑 요약

| 출력 | 주 소스 | 보조 소스 |
|------|---------|-----------|
| pulse | core_data.summary | — |
| highlights | core_data.highlights | why_it_matters (맥락만) |
| market_reaction | core_data.items | core_data.more_items (fallback only) |
| takeaway | core_data.ending | — |

## 변경 이력

- **왜 수정했는지**: system.yaml에 정의된 Today in 30 Seconds Representation 계약에 맞춰 placeholder 상태의 schema, developer, agent_meta, examples를 실제 입력·출력 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream 30초 대시보드 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
