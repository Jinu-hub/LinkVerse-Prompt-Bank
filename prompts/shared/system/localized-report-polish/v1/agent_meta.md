# localized-report-polish v1

## Agent metadata

| key | value |
|-----|-------|
| id | localized-report-polish |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Localized Report Polish Agent |
| description | 완성된 시장 리포트 Markdown을 output_lang에 맞게 자연스럽게 다듬는 최종 언어 편집 에이전트. 사실·구조·해석은 유지하고 가독성·용어 일관성·자연스러움만 개선 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | output_lang, final_report_md |
| input_contract.optional_fields | terminology_overrides |
| output_contract.type | json |
| output_contract.required_fields | final_report_md |
| model_hints.temperature | 0.2 |

### Tags
- report-polish
- localization
- markdown
- editing
- market-report
- post-processing

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

| key | required | binding |
|-----|:--------:|---------|
| output_lang | ✓ | `{{$json.output_lang}}` |
| final_report_md | ✓ | `{{$json.final_report_md}}` |
| terminology_overrides | | `{{$json.terminology_overrides}}` |

## Top-level 입력 구조

```json
{
  "output_lang": "ko | ja | en",
  "final_report_md": "# Report title\n\n...",
  "terminology_overrides": {}
}
```

| key | required | type |
|-----|:--------:|------|
| output_lang | ✓ | string — 최종 편집 대상 언어 (`ko`, `ja`, `en`) |
| final_report_md | ✓ | string — 편집 대상 전체 시장 리포트 Markdown |
| terminology_overrides | | object — 리포트별 선택적 용어 치환 규칙 |

## `terminology_overrides` (optional)

리포트별 용어 선호를 전달할 때만 사용. 미제공 시 에이전트가 임의로 생성하지 않음.

| key | type | 설명 |
|-----|------|------|
| (free-form key-value) | string → string | 원문 표현 → 선호 표현. 의미 변경·부자연스러운 치환 시 무시 |

적용 원칙:
- 현재 리포트에만 적용
- 의미를 바꾸거나 사실과 충돌하면 무시
- output_lang 자연스러움과 충돌하면 의도는 유지하되 표현을 자연스럽게 조정

## 출력 개요

`system.yaml`의 `output_schema` 및 `schema.json` 기준:

- `final_report_md` — output_lang에 맞게 다듬어진 전체 시장 리포트 Markdown 문자열

메타데이터·분석 노트·출처·주석은 출력하지 않음. 최종 독자용 prose만 반환.

## 변경 이력

- **왜 수정했는지**: system.yaml 출력·입력 계약 정의에 맞춰 schema, developer, agent_meta, examples를 placeholder에서 실제 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream 리포트 편집 검증 및 n8n 연동이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
