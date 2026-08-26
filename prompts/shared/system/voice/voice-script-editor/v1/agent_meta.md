# voice-script-editor v1

## Agent metadata

| key | value |
|-----|-------|
| id | voice-script-editor |
| version | 1.0 |
| status | active |
| scope | shared |
| owner | marketmemory |
| name | Voice Script Editor |
| description | Today in 30 Seconds 구조화 브리프를 TTS에 바로 넣을 수 있는 단일 내레이터 음성 스크립트로 변환하는 에이전트. meta_data를 우선 사용해 intro→pulse→highlights→market reaction→closing 흐름의 30–45초 오디오 브리핑을 작성 |

| contract | detail |
|----------|--------|
| input_contract.required_fields | briefs (lang_code, content, meta_data) |
| output_contract.type | json |
| output_contract.required_fields | voice_script |
| model_hints.temperature | 0.35 |

### Tags
- voice-script
- tts
- today-in-30-seconds
- market-briefing
- audio-narration
- shared-system

# INPUT_DATA

n8n에는 아래 필드를 전달. 전체 샘플은 `examples/input_01.md` 참고.

입력은 **객체 1개를 담은 배열** 형태입니다. 실제 브리핑 데이터는 `briefs` 안에 있습니다.

| key | required | binding |
|-----|:--------:|---------|
| briefs | ✓ | `{{$json.briefs}}` |
| briefs.lang_code | ✓ | `{{$json.briefs.lang_code}}` |
| briefs.content | ✓ | `{{$json.briefs.content}}` |
| briefs.meta_data | ✓ | `{{$json.briefs.meta_data}}` |

## Top-level 입력 구조

```json
[
  {
    "briefs": {
      "lang_code": "ko",
      "content": "string",
      "meta_data": { }
    }
  }
]
```

| key | required | type |
|-----|:--------:|------|
| briefs.lang_code | ✓ | `ko` \| `ja` \| `en` 등 — 음성 스크립트 출력 언어 |
| briefs.content | ✓ | string — 보조 참고/fallback 본문 |
| briefs.meta_data | ✓ | object — PRIMARY 구조화 소스 |

## `briefs.meta_data` 구조

| key | required | type |
|-----|:--------:|------|
| topic | ✓ | string — 디스플레이용 주제 (음성용으로 자연스럽게 재작성) |
| market_date | ✓ | string — `YYYY-MM-DD` (권위 있는 날짜) |
| pulse | ✓ | string — 당일 시장 환경 |
| highlights | ✓ | object[] — 핵심 이슈 (보통 2–3개) |
| market_reaction | ✓ | object[] — 관측 가능한 시장 반응 |
| takeaway | ✓ | string — 클로징 프레임의 주 가이드 |

### `highlights[]`

| key | required | type |
|-----|:--------:|------|
| title | ✓ | string |
| summary | ✓ | string |

### `market_reaction[]`

| key | required | type |
|-----|:--------:|------|
| label | ✓ | string |
| value | ○ | string \| null |
| direction | ○ | `up` \| `down` \| `flat` \| `mixed` \| `unchanged` \| null |

upstream `today-in-30-seconds-representation` 출력을 `meta_data`로 매핑해 전달하는 것을 권장. `content`는 보조 참고용.

## 소스 우선순위

1. `meta_data.market_date`
2. `meta_data.topic`
3. `meta_data.pulse`
4. `meta_data.highlights`
5. `meta_data.market_reaction`
6. `meta_data.takeaway`

`content`는 structured meta_data가 부족할 때만 fallback.

## 출력 개요

`system.yaml` Output 및 `schema.json` 기준:

```json
{
  "voice_script": "string"
}
```

| 필드 | 역할 | 제약 |
|------|------|------|
| voice_script | TTS 직행용 단일 내레이션 | plain spoken sentences only; ~30–45초 |

## 내레이션 아크 요약

| 구간 | 내용 |
|------|------|
| Intro | market_date + topic + pulse로 당일 프레임 확립 |
| Pulse | 시장 환경의 중심 역학 (intro와 중복 금지) |
| Key developments | highlights의 구체 사건 보존 |
| Market reaction | 가격·금리·지수 움직임을 구어체로 전달 |
| Closing | takeaway 기반 1문장 종합 프레임 |

## 변경 이력

- **왜 수정했는지**: system.yaml에 정의된 Voice Script Editor 계약에 맞춰 placeholder 상태의 schema, developer, agent_meta, examples를 실제 입력·출력 계약으로 정리.
- **어떤 문제가 있었는지**: placeholder schema·meta·예시로 인해 downstream TTS 연동 및 스크립트 검증이 불가능했음.
- **어떤 예시에서 실패했는지**: (추가 시 `examples/input_01.md` / `expected_01.json` 기준으로 기록)
