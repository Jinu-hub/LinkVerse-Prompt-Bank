# timeline-core-enrichment v1

## Agent metadata

| key | value |
|-----|-------|
| id | timeline-core-enrichment |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | timeline-p1-pipeline |
| name | Timeline Core Enrichment Agent |
| description | 이미 선별된 시장 하이라이트 core 데이터를 타임라인 리포트 작성에 필요한 분류·그룹·서사 메타데이터로 보강하는 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | core_data |
| input_contract.optional_fields | market_date, topic, from, to |
| output_contract.type | json |
| output_contract.required_fields | agent_name, version, source_report, timeline_overview, items, daily_groups, continuity_groups, report_planning_hints |
| model_hints.temperature | 0.3 |

### Tags
- timeline
- enrichment
- classification
- continuity-grouping
- english-metadata
- pipeline
- timeline-p1

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| market_date | | `{{$json.market_date}}` |
| topic | | `{{$json.topic}}` |
| from | | `{{$json.from}}` |
| to | | `{{$json.to}}` |
| core_data | ✓ | `{{$json.core_data}}` |

## Top-level 입력 구조

```json
{
  "market_date": "string",
  "topic": "string",
  "from": "YYYY-MM-DD",
  "to": "YYYY-MM-DD",
  "core_data": []
}
```

| key | required | type |
|-----|:--------:|------|
| market_date | | string — 리포트 기준일 또는 기간 앵커 |
| topic | | string — 타임라인 주제 |
| from | | string — 기간 시작일 (YYYY-MM-DD) |
| to | | string — 기간 종료일 (YYYY-MM-DD) |
| core_data | ✓ | object[] — 선별된 하이라이트 항목 목록 |

## `core_data[]` (per item)

| key | required | type |
|-----|:--------:|------|
| market_date | ✓ | string — YYYY-MM-DD |
| title | ✓ | string — 원문 제목 (출력에서 그대로 보존) |
| summary | ✓ | string — 사실 요약 |
| why_it_matters | ✓ | string — 시장·서사적 중요성 |

```json
{
  "market_date": "YYYY-MM-DD",
  "title": "string",
  "summary": "string",
  "why_it_matters": "string"
}
```

## 출력 개요

`system.yaml`의 `output_schema` 및 `schema.json` 기준. 주요 top-level 키:

- `source_report` — 입력 메타데이터 에코
- `timeline_overview` — 기간 전체 서사 요약
- `items` — 항목별 분류·태그·continuity_group (입력 항목 수와 1:1)
- `daily_groups` — 날짜별 main/supporting/parallel 배치
- `continuity_groups` — 스토리라인 그룹 정의
- `report_planning_hints` — downstream timeline-report-agent용 힌트

모든 생성 메타데이터는 **영어**로 출력. 최종 리포트 문장·현지화는 downstream 에이전트가 담당.

## 변경 이력

- **왜 수정했는지**: system.yaml 출력 계약 정의에 맞춰 schema, developer, agent_meta, examples를 placeholder에서 실제 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 파이프라인 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
