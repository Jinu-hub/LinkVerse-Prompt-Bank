# thesis-report-enhancer v2

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-report-enhancer |
| version | 2.0 |
| status | active |
| scope | shared |
| owner | prompt-bank |
| name | Thesis Report Enhancer |
| description | 논문형 리포트를 대중 친화적 에디토리얼 리포트로 재작성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | full_md_report, output_lang |
| output_contract.type | json |
| model_hints.temperature | 0.3 |

### Tags
- thesis
- editorial-rewrite
- readability
- multilingual

# Input_DATA

| key | value |
|-----|-------|
| full_md_report | {{$json.full_md_report}} |
| output_lang | {{$json.output_lang}} |

## 변경 이력

- **2026-05-08**: report-enhancer v2 과도한 룰을 해제 하고, 좀더 독자로 하여금 읽기 편하게 내용을 변경 가능하도록 수정
