# daily-market-summary-posting v1

## Agent metadata

| key | value |
|-----|-------|
| id | daily-market-summary-posting |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Daily Market Summary Posting Agent |
| description | 이미 준비된 시장 분석 입력(core_data, reports_summary)을 자연스럽고 읽기 쉬운 일일 SNS 포스트로 변환하는 에이전트. 신규 분석·추가 팩트 생성 없이 당일 시장 스토리를 2–3개 테마로 엮어 서술 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | core_data, reports_summary, lang_code |
| output_contract.type | text |
| model_hints.temperature | 0.3 |

### Tags
- daily-market-memory
- sns-posting
- market-summary
- editorial
- shared-pattern

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| core_data | ✓ | `{{$json.core_data}}` |
| reports_summary | ✓ | `{{$json.reports_summary}}` |
| lang_code | ✓ | `{{$json.lang_code}}` |

## Top-level 입력 구조

```json
{
  "core_data": { },
  "reports_summary": "string",
  "lang_code": "ko"
}
```

| key | required | type |
|-----|:--------:|------|
| core_data | ✓ | object — 당일 시장 프레이밍의 기준 데이터 |
| reports_summary | ✓ | string — `=====`로 구분된 여러 리포트 요약 텍스트 |
| lang_code | ✓ | `ko` \| `ja` \| `en` — SNS 포스트 출력 언어 |

## `core_data` 구조

| key | required | type |
|-----|:--------:|------|
| top_themes | ✓ | object[] — 당일 핵심 테마 (theme_title, summary, signal_strength 등) |
| market_mood | ✓ | object — type, label, summary 등 당일 시장 분위기 |
| core_summary | ✓ | string — 당일 시장 요약 (2–4문장) |
| display_title | ✓ | string — 당일 헤드라인 |
| display_subtitle | ✓ | string — 부제·긴장 요약 |
| source_lang_code | ✓ | string — core_data 원본 언어 코드 |

`signal_strength`는 `high` \| `medium` \| `low`. 테마 선택 시 `high` 우선, 최종 포스트는 2–3개 핵심 포인트에 집중.

upstream `daily-market-memory-core` 또는 `daily-market-memory-data`의 `core_data`와 리포트 요약 문자열을 전달하는 것을 권장.

## 출력 개요

`system.yaml`의 `OUTPUT_FORMAT` 및 `schema.json` 기준:

- **plain text** — 최종 SNS 포스트 본문만 반환 (JSON·메타데이터·설명 없음)
- 권장 길이: ko/ja 700–1,200자, en 180–300 words

## 포스트 구조 요약

| 구간 | 내용 |
|------|------|
| Opening hook | SNS 네이티브 훅 (🧵, 📌, 🌐, 📊 등 선택적 사용) |
| Short setup | market_mood·core_summary 기반 당일 분위기 (2–4문장) |
| Key points | 1/, 2/, 3/ 형식의 2–3개 테마 (자연스러운 단락, 보고서 아웃라인 금지) |
| Daily market memo | lang_code별 마무리 한 줄 (예: ko `오늘의 시장 메모:`) |

## 변경 이력

- **왜 수정했는지**: system.yaml에 정의된 Daily Market Summary Posting 계약에 맞춰 placeholder 상태의 schema, developer, agent_meta, examples를 실제 입력·출력 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream SNS 포스트 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
