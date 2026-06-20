# weekly-market-report-writer v1

## Agent metadata

| key | value |
|-----|-------|
| id | weekly-market-report-writer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | timeline-p1-pipeline |
| name | Weekly Market Report Writer Agent |
| description | timeline-core가 생성한 구조화 core_data를 바탕으로 주간 시장 리포트 Markdown을 작성하는 최종 리포트 작성 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | output_lang, core_data.source_report, core_data.timeline_overview, core_data.items, core_data.daily_groups, core_data.continuity_groups, core_data.report_planning_hints |
| output_contract.type | json |
| output_contract.required_fields | final_report_md |
| model_hints.temperature | 0.3 |

### Tags
- timeline
- report-writing
- markdown
- localization
- pipeline
- timeline-p1

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| output_lang | ✓ | `{{$json.output_lang}}` |
| core_data | ✓ | `{{$json.core_data}}` |

## Top-level 입력 구조

```json
{
  "output_lang": "ko | ja | en",
  "core_data": {}
}
```

| key | required | type |
|-----|:--------:|------|
| output_lang | ✓ | string — 최종 리포트 출력 언어 (`ko`, `ja`, `en`) |
| core_data | ✓ | object — timeline-core downstream 출력의 핵심 필드 묶음 |

## `core_data` (required sections)

| key | required | type |
|-----|:--------:|------|
| source_report | ✓ | object — 리포트 기간·주제 메타 |
| timeline_overview | ✓ | object — 기간 전체 서사 요약 |
| items | ✓ | object[] — 이벤트 항목 (사실 근거) |
| daily_groups | ✓ | object[] — 날짜별 흐름 |
| continuity_groups | ✓ | object[] — 주요 테마/스토리라인 |
| report_planning_hints | ✓ | object — 리포트 각도·강조·주의사항 |

`core_data`는 timeline-core 출력에서 `agent_name`, `version`을 제외한 본문 필드를 전달하는 것을 권장.

## 출력 개요

`system.yaml`의 `output_schema` 및 `schema.json` 기준:

- `final_report_md` — output_lang에 맞게 작성된 전체 주간 시장 리포트 Markdown 문자열

메타데이터·분류·점수·planning hints는 출력하지 않음. 최종 독자용 prose만 생성.

## 변경 이력

- **왜 수정했는지**: system.yaml 출력 계약 정의에 맞춰 schema, developer, agent_meta, examples를 placeholder에서 실제 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream 리포트 작성 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
