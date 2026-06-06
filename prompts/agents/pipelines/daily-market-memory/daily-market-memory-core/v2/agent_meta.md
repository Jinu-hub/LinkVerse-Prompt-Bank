# daily-market-memory-core v2

## Agent metadata

| key | value |
|-----|-------|
| id | daily-market-memory-core |
| version | 2.0 |
| status | active |
| scope | shared |
| owner | daily-market-memory-pipeline |
| name | Daily Market Memory Core Generator |
| description | 일일 시장 리포트·스냅샷 입력을 영어 대시보드용 core JSON으로 압축 생성하는 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_context.reports |
| input_contract.optional_fields | input_context.market_snapshot, input_context (partial fields) |
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

n8n에는 **`input_context`만** 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| input_context | ✓ | `{{$json.input_context}}` |

## `input_context` 구조

```json
{
  "reports": [],
  "market_snapshot": {
    "items": [{ "id": "string", "price": 0, "change": 0, "changePercent": 0 }],
    "fearGreed": { "asOf": "string", "value": 0, "classification": "string" },
    "fetchedAt": "string"
  }
}
```

| key | required | type |
|-----|:--------:|------|
| reports | ✓ | object[] — 일일 시장 메모리 리포트 목록 |
| market_snapshot | | object — 시장 지표·Fear&Greed (optional) |

`system.yaml`은 top-level `source_report_count`, `core_lang_code`, `market_snapshot`도 허용하나, **파이프라인 바인딩은 `input_context` 단일 객체** 기준.

# OUTPUT_DATA

출력 스키마는 `schema.json` / `examples/expected_01.json` 기준.

| key | required | type |
|-----|:--------:|------|
| core_data | ✓ | object — display_title, display_subtitle, core_summary, top_themes, market_mood, core_generation_notes |
| top_tags | ✓ | object[] — 최대 10 |
| top_entities | ✓ | object — companies, industries, technologies, indicators, countries, institutions, asset_classes (각 최대 8) |
| risk_signals | ✓ | string[] — 2~5 |

## `core_data.top_themes[]` (per item)

| key | required | type |
|-----|:--------:|------|
| theme_title | ✓ | string |
| summary | ✓ | string |
| signal_strength | ✓ | `high` \| `medium` \| `low` — 당일 입력에서의 테마 중요도(가격·추세 방향 아님) |
| related_tags | ✓ | string[] — 2~5 |
| related_report_count | ✓ | integer |
| source_report_ids | ✓ | string[] |
| source_item_content_ids | ✓ | string[] |

v1의 `trend_status`(rising/steady/weakening)는 v2에서 사용하지 않음.

## `input_context.reports[]` (per item)

| key | required | type |
|-----|:--------:|------|
| tags | ✓ | string[] |
| entities / entitys | ✓ | object — companies, products, technologies, industries, indicators, countries, institutions, persons (둘 다 올 수 있음, 병합) |
| regions | | string[] |
| category | | string — e.g. sector, macro, geopolitics |
| coreData | ✓ | object — topic, summary, key_takeaways[], highlights[]{ title, summary, why_it_matters } |
| coreType | | string |
| countries | | string[] |
| inputDate | | string — YYYY-MM-DD |
| confidence | | object — confidence_score, what_to_verify[] |
| reportType | | string — e.g. market_memory |
| asset_classes | | string[] |
| itemContentId | ✓ | string |
| marketMemoryItemId | ✓ | string |

```json
{
  "tags": ["string"],
  "entities": {
    "companies": ["string"], "products": ["string"], "technologies": ["string"],
    "industries": ["string"], "indicators": ["string"], "countries": ["string"],
    "institutions": ["string"], "persons": ["string"]
  },
  "regions": ["string"],
  "category": "string",
  "coreData": {
    "topic": "string",
    "summary": "string",
    "key_takeaways": ["string"],
    "highlights": [{ "title": "string", "summary": "string", "why_it_matters": "string" }]
  },
  "coreType": "string",
  "countries": ["string"],
  "inputDate": "YYYY-MM-DD",
  "confidence": { "confidence_score": "low | medium | high", "what_to_verify": ["string"] },
  "reportType": "market_memory",
  "asset_classes": ["string"],
  "itemContentId": "string",
  "marketMemoryItemId": "string"
}
```

## 변경 이력

- **v2**: `top_themes`의 `trend_status`를 `signal_strength`(`high` \| `medium` \| `low`)로 교체. `market_mood`에 `bias`, `shift` 추가 및 `core_generation_notes.previous_market_context_used` 반영. schema, developer, examples, downstream data/copy-polisher 스키마와 동기화.
- **왜 수정했는지**: system.yaml 출력 계약 정의 및 n8n 실제 바인딩(`input_context` 단일 객체)에 맞춰 schema, developer, agent_meta, examples 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 파이프라인 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
