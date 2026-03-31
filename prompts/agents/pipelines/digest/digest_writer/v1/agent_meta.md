# Digest Writer v1

## Agent metadata

| key | value |
|-----|-------|
| id | digest-writer |
| version | 1.0 |
| status | active |
| scope | pipelines/digest |
| owner | marketmemory |
| name | Digest Writer Agent |
| description | Writes digest output from pre-selected highlights and items |

**tags:** digest, editorial, multi-item

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, item_count, actual_item_count, highlight_count, highlights_json, items_json |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

# INPUT_DATA

| key | value |
|-----|-------|
| input_date | {{$json.input_date}} |
| topic | {{$json.topic}} |
| highlights_json | {{ $json.highlights_json }} |
| items_json | {{ $json.items_json }} |

## 변경 이력

- **왜 수정했는지**: `examples/input_01.md` 기반 입력 메타 정보를 `agent_meta.md`로 이관
- **어떤 문제가 있었는지**: 샘플 입력 파일과 입력 계약 정보가 분리되어 참조 지점이 불명확함
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
