# analysis_creator v1

## Agent metadata

| key | value |
|-----|-------|
| id | analysis_creator |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | linkverse |
| name | Report Creator |
| description | 구조화 분석 결과를 게시 가능한 기사형 리포트 JSON으로 편집 생성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | input_date, topic, structured_analysis, summary, confidence, source_lang |
| output_contract.type | json |
| model_hints.temperature | 0.3 |


### Tags
- reporting
- editorial
- synthesis
- json-output


# INPUT_DATA

| key | value | required |
|-----|-------|----------|
| input_date | {{$json.input_date}} | required |
| topic | {{$json.topic}} | required |
| structured_analysis | {{$json.structured_analysis}} | required |
| summary | {{$json.summary}} | required |
| confidence | {{$json.confidence}} | required |
| source_lang | {{$json.source_lang}} | required |
| source_text | {{$json.source_text}} | optional |


## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
