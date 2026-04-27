# English Translation v1

## Agent metadata

| key | value |
|-----|-------|
| id | en-translation |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | English Translation Agent |
| description | Translates source content into natural English while preserving meaning and structure |

| contract | detail |
|----------|--------|
| input_contract.required_fields | source_data |
| output_contract.type | json |
| model_hints.temperature | 0.2 |


### Tags
- translation
- english
- structure-preserving
- preprocessing


# INPUT_DATA

| key | value |
|-----|-------|
| source_data | {{$json.source_data}} |
| translation_mode | {{$json.translation_mode}} |

Notes:
- `source_data` may be plain text, object, array, or mixed content.
- `translation_mode` is optional (`strict`, `natural`, `financial`).


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
