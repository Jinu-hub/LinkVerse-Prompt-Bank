# Naming Conventions

## 에이전트 폴더명

- **소문자 snake_case** 로 통일
- 예: `normalizer`, `table_extractor`, `market_summarizer`, `report_writer`

## 파일명 (고정 규칙)

- `system.yaml`
- `developer.yaml`
- `user_template.md`
- `schema.json`
- `NOTES.md`

## 버전 폴더

- `v1`, `v2`, `v3-experimental` 등

## 템플릿 변수

- 대문자 스네이크 예: `{{SOURCE_TEXT}}`, `{{OUTPUT_FORMAT}}`
- 프레임워크 문법 예: `{{$json.input_date}}`, `{{ $json.items_json }}` (에이전트·워크플로에 따라 사용)

## 메타 위치

- 에이전트 메타(id, version, tags, contract 등)는 **NOTES.md**에 기록. `prompt-writing-guide.md` 참고.
