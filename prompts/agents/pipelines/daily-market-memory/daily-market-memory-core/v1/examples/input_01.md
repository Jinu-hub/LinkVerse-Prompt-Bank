# Sample input

```json
{
  "source_report_count": 3,
  "core_lang_code": "en",
  "market_snapshot": {
    "items": [
      {
        "id": "SPX",
        "price": 5284.2,
        "change": 12.4,
        "changePercent": 0.24
      },
      {
        "id": "BTC",
        "price": 67250.0,
        "change": -820.0,
        "changePercent": -1.2
      },
      {
        "id": "CL",
        "price": 78.6,
        "change": 1.8,
        "changePercent": 2.34
      }
    ],
    "fearGreed": {
      "asOf": "2026-05-14",
      "value": 62,
      "classification": "Greed"
    },
    "fetchedAt": "2026-05-14T21:00:00Z"
  },
  "input_context": {
    "reports": [
      {
        "tags": ["ai-infrastructure", "memory-hbm", "cowos-advanced-packaging", "power-cooling"],
        "entities": {
          "companies": ["NVIDIA", "TSMC", "SK hynix", "Broadcom"],
          "products": ["HBM3E", "Blackwell"],
          "technologies": ["CoWoS", "liquid cooling"],
          "industries": ["semiconductors", "AI infrastructure"],
          "indicators": [],
          "countries": ["United States", "Taiwan", "South Korea"],
          "institutions": [],
          "persons": []
        },
        "regions": ["global"],
        "category": "sector",
        "coreData": {
          "topic": "AI infrastructure bottlenecks",
          "summary": "Structural AI demand remains strong, but returns may concentrate in suppliers that solve HBM, advanced packaging, power, and cooling constraints.",
          "key_takeaways": [
            "HBM and CoWoS capacity remain binding constraints for AI accelerators.",
            "Power and cooling density are becoming a bigger share of total AI infrastructure cost."
          ],
          "highlights": [
            {
              "title": "Packaging and memory scarcity",
              "summary": "Advanced packaging and HBM supply continue to shape which vendors capture AI infrastructure profits.",
              "why_it_matters": "Bottlenecks can persist even when GPU demand is strong."
            }
          ]
        },
        "coreType": "sector_flow",
        "countries": ["United States", "Taiwan"],
        "inputDate": "2026-05-14",
        "confidence": {
          "confidence_score": "medium",
          "what_to_verify": ["HBM shipment cadence", "CoWoS capacity additions"]
        },
        "reportType": "market_memory",
        "asset_classes": ["equities", "technology"],
        "itemContentId": "ic-mm-001",
        "marketMemoryItemId": "mm-001"
      },
      {
        "tags": ["inflation-expectations", "energy-prices", "fed-policy", "oil"],
        "entities": {
          "companies": [],
          "products": ["WTI crude"],
          "technologies": [],
          "industries": ["energy"],
          "indicators": ["CPI", "PCE"],
          "countries": ["United States"],
          "institutions": ["Federal Reserve"],
          "persons": []
        },
        "regions": ["United States"],
        "category": "macro",
        "coreData": {
          "topic": "Inflation and energy pressure",
          "summary": "Sticky services inflation and higher oil prices may keep the Fed in a higher-for-longer posture.",
          "key_takeaways": [
            "Energy prices are feeding back into inflation expectations.",
            "Policy patience may limit near-term easing hopes."
          ],
          "highlights": [
            {
              "title": "Oil-led inflation risk",
              "summary": "Rising crude prices could complicate disinflation progress.",
              "why_it_matters": "Rates-sensitive assets may stay volatile."
            }
          ]
        },
        "coreType": "macro_policy",
        "countries": ["United States"],
        "inputDate": "2026-05-14",
        "confidence": {
          "confidence_score": "medium",
          "what_to_verify": ["next CPI print", "Fed communication tone"]
        },
        "reportType": "market_memory",
        "asset_classes": ["rates", "commodities"],
        "itemContentId": "ic-mm-002",
        "marketMemoryItemId": "mm-002"
      },
      {
        "tags": ["geopolitical-risk", "supply-chain", "china-taiwan", "shipping"],
        "entities": {
          "companies": [],
          "products": [],
          "technologies": [],
          "industries": ["shipping", "semiconductors"],
          "indicators": [],
          "countries": ["China", "Taiwan", "United States"],
          "institutions": [],
          "persons": []
        },
        "regions": ["Asia-Pacific", "global"],
        "category": "geopolitics",
        "coreData": {
          "topic": "Geopolitical supply risk",
          "summary": "Trade and shipping friction around key technology supply chains is raising tail-risk for hardware-heavy sectors.",
          "key_takeaways": [
            "Semiconductor supply chains remain exposed to geopolitical escalation.",
            "Shipping disruptions could reinforce energy and goods inflation."
          ],
          "highlights": [
            {
              "title": "Cross-strait supply sensitivity",
              "summary": "Any escalation near Taiwan could disrupt advanced chip flows.",
              "why_it_matters": "AI and hardware valuations are vulnerable to supply shocks."
            }
          ]
        },
        "coreType": "geopolitics",
        "countries": ["China", "Taiwan", "United States"],
        "inputDate": "2026-05-14",
        "confidence": {
          "confidence_score": "low",
          "what_to_verify": ["shipping route disruptions", "export control headlines"]
        },
        "reportType": "market_memory",
        "asset_classes": ["equities", "commodities"],
        "itemContentId": "ic-mm-003",
        "marketMemoryItemId": "mm-003"
      }
    ]
  }
}
```
