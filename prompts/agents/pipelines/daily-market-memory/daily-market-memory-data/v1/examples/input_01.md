# Sample input

Daily Market Memory core 객체 (`daily-market-memory-core` 출력). `core_data` 필수, 나머지는 맥락 보강용 optional.

```json
{
  "core_data": {
    "source_lang_code": "en",
    "display_title": "AI Bottlenecks Meet Macro and Geopolitical Friction",
    "display_subtitle": "Structural AI demand stays strong, but inflation, energy, and supply-chain risks are keeping market tone selective rather than fully risk-on.",
    "core_summary": "Today's reports point to a market where AI infrastructure scarcity in memory, packaging, power, and cooling remains the dominant growth narrative. At the same time, higher oil prices and sticky inflation expectations may keep policy restraint in focus, while geopolitical and shipping risks add fragility to hardware-heavy supply chains. Equities look modestly positive and sentiment reads greedy, but weaker crypto and elevated macro risks suggest a cautious rather than broad risk-on backdrop.",
    "top_themes": [
      {
        "theme_title": "AI Infrastructure Bottlenecks",
        "summary": "Scarcity in HBM, advanced packaging, power, and cooling may determine which suppliers capture the next layer of AI infrastructure returns.",
        "trend_status": "rising",
        "related_tags": [
          "ai-infrastructure",
          "memory-hbm",
          "cowos-advanced-packaging",
          "power-cooling"
        ],
        "related_report_count": 1,
        "source_report_ids": ["mm-001"],
        "source_item_content_ids": ["ic-mm-001"]
      },
      {
        "theme_title": "Inflation and Energy Pressure",
        "summary": "Rising energy prices and persistent inflation expectations may keep the Fed patient and rates-sensitive assets volatile.",
        "trend_status": "steady",
        "related_tags": [
          "inflation-expectations",
          "energy-prices",
          "fed-policy",
          "oil"
        ],
        "related_report_count": 1,
        "source_report_ids": ["mm-002"],
        "source_item_content_ids": ["ic-mm-002"]
      },
      {
        "theme_title": "Geopolitical Supply Risk",
        "summary": "Trade, shipping, and cross-strait tensions could disrupt semiconductor flows and reinforce inflation tail risks.",
        "trend_status": "steady",
        "related_tags": [
          "geopolitical-risk",
          "supply-chain",
          "china-taiwan",
          "shipping"
        ],
        "related_report_count": 1,
        "source_report_ids": ["mm-003"],
        "source_item_content_ids": ["ic-mm-003"]
      }
    ],
    "market_mood": {
      "type": "Mixed",
      "label": "Selective Risk Appetite",
      "summary": "Equities are slightly higher and sentiment looks greedy, but softer crypto, firmer oil, and macro plus geopolitical risks suggest investors are staying selective rather than broadly aggressive."
    }
  },
  "top_tags": [
    { "tag": "ai-infrastructure", "count": 1, "source_report_count": 1 },
    { "tag": "memory-hbm", "count": 1, "source_report_count": 1 },
    { "tag": "inflation-expectations", "count": 1, "source_report_count": 1 }
  ],
  "top_entities": {
    "companies": [{ "name": "NVIDIA", "count": 1, "source_report_count": 1 }],
    "industries": [],
    "technologies": [],
    "indicators": [],
    "countries": [],
    "institutions": [],
    "asset_classes": []
  },
  "risk_signals": [
    "Higher oil prices could keep inflation expectations sticky and delay easing hopes.",
    "Geopolitical escalation near Taiwan or shipping disruptions could hit semiconductor supply chains."
  ]
}
```
