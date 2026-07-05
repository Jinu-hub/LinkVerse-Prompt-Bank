# Sample input

`daily-market-memory-core` / `daily-market-memory-data` 출력을 기반으로 한 일일 SNS 포스팅 입력 샘플.

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
        "signal_strength": "high",
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
        "signal_strength": "medium",
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
        "signal_strength": "medium",
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
      "bias": "risk_on",
      "shift": "improving",
      "label": "Selective Risk Appetite",
      "summary": "Risk appetite is visible in large-cap tech and passive inflows, supporting broad indices, but rate repricing, semiconductor-specific losses, and geopolitical/shipping risks are constraining broader participation and keeping volatility elevated."
    }
  },
  "reports_summary": "AI infrastructure bottlenecks remain the dominant growth story. HBM and CoWoS capacity continue to shape which vendors capture AI infrastructure profits — NVIDIA, TSMC, SK hynix, and Broadcom are central names, but bottlenecks can persist even when GPU demand is strong. Power and cooling density are becoming a bigger share of total AI infrastructure cost.\n=====\nSticky services inflation and higher oil prices may keep the Fed in a higher-for-longer posture. Energy prices are feeding back into inflation expectations, and policy patience may limit near-term easing hopes. Rates-sensitive assets may stay volatile until the next CPI print and Fed communication tone are clearer.\n=====\nTrade and shipping friction around key technology supply chains is raising tail-risk for hardware-heavy sectors. Any escalation near Taiwan could disrupt advanced chip flows, and shipping disruptions could reinforce energy and goods inflation.",
  "lang_code": "ko"
}
```
