# thesis-report-enhancer v1

## Agent metadata

| key | value |
|-----|-------|
| id | thesis-report-enhancer |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | prompt-bank |
| name | Thesis Report Enhancer |
| description | 논문형 리포트를 대중 친화적 에디토리얼 리포트로 재작성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | full_md_report, output_lang |
| output_contract.type | json |
| model_hints.temperature | 0.2 |

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

- **2026-04-13**: report-enhancer v1 메타데이터를 실제 입출력 계약 기준으로 초기 작성
