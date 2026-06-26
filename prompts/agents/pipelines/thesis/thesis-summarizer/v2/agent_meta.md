# thesis-summarizer v2

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-summarizer |
| version | 2.0 |
| status | active |
| scope | pipelines/thesis |
| owner | marketmemory |
| name | Report Summary Generation Agent |
| description | 구조화된 thesis core_data를 topic·summary_structured·key_takeaways·summary_short 네 레이어로 압축·재배치하는 요약 에이전트. 새 분석 없이 리포트의 전략 주장·인과·투자 함의·프레이밍을 downstream(DB, UI, 검색, SNS) 재사용 형태로 보존 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | output_lang, core_data |
| output_contract.type | json |
| output_contract.required_fields | topic, summary_structured, key_takeaways, summary_short |
| model_hints.temperature | 0.3 |

### Tags
- thesis
- summarization
- multi-layer-output
- investor-content
- structured-summary
- pipeline

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
| output_lang | ✓ | string — 모든 출력 **값**의 언어 (`ko`, `ja`, `en`). JSON 키 이름은 영어 고정 |
| core_data | ✓ | object — `thesis-reinterpretation` 등 upstream이 생성한 구조화 분석 데이터 |

## `core_data` (주요 optional 섹션)

upstream에 있을 때만 사용. 없는 프레이밍은 강제하지 않음.

| key | 용도 |
|-----|------|
| core_message | `primary_thesis`, `secondary_messages`, `reader_implication` — thesis·investor_implication 앵커 |
| signature_framing | 대비·프레이밍·에디토리얼 훅 보존 |
| narrative_map | tension → explanation → implication 흐름, `summary_short` shaping |
| rewrite_critical_takeaways | 고우선 보존 지시 |
| action_framework | what_to_focus / what_to_avoid / selection_criteria |
| scenario_framework | `scenario_summary` (base/upside/downside) |
| catalyst_map | `why_now`, `key_catalysts`, `key_takeaways` |
| case_studies | `case_study` (가장 illustrative 1건) |
| table_candidates | `table_candidates_summary` (0–3건) |
| hierarchical_structure / company_mapping / stakeholder_map | `beneficiary_groups` |
| risk_points / source_ambiguities / claim_integrity_notes | `risks`, caution |
| key_metrics | thesis 강화용 수치만 선택적 사용 |
| compression_plan / readability_notes / section_roles / tone_and_positioning | 편집 가이드 (직접 요약 대상 아님) |

`core_data`는 `thesis-reinterpretation/v2` downstream 출력을 그대로 전달하는 것을 권장.

## 출력 개요

`system.yaml`의 `OUTPUT_FORMAT` 및 `schema.json` 기준:

| 필드 | 소비 레이어 |
|------|-------------|
| topic | UI·카드용 한 줄 헤드라인 (~8–18단어) |
| summary_structured | DB·검색·downstream 리포트용 구조화 요약 |
| key_takeaways | 리포트 미열람 시 핵심 해석 불릿 4–6개 |
| summary_short | 카드·프리뷰·SNS용 2–4문장 서술 |

### `summary_structured` nullability

| 필드 | 비어 있을 때 |
|------|----------------|
| scenario_summary | `null` |
| case_study | `null` |
| table_candidates_summary | `[]` |
| key_catalysts | `[]` |
| beneficiary_groups | `[]` |

## 변경 이력

- **왜 수정했는지**: system.yaml v2 출력·입력 계약(topic, key_catalysts, scenario_summary, table_candidates_summary, output_lang)에 맞춰 schema, developer, agent_meta, examples를 placeholder에서 실제 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 v2 다층 요약 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
