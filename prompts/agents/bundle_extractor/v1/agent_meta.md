# Metric Bundle Extractor v1

## Agent metadata

| key | value |
|-----|-------|
| id | bundle_extractor |
| version | 0.1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Metric Bundle Extractor Agent |
| description | Classifier 결과에서 동일 지표·기간·다수 엔티티를 갖는 구조화된 metric bundle을 추출하여 저장·분석용 JSON으로 출력 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | classification result array (summary, main_entities, numeric_data, time_data per item) |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

### Tags
- metrics
- extraction
- classification
- numeric
- normalization


# INPUT_DATA

입력은 분류 결과 객체의 배열입니다. 각 요소는 다음 필드를 가집니다.

| key | value |
|-----|-------|
| classification_items | {{$json.classification_items}} (또는 입력 배열) |

각 classification item typically contains:

- summary: string
- main_entities: string (JSON 문자열)
- numeric_data: string (JSON 문자열)
- time_data: string (JSON 문자열)


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
