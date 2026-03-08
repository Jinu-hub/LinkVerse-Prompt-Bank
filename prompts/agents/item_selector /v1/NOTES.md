# Item Selector v1

## Agent metadata

| key | value |
|-----|-------|
| id | multi-item-selector |
| version | 0.1.0 |
| status | active |
| name | Multi Item Selector |
| description | Select highlight items from a multi-item digest and return grouped raw items |

**tags:** selection, ranking, digest, multi-item

| contract | detail |
|----------|--------|
| input | input_date, topic, item_count, detail |
| output | input_date, topic, item_count, actual_item_count, highlight_count, highlights, items |
| response_format | json |
| model_hints.temperature | 0.1 |

## 변경 이력

- **왜 수정했는지**: (수정 시 여기에 기록)
- **어떤 문제가 있었는지**: (이슈 발생 시 기록)
- **어떤 예시에서 실패했는지**: (실패한 input/expected 있으면 기록)
