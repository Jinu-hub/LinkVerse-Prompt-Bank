# Prompt Writing Guide

프롬프트 본문은 아래 포맷을 추천한다.

## 파일 포맷

- **설정/메타데이터**: YAML (`system.yaml`, `developer.yaml`)
- **긴 본문**: Markdown (`user_template.md`)

## 레이어 분리

- **system.yaml**: 역할, 목적, 강한 제약 (name, version, role, description, model_notes, tags, variables, constraints, output_format)
- **developer.yaml**: 구현 규칙, 포맷 규칙, 금지사항
- **user_template.md**: 실제 주입되는 입력 템플릿 (예: `{{SOURCE_TEXT}}`)

## 예시 저장

- `examples/` 에 `input_01.md`, `expected_01.json` 형태로 입력/기대 출력을 둔다.
- 좋은 프롬프트는 "설명"보다 "예시 세트"가 더 중요하다.

## 참고

- `naming-conventions.md`: 파일/변수 네이밍
- `versioning-policy.md`: 버전 관리
- `evaluation-guide.md`: 평가 방법
