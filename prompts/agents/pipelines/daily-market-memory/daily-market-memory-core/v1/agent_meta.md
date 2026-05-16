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

- **왜 수정했는지**: system.yaml 출력 계약 정의 및 n8n 실제 바인딩(`input_context` 단일 객체)에 맞춰 schema, developer, agent_meta, examples 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 파이프라인 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
