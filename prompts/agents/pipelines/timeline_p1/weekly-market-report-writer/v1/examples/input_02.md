# Sample input — weekly series topic

`input_01.md`와 동일한 주간 서사를 사용하되, `source_report.topic`이 시리즈형 weekly label + compact date range 패턴인 경우.

```json
{
  "output_lang": "ko",
  "core_data": {
    "source_report": {
      "market_date": "2026-06-27",
      "topic": "Weekly global market issues ( 260621 ~ 260627 )",
      "from": "2026. 6. 22",
      "to": "2026. 6. 26"
    },
    "timeline_overview": {
      "main_narrative": "A Middle East security confrontation escalated from warnings and shipping risk into direct military action before diplomatic contacts outlined a possible implementation-first framework.",
      "narrative_arc": "Trigger -> escalation -> direct military involvement -> peak risk -> negotiation framework",
      "dominant_theme": "geopolitical_risk",
      "dominant_continuity_groups": [
        "iran_us_israel_hormuz_crisis"
      ],
      "secondary_continuity_groups": [
        "ai_compute_infrastructure_expansion",
        "apple_ai_ecosystem_push"
      ],
      "period_start": "2026-06-22",
      "period_end": "2026-06-26"
    },
    "items": [],
    "daily_groups": [],
    "continuity_groups": [],
    "report_planning_hints": {
      "suggested_title_angle": "From Hormuz warnings to direct strike and a tentative negotiation framework",
      "suggested_summary_angle": "Open with the Middle East escalation arc, then acknowledge parallel AI infrastructure and consumer-technology developments without overstating their dominance.",
      "main_timeline_order": [
        "iran_us_israel_hormuz_crisis"
      ],
      "parallel_themes_to_mention": [
        "AI compute infrastructure expansion",
        "Apple's on-device AI rollout"
      ],
      "possible_closing_comment_angle": "The period may be closing with a diplomatic framework hint, but final settlement remains unconfirmed and geopolitical risk is not fully resolved.",
      "avoid_overemphasis": [
        "Do not claim that a final agreement was reached if the input only describes a framework.",
        "Do not describe price movements unless they are explicitly included in the input.",
        "Do not overstate parallel technology items as the dominant storyline if geopolitical risk clearly dominates."
      ]
    }
  }
}
```
