# sns-market-memory-footer v1

## Agent metadata

| key | value |
|-----|-------|
| id | sns-market-memory-footer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | SNS Market Memory Footer |
| description | `sns-human-voice-writer` 등 완성된 SNS 포스트 뒤에 붙일 Market Memory CTA 푸터를 생성하는 에이전트. 본문 주제에 맞춰 초대 멘트를 변형하고, 브랜드명·프로필/핀 고정글 안내·Google `marketmemory app` 검색 안내는 고정 패턴으로 유지한다. |

| contract | detail |
|----------|--------|
| input_contract.required_fields | source_text, lang_code |
| output_contract.type | text |
| model_hints.temperature | 0.55 |


### Tags
- sns-posting
- footer
- cta
- market-memory
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
| source_text | ✓ | string — upstream에서 완성된 SNS 포스트 본문 (`sns-human-voice-writer` v1/v2 출력 권장) |
| lang_code | ✓ | `ko` \| `ja` \| `en` — 푸터 출력 언어 |

`source_text`는 이미 완성된 SNS 포스트여야 한다. 본문을 다시 쓰지 않고, 주제에 맞는 CTA 초대 멘트만 생성한다.

## 출력 개요

`system.yaml`의 `output_rules` 및 `schema.json` 기준:

- **plain text** — CTA 푸터만 반환 (JSON·메타데이터·라벨·편집 노트 없음)
- 구조:
  1. 본문 맞춤 초대 멘트 (1–2줄)
  2. 빈 줄
  3. `🔗` 프로필 링크 또는 핀 고정글 링크 안내
  4. `🔍` Google에서 `'marketmemory app'` 검색 안내
- 브랜드명 `Market Memory`는 정확히 한 번, 변형 없이 포함
- 검색어는 항상 `marketmemory app`
- raw URL·말미 구분선(`-----` / `-------`)은 포함하지 않음

## 문장 의도 요약

| 구간 | 내용 |
|------|------|
| Invitation | 완성 포스트 주제에 맞춰, 상세 리포트/전체 시장 흐름을 Market Memory에서 확인하도록 유도 |
| Discovery | 프로필 링크 또는 핀 고정글 클릭, 또는 Google에서 `marketmemory app` 검색 |

한국어 기준 형태:

```text
상세한 분석 리포트 전문과 전체적 시장흐름은
Market Memory에서 확인하실 수 있습니다.

🔗 프로필 링크 혹은 핀 고정글의 링크를 클릭하시거나,
🔍 Google에서 'marketmemory app'으로 검색해보세요!
```

초대 멘트는 포스트에 맞게 바꿔도 되지만, 발견 경로(🔗/🔍)와 브랜드·검색어는 고정한다.

## 파이프라인 위치

| 단계 | 에이전트 | 역할 |
|------|----------|------|
| 본문 | `sns-human-voice-writer` (v1/v2) | SNS 본문 재작성 |
| 푸터 | `sns-market-memory-footer` | 본문 주제 맞춤 Market Memory CTA 생성 후 append |

## 변경 이력

- **왜 수정했는지**: 단순 1–2문장 푸터에서, 프로필/핀 고정글·Google 검색 안내를 포함한 고정 CTA 블록 + 본문 맞춤 멘트로 확장.
- **어떤 문제가 있었는지**: 본문을 받지 않아 포스트 주제와 무관한 일반 CTA만 생성 가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
