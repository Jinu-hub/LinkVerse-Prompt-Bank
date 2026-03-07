# Versioning Policy

## 버전 분리

- 프롬프트는 수정이 잦으므로 파일 하나만 덮어쓰지 말고 버전 폴더로 관리한다.
- 예: `v1`, `v2`, `v3-experimental`

## Git 브랜치 추천

- **main**: 안정 버전
- **dev**: 작업 중
- 기능 브랜치 예: `feat/normalizer-v2`, `feat/report-writer-kr`, `eval/classifier-rubric-update`

## NOTES.md

각 프롬프트 폴더 내부의 `NOTES.md`에 다음을 남긴다.

- 왜 수정했는지
- 어떤 문제가 있었는지
- 어떤 예시에서 실패했는지
