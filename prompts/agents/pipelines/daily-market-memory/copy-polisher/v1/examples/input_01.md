# Sample input

`daily-market-memory-data` v1 출력과 동일한 `i18n_rows` 객체. 문구가 다소 딱딱하거나 번역투인 상태(보정 전).

```json
{
  "i18n_rows": [
    {
      "lang_code": "ko",
      "display_title": "AI 병목과 매크로 및 지정학적 리스크의 교차 현상",
      "display_subtitle": "구조적 AI 수요는 견조한 상태이나 인플레이션 및 에너지 및 공급망 리스크가 시장 분위기를 전면적 Risk-On이 아닌 선택적 상태로 유지시키고 있음",
      "core_summary": "오늘 리포트에 따르면 메모리, 패키징, 전력, 냉각 등 AI 인프라 병목이 여전히 핵심 성장 서사로 나타남. 동시에 유가 상승과 끈적한 인플레이션 기대는 정책 제약을 부각시키는 요인이 되고, 지정학 및 해운 리스크는 하드웨어 중심 공급망에 취약성을 가중시킴. 주식은 완만한 강세이고 심리는 탐욕 구간이나, 약한 암호화폐와 높은 매크로 리스크로 시장은 광범위한 Risk-On보다 신중한 톤을 유지하는 것으로 보임.",
      "top_themes": [
        {
          "theme_title": "AI 인프라 관련 병목 현상",
          "summary": "HBM, 첨단 패키징, 전력, 냉각의 부족이 어떤 공급업체가 AI 인프라 수익의 다음 단계를 가져갈지에 영향을 미칠 수 있음",
          "trend_status": "rising",
          "trend_label": "상승",
          "related_tags": ["ai-infrastructure", "memory-hbm", "cowos-advanced-packaging", "power-cooling"],
          "related_report_count": 1,
          "source_report_ids": ["mm-001"],
          "source_item_content_ids": ["ic-mm-001"]
        },
        {
          "theme_title": "인플레이션 및 에너지 압력 요인",
          "summary": "에너지 가격 상승과 지속적 인플레이션 기대가 Fed의 신중함을 유지시키고 금리 민감 자산 변동성을 확대할 가능성이 있음",
          "trend_status": "steady",
          "trend_label": "지속",
          "related_tags": ["inflation-expectations", "energy-prices", "fed-policy", "oil"],
          "related_report_count": 1,
          "source_report_ids": ["mm-002"],
          "source_item_content_ids": ["ic-mm-002"]
        },
        {
          "theme_title": "지정학 및 공급망 리스크 요인",
          "summary": "무역, 해운, 대만 해협 긴장이 반도체 흐름에 영향을 주고 인플레이션 꼬리 리스크를 강화할 수 있음",
          "trend_status": "steady",
          "trend_label": "지속",
          "related_tags": ["geopolitical-risk", "supply-chain", "china-taiwan", "shipping"],
          "related_report_count": 1,
          "source_report_ids": ["mm-003"],
          "source_item_content_ids": ["ic-mm-003"]
        }
      ],
      "market_mood_type": "Mixed",
      "market_mood_summary": "주식은 소폭 상승하고 심리는 탐욕에 가까우나, 약한 암호화폐와 견조한 유가 및 매크로·지정학 리스크로 투자자들이 광범위한 공격적 포지셔닝보다는 선택적 접근을 유지하는 것으로 나타남"
    },
    {
      "lang_code": "en",
      "display_title": "Intersection of AI Bottlenecks With Macro and Geopolitical Risk Factors",
      "display_subtitle": "Structural AI demand remains firm in nature but inflation and energy and supply-chain risks are causing market tone to be maintained in a selective rather than fully risk-on manner",
      "core_summary": "According to today's reports, AI infrastructure scarcity in memory, packaging, power, and cooling continues to appear as the dominant growth narrative. At the same time, higher oil prices and sticky inflation expectations are becoming factors that highlight policy constraints, and geopolitical and shipping risks are adding vulnerability to hardware-heavy supply chains. Equities show modest strength and sentiment is in a greed zone, but weaker crypto and elevated macro risks indicate the market is maintaining a cautious tone rather than a broad risk-on tone.",
      "top_themes": [
        {
          "theme_title": "AI Infrastructure Bottleneck Phenomenon",
          "summary": "Shortages in HBM, advanced packaging, power, and cooling may have an impact on which suppliers will obtain the next stage of AI infrastructure returns",
          "trend_status": "rising",
          "trend_label": "Rising",
          "related_tags": ["ai-infrastructure", "memory-hbm", "cowos-advanced-packaging", "power-cooling"],
          "related_report_count": 1,
          "source_report_ids": ["mm-001"],
          "source_item_content_ids": ["ic-mm-001"]
        },
        {
          "theme_title": "Inflation and Energy Pressure Factors",
          "summary": "Rising energy prices and persistent inflation expectations may cause the Fed to maintain patience and may expand volatility in rates-sensitive assets",
          "trend_status": "steady",
          "trend_label": "Steady",
          "related_tags": ["inflation-expectations", "energy-prices", "fed-policy", "oil"],
          "related_report_count": 1,
          "source_report_ids": ["mm-002"],
          "source_item_content_ids": ["ic-mm-002"]
        },
        {
          "theme_title": "Geopolitical and Supply Chain Risk Factors",
          "summary": "Trade, shipping, and cross-strait tensions may affect semiconductor flows and may strengthen inflation tail risks",
          "trend_status": "steady",
          "trend_label": "Steady",
          "related_tags": ["geopolitical-risk", "supply-chain", "china-taiwan", "shipping"],
          "related_report_count": 1,
          "source_report_ids": ["mm-003"],
          "source_item_content_ids": ["ic-mm-003"]
        }
      ],
      "market_mood_type": "Mixed",
      "market_mood_summary": "Equities are slightly higher and sentiment is close to greed, but weaker crypto and firm oil and macro and geopolitical risks appear to show investors maintaining a selective approach rather than broad aggressive positioning"
    },
    {
      "lang_code": "ja",
      "display_title": "AIボトルネックとマクロおよび地政学リスクの交差現象",
      "display_subtitle": "構造的なAI需要は堅調な状態であるが、インフレおよびエネルギーおよびサプライチェーンリスクが市場トーンを全面的なRisk-Onではなく選択的な状態に維持させている",
      "core_summary": "本日のレポートによれば、メモリ、パッケージング、電力、冷却などのAIインフラ逼迫が依然として主要な成長ナラティブとして現れている。同時に原油高と粘着的なインフレ期待は政策抑制を強調する要因となり、地政学および海運リスクはハードウェア中心のサプライチェーンに脆弱性を加えている。株式は穏やかな強さを示しセンチメントは強気ゾーンだが、弱い暗号資産と高いマクロリスクにより、市場は広範なRisk-Onではなく慎重なトーンを維持しているように見える。",
      "top_themes": [
        {
          "theme_title": "AIインフラ関連ボトルネック現象",
          "summary": "HBM、先端パッケージング、電力、冷却の不足が、どのサプライヤーがAIインフラ収益の次段階を獲得するかに影響を与える可能性がある",
          "trend_status": "rising",
          "trend_label": "上昇",
          "related_tags": ["ai-infrastructure", "memory-hbm", "cowos-advanced-packaging", "power-cooling"],
          "related_report_count": 1,
          "source_report_ids": ["mm-001"],
          "source_item_content_ids": ["ic-mm-001"]
        },
        {
          "theme_title": "インフレおよびエネルギー圧力要因",
          "summary": "エネルギー価格の上昇と持続的なインフレ期待がFRBの慎重姿勢を維持させ、金利敏感資産のボラティリティを拡大する可能性がある",
          "trend_status": "steady",
          "trend_label": "継続",
          "related_tags": ["inflation-expectations", "energy-prices", "fed-policy", "oil"],
          "related_report_count": 1,
          "source_report_ids": ["mm-002"],
          "source_item_content_ids": ["ic-mm-002"]
        },
        {
          "theme_title": "地政学およびサプライチェーンリスク要因",
          "summary": "貿易、海運、台湾海峡の緊張が半導体フローに影響を与え、インフレのテールリスクを強める可能性がある",
          "trend_status": "steady",
          "trend_label": "継続",
          "related_tags": ["geopolitical-risk", "supply-chain", "china-taiwan", "shipping"],
          "related_report_count": 1,
          "source_report_ids": ["mm-003"],
          "source_item_content_ids": ["ic-mm-003"]
        }
      ],
      "market_mood_type": "Mixed",
      "market_mood_summary": "株式は小幅に上昇しセンチメントは強気に近いが、弱い暗号資産と堅調な原油およびマクロ・地政学リスクにより、投資家は広範な攻撃的ポジションではなく選択的なアプローチを維持しているように見える"
    }
  ]
}
```
