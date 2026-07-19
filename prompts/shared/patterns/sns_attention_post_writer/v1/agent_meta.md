# sns-attention-post-writer v1

## Agent metadata

| key | value |
|-----|-------|
| id | sns-attention-post-writer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | SNS Attention Post Writer |
| description | 시장 분석 요약을 사실 왜곡 없이 재구성해, 가장 강한 대비·신호·미해결 긴장을 전면에 둔 주목도 높은 SNS 포스트로 변환하는 에이전트 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | source_text, lang_code |
| output_contract.type | text |
| model_hints.temperature | 0.4 |


### Tags
- sns-posting
- attention
- editorial
- market-summary
- shared-pattern


# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| source_text | ✓ | `{{$json.source_text}}` |
| lang_code | ✓ | `{{$json.lang_code}}` |

## Top-level 입력 구조

```json
{
  "source_text": "string",
  "lang_code": "ko"
}
```

| key | required | type |
|-----|:--------:|------|
| source_text | ✓ | string — 재구성할 시장 분석 요약·리포트 본문 |
| lang_code | ✓ | `ko` \| `ja` \| `en` — SNS 포스트 출력 언어 |

`source_text`는 이미 정리된 분석 요약이어야 한다. 신규 리서치나 외부 지식 보강 없이, 이 텍스트에 포함된 사실·수치·불확실성만으로 포스트를 재구성한다.

## 출력 개요

`system.yaml`의 `output_rules` 및 `schema.json` 기준:

- **plain text** — 최종 SNS 포스트 본문만 반환 (JSON·메타데이터·라벨·설명 없음)
- 해시태그·별도 제목·Markdown 강조 없음
- 불릿은 신호 비교가 필요할 때만 최대 5개
- 이모지는 선택이며 최대 2개

## 포스트 구조 요약

| 구간 | 내용 |
|------|------|
| Opening | 가장 강한 사실·수치·이벤트를 첫 2–3줄에 배치 |
| Contrast | 예상과 다른 대비, 충돌하는 신호, 또는 미해결 긴장 |
| Supporting signals | 3–5개의 보조 신호 (필요 시 불릿) |
| Incomplete surface read | 표면적 해석이 불완전할 수 있는 이유 |
| Watch / close | 다음에 볼 구체 변수 1–2개, 또는 source에 근거한 특정 결론 |

구조는 가이드이며 기계적 템플릿이 아니다. 가독성과 리듬을 위해 순서·결합을 조정할 수 있다.

## 변경 이력

- **왜 수정했는지**: `system.yaml`에 정의된 SNS Attention Post Writer 계약에 맞춰 placeholder 상태의 schema, developer, agent_meta, examples를 실제 입력·출력 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream SNS 포스트 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
