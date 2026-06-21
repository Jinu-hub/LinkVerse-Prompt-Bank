# timeline-social-formatter v1

## Agent metadata

| key | value |
|-----|-------|
| id | timeline-social-formatter |
| version | 1.0 |
| status | active |
| scope | pipelines/timeline_p1 |
| owner | timeline-p1-pipeline |
| name | Timeline Social Formatter Agent |
| description | 완성된 시장 리포트 Markdown을 SNS 친화적 텍스트로 변환하는 포맷터. 의미·사실·구조는 유지하고 Markdown 문법을 제거하며 모바일 가독성에 맞는 기호·레이아웃을 적용 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | final_report_md |
| output_contract.type | json |
| output_contract.required_fields | text |
| model_hints.temperature | 0.2 |

### Tags
- timeline
- social-format
- sns
- markdown-to-text
- pipeline
- timeline-p1

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| final_report_md | ✓ | `{{$json.final_report_md}}` |

## Top-level 입력 구조

```json
{
  "final_report_md": "# Report title\n\n..."
}
```

| key | required | type |
|-----|:--------:|------|
| final_report_md | ✓ | string — SNS 포맷팅 대상 전체 시장 리포트 Markdown (한국어·영어 등 입력 언어 그대로 유지) |

upstream `localized-report-polish` 또는 `weekly-market-report-writer`의 `final_report_md` 출력을 그대로 전달하는 것을 권장.

## 출력 개요

`system.yaml`의 `OUTPUT_FORMAT` 및 `schema.json` 기준:

- `text` — Markdown 문법이 제거되고 SNS 레이아웃 기호가 적용된 전체 포맷 텍스트 문자열

번역·요약·메타데이터·분석 노트는 출력하지 않음. 입력과 동일한 언어로 포맷된 SNS 본문만 반환.

## SNS 레이아웃 요약

| 구간 | 기호·레이아웃 |
|------|---------------|
| 제목 헤더 | `━` 박스 + 📢 제목 + 📅 기간 |
| 섹션 제목 | `─` 구분선 + ■ 섹션명 |
| 날짜별 타임라인 | ▶ 날짜, • 이벤트, ▪ 세부·영향 |
| 주요 테마 | 📌 테마 헤더, ✅ 분석 포인트 |
| 리스크·주목점 | ⚠️ 항목 |
| 마무리 | 📝 결론 문단 |

## 변경 이력

- **왜 수정했는지**: system.yaml 출력·입력 계약 정의에 맞춰 schema, developer, agent_meta, examples를 placeholder에서 실제 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream SNS 포맷 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
