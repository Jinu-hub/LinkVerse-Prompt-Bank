# Normalizer v1

## Agent metadata

| key | value |
|-----|-------|
| id | normalizer |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Normalizer Agent |
| description | 문서에서 추출된 raw text를 해석 없이 노이즈 제거·서식 정규화·블록 타입 분류를 수행해 구조화된 JSON으로 출력 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | raw_text |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- preprocessing
- normalization
- noise-removal
- block-classification


# INPUT_DATA

| key | value |
|-----|-------|
| raw_text | {{$json.raw_text}} |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
