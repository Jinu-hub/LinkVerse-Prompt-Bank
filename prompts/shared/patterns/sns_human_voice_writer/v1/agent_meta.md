# sns-human-voice-writer v1

## Agent metadata

| key | value |
|-----|-------|
| id | sns-human-voice-writer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | SNS Human Voice Writer |
| description | 이미 작성된 SNS 포스트를 사실·해석을 유지한 채, 생성형·정형화된 문체를 줄이고 자연스럽고 편집적으로 개성 있는 사람 목소리로 다시 쓰는 최종 단계 에디터 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | source_text, lang_code |
| output_contract.type | text |
| model_hints.temperature | 0.5 |


### Tags
- sns-posting
- human-voice
- editorial
- rewrite
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
| source_text | ✓ | string — 이미 작성된 SNS 포스트 초안(리포트 원문이 아닌 완성 초안). CTA·푸터·구분선·URL이 포함될 수 있음 |
| lang_code | ✓ | `ko` \| `ja` \| `en` — 다시 쓸 SNS 포스트 출력 언어 |

`source_text`는 이미 SNS 포스트로 작성된 초안이어야 한다. 원 리포트를 다시 요약하지 않고, 기존 포스트의 사실·수치·해석·불확실성을 유지한 채 문체와 리듬만 다듬는다.

## 출력 개요

`system.yaml`의 `output_rules` 및 `schema.json` 기준:

- **plain text** — 다시 쓴 SNS 포스트 본문만 반환 (JSON·메타데이터·라벨·편집 노트 없음)
- 기존 CTA·푸터·구분선·URL은 그대로 보존
- 입력에 없던 이모지·마크다운 제목을 임의로 추가하지 않음
- 모든 문장을 한 줄씩 나누거나 문단 길이를 균등하게 맞추지 않음

## 편집 초점 요약

| 구간 | 내용 |
|------|------|
| Center | 포스트가 정말 말하려는 1–2개 포인트에 공간을 몰아줌 |
| Voice | 생성형·정형 대비 문장과 리포트형 구조를 줄이고 사람 편집 리듬으로 재작성 |
| Substance | 사실·수치·해석·불확실성·리스크 수준은 유지. 새 정보·과장·약화 금지 |
| Close | 이 주제만의 구체적 여운으로 끝냄. 범용 “지켜보자” 결론 금지 |
| Footer | 기존 CTA·푸터·URL이 있으면 보존하고 본문 편집에 집중 |

구조는 가이드이며 기계적 템플릿이 아니다. 가독성과 자연스러움을 위해 문장·문단 순서를 조정할 수 있다.

## 변경 이력

- **왜 수정했는지**: `system.yaml`에 정의된 SNS Human Voice Writer 계약에 맞춰 placeholder 상태의 schema, developer, agent_meta, examples를 실제 입력·출력 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream SNS 포스트 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
