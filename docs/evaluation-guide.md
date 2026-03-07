# Evaluation Guide

## 구조

- `evals/datasets/`: 에이전트별 데이터셋 (normalizer, classifier, summarizer)
- `evals/rubrics/`: 채점 기준
- `evals/results/`: `scripts/run_eval.py` 실행 결과

## 목적

- 이 레포는 단순 문서 저장소가 아니라 **검증 가능한 프롬프트 연구소**가 되는 것이 목표다.
- evals에 쌓이는 순간 가장 큰 자산이 된다.

## 실행

```bash
python scripts/run_eval.py --agent normalizer --version v1
```
