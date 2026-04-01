# Digest Writer v1

## Agent metadata

| key | value |
|-----|-------|
| id | digest-writer |
| version | 2.0 |
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
| additional_items | {{ $json.additional_items }} |

## 변경 이력

- **왜 수정했는지**: 
items 수가 많아질 경우 digest 가독성이 급격히 떨어지는 문제를 해결하기 위해,
하위 priority item들을 하나의 compressed 섹션으로 정리하는 구조를 도입
- **어떤 문제가 있었는지**: 
모든 items가 동일한 구조(H3 + summary)로 나열되어
중요도 구분이 약해지고 스캔성이 떨어짐
long-tail item(낮은 rank)까지 동일한 밀도로 출력되어
전체 digest가 불필요하게 길어짐
reader 입장에서 핵심 흐름(highlights + 상위 items)에 집중하기 어려움
- **어떤 예시에서 실패했는지**: 
item_count가 10개 이상인 경우
→ 하위 item까지 full summary로 출력되어
digest 길이가 과도하게 증가
    예:
    rank 1~5: 핵심 투자/시장 변화
    rank 6~12: 개별 기능 업데이트 / minor news
    → 이 둘이 동일한 구조로 출력되어
    중요도 대비 정보 밀도 불균형 발생
