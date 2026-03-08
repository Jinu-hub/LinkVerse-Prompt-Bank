# Prompt Writing Guide

프롬프트 본문은 아래 포맷을 추천한다.

## 파일 포맷

- **설정/메타데이터**: YAML (`system.yaml`, `developer.yaml`)
- **긴 본문**: Markdown (`user_template.md`)

## 레이어 분리

- **system.yaml**: 역할, 목적, 강한 제약 (프롬프트 본문). 메타는 여기 두지 않는다.
- **developer.yaml**: 구현 규칙, 포맷 규칙, 금지사항
- **user_template.md**: 실제 주입되는 입력 템플릿 (플레이스홀더로 변수 주입)

## 메타 위치

- **에이전트 메타**(id, version, status, scope, owner, name, description, tags, input_contract, output_contract, model_hints 등)는 **NOTES.md**에 기록한다.
- 표 형식으로 정리하면 가독성이 좋다.

## 템플릿 문법

- 프로젝트에서는 프레임워크별 문법을 사용할 수 있다 (예: `{{$json.input_date}}`, `{{ $json.highlights_json }}`).
- 통일이 필요하면 에이전트별로 같은 문법을 쓰고, naming-conventions에 예시를 적어 둔다.

## 예시 저장

- `examples/` 에 `input_01.md`, `expected_01.json` 형태로 입력/기대 출력을 둔다.
- 좋은 프롬프트는 "설명"보다 "예시 세트"가 더 중요하다.

## 참고

- `naming-conventions.md`: 파일/변수 네이밍
- `versioning-policy.md`: 버전 관리
- `evaluation-guide.md`: 평가 방법
