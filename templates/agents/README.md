# Agent 템플릿

`prompts/agents/` 에 새 에이전트를 추가할 때 사용하는 복사용 템플릿입니다.

## 디렉토리 구조

```
templates/agents/
  _template_/           # 이 폴더를 복사해서 사용
    v1/
      system.yaml        # 시스템 프롬프트
      developer.yaml     # 구현·포맷·금지 규칙
      user_template.md   # 사용자 입력 템플릿 (변수 치환)
      schema.json        # 출력 JSON 스키마
      NOTES.md           # 에이전트 메타데이터·변경 이력
      examples/
        input_01.md      # 샘플 입력
        expected_01.json # 샘플 기대 출력
  README.md              # 본 설명
```

## 사용 방법

1. **복사**
   ```bash
   cp -r templates/agents/_template_ prompts/agents/새에이전트이름
   ```

2. **이름 변경**
   - `prompts/agents/새에이전트이름/v1/` 아래 파일들이 새 에이전트용이 됩니다.

3. **내용 수정**
   - `system.yaml`: 역할, 입출력 규칙, OUTPUT_SCHEMA
   - `developer.yaml`: schema_path 유지, 구현/금지 규칙 추가
   - `user_template.md`: 실제 입력 키·변수명
   - `schema.json`: 실제 출력 스키마
   - `NOTES.md`: id, name, description, tags 등
   - `examples/input_01.md`, `expected_01.json`: 실제 예시 1건

4. **참고**
   - 기존 에이전트 예: `prompts/agents/digest_writer/v1/` 구조와 내용을 참고하면 됩니다.
